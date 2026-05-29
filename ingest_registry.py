# ingest_registry.py
# Usage: PINECONE_API_KEY=<key> python ingest_registry.py
# Indexes execution cards from content_creation/ and AIessentials_business/
# into the 'knowledge-base' Pinecone index under namespace 'execution-registry'.

import os
import hashlib
import datetime
from pathlib import Path
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

REGISTRY_DIRS = ["content_creation", "AIessentials_business"]
SKIP_FILES = {".gitkeep", ".DS_Store"}

def chunk_text(text, size=400, overlap=50):
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunks.append(" ".join(words[i:i+size]))
        i += size - overlap
    return chunks

def get_category(filepath: Path, base: Path) -> str:
    parts = filepath.relative_to(base).parts
    # parts[0] is the registry dir, parts[1] is the subfolder (LinkedIn, X, etc.)
    return parts[1] if len(parts) > 1 else "general"

def main():
    base = Path(__file__).parent
    index = pc.Index("knowledge-base")
    today = datetime.date.today().isoformat()

    all_records = []
    for dir_name in REGISTRY_DIRS:
        registry_dir = base / dir_name
        if not registry_dir.exists():
            print(f"SKIP (not found): {dir_name}/")
            continue

        for md_file in sorted(registry_dir.rglob("*.md")):
            if md_file.name in SKIP_FILES:
                continue
            text = md_file.read_text(encoding="utf-8")
            if not text.strip():
                print(f"SKIP (empty): {md_file.name}")
                continue

            category = get_category(md_file, base)
            registry = dir_name  # "content_creation" or "AIessentials_business"
            chunks = chunk_text(text)

            for i, chunk in enumerate(chunks):
                chunk_id = hashlib.md5(f"{md_file.relative_to(base)}-{i}".encode()).hexdigest()
                embedding = pc.inference.embed(
                    model="llama-text-embed-v2",
                    inputs=[chunk],
                    parameters={"input_type": "passage"}
                )[0].values
                all_records.append({
                    "id": chunk_id,
                    "values": embedding,
                    "metadata": {
                        "registry": registry,
                        "category": category,
                        "filename": md_file.name,
                        "text": chunk,
                        "date_ingested": today,
                    }
                })
            print(f"Chunked: {md_file.name} ({len(chunks)} chunks, category={category})")

    if not all_records:
        print("No execution cards found. Nothing to upsert.")
        return

    print(f"\nUpserting {len(all_records)} vectors into 'execution-registry' namespace...")
    for i in range(0, len(all_records), 100):
        batch = all_records[i:i+100]
        index.upsert(vectors=batch, namespace="execution-registry")
        print(f"  {min(i+100, len(all_records))}/{len(all_records)} done")

    print(f"\nDone. {len(all_records)} chunks in 'knowledge-base' index, namespace 'execution-registry'.")

if __name__ == "__main__":
    main()

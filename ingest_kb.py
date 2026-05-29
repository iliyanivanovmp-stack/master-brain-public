# ingest_kb.py
# Usage: PINECONE_API_KEY=<key> python ingest_kb.py knowledge_base

import os
import sys
import hashlib
import datetime
from pathlib import Path
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

DOMAIN_MAP = {
    "Sales": "sales",
    "Marketing": "marketing",
    "Content Creation": "content-creation",
    "Business Operations": "operations",
    "Research": "research",
    "AI & Automation": "ai-automation",
}

SWIPE_FILES = {"Hooks.md", "Emails.md", "LinkedIn Post Templates.md"}

def chunk_text(text, size=400, overlap=50):
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunks.append(" ".join(words[i:i+size]))
        i += size - overlap
    return chunks

def get_domain(filepath: Path, kb_root: Path) -> str:
    parts = filepath.relative_to(kb_root).parts
    return DOMAIN_MAP.get(parts[0], "general") if parts else "general"

def main():
    kb_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("knowledge_base")
    index = pc.Index("knowledge-base")
    today = datetime.date.today().isoformat()

    all_records = []
    for md_file in sorted(kb_root.rglob("*.md")):
        domain = get_domain(md_file, kb_root)
        content_type = "swipe-file" if md_file.name in SWIPE_FILES else "knowledge"
        text = md_file.read_text(encoding="utf-8")
        if not text.strip():
            print(f"SKIP (empty): {md_file.name}")
            continue
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            chunk_id = hashlib.md5(f"{md_file.relative_to(kb_root)}-{i}".encode()).hexdigest()
            embedding = pc.inference.embed(
                model="llama-text-embed-v2",
                inputs=[chunk],
                parameters={"input_type": "passage"}
            )[0].values
            all_records.append({
                "id": chunk_id,
                "values": embedding,
                "metadata": {
                    "domain": domain,
                    "filename": md_file.name,
                    "type": content_type,
                    "text": chunk,
                    "date_ingested": today,
                }
            })
        print(f"Chunked: {md_file.name} ({len(chunks)} chunks, domain={domain})")

    print(f"\nUpserting {len(all_records)} vectors...")
    for i in range(0, len(all_records), 100):
        batch = all_records[i:i+100]
        index.upsert(vectors=batch)
        print(f"  {min(i+100, len(all_records))}/{len(all_records)} done")

    print(f"\nDone. {len(all_records)} chunks loaded into 'knowledge-base' index.")

if __name__ == "__main__":
    main()

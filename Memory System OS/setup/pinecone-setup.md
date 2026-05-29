# Pinecone Setup (one-time)

The `wrap-up` and `recall` skills both need Pinecone. The `strategy-awareness` skill does not — it uses a local markdown file. So if you only want strategy governance and don't care about searchable session history, you can skip this entirely.

---

## What you need

1. A free Pinecone account
2. One Pinecone index for personal memory (e.g. named `personal-memory`)
3. Either the **Pinecone MCP** server connected to Claude Code, OR the **Pinecone Python SDK** installed locally

---

## Step 1 — Create a Pinecone account

1. Go to <https://www.pinecone.io/>
2. Sign up (free tier is enough for personal memory at this scale)
3. Note your API key from the dashboard

## Step 2 — Create your index

In the Pinecone dashboard:

| Setting | Value |
|---|---|
| **Name** | `personal-memory` (or whatever you want) |
| **Dimension** | `1024` |
| **Metric** | `cosine` |
| **Embedding model** | `llama-text-embed-v2` |
| **Cloud / region** | Default (AWS us-east-1) |

The `llama-text-embed-v2` model is the recommended Anthropic-compatible embedding for Pinecone. It's free and 1024-dimensional.

## Step 3 — Connect to Claude Code

Pick **one** of:

### Option A — Pinecone MCP (recommended)

Anthropic released an official Pinecone MCP server. Install via:

```bash
# add to ~/.claude.json or your Claude Code MCP config
{
  "mcpServers": {
    "pinecone": {
      "command": "npx",
      "args": ["-y", "@pinecone-io/mcp-server"],
      "env": {
        "PINECONE_API_KEY": "<your-api-key>"
      }
    }
  }
}
```

Restart Claude Code. Verify with: *"List available Pinecone tools."*

### Option B — Python SDK (fallback)

```bash
pip install pinecone-client

# Add to your shell profile (~/.zshrc or ~/.bashrc):
export PINECONE_API_KEY="<your-api-key>"
```

The bundled `upsert.py` and `search.py` scripts in each skill folder will then work via Bash calls.

## Step 4 — Configure your indexes

Create `~/.claude/memory-config.json`:

```json
{
  "personal_index": "personal-memory",
  "embedding_model": "llama-text-embed-v2",
  "dimension": 1024,
  "knowledge_indexes": []
}
```

That's it for the basic setup. The `wrap-up` and `recall` skills will start working in your next Claude Code session.

---

## Step 5 (optional) — Add knowledge indexes

For Bucket 02 (Knowledge), create a separate Pinecone index per topic. For example:

- `hormozi` — Alex Hormozi books, podcasts, frameworks
- `your-youtube` — your own video transcripts and scripts
- `your-community` — community posts, sentiment, customer feedback
- `your-books` — bulk-ingested book notes

After creating each index in Pinecone, add it to your config:

```json
{
  "personal_index": "personal-memory",
  "embedding_model": "llama-text-embed-v2",
  "dimension": 1024,
  "knowledge_indexes": [
    { "name": "hormozi", "topic": "Alex Hormozi business frameworks" },
    { "name": "your-youtube", "topic": "Your video transcripts" }
  ]
}
```

The `recall` skill will route queries to the right index based on the topic descriptor.

For bulk-ingest scripts (loading a whole book, a transcript folder, etc.), see `setup/bulk-ingest.md`.

---

## Cost note

The Pinecone free tier covers most personal use:
- 2 GB storage
- 5M reads/month
- 5M writes/month

A typical user's session-summary archive after a year is ~5–20 MB. You won't pay until you start ingesting large transcript libraries.

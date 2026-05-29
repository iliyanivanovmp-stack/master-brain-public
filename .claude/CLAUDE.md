# Master Brain — Memory System

This directory is the central knowledge and memory operating system for AIessentials. Everything here is designed so AI agents retrieve exactly what they need — no folder browsing, no bloated context.

## Strategy
Living strategy document is at `~/Desktop/master_brain/master_brain/strategy.md`. Use the strategy-awareness skill to read, update, or reflect on it. When running strategy-awareness, use this path instead of the skill's default.

## Knowledge Recall
Use /recall to search past decisions, frameworks, and session history stored in Pinecone. Config lives at `~/Desktop/master_brain/master_brain/memory-config.json`.

## Session Logging
Run /wrap-up at the end of every meaningful session to save a summary to Pinecone personal-memory index.

## Adding to the Knowledge Base
Tell Claude what to add and where it belongs — Claude writes the markdown file into the correct `knowledge_base/` subfolder, runs `ingest_kb.py` to embed and upsert into Pinecone, and updates `knowledge_base_index.md` with a one-line entry for the new file. No manual steps needed.

## Execution Registry
Skills and workflow cards live in `AIessentials_business/` and `content_creation/`. The full index is at `execution_index.md`. To adopt an existing workflow or project into master_brain, use the adoption skill at `AIessentials_business/SOPs/adopt_workflow.md`. After writing any execution card, run `python ingest_registry.py` from the master_brain directory to index it in Pinecone's `execution-registry` namespace — adoption is not complete until this runs. Before starting any task, run /recall to check if a relevant skill card or past decision exists.


# master_brain - Agent Protocol

## Finding What to Execute
When user says to do a task:
Search Pinecone `knowledge-base` index, **namespace `execution-registry`** before browsing any folder.
Never browse `content_creation/` or `AIessentials_business/` directly — Pinecone is the index.
Query naturally: "post on LinkedIn", "create a lead magnet", "write a proposal" — the right card will surface.

## Finding Knowledge & Context
Search Pinecone `knowledge-base` index (default namespace) for brand voice, frameworks, strategy, sales, marketing, anything theoretical and knowledge.
KB context is optional — pull it when the task benefits from it, not by default.

## Executing
Each execution card tells you which global skill to invoke and with what parameters. or what scripts to execute and in what folders.
Global skills are available in every session.

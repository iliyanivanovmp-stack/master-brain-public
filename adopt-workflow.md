# Adopt Workflow

**Type:** Pure Skill
**Domain:** AIessentials Business — SOPs
**Trigger:** User says "I want to adopt [workflow]", "migrate this workflow", or shares an external project to integrate into master_brain

---

## Purpose

Review an external project or workflow and produce a lightweight skill card for the execution registry. The external project stays where it is — master_brain gets a card only.

---

## Steps

1. **Review the workflow**
   - Read the project files the user shares (key files: main script, README, any config)
   - Identify: what does it do, what inputs does it need, what does it output

2. **Summarize back to user**
   - One paragraph: what this workflow does and how it works
   - List the exact inputs and outputs

3. **Extract embedded knowledge**
   - Scan the workflow for rules, frameworks, strategies, or domain knowledge (e.g. copywriting rules, platform-specific guidelines, scoring criteria, objection patterns)
   - Cross-reference `knowledge_base_index.md` — flag anything NOT already in the KB
   - For each gap found: propose a KB file, confirm with user, write it into the correct `knowledge_base/` subfolder, run `ingest_kb.py`, update `knowledge_base_index.md`

4. **Classify the type**
   - Can Claude execute this entirely in chat using KB context? → **Type A (Pure Skill)**
   - Does it require running external code/scripts? → **Type B (Execution Card)**
   - Does it have both a drafting phase and an execution phase? → **Type C (Hybrid)**
   - If unsure, ask the user

5. **Identify KB connections**
   - Which knowledge base files are relevant when running this? (include any newly added from step 3)
   - Reference `knowledge_base_index.md` to find the right files

6. **Draft the card**
   - Use the appropriate template (A, B, or C) from the plan
   - Keep it under 80 lines — if longer, it's trying to do too much

7. **Confirm placement**
   - Propose the folder: `content_creation/[platform]/` or `AIessentials_business/[subfolder]/`
   - Ask user to confirm before writing

8. **Write the card** to the confirmed location

9. **Update `execution_index.md`**
   - Add one row to the correct domain table: file path, what it does, type

10. **Verify**
    - Read the card back cold and confirm an agent could follow it without extra context

11. **Ingest into execution-registry**
    - Run `python ingest_registry.py` from the master_brain directory
    - This indexes the card in Pinecone so agents can discover it via semantic search
    - No ingest = the card doesn't exist to any agent (it's just a local file)

---

## Rules

- The card is a recipe, not the workflow itself. Keep it minimal.
- Never copy the full project code into the card. Only the invocation command.
- If the workflow doesn't fit Type A, B, or C cleanly — flag it and update the plan before proceeding.
- Always update `execution_index.md` after writing a card.
- Always run `ingest_registry.py` after writing a card — adoption is not complete until the card is in Pinecone.

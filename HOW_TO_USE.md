# How to Use Your Master Brain System

## What This System Is

Three layers that work together so AI agents never waste time browsing files — they retrieve exactly what they need, instantly.

```
You edit here          →    Agents retrieve from here
──────────────              ──────────────────────────
knowledge_base/        →    Pinecone: knowledge-base index  (/recall)
session work           →    Pinecone: personal-memory index (/wrap-up + /recall)
                       →    ~/.claude/strategy.md           (auto-read every session)
```

The rule: **agents never browse folders. They query or read one small file.**

---

## The Three Commands

### `strategy-awareness` + `/strategy` — Your North Star File

**`strategy-awareness`** is the governance skill that runs automatically. When you say something strategic mid-conversation — a decision, a new offer, a customer signal, a pivot — it fires, appends a dated entry to `strategy.md`, and checks for conflicts with your Don't-Do list and existing decisions. You never invoke it manually; it listens.

**`/strategy`** is the visual dashboard command. Run it when you want to see or edit your strategy interactively — it opens an HTML view in your browser where you can edit inline and apply changes back.

**When to run `/strategy`:**
- You want to see your current strategic picture
- You want to visually edit your strategy

**Why it matters:** `strategy-awareness` captures decisions the moment you make them. `/strategy` gives you the map. Together: Claude always has current context, and you can audit or edit it visually whenever you want.

**Key habit:** Just make decisions out loud — `strategy-awareness` logs them automatically. Run `/strategy` when you want to review the full picture.

---

### `/recall [query]` — Semantic Memory Search
**What it does:** Searches both Pinecone indexes — your knowledge base and past session summaries — and returns the most relevant chunks with scores.

**When to use it:**
- "What do I know about cold email infrastructure?"
- "What did we decide about pricing last month?"
- "Give me our objection handling frameworks"
- "What Hormozi concepts apply to this offer?"

**Two sources it searches:**
| Query type | Source |
|---|---|
| Frameworks, templates, tactics | `knowledge-base` index (your vault) |
| Past decisions, session work | `personal-memory` index (wrap-up logs) |

**Pro tip:** Be specific. "cold email subject lines B2B" beats "email stuff."

---

### `/wrap-up` — Session Memory
**What it does:** At the end of a work session, generates a structured summary and saves it to Pinecone's `personal-memory` index.

**When to use it:** End of every meaningful work session — strategy calls, content creation, client work, system building.

**What gets saved:** What you worked on, decisions made, key outputs, what's next.

**Why it matters:** This is what makes `/recall` useful over time. No wrap-up = no retrievable history.

**Key habit:** Before closing Claude Code, run `/wrap-up`. Takes 30 seconds. Compounds forever.

---

## Day-to-Day Workflow

### Starting a session
1. Claude auto-reads `strategy.md` — no action needed
2. If working on something specific, `/recall [topic]` to pull relevant context before starting

### During a session
- Make a strategic decision → say it out loud → Claude logs it to `strategy.md`
- Need a framework or template → `/recall [what you need]`
- Working on content or outreach → `/recall` your swipe files, ICP, or past decisions first

### Ending a session
1. Run `/wrap-up`
2. That's it

---

## What Lives Where

| Content type | Location | Accessed via |
|---|---|---|
| Sales frameworks, cold email tactics, ICP docs | `knowledge_base/` → Pinecone | `/recall` |
| Past session summaries, decisions | Pinecone `personal-memory` | `/recall` |
| Current focus, active offers, don't-do list | `~/.claude/strategy.md` | Auto-loaded + `/strategy` |
| Client SOPs, delivery docs, active work | `AIessentials_business/` | You browse manually in Obsidian |
| Content drafts, scripts, templates | `content_creation/` | You browse manually in Obsidian |

---

## Keeping the System Sharp

**Add to knowledge base:** When you learn something worth keeping (a new framework, a proven email sequence, a research finding) — drop a `.md` file into the right `knowledge_base/` subfolder and re-run `ingest_kb.py`. It becomes searchable immediately.

**Update strategy:** Don't let `strategy.md` go stale. When your offer changes, when you land a client, when you decide to kill something — log it. The file is only as useful as it is current.

**Wrap up every session:** The `personal-memory` index is only as rich as what you feed it. One missed session is fine. Making it a habit is what makes `/recall` answer questions like "what were we working on in April?"

---

## The One Mental Model

> **Strategy = what's always loaded. Knowledge = what you pull. Memory = what you leave behind.**

- `strategy.md` is the brain stem — always on, always current
- Pinecone `knowledge-base` is long-term memory — your entire vault, instantly searchable
- Pinecone `personal-memory` is episodic memory — everything you've done, session by session

When Claude has all three, it operates with full context. When it's missing any one, it's flying partial.

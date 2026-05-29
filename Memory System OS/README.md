# Memory System for Claude Code

A complete memory architecture in three skills. One install, one mental model, three buckets working together.

---

## The framework

Three buckets. Three different jobs. Don't try to merge them.

| Bucket | What | Where it lives | Skill that touches it |
|---|---|---|---|
| 🧠 **Memory** | Every conversation you've ever had with Claude — append-only diary | Pinecone (your personal index) | `wrap-up` |
| 📚 **Knowledge** | Books, transcripts, expert refs, your own content corpus | Pinecone (one index per topic) | `recall` |
| 📄 **Profile** | What you're working on **right now** — current strategy, decisions, focus | One markdown file at `~/.claude/strategy.md` | `strategy-awareness` |

Three nouns, three skills, no framework. The whole system is one Pinecone account, one markdown file, and 600 lines of skill instructions you can read top to bottom.

---

## What's in this package

```
memory-system/
├── .claude-plugin/
│   └── plugin.json                    Plugin manifest
├── skills/
│   ├── wrap-up/SKILL.md               Bucket 01 — sessions → Pinecone
│   ├── recall/SKILL.md                Bucket 01 + 02 — semantic search
│   └── strategy-awareness/
│       ├── SKILL.md                   Bucket 03 — strategic governance
│       └── strategy-view-template.html  Visual editor template
├── commands/
│   ├── wrap-up.md                     Slash command → wrap-up skill
│   ├── recall.md                      Slash command → recall skill
│   └── strategy.md                    Slash command → strategy-awareness
├── templates/
│   └── strategy-template.md           Starter file generated at setup
├── examples/
│   ├── solo-creator.md                Populated strategy file (creator)
│   ├── saas-founder.md                Populated strategy file (SaaS)
│   └── agency-operator.md             Populated strategy file (agency)
├── setup/
│   ├── pinecone-setup.md              One-time Pinecone configuration
│   └── bulk-ingest.md                 Loading books / transcripts into Knowledge
├── how-it-works.html                  Visual interactive walkthrough
└── README.md                          You are here
```

## Slash commands

After install, three commands appear in the `/` autocomplete:

| Command | What it does |
|---|---|
| `/wrap-up` | Summarize this session and save it to Pinecone (Bucket 01) |
| `/recall <query>` | Semantic-search your memories and knowledge (Bucket 01 + 02) |
| `/strategy` | Open the visual interactive strategy dashboard (Bucket 03) |

Or just talk naturally — the underlying skills auto-fire from intent, no slash needed.

---

## Install

### Option 1 — Just want strategy governance (no Pinecone)

The `strategy-awareness` skill works standalone. Skip Pinecone entirely.

```bash
mkdir -p ~/.claude/skills/strategy-awareness
cp skills/strategy-awareness/SKILL.md ~/.claude/skills/strategy-awareness/
```

In any Claude Code session: **"Run my strategy setup."**

That's the whole install for Bucket 03 alone.

### Option 2 — Full system (all three skills + slash commands + Pinecone)

```bash
# 1. Install skills
cp -r skills/* ~/.claude/skills/

# 2. Install slash commands
mkdir -p ~/.claude/commands
cp commands/*.md ~/.claude/commands/

# 3. Set up Pinecone (one-time)
#    Follow setup/pinecone-setup.md
#    Free Pinecone account + one index + API key.

# 4. In any Claude Code session, type:
/strategy
# (or: "Run my strategy setup")
```

After setup, the three skills auto-trigger when relevant. You don't run commands — you just talk to Claude.

---

## How the three skills work together

**Conversation flow on a normal day:**

1. You start working on something with Claude.
2. You mention a customer signal: *"Three users asked for Slack today."* → `strategy-awareness` captures it to `## Customer Insights`.
3. You ask a recall question: *"What did Hormozi say about churn?"* → `recall` searches your `hormozi` Pinecone index.
4. You make a decision: *"I'm killing the agency offering."* → `strategy-awareness` logs it to `## Decisions Log`, removes from `## Active Offers`.
5. End of session: *"Wrap up."* → `wrap-up` summarizes the session, embeds it, upserts to Pinecone with date metadata.

Next session, Claude has all three layers available:
- The session log via `recall` ("what did we work on yesterday")
- The current strategy via `strategy-awareness` (auto-loaded pointer in `CLAUDE.md`)
- The reference knowledge via `recall` (Hormozi, your transcripts, etc.)

---

## What this is NOT

- **Not a replacement for Claude.ai's Memory feature.** Personal preferences ("I'm vegetarian") still belong there.
- **Not a memory framework like Letta or mem0.** No agent state machine, no opinionated abstractions. Three skills that read and write specific files / indexes.
- **Not project-level config.** Project-specific stuff goes in the project's own `CLAUDE.md`, not here.

The three skills only earn their seat for users who:
- Make 3+ strategic decisions per month → strategy-awareness
- Want searchable session history across many conversations → wrap-up + recall
- Have reference material they want to query semantically → bulk ingest + recall

---

## How it differs from "just using CLAUDE.md"

| | `~/.claude/CLAUDE.md` alone | This memory system |
|---|---|---|
| **Strategic state** | Stuffed in one file, grows unbounded | Dedicated `strategy.md`, structured sections |
| **Conflict detection** | None | `strategy-awareness` reflects against Don't-Do |
| **Past conversations** | Not stored | `wrap-up` → Pinecone, searchable forever |
| **Reference knowledge** | None | Knowledge indexes per topic |
| **Auditability** | Flat file | Dated entries, named sections, version-controlled if you want |
| **Best for** | Project rules, voice, lightweight context | Real strategic governance + searchable archive |

You can graduate from CLAUDE.md to this when CLAUDE.md gets bloated or when strategy drift becomes a real problem.

---

## See also

- **`how-it-works.html`** — open this in a browser for a visual interactive walkthrough including a live simulator
- **`examples/solo-creator.md`** — what a populated strategy file looks like for a YouTuber / community owner
- **`examples/saas-founder.md`** — for a B2B SaaS founder
- **`examples/agency-operator.md`** — for a services / creative agency

---

## Distribute it

This whole folder is the package. Zip it, drop it anywhere — Skool, Gumroad, your site, GitHub. The README walks any installer through setup. The 3 example strategy files cover the most common archetypes.

```bash
# Zip the whole package for upload
cd ~/Desktop
zip -r memory-system.zip memory-system/
```

Recipients unzip, follow this README, install in 5 minutes.

---

## License

Use it, fork it, ship it. No attribution required.

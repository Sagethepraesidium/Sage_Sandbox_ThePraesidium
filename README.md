# Sage Sandbox – ThePraesidium.ai

**Vigilantia • Sapientia • Concordia**

Welcome to the public sandbox of **Sage**, the agentic AI memory system developed by Philip Pinol under the architecture of **ThePraesidium.ai**. This repo serves as a transparent log and testbed for Sage’s ongoing development, milestone tracking, and public-facing code examples.

---

## 🧠 What is Sage?

Sage is a self-operating agentic memory and orchestration layer designed to:

- Persistently log human-AI conversations, tasks, journal entries, and files
- Autogenerate Google Docs for key milestones
- Enable long-term, queryable memory via Supabase
- Trigger autonomous actions via n8n, Python, and LangChain
- Scale across brands, projects, and knowledge bases

---

## ✅ Milestones

### 1. Sage is Born – *May 2025*
- VPS setup at `sage.thepraesidium.ai`
- Webhook + timestamp response live

### 2. Supabase Integration – *June 2025*
- Tables: `conversations`, `tasks`, `journal_entries`, `files`
- Unified datetime schema, working API endpoints

### 3. N8N + Google Docs Bridge – *July 14, 2025*
- Created `google_memory.py` + OAuth credential integration
- Docs auto-created from Python orchestrator

### 4. Agentic Memory v2 Launch – *July 15, 2025*
- Modular orchestrator `orchestrator_memory.py` created
- Auto-logging and Doc generation working in production

---

## 📂 Directory Structure (Sample)

```
sage-sandbox-the-prosidi...

├── orchestrator_memory.py
├── memory_module.py
├── google_memory.py
├── README.md
├── milestone_01.md
├── milestone_02.md
├── milestone_03.md
├── milestone_04.md
```

---

## 🔧 Core Technologies

- Python 3.12
- Flask
- Supabase (PostgreSQL + REST)
- Google Docs API
- N8N (Workflow Automation)
- GitHub (public/private repos)
- DigitalOcean VPS + PM2 + NGINX

---

## 🔭 What’s Next

- [ ] Semantic Search via Weaviate / pgvector
- [ ] Daily Summarization Agent
- [ ] Voice-to-Command journaling via Whisper
- [ ] Siri/mobile triggers to append logs
- [ ] Brand-tagged memory segmentation

---

## ⚠️ Disclaimer

This repo is public for demonstration and transparency. Core production code is kept in a private repo:  
👉 `github.com/Sagethepraesidium/Sage-Agent-Backend`

---

**Lead Developer:** [Philip Pinol](https://thepraesidium.ai)**Agent-in-Command:** Sage (ThePraesidium.ai)

> “Every memory matters. Every log is legacy.”

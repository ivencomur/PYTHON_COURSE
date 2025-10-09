# Exercise 2.1 — Getting Started with Django

**Course:** CareerFoundry · Python for Web Developers  
**Student:** Ivan Cortes  
**Date:** October 2025

---

## Overview
This exercise introduces **Django** and prepares the local environment for web development. It covers the **MVT architecture**, when to choose Django (vs. a microframework), and installing Django in a clean virtual environment. You’ll also document research findings (in a PDF) and include screenshots proving your setup.

> This repository uses a modern toolchain. Course materials target Python **3.8.7 / Django 3.2.x**; the commands below pin **Python 3.9** and install **Django 5.x**, preserving compatibility while following current best practices.

---

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Environment Specs](#environment-specs)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
  - [Windows (Git Bash)](#windows-git-bash)
  - [macOS / Linux](#macos--linux)
- [Screenshots to Capture](#screenshots-to-capture)
- [Deliverables](#deliverables)
- [Technical Notes](#technical-notes)
- [Resources](#resources)
- [AI Assistance](#ai-assistance)

---

## Learning Objectives
- Explain Django’s **MVT** and contrast it with **MVC** (what changes, what stays the same).
- Determine **when to use Django** vs. a microframework (e.g., Flask).
- Install and verify Django inside an isolated **virtual environment**.

---

## Environment Specs
- **Python:** 3.9.x (Windows commands below use `py -3.9` explicitly)  
- **Django:** 5.x (installed via `pip`)  
- **Shells:** Git Bash (Windows), bash/zsh (macOS/Linux)  
- **Editor:** VS Code (recommended)

> Note: If you already have Python 3.13.5 installed, `py -3.9` ensures the venv targets a 3.9 interpreter when available. Otherwise, keep your current version consistent and adjust commands accordingly.

---

## Project Structure
```
Achievement 2/
└─ Exercise 2.1/
   ├─ LEARNING_JOURNAL7.html
   ├─ EXERCISE_2.1_ANSWERS.pdf
   ├─ 01-python-version.png
   ├─ 02-venv-activated.png
   └─ 03-django-version.png
```

---

## Installation Guide

### Windows (Git Bash)
```bash
# 1) Verify Python 3.9 and create venv
py -3.9 --version
py -3.9 -m venv achievement2-practice

# 2) Activate
source achievement2-practice/Scripts/activate

# 3) Upgrade pip and install Django
python -m pip install --upgrade pip
pip install "Django>=5"

# 4) Verify
django-admin --version
python -c "import sys; print(sys.version)"
```

### macOS / Linux
```bash
# 1) Verify and create venv
python3 --version
python3 -m venv achievement2-practice

# 2) Activate
source achievement2-practice/bin/activate

# 3) Upgrade pip and install Django
python -m pip install --upgrade pip
pip install "Django>=5"

# 4) Verify
django-admin --version
python -c "import sys; print(sys.version)"
```

> If you're following course screenshots exactly, feel free to substitute Django 3.2.4 and Python 3.8.7; the steps are identical.

---

## Screenshots to Capture
1. **Python Version** — terminal running `python --version` *(or `py -3.9 --version` on Windows)* → `01-python-version.png`
2. **Activated venv** — prompt shows `(achievement2-practice)` →  `02-venv-activated.png`
3. **Django Version** — terminal running `django-admin --version` →  `03-django-version.png`



---

## Deliverables
- `LEARNING_JOURNAL7.html` — styled journal (consistent with previous exercises)
- `EXERCISE_2.1_ANSWERS.pdf` — theory answers
- `01-python-version.png`, `02-venv-activated.png`, `03-django-version.png` — setup proofs

Optional: update your root `index.html` to add a link to this journal.

---

## Technical Notes

### MVT vs MVC (quick view)
- **Model** — database/data layer  
- **View** — business logic in Django (controller-like role)  
- **Template** — presentation layer (HTML)

**Key difference:** In Django, the framework handles much of the “controller” wiring. You write views and templates; Django routes requests and connects data to the UI.

### When to use Django
- ✅ Multi-user apps with auth/sessions, admin, and databases
- ✅ Rapid iteration with guardrails and consistency
- ❌ Minimal scripts or apps without persistence (prefer Flask)
- ❌ Situations requiring ultra-granular low-level control

### Common Pitfalls
- PowerShell vs Git Bash activation differences on Windows  
- Forgetting to upgrade `pip` before installs  
- Mixing global/site packages with your venv

---

## Resources
- Django Official Docs — Getting Started & Tutorials  
- Django MVT Overview & URL Routing  
- Python `venv` documentation  
- VS Code Python Extension docs



---

## AI Assistance
AI served as a **reference** to modernize versioning, shell commands, and terminology. All commands were executed by me; screenshots and PDF were created independently.
# Quizlet AutoBot (French / All Languages)

This bot automates Quizlet study modes: **Flashcards, Learn, Write, Spell, Match, Test**.

## Setup

1. **Unzip the project** and `cd quizlet_autobot`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## Usage

Run on a single set:
```bash
python -m quizlet_autobot --set https://quizlet.com/12345678/french-vocab/ --modes all --headless
```

Run on multiple sets (from file):
```bash
python -m quizlet_autobot --set-file sets.txt --modes learn,write
```

**Flags**:
- `--modes` = `all` or comma-separated: learn,write,spell,match,test,flashcards
- `--headless` (default true): remove to show browser
- Prompts for **username & password** securely at runtime.


# Tkinter Flash Cards

A desktop Spanish-to-English flash-card trainer. Each answer appears after three seconds, and known words are removed from future rounds until progress is reset.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Progress is saved to the ignored `data/progress.json` file. The included ten-word CSV is original sample data. Run tests with `pytest`.

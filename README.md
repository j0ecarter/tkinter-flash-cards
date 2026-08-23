# Tkinter Flash Cards

I originally completed projects from Angela Yu's 100 Days of Code course across 2021–2023. After the original files were lost during a laptop change, this project was reconstructed in 2026 with substantial AI coding assistance. The Git history represents the reconstruction and first GitHub publication, not the original course timeline.

A desktop Spanish-to-English flash-card trainer. Each answer appears after three seconds, and known words are removed from future rounds until progress is reset.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Progress is saved to the ignored `data/progress.json` file. The included ten-word CSV is original sample data. Run tests with `pytest`.

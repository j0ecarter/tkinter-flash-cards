import random
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from flashcards import Card, StudyProgress, load_cards

WORDS_PATH = Path("data/words.csv")
PROGRESS_PATH = Path("data/progress.json")
FLIP_MS = 3000


def main() -> None:
    # load saved progress if it exists
    progress = StudyProgress(load_cards(WORDS_PATH), PROGRESS_PATH)
    window = tk.Tk()
    window.title("Flash Cards")
    window.config(padx=30, pady=30, bg="#e7f0dc")

    heading = tk.Label(window, text="Word", font=("Arial", 18), bg="#e7f0dc")
    word = tk.Label(window, text="", width=24, height=5, font=("Arial", 32, "bold"), bg="white")
    status = tk.Label(window, text="", bg="#e7f0dc")
    heading.grid(row=0, column=0, columnspan=2)
    word.grid(row=1, column=0, columnspan=2, pady=12)
    status.grid(row=3, column=0, columnspan=2)

    current: Card | None = None
    flip_job: str | None = None

    def show_answer() -> None:
        if current:
            heading.config(text="English")
            word.config(text=current.back, bg="#dbeafe")

    def next_card() -> None:
        nonlocal current, flip_job
        if flip_job:
            window.after_cancel(flip_job)
        remaining = progress.remaining
        if not remaining:
            current = None
            heading.config(text="Finished")
            word.config(text="All cards known", bg="white")
            status.config(text="Reset to study again.")
            return
        current = random.choice(remaining)
        heading.config(text="Spanish")
        word.config(text=current.front, bg="white")
        status.config(text=f"{len(remaining)} card(s) remaining")
        flip_job = window.after(FLIP_MS, show_answer)

    def known() -> None:
        if current:
            progress.mark_known(current)
        next_card()

    def reset() -> None:
        if messagebox.askyesno("Reset", "Study all cards again?"):
            progress.reset()
            next_card()

    tk.Button(window, text="Again", width=16, command=next_card).grid(row=2, column=0, padx=5)
    tk.Button(window, text="Known", width=16, command=known).grid(row=2, column=1, padx=5)
    tk.Button(window, text="Reset progress", command=reset).grid(row=4, column=0, columnspan=2, pady=(12, 0))
    next_card()
    window.mainloop()


if __name__ == "__main__":
    main()

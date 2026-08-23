import csv
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Card:
    front: str
    back: str


def load_cards(path: Path) -> list[Card]:
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        cards = [Card(row["front"].strip(), row["back"].strip()) for row in reader]
    return [card for card in cards if card.front and card.back]


class StudyProgress:
    def __init__(self, cards: list[Card], path: Path):
        self.cards = cards
        self.path = path
        self.known = self._load_known()

    def _load_known(self) -> set[str]:
        try:
            values = json.loads(self.path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            return set()
        return {str(value) for value in values}

    @property
    def remaining(self) -> list[Card]:
        # only cards still being learnt
        return [card for card in self.cards if card.front not in self.known]

    def mark_known(self, card: Card) -> None:
        self.known.add(card.front)
        self._save()

    def reset(self) -> None:
        self.known.clear()
        self._save()

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(sorted(self.known), indent=2), encoding="utf-8")

from pathlib import Path

from flashcards import Card, StudyProgress, load_cards


def test_cards_load_from_csv(tmp_path: Path):
    path = tmp_path / "cards.csv"
    path.write_text("front,back\nhola,hello\nlibro,book\n", encoding="utf-8")
    assert load_cards(path) == [Card("hola", "hello"), Card("libro", "book")]


def test_known_card_is_removed_and_persisted(tmp_path: Path):
    cards = [Card("hola", "hello"), Card("libro", "book")]
    path = tmp_path / "progress.json"
    progress = StudyProgress(cards, path)
    progress.mark_known(cards[0])
    assert progress.remaining == [cards[1]]
    assert StudyProgress(cards, path).remaining == [cards[1]]


def test_reset_restores_all_cards(tmp_path: Path):
    cards = [Card("hola", "hello")]
    progress = StudyProgress(cards, tmp_path / "progress.json")
    progress.mark_known(cards[0])
    progress.reset()
    assert progress.remaining == cards

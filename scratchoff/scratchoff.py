from .extract import extract_data


def all_games():
    """All current scratch ticket games.

    Returns:
        list: List of dicts holding game data.
    """
    return extract_data()

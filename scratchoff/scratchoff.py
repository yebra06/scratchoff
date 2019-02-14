from . import clean_data


def all_games():
    """All current scratch ticket games.

    Returns:
        list: List of dicts holding game data.
    """
    return clean_data()

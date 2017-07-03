from gameset import GameSet
from utils import get_rinsed_data


class Scratchoff:
    """Scratchoff
    
    This class holds stats of scratchoff games.
    """

    def __init__(self):
        """Scratchoff constructor"""
        self.game_set = GameSet(get_rinsed_data())

    def get_scratchoff_data(self):
        """Return set scratchoff game data."""
        return self.game_set.get_game_set()


if __name__ == '__main__':
    scratchoff = Scratchoff()
    for i in scratchoff.get_scratchoff_data():
        print(i)

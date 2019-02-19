from . import clean_data


class Scratchoff:

    def __init__(self):
        self.all_games = clean_data()

    def find_game_by_id(self, id):
        for game in self.all_games:
            if game['game number'] == id:
                yield game

    def find_game(self, id, prize_level):
        for game in self.find_game_by_id(id):
            if game['prize level'] == prize_level:
                return game
        return None

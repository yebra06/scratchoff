from __future__ import division


class Game:
    """Game

    Holds game data from csv line in data set.
    """

    def __init__(self, game_number, game_name, start_date, ticket_price, prize_amount, prizes_printed, prizes_claimed):
        self.game_number = game_number
        self.game_name = game_name
        self.start_date = start_date
        self.ticket_price = ticket_price
        self.prize_amount = prize_amount
        self.prizes_printed = prizes_printed
        self.prizes_claimed = prizes_claimed

    @property
    def percent_claimed(self):
        """Percent of prizes claimed"""
        return round(float(self.prizes_claimed) / int(self.prizes_printed), 2) * 100

    def __str__(self):
        return str("game #: " + self.game_number + '\t' + "game name: " + self.game_name + '\t' + "prizes claimed: "
                   + self.prizes_claimed)


class GameSet:
    """Game set

    This class holds a set of Games data for the scratchoff games.
    It holds a set of Games since each game is unique.
    """

    def __init__(self, data=None):
        self.gameset = set()
        if data is not None:
            for line in data:
                print(line)
                game = Game(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                self.gameset.add(game)

    def get_game_set(self):
        """Return the list of games."""
        return [game for game in self.gameset]

import unittest

from scratchoff import clean_data, extract_game_info, raw_data


INIT_COLUMN_NAMES = ['game number', 'game name', 'game close date', 'ticket price',
                     'prize level', 'total prizes in level', 'prizes claimed']
FINAL_COLUMN_NAMES = INIT_COLUMN_NAMES + ['prizes remaining']


class TestScratchoffExtract(unittest.TestCase):

    def setUp(self):
        self.raw_games = raw_data()[2:]
        self.cleaned_games = clean_data()

    def test_extract_game_info_list_len(self):
        for game in self.raw_games:
            self.assertEqual(len(extract_game_info(game)), len(INIT_COLUMN_NAMES))

    def test_extract_data(self):
        for game in self.cleaned_games:
            self.assertEqual(FINAL_COLUMN_NAMES, list(game.keys()))

import unittest
import urllib.request

import config


class TestScratchoffURL(unittest.TestCase):

    def test_url_status(self):
        """Test url status code and make sure it works."""
        endpoint = urllib.request.urlopen(config.ALL_GAMES_URL)
        self.assertEqual(endpoint.getcode(), 200)

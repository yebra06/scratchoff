import requests

from scratchoff.utils import scratchoff_soup, start_url


def test_start_url():
    """Test that the target url responds success."""
    assert requests.get(start_url).status_code == 200


def test_scratchoff_soup():
    """Test that the soup exists."""
    assert scratchoff_soup is not None

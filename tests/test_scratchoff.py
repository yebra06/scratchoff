from fixtures.scratchoff_fix import scratchoff

from scratchoff.scratchoff import Scratchoff


def test_scratchoff_existence(scratchoff):
    """Test fixture for existence."""
    assert isinstance(scratchoff, Scratchoff)
    assert scratchoff is not None


def test_get_scratchoff_data(scratchoff):
    """Test filtered data."""
    assert scratchoff.get_scratchoff_data() is not None

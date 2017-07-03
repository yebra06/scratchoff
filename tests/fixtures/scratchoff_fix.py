import pytest

from scratchoff.scratchoff import Scratchoff


@pytest.fixture()
def scratchoff():
    """Scratchoff test fixture."""
    scratchoff_fixture = Scratchoff()
    yield scratchoff_fixture

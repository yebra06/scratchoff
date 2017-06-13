import requests

start_url = 'http://www.txlottery.org/\
export/sites/lottery/Games/Scratch_Offs/all.html'


def test_start_url():
    assert requests.get(start_url).status_code == 200

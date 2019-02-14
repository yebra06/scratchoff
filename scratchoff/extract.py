import re
import urllib.request

import config


def extract_game_info(line):
    """Extract game info from line.

    Args:
        line: A string of data holding game info.

    Returns:
        list: List of single games' info.

    Note:
        The returned list should have 7 elements.

        Data at each index:
            0 - game #
            1 - game name
            2 - game close date
            3 - ticket price
            4 - prize level
            5 - total prizes
            6 - prizes claimed
    """
    data = []
    line = line.strip()

    # Game number
    data.append(line[0:3])

    # Game name
    line = line[6:]
    end_name_index = line.index('"')
    data.append(line[0:end_name_index])

    # Rest of data after number and name.
    line = line[end_name_index + 2:]

    # Some weird entries have this. Extract the numerical amount.
    if '/wk***' in line:
        match = re.search(r'\$\d{1,3}(,\d{3})?(,\d{0,3})?/wk\*\*\*', line)
        if match:
            original = s = match.group(0)
            for i in ['$', ',', '/wk***']:
                s = s.replace(i, '')
            line = line.replace(original, s)

    # Strip out all the double quotes and split by commas.
    data += [i.replace('"', '') for i in line[line.index('"'):].split(',')]

    return data


def transform_to_numbers(game_data):
    """"Transform data to numerical values.

    Args:
        game_data: A list of dicts holding game data.

    Returns:
        list: List of dicts with modified game data.
    """
    for game in game_data:
        for k, v in game.items():
            try:
                game[k] = int(v)
            except ValueError:
                pass

        if game['prizes claimed'] == '':
            game['prizes claimed'] = 0
        game['prizes remaining'] = game['total prizes in level'] - game['prizes claimed']

    return game_data


def extract_data():
    """Extract and process all game data from site.

    Returns:
        list: List of dicts of all games.
    """
    with urllib.request.urlopen(config.ALL_GAMES_URL) as d:
        data = [i.decode('ISO-8859-1') for i in d]

    col_names = [x.strip().lower() for x in data[1].split(',')]

    return transform_to_numbers([
        dict(zip(col_names, extract_game_info(i)))
        for i in data[2:] if 'TOTAL' not in i
    ])

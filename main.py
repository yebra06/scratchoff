import urllib.request

import config


def extract_game_info(line):
    """
    Dirty logic to get game details from each line of game information.
    #TODO: Make more reliable.
    """
    data = []
    line = line.strip()
    data.append(line[0:3])
    line = line[6:]
    end_name_index = line.index('"')
    data.append(line[0:end_name_index])
    line = line[end_name_index + 2:]
    data += [i.replace('"', '') for i in line[line.index('"'):].split(',')]
    return data


def display_games(games):
    for i in games:
        print('#{:<7} {:<30} {:<10} {:<7} {:<7} {:<7} {:<7} {:<10}'.format(*list(i.values())))


def main():
    with urllib.request.urlopen(config.ALL_GAMES_URL) as d:
        data = [i.decode('ISO-8859-1') for i in d]
    col_names = [x.strip().lower() for x in data[1].split(',')]
    game_data = [dict(zip(col_names, extract_game_info(i))) for i in data[2:]]

    # Cast integer data if possible.
    for game in game_data:
        for k, v in game.items():
            try:
                game[k] = int(v)
            except ValueError:
                pass
        try:
            game['prizes remaining'] = game['total prizes in level'] - game['prizes claimed']
        except TypeError:
            game['prizes remaining'] = ''

    display_games(game_data)

main()

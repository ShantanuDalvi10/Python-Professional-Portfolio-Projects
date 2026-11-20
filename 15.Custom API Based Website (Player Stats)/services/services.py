from api import search_player,get_player_statistics

def get_player_data(player_name):
    player_data = search_player(player_name=player_name)

    if not player_data:
        raise ValueError

    player_identifier,player_name = player_data

    player_statistics = get_player_statistics(player_identifier=player_identifier,
                                              player_name=player_name)

    return player_statistics
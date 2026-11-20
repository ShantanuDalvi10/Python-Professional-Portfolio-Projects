
import requests
from config import Config

PLAYER_ENDPOINT = "https://api.cricketdatabase.com/v1/search"



headers = {
    "X-API-Key":Config.API_KEY
}


def search_player(player_name):
    params = {
        "q":player_name
    }
    try:
        response = requests.get(url=PLAYER_ENDPOINT,params=params,headers=headers)
        response.raise_for_status()
        player_info = response.json()
    except requests.exceptions.HTTPError:
        print("something went wrong with the API request.")
        return None
    except requests.exceptions.RequestException:
        print("Unable to connect API")
        return None
    if not player_info["data"]["players"]:
        print("Player Not Found.")
        return None

    player_identifier = player_info["data"]["players"][0]["player"]
    player_name = player_info["data"]["players"][0]["name"]


    return player_identifier,player_name



# player_name = player_info["data"]["players"][0]["name"]
# print(player_name)
# player_matches = player_info["data"]["players"][0]["matches"]
# print(player_matches)




def get_player_statistics(player_identifier,player_name):

    if not player_identifier:
        return None
    try:
        STATS_ENDPOINT = f"https://api.cricketdatabase.com/v1/players/{player_identifier}/stats"
        stat_response = requests.get(url=STATS_ENDPOINT,headers=headers)
        stat_response.raise_for_status()
        player_stats = stat_response.json()
    except requests.exceptions.RequestException:
        print("Problem in API request")
        return None

    statistics = {
        "Player Name":player_name,
        "Test Matches":player_stats["data"]["batting"]["test"]["matches"],
        "Test Runs":player_stats["data"]["batting"]["test"]["runs"],
        "ODI Matches":player_stats["data"]["batting"]["odi"]["matches"],
        "ODI Runs":player_stats["data"]["batting"]["odi"]["runs"],
        "T20 Matches":player_stats["data"]["batting"]["t20i"]["matches"],
        "T20 Runs": player_stats["data"]["batting"]["t20i"]["runs"],
    }
    return statistics


if __name__=="__main__":
    player_data = search_player(player_name="hihgiehihet")
    if player_data:
        player_identifier, player_name = player_data
        player_statistics = get_player_statistics(player_identifier=player_identifier,player_name=player_name)
        print(player_statistics)
    else:
        print("Unable to retrieve player statistics.")

        # print(f"Player Test Runs:{player_test_runs}")
        # player_odi_matches = player_stats["data"]["batting"]["odi"]["matches"]
        # print(f"Player ODI Matches:{player_odi_matches}")
        # player_odi_runs = player_stats["data"]["batting"]["odi"]["runs"]
        # print(f"Player ODI Runs:{player_odi_runs}")
        # player_t20_matches = player_stats["data"]["batting"]["t20i"]["matches"]
        # print(f"Player T20 Matches:{player_t20_matches}")
        # player_t20_runs = player_stats["data"]["batting"]["t20i"]["runs"]
        # print(f"Player T20 Runs:{player_t20_runs}")

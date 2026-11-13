import requests
import csv

URl = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2026-27&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

headers = {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "origin": "https://www.nba.com",
    "priority": "u=1, i",
    "referer": "https://www.nba.com/",
    "sec-ch-ua": '"Not:A-Brand";v="8", "Chromium";v="156", "Google Chrome";v="156"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
}


print("Sending request...")
response = requests.get(url=URl,headers=headers,timeout=30)
print("Request completed!")
print(response.status_code)
data = response.json()
players = data["resultSets"][0]["rowSet"]

player_stats = []
for player in players:
    player_data = {
        "player_name":player[1],
        "team_abbreviation":player[4],
        "games_played":player[6],
        "rebounds":player[22],
        "assists":player[23],
        "points":player[30]
    }
    player_stats.append(player_data)
print(len(player_stats))
print(player_stats[0])

with open("Player_Stats.cdv","w",encoding="utf-8") as file:
    writer = csv.DictWriter(file,fieldnames=player_stats[0].keys())
    writer.writeheader()
    writer.writerows(player_stats)
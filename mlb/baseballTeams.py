import requests
import json
import datetime

class team():
    """
    https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&date=5/12/2022
    """
    def __init__(self, jsonObj):
        self.name = jsonObj["teamName"]
        self.location = jsonObj["locationName"]
        self.league = jsonObj["league"]["name"]

    def __str__(self):
        s = f"{self.name} {self.location}"
        return s

def getData():
    """
    :param date: String date in the format MM/DD/YYYY
    :return: JSON object from MLB for all games on the docket on the chosen date
    """
    apiPage = f"https://statsapi.mlb.com/api/v1/teams"
    apidata = requests.get(apiPage) # Load page from MLB
    data = json.loads(apidata.text) # JSON object with all game info for chosen date
    return data["teams"]



def main():

    teams = getData()
    for i in teams:
        thisTeam = team(i)
        print(thisTeam)
    print()

main()
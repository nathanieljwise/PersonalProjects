import requests
import json
import datetime

class game():
    """
    https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&date=5/12/2022
    """
    def __init__(self, jsonObj):
        self.gameDate = jsonObj["gameDate"]
        
        self.startTime = self.gameDate[-9:-4] # HH:MM
        isDaylightSavings = True
        timeDifference = 5
        if isDaylightSavings: 
            self.startHour = (int((self.startTime[:2]) )-4)%24 # Convert from UTC to EDT
        else: 
            self.startHour = (int((self.startTime[:2]) )-5)%24 # Convert from UTC to EST
        self.startMinute =  self.startTime[3:5]
        self.startTime = f"{self.startHour}:{self.startMinute}" # Eastern Time

        self.venue = jsonObj["venue"]["name"] # Ballpark for game
        self.away = jsonObj["teams"]["away"] # Away team dictionary
        self.home = jsonObj["teams"]["home"] # Home team dictionary
        
        self.awayName = jsonObj["teams"]["away"]["team"]["name"] # Away team name
        self.homeName = jsonObj["teams"]["home"]["team"]["name"] # Home team name
        
        self.awayWins = jsonObj["teams"]["away"]["leagueRecord"]["wins"] # Away season wins
        self.awayLosses =jsonObj["teams"]["away"]["leagueRecord"]["losses"] # Away season losses
        self.awayWLRecord = f"{self.awayWins}-{self.awayLosses}" # Away season wins
        
        self.homeWins = jsonObj["teams"]["home"]["leagueRecord"]["wins"] # Home season wins
        self.homeLosses = jsonObj["teams"]["home"]["leagueRecord"]["losses"] # Home season losses
        self.homeWLRecord = f"{self.homeWins}-{self.homeLosses}" # WL record string
        
        self.gameState = jsonObj["status"]["detailedState"] # E.g. Scheduled, PreGame, Warmup, In Progress, Final
        self.awayScore = 0
        self.homeScore = 0
        
        if "score" in jsonObj["teams"]["away"]: # Can be missing key (e.g., game is "Scheduled")
            self.awayScore = jsonObj["teams"]["away"]["score"]
        if "score" in jsonObj["teams"]["home"]: # Can be missing key (e.g., game is "Scheduled") 
            self.homeScore = jsonObj["teams"]["home"]["score"]
            

    def __str__(self):
        s = f"{self.startTime}\t{self.awayName:22} ({self.awayWLRecord:<5})\tvs\t{self.homeName:22} ({self.homeWLRecord:<5})\t{self.awayScore:<2} to {self.homeScore:<2}\t{self.gameState:10}\t{self.venue:22}"
        return s

def getData(date):
    """
    :param date: String date in the format MM/DD/YYYY
    :return: JSON object from MLB for all games on the docket on the chosen date
    """
    apiPage = f"https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&date={date}"
    apidata = requests.get(apiPage) # Load page from MLB
    data = json.loads(apidata.text) # JSON object with all game info for chosen date
    return data["dates"][0]["games"] # All games on schedule from API URL


def getDate():
    """
    :return: Date in the format MM/DD/YYYY
    """
    showPastGames = int(input("Show yesterday's games? 1 for yes, 0 for no. "))
    
    today = datetime.date.today()

    yesterday = today - datetime.timedelta(days = 1)
    yMonth = f"{yesterday.month:02d}" # Two digit month
    yDay = f"{yesterday.day:02d}" # Two digit day
    yYear = f"{yesterday.year:04d}" # Four digit year
    yDate = f"{yMonth}/{yDay}/{yYear}" # Formatted date for API URL


    month = f"{today.month:02d}" # Two digit month
    day = f"{today.day:02d}" # Two digit day
    year = f"{today.year:04d}" # Four digit year
    tDate = f"{month}/{day}/{year}" # Formatted date for API URL

    if showPastGames:
        return yDate
    else:
        return tDate

def printHeader(date):
    """
    Prints date, and column labels.
    """
    print()
    print(f"{date}:")
    print (f"{'START'}\t{'AWAY':27}\t\t{'HOME':27}\t{'SCORE':8}\t{'STATUS':10}\t{'BALLPARK':22}")

def main():
    thisDate = getDate()
    #thisDate = "05/12/2022"
    printHeader(thisDate)
    gamesToday = getData(thisDate)
    for i in gamesToday:
        thisGame = game(i)
        print(thisGame)
    print()

main()

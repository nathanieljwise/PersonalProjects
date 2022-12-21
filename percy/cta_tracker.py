"""
http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=c88f71976c9d4874a05eaf932f80a331&mapid=40380&outputType=JSON
https://www.transitchicago.com/station/wils/
"""

from cta import CTAStation, Prediction, getData, printArrivals, stations


def displayStations():
    """
    Description: Prints a numbered list of all CTA train stations.
    """
    count = 0
    for j in range(0,int(len(stations))//3+1):
        for i in range(0, 3):
            if count < len(stations):
                strCount = str(count+1) + "."
                #print(f" {stations[count-1]['name']:<42} |{stations[i]['id']}|",end="")
                print(f"{strCount:<4} {stations[count]['name']:43}",end="")
                count+=1
        print()


def main():
    displayStations()
    userStation = int(input("\nChoose a station (-1 to quit): "))
    print()

    while userStation > -1:  # -1 to quit
        if userStation == 0:  # Hidden command
            displayStations()
        elif userStation > 142:  # 142 stations in CTA system
            print("Please enter a valid station number.")
        else:
            theseTrains = getData(userStation-1)
            printArrivals(theseTrains)
        userStation = int(input("\nChoose a station (-1 to quit): "))
        print()


main()
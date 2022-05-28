import requests
import xmltodict


class HighwaySign:
    def __init__(self, xmlOBJ):
        self.location = xmlOBJ["location"]
        self.dmsid = xmlOBJ["dmsid"]
        self.name = xmlOBJ["name"]
        self.message = xmlOBJ["message"]
        self.updated = xmlOBJ["updated"]
        self.beacon = xmlOBJ["beacon"]
        self.latitude = xmlOBJ["latitude"]
        self.longitude = xmlOBJ["longitude"]


    def __str__(self):
        s = f"\t{self.message}"
        s = s.replace("<BR>","\n\t")  # Add line break
        s = s.replace("<P>","\n\n\t")  # Add paragraph break
        return s


def loadData(url):
    r = requests.get(url).text
    data_dict = xmltodict.parse(r)
    return data_dict["MessageSigns"]["messageSign"]


if __name__ == "__main__":
    chartURL = "https://chart.maryland.gov//rss/ProduceRss.aspx?Type=DMSXML"
    allSigns = loadData(chartURL)

    for i in allSigns:
        thisSign = HighwaySign(i)
        thisLocation = thisSign.location
        print(thisLocation)
        print(thisSign)
        print()

        """
        thisSign = HighwaySign(i)
        if "I-95" in thisLocation:
            print(thisLocation)
            print(thisSign)
            print()
        """
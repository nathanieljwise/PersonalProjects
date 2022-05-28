import json
import urllib.request
import os
import time
import datetime
from location_water import LocationDataPoints  # My class

now = datetime.datetime.now()
current_time = now.strftime("%Y%m%d %H:%M")

sites = [{"name":"towanda", "id":"01532000"},
		 {"name":"lycoming", "id":"01550000"},
		 {"name":"penns", "id":"01555000"},
		 {"name":"reedy", "id":"02164000"},
		 {"name":"loyalsock", "id":"01552000"}]

log_header = "date\ttime\tstream flow\tgage height\n"

for i in range(len(sites)):
	city = sites[i]["name"]
	file_name = f"{city}_waterflow.txt"
	with open(file_name, "a") as f:
		f.write(log_header)
		f.close()
		
starttime = time.time()
print(f"Started successfully at {starttime}.")
while True:
	for i in range(len(sites)):
		city = sites[i]["name"]
		file_name = f"{city}_waterflow.txt"
		id = sites[i]["id"]
		output = LocationDataPoints(id, city)
		log_point = f"{output.final_output}\n"
		with open(file_name, "a") as log:
			log.write(f"{log_point}")
			log.close()
	time.sleep(3600.0 - ((time.time() - starttime) % 3600.0))

"""
for site in sites:
	api_url = f"https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&sites={site['id']}"
	with urllib.request.urlopen(api_url) as url:
		data = json.loads(url.read().decode())
		
		name = f'{site["name"]}'
		#print(LocationDataPoints.final_output())
		stream_flow = data["value"]["timeSeries"][0]["values"][0]["value"][0]["value"]
		gage_height = data["value"]["timeSeries"][1]["values"][0]["value"][0]["value"]

		print(f'{name}\tStream flow: {stream_flow}\tGage height: {gage_height}')  #Stream flow=(cubic ft)/s; gage height=ft
"""
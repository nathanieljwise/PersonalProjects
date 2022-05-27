import json
import urllib.request
import os
import time
from datetime import datetime

from twython import Twython
import credentials as cred
consumer_key, consumer_secret, open_weather_app_id = cred.consumer_key, cred.consumer_secret, cred.open_weather_app_id
access_token, access_token_secret = cred.buoy_access_token, cred.buoy_access_token_secret


def get_buoy_conditions(txt_file):
	count = 0
	for line in txt_file:  # Go line by line in the .txt
		line = line.decode("utf-8").split()  # .txt files are dumb
		date = "".join([line[0], line[1], line[2]])
		hour = line[3]
		minute = line[4]
		wind_direction = line[5]
		wind_speed = line[6]
		gust = line[7]
		wave_height = line[8]
		dominant_wave_period = line[9]
		average_wave_period = line[10]
		wave_heading = line[11]
		pressure = line[12]
		air_temp = line[13]
		sea_surface_temp = line[14]
		dewpoint_temp = line[15]
		visibility = line[16]
		pressure_tendency =  line[17]
		tide = line[18]
		avail_data = {"Location": "Pismo Beach",  # This dictionary holds the various data points for the buoy
					  "Date": date,  # line[0]=YEAR, line[1]=MONTH, line[2]=DAY
					  "Time": "".join([hour, minute]),  # GMT; line[3]=HOUR, line[4]=MINUTE
					  "Wind direction": wind_direction,
					  "Wind speed": wind_speed,
					  "Gust": gust,
					  "Wave height": wave_height,
					  "Dominant wave period": dominant_wave_period,
					  "Average wave period": average_wave_period,
					  "Wave heading": wave_heading,
					  "Sea level pressure": pressure,
					  "Air temperature": air_temp,
					  "Sea surface temperature": sea_surface_temp,
					  "Dewpoint temperature": dewpoint_temp,
					  "Visiblity": visibility,
					  "Pressure tendency": pressure_tendency,
					  "Tide": tide
					  }
		"""for data_point in avail_data:
		            if avail_data[f"{data_point}"] != "MM":
		                print(f"{data_point}: {avail_data[f'{data_point}']}")"""
		if  count == 2:  # The most recent data is on the third line down
			if int(minute) != 50:  # Full wave data is only available at HH:50
				message = False
				return message
			else:
				message = f'{avail_data["Date"]}\t{avail_data["Time"]}\t ' \
						  f'{avail_data["Wind speed"]}\t{avail_data["Wind direction"]}\t{avail_data["Gust"]}\t' \
						  f'{avail_data["Wave height"]}\t{avail_data["Wave heading"]}\t' \
						  f'{avail_data["Dominant wave period"]}\t{avail_data["Average wave period"]}\t' \
						  f'{avail_data["Sea level pressure"]}\n'
				return message
		count += 1

starttime = time.time()
while True:
	# https://www.ndbc.noaa.gov/station_page.php?station=46011
	site = "46011"
	ndbc_url = f"https://www.ndbc.noaa.gov/data/realtime2/{site}.txt"
	data = urllib.request.urlopen(ndbc_url)
	message = get_buoy_conditions(data)
	file_name = "santa_maria_buoy.txt"

	now = datetime.now()
	hour = str((int(now.strftime("%H"))-3)%24)
	minute = now.strftime("%M")
	time_string_pacific = "".join([hour, minute])

	#time_string = "".join([hour, minute])
	if message:
		log_point = f"{message}"
		with open(file_name, "a") as log:
			log.write(f"{log_point}")
			log.close()
	data.close()
	time.sleep(600.0 - ((time.time() - starttime) % 600.0))
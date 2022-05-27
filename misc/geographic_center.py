#Initialize empty lists to hold latitude values and longitude values
lats =[]
longs = []

while True:
	#Get all the coordinates in the form 123.456,456.789
	print('Enter a latitude and longitude separated by a comma (no space). Type "Done" when done.')
	try:
		lat_long = input()
		coords = lat_long.split(',')
		lat = float(coords[0])
		long = float(coords[1])
		#Add the new input to the lists.
		lats.append(lat)
		longs.append(long)

	except ValueError:
		#Print comma delimited list of only latitude/longitude values
		print(lats)
		print(longs)
		
		#Average the values
		avg_lat = sum(lats) / len(lats)
		avg_long = sum(longs) / len(longs)
		break
#Show the user
print("Your geographic center is " + str(avg_lat) + ", " + str(avg_long) + ".")

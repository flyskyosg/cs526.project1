import csv

f = open('Crimes2013_2_no_xy.csv', 'rb')
res = open('Crimes2013_3_final.csv', 'wb')
csvread = csv.reader(f)
csvwrite = csv.writer(res)
count = 0
for line in csvread:
	# ROBBERY & HOMICIDE & MOTOR VEHICLE THEFT
	if (cmp(line[2],'ROBBERY') == 0) or (cmp(line[2], 'HOMICIDE') == 0) or (cmp(line[2], 'MOTOR VEHICLE THEFT') == 0):
		csvwrite.writerow(line)
		count+=1
		print count
	else:
		# CRIMINAL DAMAGE that TO CITY OF CHICAGO PROPERTY or end with VANDALISM
		if (cmp(line[2], 'CRIMINAL DAMAGE') == 0) and (cmp(line[3], 'TO CITY OF CHICAGO PROPERTY')==0 or line[3].endswith('VANDALISM')):
			csvwrite.writerow(line)
			count+=1
			print count
		else:
			# THEFT that is OVER $500
			if (cmp(line[2], 'THEFT')==0) and (cmp(line[3], 'OVER $500')==0):
				csvwrite.writerow(line)
				count+=1
				print count
			else:
				# ASSULT & CRIM SEXUAL ASSAULT that start with AGGRAVATED
				if (cmp(line[2], 'ASSAULT')==0) or (cmp(line[2], 'CRIM SEXUAL ASSAULT')==0):
					if (line[3].find('AGGRAVATED') == 0): # start 
						csvwrite.writerow(line)
						count+=1
						print count
				else:
					# BURGLARY that is FORCIBEL ENTRY
					if (cmp(line[2], 'BURGLARY') == 0) and (cmp(line[3], 'FORCIBLE ENTRY')==0):
						csvwrite.writerow(line)
						count+=1
						print count	
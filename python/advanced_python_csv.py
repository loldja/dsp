import csv, re, numpy as np

##lines 5-21 copied over from previous exercise##

def get_data(csv_file):
	with open(csv_file, 'r') as f:
		csv_file = [row for row in csv.reader(f.read().splitlines())]
		return csv_file

def mailing_list(parsed_data):
	emailRegex = re.compile(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]')		#define email pattern match
	flat_list = [item for sublist in parsed_data for item in sublist]
	email_list=[row for row in flat_list if re.findall(emailRegex, row)]
	return email_list


#############################################################

data = 'faculty.csv'
parsed_data = get_data(data)
mailing_list = mailing_list(parsed_data)


#############################################################

###Output file of email addresses

outputFile = open('emails.csv','w')
outputWriter = csv.writer(outputFile)
for item in mailing_list:
	outputWriter.writerow([item])
outputFile.close()
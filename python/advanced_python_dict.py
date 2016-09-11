import csv, re, numpy as np

def get_data(csv_file):
	with open(csv_file, 'r') as f:
		csv_file = [row for row in csv.reader(f.read().splitlines())]
		return csv_file

def get_faculty_dict(parsed_data):
	del(parsed_data[0])			#removes headers
	faculty_dict = {}
	for i in range(len(parsed_data)):
		key = parsed_data[i][0].rsplit(None,1)[-1]
		degree = parsed_data[i][1].strip()
		title = parsed_data[i][2].replace(" of Biostatistics",'').replace(" is Biostatistics",'')
		email = parsed_data[i][3]
		faculty_dict.update({key: [degree, title, email]})
	return faculty_dict

def get_prof_dict(parsed_data):
	del(parsed_data[0])			#removes headers
	faculty_dict = {}
	for i in range(len(parsed_data)):
		fname = parsed_data[i][0].split(None,1)[0]
		lname = parsed_data[i][0].rsplit(None,1)[-1]
		degree = parsed_data[i][1].strip()
		title = parsed_data[i][2].replace(" of Biostatistics",'').replace(" is Biostatistics",'')
		email = parsed_data[i][3]
		faculty_dict.update({str(fname) + " " + str(lname): [degree, title, email]})
	return faculty_dict


def get_prof_dict_lname(parsed_data):
	del(parsed_data[0])			#removes headers
	faculty_dict = {}
	for i in range(len(parsed_data)):
		fname = parsed_data[i][0].split(None,1)[0]
		lname = parsed_data[i][0].rsplit(None,1)[-1]
		degree = parsed_data[i][1].strip()
		title = parsed_data[i][2].replace(" of Biostatistics",'').replace(" is Biostatistics",'')
		email = parsed_data[i][3]
		faculty_dict.update({str(lname) + ", " + str(fname): [degree, title, email]})
	return faculty_dict


#############################################################

data = 'faculty.csv'
parsed_data = get_data(data)

faculty_dict = get_faculty_dict(parsed_data)

#Q6

print "\nFirst three key/value pairs for dictionary sorted by last name only: "
count = 0
for key in sorted(faculty_dict):
	if count < 3:
		print key, faculty_dict[key]
	count += 1

#Q7

professor_dict = get_prof_dict(parsed_data)

print "\nFirst three key/value pairs for dictionary sorted by first name/ last name: "
count = 0
for key in sorted(professor_dict):
	if count < 3:
		print key, professor_dict[key]
	count += 1

#Q7

lname_dict = get_prof_dict_lname(parsed_data)

print "\nFirst three key/value pairs for dictionary sorted by last name/ first name: "
for key in sorted(lname_dict):
	print key, lname_dict[key]



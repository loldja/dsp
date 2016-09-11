import csv, re, numpy as np

def get_data(csv_file):
	with open(csv_file, 'r') as f:
		csv_file = [row for row in csv.reader(f.read().splitlines())]
		return csv_file

def freq_degrees(parsed_data):
	del(parsed_data[0])			#removes headers
	get_degree_col = []
	for i in range(len(parsed_data)):
		degrees = parsed_data[i][1].split()
		get_degree_col.append(degrees)

	flat_list = [item for sublist in get_degree_col for item in sublist]
	listRegex = [re.compile(r'((Ph)(\.)*(D)(\.)*)'), 					#[0]PhD
				re.compile(r'((Sc)(\.)*(D)(\.)*)'),						#[1]ScD
				re.compile(r'((M)(\.)*(D)(\.)*)'),						#[2]MD
				re.compile(r'((J)(\.)*(D)(\.)*)'),						#[2]JD
				re.compile(r'((M)(\.)*(S)(\.)*)'),						#[4]MS
				re.compile(r'((M)(\.)*(S)(\.)*(P)(\.)*(H)(\.)*)'),		#[5]MSPH
				re.compile(r'((M)(\.)*(P)(\.)*(H)(\.)*)'),				#[6]MPH
				re.compile(r'((M)(\.)*(B)(\.)*(A)(\.)*)'),				#[7]MBA
				re.compile(r'((M)(\.)*(A)(\.)*)'),						#[8]MA
				re.compile(r'((B)(\.)*(S)(\.)*(Ed)(\.)*)')				#[9]BSEd
				]

	degree_count = [0]*len(listRegex)
	degree_list = ['PhD','ScD','MD','JD','MS','MSPH','MPH','MBA','MA','BSEd']
	for i in range(len(flat_list)):
		for j in range(len(listRegex)):
			if listRegex[j].findall(flat_list[i]) != []:
				degree_count[j] += 1
	print zip(degree_list, degree_count)


def title_count(parsed_data):

	get_title_col = []
	for i in range(len(parsed_data)):
		get_title_col.append(parsed_data[i][2])

	#flat_list = [item for sublist in get_title_col for item in sublist]
	x = np.array(get_title_col)
	unique, counts = np.unique(x, return_counts=True)
	return np.asarray((unique, counts)).T


#def mailing_list_old(parsed_data):
#	emailRegex = re.compile(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]')		#define email pattern match
#	flat_list = [item for sublist in parsed_data for item in sublist]
#	email_list=[]
#	for row in flat_list:
#		if re.findall(emailRegex, row):
#			email_list.append(row)
#	return email_list

def mailing_list(parsed_data):
	emailRegex = re.compile(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]')		#define email pattern match
	flat_list = [item for sublist in parsed_data for item in sublist]
	email_list=[row for row in flat_list if re.findall(emailRegex, row)]
	return email_list

def unique_domains(mailing_list):
	domain_list=[]
	for row in mailing_list:
		domain_list.append(row[row.find('@'):])
	#unique_domain_list = [row for row in mailing_list if row[row.find('@'):]]

	x = np.array(domain_list)
	unique = np.unique(x)
	return [len(unique), np.asarray(unique)]


#############################################################

data = 'faculty.csv'
parsed_data = get_data(data)

#Q1

print "Frequency table for the following degrees: "
print freq_degrees(parsed_data)

#Q2

print "Frequency table for job titles: "
print title_count(parsed_data)

#Q3

print "Here's a list of email addresses: "
mailing_list = mailing_list(parsed_data)
print mailing_list

#Q4

print "This a count of unique email domains, followed by a list: "
print unique_domains(mailing_list)
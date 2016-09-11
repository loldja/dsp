import csv

def read_data(data):
   readFile = open(data)
   readReader = csv.reader(readFile)
   readData = list(readReader)
   return readData
	
def get_min_score_index(parsed_data):
	parsed_data.pop(0)
	goals = [x[5] for x in parsed_data]
	goals_allowed = [x[6] for x in parsed_data]
	goal_diff = [abs(float(x)-float(y)) for x, y in zip(goals, goals_allowed)]
	return [goal_diff[goal_diff.index(min(goal_diff))], goal_diff.index(min(goal_diff))]

def get_team(parsed_data, index):
	parsed_data.pop(0)
	team_name = [x[0] for x in parsed_data]
	return team_name[index[1]]



parsed_data = read_data('football.csv')
team_and_index = get_min_score_index(parsed_data)



print "The team with the smallest difference is", get_team(parsed_data, team_and_index), "with a difference of", team_and_index[0], "goals between goals scored and goals scored upon"
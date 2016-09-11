# Hint:  use Google to find python function

from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

def __datetime(date_str):
	return datetime.strptime(date_str, '%m-%d-%Y')

start = __datetime(date_start)
end = __datetime(date_stop)

delta = end-start
print 'Between ' + date_start + ' and ' + date_stop + ' there are ' + str(delta) + ' seconds'

####b)  
date_start = '12312013'  
date_stop = '05282015'  

def __datetime2(date_str):
	return datetime.strptime(date_str, '%m%d%Y')

start = __datetime2(date_start)
end = __datetime2(date_stop)

delta = end-start
print 'Between ' + date_start + ' and ' + date_stop + ' there are ' + str(delta) + ' seconds'


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

def __datetime3(date_str):
	return datetime.strptime(date_str, '%d-%b-%Y')

start = __datetime3(date_start)
end = __datetime3(date_stop)

delta = end-start
print 'Between ' + date_start + ' and ' + date_stop + ' there are ' + str(delta) + ' seconds'

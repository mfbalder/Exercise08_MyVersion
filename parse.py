import re

f = open('parsed_parks.txt')
f_new = open('parks_and_rec.txt', 'w')

f_new.truncate()
for line in f:
	line = re.sub('==[^>]+>==', '', line).replace("'''", "")
	f_new.write(line)



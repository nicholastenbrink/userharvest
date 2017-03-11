# to extract users to inject into JIRA via API

import re

names = "SupportAll.txt"  #source of users

harvestedUsergroup = open("harvestedusers.txt","a")  #target to drop users into

namePool = open(names, 'r')

stringOut = ""

email_pattern = re.compile('([\w\-\.]+)@(\w[\w\-]+\.)+[\w\-]+')

for line in namePool:
	for match in email_pattern.findall(line):
		stringOut = ('"'+ match[0] + '"')+ ', ' + stringOut


print stringOut
harvestedUsergroup.write(stringOut)  #writes stringOut to file
harvestedUsergroup.close()  # closes file

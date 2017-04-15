#!/usr/bin/env	python3

""" author: qwart 2.0 | twitter: @qwartz_ """
# Credits for page: http://stalkscan.com/ & RedBird

import sys,os
import doxing

time=""
user_id=""
relationship_status=""

#colors
cyan="\033[1;36m"
green="\033[1;32m"
red="\033[1;31m"
yellow="\033[33m"
reset="\033[00m"

def banner():
	print("""         _        _ _             
        | |      | | |            
     ___| |_ __ _| | | _____ _ __ 
    / __| __/ _` | | |/ / _ \ '__|
    \__ \ || (_| | |   <  __/ |   
    |___/\__\__,_|_|_|\_\___|_|
 %sAuthor:%sqwartz 2.0 | %sTwitter:%s@qwartz_\n"""%(green,reset,cyan,reset))

def help():
	print('''            %sHelp Stalker%s
 show options      View search options
 set option=value  Set value from element
 run               Start
 reset             Reset values
 clear	           Clear current screen
 help              Show help
 quit	           Close stalker
	'''%(yellow,reset))

def show_options():
	if user_id == "":
		print(red+" -"+reset, "id: ("+red+"is required"+reset+")")
	else:
		print(green+" +"+reset, "id: "+user_id)
	if time == "":
		print(red+" -"+reset, "time: ("+yellow+"optional"+reset+") today | this-week | this-month | 20XX")
	else:
		print(green+" +"+reset, "time: "+time)
	if relationship_status == "":
		print(red+" -"+reset, "relationship_status: ("+yellow+"optional"+reset+") single | engaged | married")
	else:
		print(green+" +"+reset, "relationship_status: "+relationship_status)

os.system('clear')
banner()
action = False

while action == False:
	
	input_user = input("➜ stalket› ")
	new_input_user = input_user.split('=')
	
	if new_input_user[0] == "set time":
		time=new_input_user[1]
	elif new_input_user[0] == "set id":
		user_id=new_input_user[1]
	elif new_input_user[0] == "set relationship_status":
		relationship_status=new_input_user[1]
	
	elif input_user == "help":
		help()
	elif input_user == "show options":
		show_options()
	elif input_user == "run":
		doxing.run(user_id, time, relationship_status)
	elif input_user == "quit":
		sys.exit()
	elif input_user == "reset":
		time=""
		user_id=""
		relationship_status=""
	elif input_user == "clear":
		os.system('clear')
	else:
		help()
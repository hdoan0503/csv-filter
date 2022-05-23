# csv-filter
# How-To
The easiest way to run this problem is to click the "play" button from an IDE
This program can also be run by using command line "python3 main.py"

# Assumptions
I assume the csv file will be provided, so I created a csv function to accept the any csv file and start to parse them into a list of record\
I assume the user will enter first name, last name "OR" birth year whichever they want to enter we will filter the record for them\
I assume the first name or last name from the user input have to be matched exactly our record which means if the user want to search for Bobby but the user just enter Bob, the program will not return the record which have the name Bobby. (1)\
I assume the user only need to enter birth year, if the user enter the whole dob, the program will not return the result. (2)\
From (1) and (2) I assume no wildcards search is allowed. If in the future, the user want to use the wildcards search, we can improve the program.\
I assume no case sensitive which means the user can either enter Bobby or bobby and the program can still filter out the results.
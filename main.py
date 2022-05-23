"""
@File: main.py
@Author: Hieu Doan
@Date: 05/23/2022
@version 0.1
@Description: This program will read the csv file and filter the results based on user input.

@copyright Copyright (c) 2022
"""
import csv

#This function will read the provided csv and parse into a easy to work with data structure which is list
def csv_parser(filename):
    records = []
    with open(filename, 'r', encoding='utf-8-sig') as csv_file: #open and read csv files
        reader = csv.reader(csv_file)
        header = next(reader)
        
        for row in reader:
            records.append(row)
    
    return header, records

#This function will take the records, ask for user input and start to filter out the result
def filterRequest(records):
    result = []
    
    userInput = input("Enter first name, last name or birth year: ")
    
    #Check if user input is birth year?
    try:
        int(userInput)
        isBirthYear = True
    except ValueError:
        isBirthYear = False

    #If it's the birth year, filter out the dob that match the birth year from user input 
    if isBirthYear:
        for i in records:
            if(userInput == i[2][0:4]):
                result.append(i) #if match, store the record into a result
    
    #If not a birth year, filter out the first name and last name that match user input
    else:
        for i in records:
            if(userInput.capitalize() == i[0] or userInput.capitalize() == i[1]):
                result.append(i) #if match, store the record into a result
    return result



if __name__ == "__main__":
    header, records = csv_parser('example.csv')
    results = filterRequest(records)
    ##print out the result
    print("------------Results--------------")
    print(",".join(header))
    for i in results:
        print(",".join(i))


    

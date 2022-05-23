"""
@File: main.py
@Author: Hieu Doan
@Date: 05/23/2022
@version 0.1
@Description: This program will read the csv file and filter the results based on user input.

@copyright Copyright (c) 2022
"""
import csv

def csv_parser(filename):
    records = []
    with open(filename, 'r', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        
        for row in reader:
            records.append(row)
    
    return header, records


def filterRequest(records):
    result = []
    
    userInput = input("Enter first name, last name or birth year: ")
    try:
        int(userInput)
        isDob = True
    except ValueError:
        isDob = False

    if isDob:
        for i in records:
            if(userInput == i[2][0:4]):
                result.append(i)
    else:
        for i in records:
            if(userInput.capitalize() == i[0] or userInput.capitalize() == i[1]):
                result.append(i)
    return result



if __name__ == "__main__":
    header, records = csv_parser('example.csv')
    results = filterRequest(records)

    print("------------Results--------------")
    print(",".join(header))
    for i in results:
        print(",".join(i))


    

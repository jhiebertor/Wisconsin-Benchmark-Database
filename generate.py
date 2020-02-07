#James Hiebert
#CS487P Winter 2020
#Project Part 1
#This file contains code called in main to generate csv files containing 
#data according to the Wisconsin Benchmark
import csv
import numpy
import itertools
        
#Given a file name and the number of tuples to create, generate a csv file
#containing columns that match the specifications of the Wisconsin Benchmark paper
def generateBenchmarkData(filename, MAXTUPLES):
    with open(filename, 'w') as file:
        #Open file
        output = csv.writer(file, delimiter=',', lineterminator='\n')
        #Generate all values for each attribute
        
        #Create ints from 0 to MAXTUPLES-1 and randomize them
        unique1 = numpy.arange(0, MAXTUPLES)
        numpy.random.shuffle(unique1)
        
        #Create ints from 0 to MAXTUPLES-1 and randomize them
        unique2 = numpy.arange(0, MAXTUPLES)
        numpy.random.shuffle(unique2)
        
        #Cycles 0, 1, 0, 1, ... creating MAXTUPLES number of entries
        two = numpy.arange(0, MAXTUPLES)
        #Create array from 0 to MAXTUPLES-1 and element-wise modulo by 2
        two = two % 2
        #Cycles 0, 1, 2, 3, 0, ...
        four = numpy.arange(0, MAXTUPLES)
        four = four % 4
        #Cycles from 0-9 repeating
        ten = numpy.arange(0, MAXTUPLES)
        ten = ten % 10
        #Cycles from 0-19 repeating
        twenty = numpy.arange(0, MAXTUPLES)
        twenty = twenty % 20
        #Cycles from 0-99 repeating
        hundred = numpy.arange(0, MAXTUPLES)
        hundred = hundred % 100
        #Cycles from 0-999 repeating
        thousand = numpy.arange(0, MAXTUPLES)
        thousand = thousand % 1000
        #Cycles from 0-1999 repeating
        twothous = numpy.arange(0, MAXTUPLES)
        twothous = twothous % 2000
        #Cycles from 0-4999 repeating
        fivethous = numpy.arange(0, MAXTUPLES)
        fivethous = fivethous % 5000
        #Cycles from 0-9999 repeating
        tenthous = numpy.arange(0, MAXTUPLES)
        tenthous = tenthous % 10000
        #Cycles odd numbers from 0-100 repeating: 1, 3,..., 99, 1, ...
        odd100 = numpy.linspace(1, (2*MAXTUPLES)-1, MAXTUPLES, dtype=int)
        odd100 = odd100 % 100
        #Cycles even numbers from 2 to 100, repeating: 2, 4, ..., 100, 2...
        even100 = numpy.linspace(0, (2*MAXTUPLES)-2, MAXTUPLES, dtype=int)
        even100 = (even100 % 100) + 2
        
        #Generate string attributes
        
        #Generate list of chars from A-V
        charList = []
        for num in range(65, 87):
            charList.append(chr(num))
        
        #To ensure we get unique combinations of random characters we create 3 copies of our character list and shuffle them   
        stringu1 = []
        combinations = [] #holds unique random 3 character combinations
        for i in itertools.product(charList, repeat=3):
            combinations.append(i)
        numpy.random.shuffle(combinations)
        for i in range(MAXTUPLES):
            stringu1.append(combinations[i][0] + 'xxxxxxxxxxxxxxxxxxxxxxxxx' + combinations[i][1] + 'xxxxxxxxxxxxxxxxxxxxxxxx' + combinations[i][2])
                        
        
        stringu2 = []
        for i in charList:
            for j in charList:
                for k in charList:
                    if(len(stringu2) < MAXTUPLES):
                        stringu2.append(k + 'xxxxxxxxxxxxxxxxxxxxxxxxx' + j + 'xxxxxxxxxxxxxxxxxxxxxxxx' + i)
        
        string4 = []
        string4charList = ['A', 'H', 'O', 'V']
        for i in range(0, MAXTUPLES):
            tempChar = string4charList[i % 4]
            string4.append(tempChar + 'xxxxxxxxxxxxxxxxxxxxxxxxx' + tempChar + 'xxxxxxxxxxxxxxxxxxxxxxxx' + tempChar)
            
        #Now that all attributes are generated, iterate through them to create tuples and write them to csv
        for i in range(MAXTUPLES):
            output.writerow([unique1[i], unique2[i], two[i], four[i], ten[i], twenty[i], hundred[i], thousand[i],
                            twothous[i], fivethous[i], tenthous[i], odd100[i], even100[i], stringu1[i], stringu2[i], string4[i]])
                            
        
        
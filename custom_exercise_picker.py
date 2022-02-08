# PYTHON Version - This program will prompt user for input and based on that input the program will generate a custom plan of exercises
# All exercise plans are well thought out and have been personaly tested in the gym by myself
# Have fun!


import math
import csv
from os import write
from typing import ContextManager
#------------------------------------menu functions
def goalmenu():
    print ("\nWhat are you're fitness goals? ")
    print ("\n Stay in shape? [Press 1] ")
    print("\n Loose Weight? [Press 2] ")
    print("\n Gain size or strength? [Press 3] ")   
    print("\n Press [q] to quit")
def experiancemenu():
    print ("\nWhat is you're current workout experiance? ")
    print ("\n None or less than 1 year, [Press 1] ")
    print ("\n Less than 2 years? [Press 2] ")
    print ("\n More than 2 years? [Press 3] ")
    print("\n Press [q] to quit")
# --------------------------------------frequentcy functions (how often to workout)
def beginfreq():
    print("\n This plan requires 3 of theses workouts each week, We recomend doing these workouts everyother day \n")
    print("\n After 6 weeks of this routine run this again and update experiance to 2")
def interfreq():
    print("\n This plan requires 4 of these workouts each week unless instructed otherwise, choose rest days accordingly \n")
    print("\n After 6 weeks of this routine run this again and update experiance to 3")
def advancedfreq():
    print ("\n This is an advanced program, Workouts to be done 6 days a week, rest on day 7\n")
def diet():
    print("\n DIET:")
    print("\n DO NOT eat or drink the following:")
    print("\n Soda, Candy, Fast Food, Pizza, Chocolate, Ice cream, Bacon, Heavy sodium, or fast carbs like pasta")
    print('\n Try to Avoid: \n Excess Alcohol, Processed foods, Artificial Sugars, and red meat unless bulking \n')
#--------------------------------------function that reads file, prints to terminal and output file with proper syntax
def filereader(filename):
    outstring = ''
    with open(filename) as file:
            content = file.read().splitlines()
            for line in content:
                cols = (line.split(','))
                for column in cols:
                    outstring += column + "\t"
                outstring += "\n"
    print(outstring)
# ------------------------------outputs to file
    outfile =open('List of Exercises to Try.csv','w')
    outfile.write(outstring)
#-------------------------------while loop to start user inputs
while True:
    goalmenu()
    goals = input()
    experiancemenu()
    experiance = input ()
#------------- stay in shape goal programs--------------------
    if goals == '1' and experiance == '1':
        print ("\n Your workout plan: BEGINNER SHAPE")
        beginfreq()
        diet()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\beginshape.csv') #reading file to program by calling function
    elif goals == '1' and experiance == '2':
        print('\n Your workout plan: INTERMEDIATE SHAPE')
        interfreq()
        diet()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\intershape.csv')
    elif goals == '1' and experiance == '3':
        print("\n Your workout plan: ADVANCED SHAPE")
        print('\n Full body workout: train 3-5 times per week')
        diet()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\advancedshape.csv')
#------------- loose weight goal programs--------------------
    elif goals =='2' and experiance == '1':
        print ('\n Your workout plan: BEGINNER CUT')
        beginfreq()
        diet()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\begincut.csv')
    elif goals =='2' and experiance == '2':
        print ('\n Your workout plan: INTERMEDIATE CUT')
        interfreq()
        diet()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\intercut.csv')
    elif goals =='2' and experiance == '3':
        print ('\n Your workout plan: ADVANCED CUT')
        diet()
        advancedfreq()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\advancedcut.csv')
#------------------SIZE AND STRENGTH GOAL PROGRAMS-------------
    elif goals =='3' and experiance == '1':
        print ('\n Your workout plan: BEGINNER BULK')
        beginfreq()
        diet()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\beginbulk.csv')
    elif goals =='3' and experiance == '2':
        print ('\n Your workout plan: INTERMEDIATE BULK')
        interfreq()
        diet()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\interbulk.csv')
    elif goals =='3' and experiance == '3':
        print ('\n Your workout plan: ADVANCED BULK')
        advancedfreq()
        diet()
        filereader(r'C:\Users\CEO of S&P\Desktop\SUNY Albany\Fall 2021\INF 308\seans308respository\inf308fall2021-SeanFerris\Personal_Project_files\advancedbulk.csv')
#---------------------------------------------------help option of menu
    elif goals == 'help' or experiance == 'help':
        goalmenu()
        experiancemenu()
#-----------------------------------------------------quit function: ends loop
    elif goals == 'q' or experiance == 'q':
        print("\n Thank you, you can check your files for you're new workout plan! ")
        break
#-----------------------------------------------wrong input failsafe
    else:
        print("\n Please choose from the options listed or type 'help' to see options")

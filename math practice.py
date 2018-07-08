# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 22:50:45 2018

@author: Milan Lamsal
"""
import random  # library that is used to generate random number

# function to that perform mathematical operations and check ##
def practice(choice):
    
    ## ramdom numbers generation
    number_1 = random.randint(1,101)
    number_2 = random.randint(1,10)
    
    #performs calculation according to input
    
    ##### performs addition
    if(choice=='a' or choice=='A'):                        
        answer = int(input(str(number_1) +'+'+str(number_2)+ ' = '))  # take answer from user
        if (answer==(number_1+number_2)):
            print('correct!!!! You are good')
            return
        else:
            print('incorrect!!!! Practice more')
            print(number_1, '+',number_2, ' = ',(number_1+number_2))
            return
        
    #### if choice is for multiplication ######
    elif (choice=='M' or choice=='m'):
        answer = int(input(str(number_1) +'*'+str(number_2)+ ' = '))  # takes answer as input
        if (answer==(number_1*number_2)):
            print('Correct!!! Great ')
            return
        else:
            print('incorrect!!!!! Practise more')
            print(number_1, '*',number_2, ' = ',(number_1*number_2))
            return
        
    ####  if input is other than a,m,q  
    else:
        print('Invalid input')
        print('Please enter valid data')
        return
    

#### main function to start program execution #######
def main():   
    print('enter:::')
    print('a => addition')
    print('m => multiplication')
    print( 'q => quit')

    while True:
        choice = input('enter you choice (a/m/q)')
        if(choice=='q' or choice=='q'): 
            break                                  ## quits the program for input q
        else:
            practice(choice)
        
if( __name__=='__main__'):
    main()       

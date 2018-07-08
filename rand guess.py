# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 23:20:44 2018

@author: Milan
"""
import random

def main():
    rand_number = random.randint(1,101)       ## random number between 1 and 100

    ## initialize initial minimum and maximum value
    min_val = 1
    max_val=100
    
    print('A random number has been generate between 1 and 100')
    while True:
        guess = int(input('Make a guess ') )                       
        if(rand_number==guess):
            print('Congratulations!!!! You got the right number')
            print('')
            return
        elif(rand_number<guess):
            max_val = guess      #number can't be more than guess
        else:
            min_val = guess      #number can't be less than guess
                
        print('Wrong!!!! the number is between ',min_val,' and ', max_val)
        print('')
    
    
if(__name__=='__main__'):
    main()
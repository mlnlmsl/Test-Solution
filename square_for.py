# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:00:43 2018

@author: Milan
"""

def main():
    min_num=int(input('enter minimun number to take square'))
    max_num=int(input('enter maximun number to take square'))
    
    #### checking valid input
    if(max_num<min_num):
        print('invalid input !!!! ')
        return
    
    number_list=[i for i in range(min_num,max_num+1)]
    
    ### list containing square of numbers between minimun and maximum number
    square_list=[i*i for i in range(min_num,max_num+1)] 

    ##### list containing the last digit of the number
    last_digit =[square_num%10 for square_num in square_list]
    
    number_lenght=len(square_list)    #lenght of the list

    ## formatting the output
    print('{:<10} {:>5} {:^20}'.format('number','squares','last digits'))
    for i in range(number_lenght):
        print('{:<10} {:>5} {:^20}'.format(number_list[i],
                                           square_list[i],
                                           last_digit[i]))
        
if __name__=='__main__' :
    main()
    
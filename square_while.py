# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:16:03 2018

@author: Milan
"""

def main():
    square_list=[]
    num_list=[]
    lastdigit_list=[]
    
    min_num=int(input('enter minimun number to take square'))
    max_num=int(input('enter maximun number to take square'))
    
    ### checking valid user data
    #### if user enter max_value<min_value, it results invalid condition
    if(max_num<min_num):
        print('invalid input !!!! ')
        return
    
    ### preparing the list of the required fields
    while(min_num<=max_num):
        square_list.append(min_num**2)
        num_list.append(min_num)
        lastdigit_list.append((min_num)%10)
        min_num=min_num+1
    
    number_lenght=len(square_list)
    
    ##### formatting the display
    print('{:<10} {:>5} {:^20}'.format('number','squares','last digits'))
    for i in range(number_lenght):
        print('{:<10} {:>5} {:^20}'.format(num_list[i],
                                           square_list[i],
                                           lastdigit_list[i]))
        
        
if __name__=='__main__':
    main()

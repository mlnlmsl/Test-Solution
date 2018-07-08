# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:25:07 2018

@author: Milan
"""

### fucntion to calculate interest and principle a 
def calculate_interest(p,t,r):
    principle =[p]   #to initialize the start of year balance
    interest =[]
    for i in range(0,t):
        interest.append(p*(i+1)*r/100)
        principle.append(p+interest[i])
        p=principle[i+1]
    yearly_transaction={
        'interest':interest,
        'principle':principle
    }
    return yearly_transaction     ### returns dictionary of interest and principle
 
## fucntion to display fromatted output
    
def display(transaction,duration):
    print('{:<10}{:<20}{:^25}{:>25}'.format(' ',
                                            'start of year',
                                            'interest ',
                                            'end of year'
                                            ))
    for i in range(duration):
        print('{:<10}{:<20.2f}{:^25.2f}{:>25.2f}'.format(i+1,
                                                transaction['principle'][i],
                                                transaction['interest'][i],
                                                transaction['principle'][i+1]
                                           ))

def main():
    
    #user data 
    principle_amount=int(input('enter the principle amount '))
    interest_rate = float(input('enter interest rate '))
    duration = int(input('enter year of duration '))
    
    transaction = calculate_interest(principle_amount,duration, interest_rate)
    
    display( transaction ,duration)
    
    
if __name__=='__main__':
    main()
    
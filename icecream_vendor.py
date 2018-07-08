# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 06:51:11 2018

@author: Milan
"""

class ice_cream():
    def __init__(self,flavor,size,topping):
        self.flavor=flavor
        self.size=size
        self.topping=topping
        self.total=0

    ### class instance to calculate total only    
    def order_total(self):
        if (self.size == 's' or self.size == 'S' ):
            if(self.topping =='Y' or self.topping == 'y'):
                self.total=6
            else:
                self.total=5
        elif(self.size == 'm' or self.size == 'M'):
            if(self.topping =='Y' or self.topping == 'y'):
                self.total=8
            else:
                self.total=7
        elif(self.size == 'l' or self.size == 'L'):
            if(self.topping =='Y' or self.topping == 'y'):
                self.total=11
            else:
                self.total=10
        else:
            self.total=0

    ## display the order items and total
    def display_order(self):
        print('{:*<50}'.format(''))
        if (self.total!=0):             ## total !=0 implies the valid user entry
            if (self.topping =='Y' or self.topping == 'y'):
                print('{} {} ${}'.format((self.flavor),
                                          ('choc topping'),
                                          (self.total)))
            else:
                print('{} : ${}'.format((self.flavor),(self.total)))
        else:
            print('Please Make a Valid entryt')
            return
        
        print('thank you for order ')
        print('{:*<50}'.format('')) 
        
def main():
    flavor_list = ['Banana',
                   'Almond Macaron',
                   'Baseball Nut', 
                   'Citrus Twist Ice',
                   'Cookies n Cream']
    
    print('{:*<50}'.format(''))
    print('{:*^50}'.format('Welcome to Joe\'s Ice Cream Shop!',))
    print('{:*<50}'.format('')) 
    print('Small $5, Medium $7, Large $10 ')
    print('\n Please make you order :::')
    print(""" flavors:
          1 - banana
          2 - Almond Macaron
          3 - Baseball Nut
          4 - Citrus Twist Ice
          5 - Cookies n Cream
        """)
    flavor = int(input('Please Select Flavor(1-5) : '))
    size = input('Please Select size(s/m/l) : ')
    topping = input('Chocolate topping for an extra $1? (Y/N): ')
    
    order = ice_cream(flavor_list[flavor-1], size, topping)
    order.order_total()
    order.display_order()    
  


if __name__=='__main__':
    main()        
#calculate price w/tax
#Tax Caclulator function
def tax_calculator(price):
    price = price
    tax_rate = .0625 #current texas tax rate
    calculate_tax = price * tax_rate #getting the taxes by multiplying tax rate with price of item
    price_with_tax = price + calculate_tax #getting total by adding the calculated tax with price of item
    return 'Total price w/ taxes is {:.2f} '.format(price_with_tax)  #returning total item price, formatted using {:.2f} expression. 
                                                        #this is done by starting the formatting using {:} 
                                                        #then using {:.2f} f = formatting float number (a decimal)
                                                        #and .2 = up to 2 digits from decimal dot 
price = input('Enter price of item: ')
print(tax_calculator(float(price)))
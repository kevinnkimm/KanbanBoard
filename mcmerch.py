import sys

def parseArgument():
    arguments = {
        "price": int(sys.argv[1]),
        "quantity": sys.argv[2],
        "province": sys.argv[3]
    }
    
    return arguments

def taxRate(province):
    tax = {
        "ON": 0.13
    }
    return tax[province]



def mcmerchCalculator():
    arguments = parseArgument()
    tax = taxRate(arguments['province'])
    print(arguments['price']*arguments['quantity']*(1+tax), 2)

mcmerchCalculator()



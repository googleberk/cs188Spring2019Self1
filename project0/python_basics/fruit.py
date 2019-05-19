fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}


def buyFruit(fruit, numPounds):
    if fruit not in fruitPrices:
        print("Sorry we don't have %s" % (fruit))
    else:
        cost = fruitPrices[fruit] * numPounds
        print("That'll be %f please" % (cost))


# Rather than having a main function as in Java, the __name__ == '__main__'
# check is used to delimit expressions which are executed when the file is
# called as a script from the command line. The code after the main check is thus
# the same sort of code you would put in a main function in Java.

# Main Function
if __name__ == '__main__':
    buyFruit('apples', 2.4)
    buyFruit('coconuts', 2)

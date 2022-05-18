
def Helper(x):
    if x == "First Owner":
        return [1, 0, 0, 0, 0]
    elif x == "Second Owner":
        return [0, 0, 1, 0, 0]
    elif x == "Third Owner":
        return [0, 0, 0, 0, 1]
    if x == "Fourth & Above Owner":
        return [0, 1, 0, 0, 0]
    if x == "Test Drive Car":
        return [0, 0, 0, 1, 0]

def ref1(x):
    if x == 'Manual':
        return 1
    else:
        return 0

def ref2(x):
    if x == 'Individual':
        return 1
    elif x == 'Dealer':
        return 0
    else:
        return -1

def ref3(x):
    if x == 'Petrol':
        return 1
    elif x == 'Diesel':
        return 0
    else:
        return -1



        return
balance = 3000

def withdraw(amount):
    global balance
    balance = balance - amount
def deposit(amount):
    global balance
    balance = balance + amount
    return balance
def enquiry():
    return balance


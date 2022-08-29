import random
import string


class Person():
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name

class Client(Person):
    def __init__(self, name, last_name, num_account, balance = 0):
        super().__init__(name, last_name)
        self.num_account = num_account
        self.balance = balance
    
    def __str__(self):
        return f"The client is '{self.name} {self.last_name}'\nBalance of account '{self.num_account}': {self.balance}$"

    def deposit_amount(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"You deposit {amount}. Your total balance is {self.balance}")
            return self.balance
        else:
            print("You can't deposit that amount")

    def retire_amount(self,amount):
        if self.balance - amount >= 0 and amount > 0:
            self.balance -= amount
            print(f"You retired {amount}. Your total balance is {self.balance}")
            return self.balance
        else:
            print(f"Insuficient balance. Your balance is {self.balance}")



def create_client():
    name = input('Introduce your name ')
    last_name = input('Introduce your lastname ')
    num_account = ''.join(random.choice(string.digits) for _ in range(8))
    client = Client(name, last_name, num_account)

    return client

def init():
    client = create_client()
    print(client)

    menu_option = 0

    while menu_option != 'E':
        print('Select: Deposit(D), Retire(R), or Exit(E)')
        menu_option = input('Select an operation: ')

        if menu_option == 'R':
            quantity_to_retire = int(input('Introduce the quantity you want to retire: '))
            client.retire_amount(quantity_to_retire)
        elif menu_option == 'D':
            quantity_to_deposit = int(input('Introduce the quantity you want to deposit: '))
            client.deposit_amount(quantity_to_deposit)
        print(client)

    print("Thanks for operating whith us!")

init()
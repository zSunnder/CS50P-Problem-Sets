import random
from pyfiglet import Figlet
from tabulate import tabulate

class Money:
    def __init__(self):
        self._size = 0

    def __str__(self):
        return f"{self._size}"

    def deposit(self, n):
        if 0 < n:
            self._size += n
        else:
            raise ValueError("Invalid data")

    def withdraw(self, n):
        if 0 < n:
            self._size -= n
        else:
            raise ValueError

    @property
    def size(self):
        return self.size


class Blackjack:
    def __init__(self):
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["♠", "♡", "♢", "♣"]
        self.user = []
        self.dealer = []

    def generate_card(self):
        self.value = random.choice(self.values)
        self.suit = random.choice(self.suits)
        return f"{self.value}{self.suit}"

    def hand(self):
        self.user = [self.generate_card(), self.generate_card()]
        self.dealer = [self.generate_card(), self.generate_card()]

    def calculate(self, hand):
        values_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
        total_value = sum(values_dict[card[:-1]] for card in hand)
        for card in hand:
            if card.startswith("A") and total_value > 21:
                total_value -= 10
        return total_value

    def game(self):
        self.hand()
        print(f"Your cards:{', '.join(self.user)}")
        print(f"Dealer hand:{self.dealer[0]} ")

        while True:
            choice = input("Hit or Stand:  ").lower()
            if choice == "hit":
                self.user.append(self.generate_card())
                print(f"Your cards:{', '.join(self.user)}")
                total = self.calculate(self.user)
                if total > 21:
                    print("You pass 21")
                    return False
            else:
                break

        while self.calculate(self.dealer) < 17:
            self.dealer.append(self.generate_card())

        print(f"Dealer cards:{', '.join(self.dealer)}")
        totalDealer = self.calculate(self.dealer)
        total = self.calculate(self.user)

        if totalDealer > 21 or (total <= 21 and total > totalDealer):
            return True
        elif total == totalDealer:
            print("Tie.")
        else:
            return False

def main():
    blackjack = Blackjack()
    money = Money()
    while True:
        get_menu()
        try:
            choice = int(input("Write the option: "))
            if choice > 4:
                print("Please select a valid option")
                continue
            elif choice == 1:
                money.deposit(int(input("Deposit: ")))

            elif choice == 2:
                try:
                    apuesta = int(input("Bet: "))
                    bet = blackjack.game()
                    if bet:
                        money.deposit(apuesta * 2)
                        print("You win")

                    elif bet == False:
                        money.withdraw(apuesta)
                        print("You lose!")
                except ValueError:
                    print("Write a valid bet")

            elif choice == 3:
                    getmoney(f"Money:$ {money}")

            elif choice == 4:
                say_goobye()
                return True

        except ValueError:
            print("Write a Valid option")

def get_menu():
    table = [["Deposit", 1], ["Play", 2], ["Money", 3], ["Exit", 4]]
    headers = ["Menu", "Options"]
    print(tabulate(table, headers, tablefmt="grid"))


def getmoney(n):
    figlet = Figlet()
    figlet.setFont(font="doom")
    print(figlet.renderText(n))

def say_goobye():
    figlet = Figlet()
    figlet.setFont(font="speed")
    print(figlet.renderText("GOODBYE"))

if __name__ == "__main__":
    main()


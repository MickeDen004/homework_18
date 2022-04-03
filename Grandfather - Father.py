"""
Creating three classes: Grandfather, Father, Son. Properties shared by all:
first name
last name
age
citizenship
Methods:
    printname
    print date of birth
    print
"""
import random


class Grandfather():
    """
    This is a "Grandfather" class.
    All the following classes descend from this particular class
    """

    def __init__(self, fname, lname, age, country):
        self.__fname = fname
        self.__lname = lname
        self.age = age
        self.country = country

    def print_name(self):
        print(f"Greetings! My name is {self.__fname} {self.__lname}")

    def print_age(self):
        print(f"I'm {self.age} years old")

    def print_country(self):
        print(f"I am a citizen of {self.country}")

    def calculate_savings(self, starting_sum, annual_interest_rate, term_units, term):
        accrued_sum = starting_sum * ((annual_interest_rate/ 100) /term_units ) * term
        grand_total = accrued_sum + starting_sum
        D = (grand_total/starting_sum - 1) * 100
        sum_per = float('{:.2f}'.format(accrued_sum))
        fin_sum = float('{:.2f}'.format(grand_total))
        profit_percent = float('{:.2f}'.format(D))
        print(f"Accrued sum: {sum_per},\nGrand total: {fin_sum},\nProfitability: {profit_percent} %")


class Father(Grandfather):
    """This class represents father"""
    def choose_book(self, books):
        rand_idx = random.randrange(len(books))
        f_book = books[rand_idx]
        print(f"I want to read: {f_book}")

    @staticmethod
    def leave_tip(bill_amount, tip_perc=10):
        total = bill_amount*(1+0.01*tip_perc)
        total = round(total, 2)
        print(f"Tip: {total}")


class Son(Father):
    """This is son class """

    def __init__(self, fname, lname, age, country, year, university):
        super().__init__(fname, lname, age, country)
        self.graduation_year = year
        self.university = university

    def welcome(self):
        print(f"Welcome {self.__fname} {self.__lname} to the class of {self.graduation_year}")

    def calculate_student_loan_interest(self, annual_interest_rate, loan_balance, days_since_last_payment):
         daily_interest_rate = (annual_interest_rate/100)/365
         daily_interest_accrued = loan_balance * daily_interest_rate
         monthly_interest_payment = days_since_last_payment * daily_interest_accrued
         print(f"Daily interest rate: {daily_interest_rate}%,\nDaily interest accrued: ${daily_interest_accrued},\n:Interest accrued since last payment: ${monthly_interest_payment}")


grandfather = Grandfather("Joshua", "Bradisley", 83, "Canada")
grandfather.print_name()
grandfather.print_age()
grandfather.print_country()
print(grandfather.calculate_savings(1200, 13, 1, 5))
print()
father = Father("Kelly", "Bradisley", 38, "Canada")
b = ["Crime and Punishment", "Lord of the Rings", "Shinning", "Withering Heights", "Dracula"]
father.choose_book(b)
father.leave_tip(12.34)
father.print_name()
father.print_age()
father.calculate_savings(13450.34, 21, 1, 2)
print(father.__dir__())
print()
son = Son("Steve", "Bradisley", "20", "Canada")
print(son.__dir__())


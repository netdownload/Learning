from flat import Bill, Flatmate
from reports import PdfReport



# CLI
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in in the house during the bill period? "))


bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays:", flatmate1.pays(bill, flatmate2))
print(f"{flatmate2.name} pays:", flatmate2.pays(bill, flatmate1))

pdf_bill = PdfReport(f"{bill.period}.pdf")
pdf_bill.generate(flatmate1, flatmate2, bill)

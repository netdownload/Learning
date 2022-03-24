from fileinput import filename
from re import S


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of a bill.
    """

    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatname person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / \
            (self.days_in_house + flatmate2.days_in_house)
        pay = weight*bill.amount
        return pay


class PdfReport:
    """
    Creates a PDF file that contains data about the flatnames such as their names, 
    they due amounts and the periods of the bill.
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(john.name, "pays:", john.pays(bill=bill, flatmate2=marry))
print(marry.name, "pays:",marry.pays(bill=bill, flatmate2=john))

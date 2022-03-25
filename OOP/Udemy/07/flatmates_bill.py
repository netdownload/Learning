from fileinput import filename
from ntpath import join
from fpdf import FPDF


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
        pdf = FPDF(format="a4", orientation="portrait", unit="pt")
        pdf.add_page()

        # Insert a title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatemates Bill", border=1, align="C", ln=1)

        # Insert period
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        #
        pdf.cell(w=150, h=40, txt=john.name, border=1)
        pdf.output("bill.pdf")


bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(john.name, "pays:", john.pays(bill=bill, flatmate2=marry))
print(marry.name, "pays:", marry.pays(bill=bill, flatmate2=john))

pdf_bill = PdfReport("bill")
pdf_bill.generate(john, marry, bill)

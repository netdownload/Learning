import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF file that contains data about the flatnames such as their names, 
    they due amounts and the periods of the bill.
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(
            round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))
        flatmate2_pay = str(
            round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))

        pdf = FPDF(format="a4", orientation="portrait", unit="pt")
        pdf.add_page()
        # Add icon
        pdf.image("OOP\\Udemy\\07\\files\\house.png", w=30, h=30)

        # Insert a title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatemates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=200, h=25, txt=flatmate1_pay, border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=200, h=25, txt=flatmate2_pay, border=0, ln=1)
        
        
        # Change directory
        os.chdir("OOP\\Udemy\\07\\files\\")
        
        pdf.output(self.filename)
        webbrowser.open(self.filename)

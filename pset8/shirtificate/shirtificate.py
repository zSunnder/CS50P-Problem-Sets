from fpdf import FPDF

class Shirt(FPDF):
    ...


def main():
    pdf = Shirt(orientation="Portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 40)
    pdf.set_y(20)
    pdf.set_x(90)
    pdf.cell(30, 10, "CS50 Shirtificate", align="C")
    pdf.set_y(60)
    pdf.image("shirtificate.png", w=pdf.epw)
    user = input("Name: ")
    txt = f"{user} took CS50"
    pdf.set_font("helvetica", "B", 25)
    pdf.set_y(120)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(text=txt, align="C", center="True")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

#pdf.cell align=c

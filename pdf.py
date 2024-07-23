from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter.messagebox import askokcancel, WARNING
from PIL import Image
import img2pdf

def create_pdf():
    cap = tk.Capturer(tk.Tk())
    ID = "Reporte" + str(cap.reportID) + ".jpg"
    img = cap.capture(ID)
    img = Image.open(ID)
    img = img.convert("RGB")
    pdf_path = r"Reporte" + str(cap.reportID) + ".pdf"
    img.save(pdf_path)
    cap.reportID += 1
    showinfo(title="PDF", message="El PDF fue generado con éxito.")

if __name__ == "__main__":
    create_pdf()
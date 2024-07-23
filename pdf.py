from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter.messagebox import askokcancel, WARNING
from PIL import Image
import img2pdf
from tkinter import *

def create_pdf(self):
    cap = cap = tk.Capturer(tk.Tk())
    ID = "Reporte" + str(self.reportID) + ".jpg"
    img = cap.capture(ID)
    img = Image.open(ID)
    img = img.convert("RGB")
    pdf_path = r"Reporte" + str(self.reportID) + ".pdf"
    img.save(pdf_path)
    self.reportID += 1
    showinfo(title="PDF", message="El PDF fue generado con éxito.")
    
if __name__ == "__main__":
    create_pdf()
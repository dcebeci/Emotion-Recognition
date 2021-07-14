from tkinter import *
import cv2
from test import start_capturing
root = Tk()
root.title('Emotion Detection')
root.iconbitmap(r'C:\Users\Doğukan\OneDrive\Masaüstü\ED\icon.ico')
root.geometry("500x300")

def run():
   # root.destroy()
    start_capturing()

myButton = Button(root, text="Calıştır",command=run, padx=50)
myButton.pack(pady=20)
def info():
    global pop
    pop = Toplevel(root)
    pop.title("Hakkında")
    pop.geometry("270x100")
    pop.config(bg="green")
    pop_label = Label(pop, text=" Hazırlayan: Doğukan Cebeci \nİletişim: cebecidogukan@gmail.com\" , bg="green",fg="white", font=("helvetica", 12))
    pop_label.pack(pady=10)
    my_frame = Frame(pop, bg="green")
    my_frame.pack(pady=5)
infoBtn = Button(root, text="Info",command=info, padx=30)
infoBtn.pack(pady=20)

button_quit = Button(root, text="Programı Sonlandır", command=root.quit, padx=40)
button_quit.pack(pady=20)
root.mainloop()
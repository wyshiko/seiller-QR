import tkinter as tk
import qrcode
from PIL import Image
from tkinter import filedialog

root = tk.Tk()
root.title('SEILLER - QR NOTICE')
photo = tk.PhotoImage(file = "img/logo seiller.png")
root.iconphoto(False, photo)

def gen_qr():
    error = False
    if len(enter_url.get()) == 0:
        error = True
        pop_up = tk.Toplevel(root)
        tk.Label(pop_up, text= "OUPS! Veuillez entrer le contenu du QR code.").pack(padx=10,pady=50)
    elif len(file_name.get()) == 0:
        error = True
        pop_up = tk.Toplevel(root)
        tk.Label(pop_up, text= "OUPS! Veuillez entrer un nom de fichier.").pack(padx=10,pady=50)
    if error == False:
        path= filedialog.askdirectory(title="Select a File")
        url = enter_url.get()
        name = file_name.get()

        #Creating an instance of qrcode
        img_bg = Image.open('img/print_pattern.png')
        qr = qrcode.QRCode(box_size=16)
        qr.add_data(url)
        qr.make()
        img = qr.make_image()
        pos = (int((img_bg.size[0] - img.size[0])/2), int((img_bg.size[1] - img.size[1])/2))
        img_bg.paste(img, pos)
        img_bg.save(f'{path}/{name}.png')

        pop_up = tk.Toplevel(root)
        tk.Label(pop_up, text= "SUPER! Le QR code à bien été generé, merci.").pack(padx=10,pady=50)
    else:
        print('Veuillez entrer toutes les informations')
img = tk.PhotoImage(file="img/logo seiller_full.png")
tk.Label(root, image=img).pack(pady=10)

tk.Label(root, text='QR CODE - NOTICE', font=("Helvetica", 12,"bold")).pack(pady=10)

tk.Label(root, text='URL').pack()
enter_url = tk.Entry(root, width=50)
enter_url.pack(padx=10, pady=10)

tk.Label(root, text='Nom du QR code').pack()
file_name = tk.Entry(root, width=50)
file_name.pack(padx=10, pady=10)

tk.Button(root, text='Génerer',command=gen_qr).pack(pady=10)

root.mainloop()
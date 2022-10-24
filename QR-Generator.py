import tkinter as tk
import qrcode

root = tk.Tk()
root.title("Seiller - NOTICE QR CODE GENERATEUR")

tk.Label(root, text = 'QR CODE ', 
      font =('Verdana', 15)).pack(pady = 10)

tk.Label(root, text = 'URL', 
      font =('Verdana', 15)).pack()
entry_url = tk.Entry(root, width=50)
entry_url.pack(padx=30)
tk.Label(root, text = 'Nom du fichier', 
      font =('Verdana', 15)).pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack(padx=30)

def gen_qr():
      url = entry_url.get()
      fil_name = entry_name.get()
      #Creating an instance of qrcode
      qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
      qr.add_data(url)
      qr.make(fit=True)
      img = qr.make_image(fill='black', back_color='white')
      img.save(f'{fil_name}.png')
      
      print('le code a ete genere')
      
tk.Button(root, text="Génerer", command=gen_qr).pack(pady=10)

root.mainloop()

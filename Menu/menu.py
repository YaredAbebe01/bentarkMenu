 import qrcode 

menu_url = "https://drive.google.com/drive/folders/1ZbYQY0BYqqu4oqLiL1R6dvuf_xbZRQj_?usp=drive_link"

qr = qrcode.make(menu_url)

qr.save("menu_qr.png")

print("QR code saved as 'menu_qr.png'")

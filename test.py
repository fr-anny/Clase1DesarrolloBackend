import qrcode

texto= input("Ingresw el texto para generar el códio QR: ")
img= qrcode.make(texto)
img.save("test.png")

textoomagen = input("Ingrese el texto para IMG: ")
img.save(textoomagen + ".png")
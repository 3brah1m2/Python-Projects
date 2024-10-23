import qrcode
def qrcode_encoder(data):
    img = qrcode.make(data)
    img.save('C:/Users/Ebrahim R/Documents/Python-Projects/qrcode.png')
qrcode_encoder('Hello People')
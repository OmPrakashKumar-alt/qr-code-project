import qrcode
from PIL import Image
import qrcode.constants
qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=3)
qr.add_data("https://www.instagram.com/omu_prkash042/")
qr.make(fit=True)
img = qr.make_image(fill_color = "blue", back_color = "white")
img.save("OP_Insta.png")
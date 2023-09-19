import qrcode
from PIL import Image

data = "https://chat.openai.com/"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Convert the qrcode image to a PIL Image object
pil_img = Image.new("RGB", (img.width, img.height), "white")
pil_img.paste(img)

# Save the image
pil_img.save("myqr.png")

# Display the image using the default image viewer
pil_img.show()

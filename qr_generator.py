import qrcode

def generate_qr():
    data = input("Enter the text or URL to encode in QR Code: ").strip()
    filename = input("Enter the output filename(without extension):").strip()

    #Customize QR settings
    qr = qrcode.QRCode(
        version = 1,#size of the QR code
        error_correction = qrcode.constants.ERROR_CORRECT_H, #High error correction
        box_size = 10,#pixel size
        border = 4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black",back_color="White")
    img.save(f"{filename}.png")
    print(f"QR code successfully saved as {filename}.png")

if __name__ == "__main__":
    generate_qr()
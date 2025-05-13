# free-qr-code
easily create qr codes to your documents etc.

pip install qrcode[pil]

# import qrcode

# Dicionário com os currículos
curriculums = {
    "spanish": "www.curriculum-spanish.pdf-example",
    "english": "www.url-english-with-.pdf"
}

# Gerar e salvar QR Codes
for nome, url in curriculos.items():
    qr = qrcode.make(url)
    qr.save(f"qr_{nome}.png")
    print(f"QR code salvo como qr_{nome}.png")

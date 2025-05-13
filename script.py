import qrcode

# Dicionário com os currículos
curriculos = {
    "ingles": "https://dev-walbarello.netlify.app",
    "servico_publico": "https://dev-walbarello.netlify.app"
}

# Gerar e salvar QR Codes
for nome, url in curriculos.items():
    qr = qrcode.make(url)
    qr.save(f"qr_{nome}.png")
    print(f"QR code salvo como qr_{nome}.png")

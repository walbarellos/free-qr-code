# 📌 free-qr-code
Easily create QR codes to your documents, PDFs, links, etc.

---

## 🚀 Instalação

### ✅ Com ambiente virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
pip install "qrcode[pil]"

```
⚠️ Ou diretamente no sistema (não recomendado)

```bash

pip install "qrcode[pil]" --break-system-packages

```

💻 Exemplo de uso em Python

```python

import qrcode

# Dicionário com os currículos
curriculums = {
    "spanish": "https://example.com/curriculum-spanish.pdf",
    "english": "https://example.com/curriculum-english.pdf"
}

# Gerar e salvar QR Codes
for nome, url in curriculums.items():
    qr = qrcode.make(url)
    qr.save(f"qr_{nome}.png")
    print(f"QR code salvo como qr_{nome}.png")

```

🖼️ Resultado

O script salva os arquivos:
```
    qr_spanish.png

    qr_english.png
```
Prontos para imprimir, compartilhar ou anexar a apresentações.

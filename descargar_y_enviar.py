import os
import time
import subprocess
from email.message import EmailMessage
import smtplib

FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')

recipes = {
    'El_Mundo': 'recipes/elmundo.recipe',
    'Expansion': 'recipes/expansion_spanish.recipe',
    'Wall_Street_Journal': 'recipes/wsj_news.recipe',
}

epubs = []
for name, path in recipes.items():
    epub_file = f"{name}.epub"
    print(f"Generando {epub_file}...")
    subprocess.run(['ebook-convert', path, epub_file], check=True)
    epubs.append(epub_file)
    time.sleep(5)

msg = EmailMessage()
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = "Tus periódicos del día (Calibre News)"

for epub_file in epubs:
    with open(epub_file, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='epub+zip', filename=epub_file)

print("Enviando email...")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(FROM_EMAIL, APP_PASSWORD)
    smtp.send_message(msg)
print("¡Correo enviado!")

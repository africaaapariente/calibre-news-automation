# Calibre News Automation

Este proyecto descarga periódicos (El Mundo, Expansión y Wall Street Journal gratuito), los convierte a EPUB y los envía automáticamente por correo electrónico a tu Kindle.

## 🔧 Requisitos

- Tener instalado Calibre CLI (`ebook-convert`)
- Python 3
- Una cuenta Gmail con clave de app

## ⚙️ Variables de entorno

Debes configurar las siguientes variables en Railway:

- `FROM_EMAIL`: tuemail@gmail.com
- `TO_EMAIL`: tunombre@kindle.com
- `APP_PASSWORD`: clave de app de Gmail

## 🕒 Automático

Puedes programar la ejecución diaria con Railway CRON:


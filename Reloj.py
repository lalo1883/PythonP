from pytube import YouTube
import os

# Dirección URL del video de YouTube
url = "https://youtu.be/CocEMWdc7Ck"

# Crea un objeto YouTube
yt = YouTube(url)

# Filtra solo los streams de video disponibles en HD
hd_video = yt.streams.filter(progressive=True, file_extension='mp4').first()

# Pide al usuario especificar la ruta de descarga
ruta_descarga = ("/Users/joseeduardonunezarenas/Desktop/Python")

# Descarga el video en la ruta especificada
hd_video.download(ruta_descarga)

print("Video en HD descargado correctamente en la ruta: ", ruta_descarga)

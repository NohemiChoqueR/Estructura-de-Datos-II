import cloudinary
import cloudinary.uploader
import os

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("CLOUD_API_KEY"),
    api_secret=os.getenv("CLOUD_API_SECRET")
)

def subir_imagen(file):
    resultado = cloudinary.uploader.upload(file)
    return resultado["secure_url"]

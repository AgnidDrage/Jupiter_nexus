INPUT_DIR = "../images"
OUTPUT_DIR = "../output"
from jupiter_image import Jupiter


def main():
    imagen = input("")
    clase = Jupiter(imagen)
    clase.openImage()
    
    pass
"""
Script para generar datos ficticios de usuarios usando la librería Faker.

Se generan 50 registros con nombre, correo electrónico, dirección
y perfil profesional. Los datos se guardan en un archivo CSV.
"""

from faker import Faker
import csv

# Cantidad de usuarios a generar
NUM_REGISTROS = 50

# Nombre del archivo de salida
ARCHIVO_SALIDA = "usuarios_ficticios.csv"

# Inicializar Faker en español (México)
fake = Faker("es_MX")

# Lista para guardar los usuarios
usuarios = []

# Generar los datos ficticios
for _ in range(NUM_REGISTROS):
    usuario = {
        "nombre": fake.name(),
        "correo": fake.email(),
        "direccion": fake.address().replace("\n", ", "),
        "perfil": fake.job()
    }
    usuarios.append(usuario)

# Guardar los datos en un archivo CSV
with open(ARCHIVO_SALIDA, mode="w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "correo", "direccion", "perfil"]
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    writer.writerows(usuarios)

# Mensaje final
print(f"Se generaron {NUM_REGISTROS} usuarios en el archivo '{ARCHIVO_SALIDA}'.")

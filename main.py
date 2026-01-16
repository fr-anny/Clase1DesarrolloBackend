"""
Script para generar datos ficticios de usuarios usando la librería Faker.

Este programa genera 50 registros de usuarios ficticios con información completa:
- Nombre completo
- Correo electrónico
- Teléfono
- Dirección
- Ciudad
- Código postal
- Perfil profesional
- Empresa

Los datos se exportan automáticamente a un archivo CSV.

Autor: Ramírez Figueroa Anita
Fecha: 15 de enero 2026
"""

from faker import Faker
import csv

# Constantes
NUM_REGISTROS = 50
NOMBRE_ARCHIVO = 'usuarios_ficticios.csv'
LOCALIZACION = 'es_MX'


def inicializar_faker(localizacion=LOCALIZACION):
    """
    Inicializa y retorna una instancia de Faker.

    Args:
        localizacion (str): Código de localización (default: 'es_MX').

    Returns:
        Faker: Instancia de Faker configurada con la localización indicada.
    """
    return Faker(localizacion)


def generar_usuario(fake):
    """
    Genera un diccionario con datos ficticios de un usuario.

    Args:
        fake (Faker): Instancia de Faker para generar datos.

    Returns:
        dict: Diccionario con información del usuario, incluyendo:
              'nombre', 'correo', 'telefono', 'direccion',
              'ciudad', 'codigo_postal', 'perfil', 'empresa'.
    """
    return {
        'nombre': fake.name(),
        'correo': fake.email(),
        'telefono': fake.phone_number(),
        'direccion': fake.address().replace("\n", ", "),
        'ciudad': fake.city(),
        'codigo_postal': fake.postcode(),
        'perfil': fake.job(),
        'empresa': fake.company()
    }


def generar_registros(fake, cantidad=NUM_REGISTROS):
    """
    Genera múltiples registros de usuarios ficticios.

    Args:
        fake (Faker): Instancia de Faker.
        cantidad (int): Número de registros a generar (default: 50).

    Returns:
        list: Lista de diccionarios con información de usuarios.
    """
    print(f"\nGenerando {cantidad} registros de usuarios...\n")
    usuarios = []

    for i in range(cantidad):
        usuario = generar_usuario(fake)  # Crear un usuario ficticio
        usuarios.append(usuario)         # Agregarlo a la lista

        # Mostrar progreso cada 10 registros
        if (i + 1) % 10 == 0:
            print(f"{i + 1}/{cantidad} registros generados")

    print(f"\n{cantidad} registros generados exitosamente!\n")
    return usuarios


def exportar_a_csv(usuarios, nombre_archivo=NOMBRE_ARCHIVO):
    """
    Exporta los datos de usuarios a un archivo CSV.

    Args:
        usuarios (list): Lista de diccionarios con datos de usuarios.
        nombre_archivo (str): Nombre del archivo CSV de salida.

    Returns:
        bool: True si la exportación fue exitosa, False en caso de error.
    """
    try:
        campos = list(usuarios[0].keys())  # Obtener los nombres de las columnas

        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()        # Escribir cabecera
            writer.writerows(usuarios)  # Escribir registros

        print(f"Datos exportados a '{nombre_archivo}'\n")
        return True

    except Exception as error:
        print(f"Error al exportar: {error}\n")
        return False


def main():
    """Función principal que coordina la ejecución del programa."""
    # Inicializar Faker
    fake = inicializar_faker()

    # Generar registros de usuarios
    usuarios = generar_registros(fake, NUM_REGISTROS)

    # Exportar los registros a CSV
    exportar_a_csv(usuarios, NOMBRE_ARCHIVO)


# Punto de entrada del script
if __name__ == "__main__":
    main()

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    import pandas as pd

    filas = []
    fila_actual = []
    with open("files/input/clusters_report.txt", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for linea in lineas[4:]:
        if linea.strip():
            fila_actual.append(linea.strip())
        else:
            if fila_actual:
                filas.append(" ".join(fila_actual))
                fila_actual = []
    
    if fila_actual:
        filas.append(" ".join(fila_actual))

    datos = []
    for fila in filas:
        partes = fila.split()
        id_cluster = int(partes[0])
        total_palabras = int(partes[1])
        porcentaje_palabras = float(partes[2].replace(",", "."))
        palabras_clave = (
            " ".join(partes[3:])
            .replace(" ,", ",")
            .replace(", ", ", ")
            .strip("%")
            .rstrip(".")
            .strip()
        )
        datos.append([id_cluster, total_palabras, porcentaje_palabras, palabras_clave])

    columnas = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ]
    df = pd.DataFrame(datos, columns=columnas)
    print(df)
    return df

pregunta_01()
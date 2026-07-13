# R1 - Catálogo de libros

def registrar_libro(catalogo, codigo, titulo, autor, genero):
    catalogo[codigo] = {"titulo": titulo, "autor": autor, "genero": genero}
    print(f"Libro '{titulo}' ({genero}) registrado con código {codigo}.")

def pedir_genero():
    while True:
        genero = input("Género del libro (novela/ciencia): ").strip().lower()
        if genero in ("novela", "ciencia"):
            return genero
        print("Género no válido. Escriba 'novela' o 'ciencia'.")

def buscar_libro(catalogo, codigo):
    libro = catalogo.get(codigo)
    if libro is None:
        print(f"No existe ningún libro con el código '{codigo}'.")
    else:
        print(f"Código: {codigo} | Título: {libro['titulo']} | Autor: {libro['autor']} | Género: {libro['genero']}")
    return libro


# R2 - Catálogo ordenado

def mostrar_catalogo_ordenado(catalogo):
    codigos_ordenados = sorted(catalogo.keys())

    if not codigos_ordenados:
        print("El catálogo está vacío.")
        return

    print("\n--- Catálogo ordenado por código ---")
    for codigo in codigos_ordenados:
        libro = catalogo[codigo]
        print(f"{codigo} | {libro['titulo']} | {libro['autor']} | {libro['genero']}")


# R3 - Socios registrados

def registrar_socio(socios, id_socio):
    if id_socio in socios:
        print(f"El socio '{id_socio}' ya está registrado.")
    else:
        socios.add(id_socio)
        print(f"Socio '{id_socio}' registrado correctamente.")

def existe_socio(socios, id_socio):
    return id_socio in socios


# R4 - Análisis de préstamos (operaciones entre conjuntos)

def registrar_prestamo(socios, socios_novela, socios_ciencia, id_socio, genero):
    if id_socio not in socios:
        socios.add(id_socio)
        print(f"Socio '{id_socio}' no estaba registrado; se registró automáticamente.")

    if genero == "novela":
        socios_novela.add(id_socio)
    else:
        socios_ciencia.add(id_socio)

    print(f"Préstamo registrado: socio '{id_socio}' -> género '{genero}'.")

def analizar_prestamos(socios_novela, socios_ciencia):
    interseccion = socios_novela & socios_ciencia
    solo_novela = socios_novela - socios_ciencia
    union_total = socios_novela | socios_ciencia

    print("\n--- Análisis de préstamos ---")
    print(f"Socios que leen ambos géneros (intersección): {interseccion}")
    print(f"Socios que solo leen novela (diferencia):      {solo_novela}")
    print(f"Total de socios distintos con préstamos (unión): {union_total}")
    print(f"Cantidad total de socios distintos con préstamos: {len(union_total)}")

    return interseccion, solo_novela, union_total
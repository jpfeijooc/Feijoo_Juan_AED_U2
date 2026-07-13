from utilidades import (
    registrar_libro,
    pedir_genero,
    buscar_libro,
    mostrar_catalogo_ordenado,
    registrar_socio,
    existe_socio,
    registrar_prestamo,
    analizar_prestamos,
)

catalogo = {}
socios = set()
socios_novela = set()
socios_ciencia = set()

def cargar_datos_ejemplo():
    """Carga algunos libros, socios y préstamos de ejemplo para poder probar el programa."""
    registrar_libro(catalogo, "L001", "Cien años de soledad", "Gabriel García Márquez", "novela")
    registrar_libro(catalogo, "L002", "Breve historia del tiempo", "Stephen Hawking", "ciencia")
    registrar_libro(catalogo, "L003", "Don Quijote de la Mancha", "Miguel de Cervantes", "novela")
    registrar_libro(catalogo, "L004", "Cosmos", "Carl Sagan", "ciencia")

    for id_socio in ["070657", "131251", "070245", "171469"]:
        registrar_socio(socios, id_socio)

    registrar_prestamo(socios, socios_novela, socios_ciencia, "070657", "novela")
    registrar_prestamo(socios, socios_novela, socios_ciencia, "131251", "novela")
    registrar_prestamo(socios, socios_novela, socios_ciencia, "131251", "ciencia")
    registrar_prestamo(socios, socios_novela, socios_ciencia, "070245", "novela")
    registrar_prestamo(socios, socios_novela, socios_ciencia, "171469", "ciencia")

    print("\nDatos de ejemplo cargados correctamente.\n")

def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Buscar libro por código")
    print("3. Mostrar catálogo ordenado por código")
    print("4. Registrar socio")
    print("5. Verificar si un socio está registrado")
    print("6. Registrar préstamo (el socio elige el género)")
    print("7. Analizar préstamos (novela vs ciencia)")
    print("8. Cargar datos de ejemplo")
    print("0. Salir")

def main():
    cargar_datos_ejemplo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código del libro: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            genero = pedir_genero()
            registrar_libro(catalogo, codigo, titulo, autor, genero)

        elif opcion == "2":
            codigo = input("Código del libro a buscar: ").strip()
            buscar_libro(catalogo, codigo)

        elif opcion == "3":
            mostrar_catalogo_ordenado(catalogo)

        elif opcion == "4":
            id_socio = input("Identificador del socio: ").strip()
            registrar_socio(socios, id_socio)

        elif opcion == "5":
            id_socio = input("Identificador del socio a verificar: ").strip()
            if existe_socio(socios, id_socio):
                print(f"El socio '{id_socio}' SÍ está registrado.")
            else:
                print(f"El socio '{id_socio}' NO está registrado.")

        elif opcion == "6":
            id_socio = input("Identificador del socio: ").strip()
            genero = pedir_genero()
            registrar_prestamo(socios, socios_novela, socios_ciencia, id_socio, genero)

        elif opcion == "7":
            analizar_prestamos(socios_novela, socios_ciencia)

        elif opcion == "8":
            cargar_datos_ejemplo()

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
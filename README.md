# Sistema de Gestión de una Biblioteca

Programa de consola en Python que gestiona el catálogo y los préstamos de una
pequeña biblioteca, usando **diccionarios (`dict`)** y **conjuntos (`set`)**
como estructuras principales (Unidad 2 - Algoritmos y Estructuras de Datos).

## Requisitos

- Python 3.8 o superior (no requiere librerías externas).

## Cómo ejecutar el programa

```bash
python main.py
```

Al iniciar, el programa carga automáticamente algunos **libros y socios de
ejemplo** para poder probar todas las opciones del menú de inmediato.

## Estructura del proyecto

```
biblioteca/
├── main.py         # Menú de consola y datos de ejemplo
├── utilidades.py   # Funciones auxiliares (lógica de cada requerimiento)
└── README.md
```

## Descripción de los requerimientos

- **R1 – Catálogo de libros (diccionario / HashMap):**
  El catálogo se guarda en un `dict` cuya clave es el código del libro y cuyo
  valor es un diccionario con el título, el autor y el **género** (novela o
  ciencia, elegido al registrar el libro con `pedir_genero`). Esto permite
  registrar un libro (`registrar_libro`) y buscarlo por su código
  (`buscar_libro`) de forma inmediata, en tiempo promedio O(1).

- **R2 – Catálogo ordenado (equivalente a TreeMap):**
  La función `mostrar_catalogo_ordenado` usa `sorted()` sobre las claves del
  diccionario para mostrar el catálogo ordenado por código. Un `TreeMap`
  (como en Java) da este orden "gratis" porque internamente organiza sus
  claves en un árbol binario de búsqueda balanceado, por lo que siempre
  recorre las claves en orden sin necesidad de ordenarlas explícitamente cada
  vez; en Python, con un `dict` normal, ese ordenamiento hay que pedirlo
  explícitamente con `sorted()` (o usar `sortedcontainers.SortedDict` si se
  necesita mantenerlo ordenado todo el tiempo).

- **R3 – Socios registrados (conjunto):**
  Los identificadores de los socios se guardan en un `set`, lo que evita
  duplicados automáticamente y permite verificar en tiempo O(1) si un socio
  ya existe (`existe_socio`) antes de registrarlo (`registrar_socio`).

- **R4 – Análisis de préstamos (operaciones entre conjuntos):**
  Se mantienen dos conjuntos de socios según el género que han pedido en
  préstamo (novela y ciencia). Cada préstamo se registra con
  `registrar_prestamo`, donde **el propio socio elige el género** que quiere
  leer, y su id se agrega automáticamente al set correspondiente
  (`socios_novela` o `socios_ciencia`). Luego, `analizar_prestamos` calcula:
  - **Intersección (`&`):** socios que leen ambos géneros.
  - **Diferencia (`-`):** socios que solo leen novela.
  - **Unión (`|`):** total de socios distintos con algún préstamo.

## Tabla de complejidades

| Operación                                   | Estructura | Complejidad     |
|----------------------------------------------|------------|-----------------|
| Registrar / buscar libro por código           | dict       | O(1) promedio   |
| Mostrar catálogo ordenado                      | dict       | O(n log n)      |
| Registrar / verificar socio                    | set        | O(1) promedio   |
| Intersección, diferencia y unión de préstamos  | set        | O(n + m)        |

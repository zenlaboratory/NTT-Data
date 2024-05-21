# Ejercicio 1

# Crea una lista llamada `lista_id_bombas` con una serie de valores de identificación de bombas.

lista_id_bombas = [
    8776,
    34310,
    67743,
    19728,
    9944,
    19816,
    54551,
    53934,
    46144,
    49056,
    50409,
    36957,
    50495,
    53752,
    61848,
    48451,
    58155,
    18274,
    48375,
    6091,
    37862,
    51058,
    55012,
    9944,
    20145,
    19685,
    69124,
    46804,
    6696,
    12402,
    41583,
    57355,
    67359,
    60048,
    16583,
    25,
    70238,
    12796,
    52019,
    19282,
]

# Convierte la lista en un conjunto (set) para eliminar duplicados y convierte el conjunto de nuevo en una lista llamada lista_sin_duplicados.

lista_sin_duplicados = list(set(lista_id_bombas))

# Comprobar las longitudes de las listas.

longitud_original = len(lista_id_bombas)
longitud_sin_duplicados = len(lista_sin_duplicados)

# Imprime la longitud de la lista lista_id_bombas (número de elementos iniciales).

print(f"Longitud de la lista original: {longitud_original}")

# Imprime la longitud de la lista lista_sin_duplicados (número de elementos sin duplicados).

print(f"Longitud de la lista sin duplicados: {longitud_sin_duplicados}")

# Insertar la nueva ID 59398 en la tercera posición de la lista sin duplicados.

lista_sin_duplicados.insert(2, 59398)

# Calcula la longitud de la lista_sin_duplicados con el ID agregado anteriormente en la tercer posición

longitud_final = len(lista_sin_duplicados)

# imprime la longitud de la lista_sin_duplicados y muestra todos los elementos.

print(
    f"La longitud final de la lista sin duplicados es de: {longitud_final}. Sus elementos son: {lista_sin_duplicados}"
)

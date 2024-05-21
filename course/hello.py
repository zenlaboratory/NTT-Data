# Este fragmento de código define una clase Ubicacion que representa un punto geográfico con nombre, latitud y longitud.

from haversine import haversine

# La clase Ubicacion tiene un constructor que inicializa los atributos nombre, latitud y longitud.


class Ubicacion:
    def __init__(self, id, latitud, longitud):
        """
        Constructor de la clase Ubicacion.

        :param nombre: Nombre de la ubicación.
        :param latitud: Latitud de la ubicación.
        :param longitud: Longitud de la ubicación.
        """
        self.id = id
        self.latitud = latitud
        self.longitud = longitud


# Se solicita al usuario ingresar los datos de dos ubicaciones y se crean dos objetos Ubicacion con los datos ingresados por el usuario.

id = int(input("Introduzca id del sitio 1: "))
latitud = float(input("Introduzca latitud 1: "))
longitud = float(input("Introduzca longitud 1: "))

punto1 = Ubicacion(id, latitud, longitud)

id = int(input("Introduzca id del sitio 2: "))
latitud = float(input("Introduzca latitud 2: "))
longitud = float(input("Introduzca longitud 2: "))

punto2 = Ubicacion(id, latitud, longitud)

# Imprimimos cada punto por independiente

print(f"Id: {punto1.id} Latitud: {punto1.latitud} Longitud: {punto1.longitud}")
print(f"Id: {punto2.id} Latitud: {punto2.latitud} Longitud: {punto2.longitud}")

# Se calcula la distancia entre las dos ubicaciones utilizando la fórmula de Haversine.

distancia = haversine(
    (punto1.latitud, punto1.longitud), (punto2.latitud, punto2.longitud)
)

# Finalmente, se imprimen los id's, latitudes, longitudes y la distancia entre las dos ubicaciones en kilómetros.

print("")
print(f"La distancia entre {punto1.id} y {punto2.id} es de {distancia} Km")
#En el siguiente programa vamos a manejar un flujo de caja, en una veterinaria en la cual se da atencion exclusiva a perros y gatos, y necesitaban una base de datos diaria, para tener un registro de dichos animales con sus caracteristicas y asi desarrollar cuentas al final del dia. 
class Animal:
  #Clase base para animales

  def __init__(self, nombre, edad, especie):
    """
    Argumentos:
      nombre: El nombre del animal.
      edad: La edad del animal.
      especie: La especie del animal.
    """
    self.__nombre = nombre
    self.__edad = edad
    self.__especie = especie

  def obtener_nombre(self):
    """
    Obtiene el nombre del animal.

    """
    return self.__nombre

  def obtener_edad(self):
    """
    Obtiene la edad del animal.

    """
    return self.__edad

  def obtener_especie(self):
    """
    Obtiene la especie del animal.

    """
    return self.__especie

  def set_nombre(self, nombre):
    """Establece el nombre del animal.

    Argumento
      nombre: El nuevo nombre del animal.
    """
    self.__nombre = nombre

  def set_edad(self, edad):
    """Establece la edad del animal.

    Argumento
      edad: La nueva edad del animal.
    """
    self.__edad = edad

  def set_especie(self, especie):
    """Establece la especie del animal.

    Argumento
      especie: La nueva especie del animal.
    """
    self.__especie = especie

  def hablar(self):
    """Método abstracto para hacer que el animal hable."""
    raise NotImplementedError("El método hablar() debe ser implementado por las subclases.")


class Perro(Animal):
  """Clase para representar un perro."""

  def __init__(self, nombre, edad, raza):
    """Inicializa un nuevo objeto Perro.

    Argumentos:
      nombre: El nombre del perro.
      edad: La edad del perro.
      raza: La raza del perro.
    """
    super().__init__(nombre, edad, "Perro")
    self.__raza = raza

  def obtener_raza(self):
    """Obtiene la raza del perro.

    Returns:
      La raza del perro.
    """
    return self.__raza

  def set_raza(self, raza):
    """Establece la raza del perro.

    Argumento
      raza: La nueva raza del perro.
    """
    self.__raza = raza

  def hablar(self):
    """Hace que el perro ladre."""
    print("¡Guau!")


class Gato(Animal):
  """Clase para representar un gato."""

  def __init__(self, nombre, edad, color):
    """Inicializa un nuevo objeto Gato.

    Args:
      nombre: El nombre del gato.
      edad: La edad del gato.
      color: El color del gato.
    """
    super().__init__(nombre, edad, "Gato")
    self.__color = color

  def obtener_color(self):
    """Obtiene el color del gato.

    Returns:
      El color del gato.
    """
    return self.__color

  def set_color(self, color):
    """Establece el color del gato.

    Args:
      color: El nuevo color del gato.
    """
    self.__color = color

  def hablar(self):
    """Hace que el gato maulle."""
    print("¡Miau!")


def main():
  """Función principal para interactuar con los animales."""

  animales = []  # Lista para almacenar los animales

  while True:
    tipo_animal = input("Ingrese el tipo de animal (perro/gato/salir): ")
    if tipo_animal.lower() == "perro":
      nombre = input("Ingrese el nombre del perro: ")
      edad = int(input("Ingrese la edad del perro: "))
      raza = input("Ingrese la raza del perro: ")
      perro = Perro(nombre, edad, raza)
      animales.append(perro)
    elif tipo_animal.lower() == "gato":
      nombre = input("Ingrese el nombre del gato: ")
      edad = int(input("Ingrese la edad del gato: "))
      color = input("Ingrese el color del gato: ")
      gato = Gato(nombre, edad, color)
      animales.append(gato)
    elif tipo_animal.lower() == "salir":
      break
    else:
      print("Tipo de animal inválido.")

  for animal in animales:
    print("El animal se llama", animal.obtener_nombre(), "y tiene", animal.obtener_edad(), "años.")
    print("El animal es de especie", animal.obtener_especie())
    if isinstance(animal, Perro):
      print("El perro es un", animal.obtener_raza())
    elif isinstance(animal, Gato):
      print("El gato es de color", animal.obtener_color())
    animal.hablar()

if __name__ == "__main__":
  main()
  print("cambios nuevos")
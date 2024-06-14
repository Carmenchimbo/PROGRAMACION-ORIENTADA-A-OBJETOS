class RegistroTemperatura:
  """
  Clase que representa la información diaria del clima.
  """

  def __init__(self, fecha, temperatura):
    """
    Constructor de la clase.

    Inicializa los atributos de la clase.
    """
    self.fecha = fecha
    self.temperatura = temperatura

  def ingresar_datos(self):
    """
    Método para ingresar la fecha y la temperatura del día.
    """
    self.fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    self.temperatura = float(input("Ingrese la temperatura: "))

  def calcular_promedio_semanal(self, registros_diarios):
    """
    Método para calcular el promedio semanal de las temperaturas.

    Recibe una lista de objetos RegistroTemperatura como parámetro.
    Retorna el promedio semanal de las temperaturas.
    """
    suma_temperaturas = 0
    for registro in registros_diarios:
      suma_temperaturas += registro.temperatura
    promedio_semanal = suma_temperaturas / len(registros_diarios)
    return promedio_semanal

def main():
  """
  Función principal del programa.
  """
  registros_diarios = []
  for i in range(7):
    registro = RegistroTemperatura(None, None)
    registro.ingresar_datos()
    registros_diarios.append(registro)

  promedio_semanal = registros_diarios[0].calcular_promedio_semanal(registros_diarios)
  print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}")

if __name__ == "__main__":
  main()
def ingresar_temperatura():
    # Función para solicitar al usuario la fecha y la temperatura y devolverlas como una tupla
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")  # Solicita al usuario que ingrese la fecha
    temperatura = float(input("Ingrese la temperatura: "))  # Solicita al usuario que ingrese la temperatura y la convierte a float
    return fecha, temperatura  # Devuelve la fecha y la temperatura como una tupla

def calcular_promedio_semanal(registros_diarios):
    # Función para calcular el promedio semanal de las temperaturas
    suma_temperaturas = sum(registro[1] for registro in registros_diarios)  # Suma todas las temperaturas en la lista de registros diarios
    promedio_semanal = suma_temperaturas / len(registros_diarios)  # Calcula el promedio dividiendo la suma de temperaturas entre la cantidad de registros
    return promedio_semanal  # Devuelve el promedio semanal de las temperaturas

def main():
    # Función principal del programa
    registros_diarios = []  # Lista para almacenar los registros diarios
    for i in range(7):  # Itera sobre 7 días
        print(f"Ingrese los datos del día {i+1}:")
        fecha, temperatura = ingresar_temperatura()  # Llama a la función para ingresar la fecha y la temperatura
        registros_diarios.append((fecha, temperatura))  # Agrega la tupla (fecha, temperatura) a la lista de registros diarios

    promedio_semanal = calcular_promedio_semanal(registros_diarios)  # Calcula el promedio semanal llamando a la función correspondiente
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}")  # Imprime el promedio semanal con dos decimales

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta como un programa independiente

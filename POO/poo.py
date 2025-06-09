class ClimaDiario:
    def __init__(self):
        # Encapsulación: Lista privada para almacenar temperaturas
        self.__temperaturas = []

    def ingresar_temperatura(self, temp):
        """Metodo para agregar una temperatura a la lista."""
        self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """Metodo para calcular el promedio semanal de temperaturas."""
        return sum(self.__temperaturas) / len(self.__temperaturas) if self.__temperaturas else 0


# Programa principal
def main():
    clima = ClimaDiario()

    for i in range(7):
        temp = float(input(f"Por favor ingrese la temperatura del día {i + 1}: "))
        clima.ingresar_temperatura(temp)

    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


# Ejecutar el programa
if __name__ == "__main__":
    main()

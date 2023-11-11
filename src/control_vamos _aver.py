import serial
import time
import keyboard  # Asegúrate de haber instalado la biblioteca

# Configurar el puerto serie
ser = serial.Serial("COM16", baudrate=9600, timeout=1)  # Ajusta el nombre del puerto según tu configuración

# Bucle para leer los valores
while True:
    # Leer datos desde el puerto serie
    data = ser.readline().decode('utf-8').strip()
    if data != "":
        print("Received:", data)

        # Emular la tecla correspondiente
        keyboard.press(data)
        time.sleep(0.1)
        keyboard.release(data)
    else:
        pass

    # Esperar un breve período de tiempo antes de la próxima lectura
    time.sleep(0.1)
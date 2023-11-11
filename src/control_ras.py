import machine
import utime



uart = machine.UART(0, baudrate=9600, tx=0, rx=1)  # Pines TX y RX dependen de tu conexión física

# Configuración de pines
joystick_x_pin = 26
joystick_y_pin = 27
buttons_pin = [2,3,4,5,6,7,8,9]

# Configuración de ADC
adc_x = machine.ADC(joystick_x_pin)
adc_y = machine.ADC(joystick_y_pin)

# Configuración de botones
buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in buttons_pin]

# Mapa de letras para cada botón
button_letters = {
    9: "Q",
    8: "E",
    7: "R",
    6: "T",
    5: "Y",
    4: "U",
    3: "I",
    2: "O",
}

# Variable para almacenar el estado anterior de los botones
prev_button_states = [0] * len(buttons)

# Función para leer el joystick y los botones
def read_input():
    x_value = adc_x.read_u16()
    y_value = adc_y.read_u16()
    button_states = [button.value() for button in buttons]

    return x_value, y_value, button_states

# Bucle principal
while True:
    x, y, button_states = read_input()

    # Determinar la dirección del joystick
    if x < 2000:
        uart.write("A")
        print("A")
    elif x > 60000:
        uart.write("D")
        print("D")

    if y < 2000:
        uart.write("W")
        print("W")
    elif y > 60000:
        uart.write("S")
        print("S")

    # Verificar el estado de los botones e imprimir letras correspondientes
    for pin, state, prev_state in zip(buttons_pin, button_states, prev_button_states):
        if state == 1 and prev_state == 0:
            if pin in button_letters:
                uart.write(button_letters[pin])
                print(button_letters[pin])

    # Actualizar el estado anterior de los botones
    prev_button_states = button_states.copy()

    # Esperar un breve período de tiempo para evitar lecturas rápidas
    utime.sleep_ms(100)
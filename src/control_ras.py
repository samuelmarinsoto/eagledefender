from machine import Pin, ADC
import utime
import keyboard

# Configuración de pines para el joystick
pin_x = 26
pin_y = 27
button_pin = 15

# Configuración de pines para las teclas emuladas
key_a = 'a'
key_w = 'w'
key_s = 's'
key_d = 'd'

# Configuración de umbrales para la posición del joystick
threshold_low = 500
threshold_high = 6000

# Inicialización de pines
x_pin = ADC(Pin(pin_x))
y_pin = ADC(Pin(pin_y))
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

# Función para emular las teclas
def emulate_keys(x, y):
    if x < threshold_low:
        keyboard.press_and_release(key_a)
    elif x > threshold_high:
        keyboard.press_and_release(key_d)

    if y < threshold_low:
        keyboard.press_and_release(key_w)
    elif y > threshold_high:
        keyboard.press_and_release(key_s)

# Bucle principal
while True:
    x = x_pin.read_u16()
    y = y_pin.read_u16()
    button_state = button.value()

    # Emular teclas solo si el botón del joystick está presionado
    if button_state == 0:
        emulate_keys(x, y)

    utime.sleep(0.1)  # Ajusta según sea necesario para evitar la repetición rápida de teclas

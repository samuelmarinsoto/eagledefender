#include <Keyboard.h>

// Configurar los pines para los botones y el joystick
const int buttonPin1 = 7;
const int buttonPin2 = 8;
const int buttonPin3 = 9;
const int buttonPin4 = 10;
const int joyXPin = A0;
const int joyYPin = A1;
const int Buttonjoy = 2;

bool button1Pressed = false;
bool button2Pressed = false;
bool button3Pressed = false;
bool button4Pressed = false;
bool buttonjoypressed = false;

// Definir umbrales para las direcciones del joystick
const int joyThresholdLow = 200;
const int joyThresholdHigh = 800;

void setup() {
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(Buttonjoy, INPUT);

  Keyboard.begin();
}

void loop() {
  // Verificar si se ha presionado el botón del joystick (Buttonjoy)
  if (digitalRead(Buttonjoy) == LOW) {
    if (!buttonjoypressed) {
      Serial.println("Joystick Button Pressed");
      buttonjoypressed = true;

      // Emular la tecla "q" al servidor
      Keyboard.write('q');
    }
  } else {
    buttonjoypressed = false;
  }
  // Verificar si se ha presionado el botón 1 (pin 7)
  if (digitalRead(buttonPin1) == LOW) {
    if (!button1Pressed) {
      Serial.println("1");
      button1Pressed = true;

      // Enviar la letra "h" al servidor
      Keyboard.write('1');
    }
  } else {
    button1Pressed = false;
  }

  // Verificar si se ha presionado el botón 2 (pin 8)
  if (digitalRead(buttonPin2) == LOW) {
    if (!button2Pressed) {
      Serial.println("2");
      button2Pressed = true;

      // Enviar la letra "j" al servidor
      Keyboard.write('2');
    }
  } else {
    button2Pressed = false;
  }



  // Verificar si se ha presionado el botón 3 (pin 9)
  if (digitalRead(buttonPin3) == LOW) {
    if (!button3Pressed) {
      Serial.println("3");
      button3Pressed = true;

      // Enviar la letra "k" al servidor
      Keyboard.write('3');
    }
  } else {
    button3Pressed = false;
  }

  // Verificar si se ha presionado el botón 4 (pin 10)
  if (digitalRead(buttonPin4) == LOW) {
    if (!button4Pressed) {
      Serial.println("4");
      button4Pressed = true;

      // Enviar la letra "o" al servidor
      Keyboard.write('4');
    }
  } else {
    button4Pressed = false;
  }

  // Leer las lecturas analógicas del joystick
  int joyXValue = analogRead(joyXPin);
  int joyYValue = analogRead(joyYPin);

  // Imprimir 'w', 'a', 's' o 'd' según la dirección del joystick
  if (joyXValue < joyThresholdLow) {
    Keyboard.write('a');
  } else if (joyXValue > joyThresholdHigh) {
    Keyboard.write('d');
  }
  if (joyYValue < joyThresholdLow) {
    Keyboard.write('w');
  } else if (joyYValue > joyThresholdHigh) {
    Keyboard.write('s');
  }

  delay(100);
}
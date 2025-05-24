import sys  # Importamos sys para poder cerrar la aplicación correctamente
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QGridLayout,
                             QPushButton, QLineEdit)  # Importamos los widgets necesarios
from PyQt5.QtCore import Qt  # Importamos Qt para usar alineaciones

# Clase principal de la calculadora, hereda de QWidget
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base
        self.setWindowTitle("Calculadora Mejorada")  # Establece el título de la ventana
        self.setFixedSize(320, 400)  # Tamaño fijo de la ventana
        self.init_ui()  # Llama al método que construye la interfaz

    # Método para construir la interfaz de usuario
    def init_ui(self):
        layout = QVBoxLayout()  # Layout vertical principal
        self.setLayout(layout)  # Establece el layout para el widget principal

        # Campo de texto donde se muestra la operación y el resultado
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)  # Alineación del texto a la derecha
        self.display.setFixedHeight(50)  # Altura fija del campo de texto
        self.display.setStyleSheet("font-size: 24px;")  # Estilo (tamaño de fuente)
        self.display.setReadOnly(True)  # El usuario no puede escribir directamente
        layout.addWidget(self.display)  # Se añade al layout principal

        # Definimos los botones en una matriz (listas de listas)
        botones = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '⌫']  # Botón para limpiar todo y para borrar el último dígito
        ]

        grid = QGridLayout()  # Layout de cuadrícula para organizar los botones
        layout.addLayout(grid)  # Se añade el layout de botones al layout principal

        # Recorremos la lista de botones para crearlos y colocarlos
        for fila, fila_valores in enumerate(botones):
            for col, texto in enumerate(fila_valores):
                boton = QPushButton(texto)  # Creamos el botón
                boton.setFixedSize(70, 50)  # Tamaño fijo del botón
                boton.setStyleSheet("font-size: 18px;")  # Estilo del botón
                grid.addWidget(boton, fila, col)  # Lo añadimos al grid en la posición fila, col
                boton.clicked.connect(self.on_click)  # Conectamos el clic del botón con el método on_click

    # Método que se ejecuta al hacer clic en cualquier botón
    def on_click(self):
        boton = self.sender()  # Obtiene el botón que fue presionado
        texto = boton.text()  # Obtiene el texto del botón

        # Lógica según el botón presionado
        if texto == 'C':
            self.display.clear()  # Limpia toda la pantalla
        elif texto == '⌫':
            self.display.backspace()  # Elimina el último carácter
        elif texto == '=':
            self.calcular()  # Llama al método calcular()
        else:
            # Añade el texto del botón actual al display
            self.display.setText(self.display.text() + texto)

    # Método para calcular el resultado
    def calcular(self):
        try:
            expresion = self.display.text()  # Obtiene la expresión del display

            # Validamos que solo haya caracteres seguros: números, punto y operadores
            if not all(c in '0123456789.+-*/' for c in expresion):
                self.display.setText('Error')  # Si hay caracteres inválidos, mostramos error
                return

            # Evalúa la expresión de forma segura (porque validamos antes)
            resultado = str(round(eval(expresion), 6))  # Redondea el resultado a 6 decimales
            self.display.setText(resultado)  # Muestra el resultado
        except Exception:
            self.display.setText("Error")  # Si ocurre algún error, se muestra 'Error'

# Código principal que lanza la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea la aplicación
    window = Calculadora()  # Crea una instancia de la clase Calculadora
    window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta la aplicación y espera hasta que se cierre

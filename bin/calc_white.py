import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):  # Herdando de 'QMainWindow'.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Leandro')  # Mudando o nome da calculadora.
        self.setFixedSize(400, 400)  # Estabelecendo um tamanho fixo para a calculadora.
        self.cw = QWidget()  # Criando o widget.
        modo = 0
        self.cw.setStyleSheet('* {background: #ffffff;}')

        self.grid = QGridLayout(self.cw) # Definindo o grid.

        self.display = QLineEdit()  # Criando o display da calculadora.
        self.grid.addWidget(self.display, 0, 0, 1, 5)  # Adicionando no grid.
        # Posição: 0, 0 (linha 0, coluna 0) | Ocupa: 1, 5 (1 linha e 5 colunas)

        self.display.setDisabled(True)  # Desabilitando o input do display
        self.display.setStyleSheet('* {background: #dfdfdf; color: #000; font-size: 30px;}')

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # Ocupa todo o espaço disponínel.
        
        # Linha 1:
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)  # botão('7') / l1 / c0 / ocupa: 1, 1
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)  # botão('8') / l1 / c1 / ocupa: 1, 1
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)  # botão('9') / l1 / c2 / ocupa: 1, 1
        self.add_btn(QPushButton('+'), 1, 3, 1, 1,  # botão('+') / l1 / c3 / ocupa: 1, 1
                    style='background: #868686; color: #000; font-size: 20px; font-weight: 700;')

        self.add_btn(QPushButton('C'), 1, 4, 1, 1,  # botão('C') / l1 / c4 / ocupa: 1, 1
                    lambda: self.display.setText(''),  # Com função específica, limpar.
                    'background: #5e5e5e; color: #000; font-size: 20px; font-weight: 700;')

        # Linha 2:
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)  # botão('4') / l2 / c0 / ocupa: 1, 1
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)  # botão('5') / l2 / c1 / ocupa: 1, 1
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)  # botão('6') / l2 / c2 / ocupa: 1, 1
        self.add_btn(QPushButton('-'), 2, 3, 1, 1,  # botão('-') / l2 / c3 / ocupa: 1, 1
                    style='background: #868686; color: #000; font-size: 20px; font-weight: 700;')

        self.add_btn(QPushButton('<-'), 2, 4, 1, 1,  # botão('<-') / l2 / c4 / ocupa: 1, 1
                    lambda: self.display.setText(self.display.text()[:-1]),  # Apaga 1 nº
                    'background: #5e5e5e; color: #000; font-size: 20px; font-weight: 700;')

        # Linha 3:
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)  # botão('1') / l3 / c0 / ocupa: 1, 1
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)  # botão('2') / l3 / c1 / ocupa: 1, 1
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)  # botão('3') / l3 / c2 / ocupa: 1, 1
        self.add_btn(QPushButton('/'), 3, 3, 1, 1,  # botão('/') / l3 / c3 / ocupa: 1, 1
                    style='background: #868686; color: #000; font-size: 20px; font-weight: 700;')

        #self.add_btn(QPushButton(''), 3, 4, 1, 1)  # botão('') / l3 / c4 / ocupa: 1, 1

        # Linha 4:
        self.add_btn(QPushButton('.'), 4, 0, 1, 1,  # botão('.') / l4 / c0 / ocupa: 1, 1
                    style='background: #868686; color: #000; font-size: 20px; font-weight: 700;')
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)  # botão('0') / l4 / c1 / ocupa: 1, 1
        self.add_btn(QPushButton('%'), 4, 2, 1, 1,  # botão('') / l4 / c2 / ocupa: 1, 1
                    style='background: #868686; color: #000; font-size: 20px; font-weight: 700;')
        self.add_btn(QPushButton('*'), 4, 3, 1, 1,  # botão('*') / l4 / c3 / ocupa: 1, 1
                    style='background: #868686; color: #000; font-size: 20px; font-weight: 700;')

        self.add_btn(QPushButton('='), 3, 4, 2, 1,  # botão('=') / l3 / c4 / ocupa: 2, 1
                    self.eval_igual,
                    'background: #5e5e5e; color: #000; font-size: 20px; font-weight: 700;')

        self.setCentralWidget(self.cw)  # Definindo o eidget central.


    def add_btn(self, btn, row, col, rowspan, colspan, fun=None, style=None):  # botão/linha/coluna...
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not fun:  # Se não for informada uma função, recebe o comportamento padrão:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            btn.setStyleSheet('background: #b3b3b3; color: #000; font-size: 20px; font-weight: 700;')

        else:  # Caso haja uma função específica ao ser enviada ela é implementada aqui:
            btn.clicked.connect(fun)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if style:
            btn.setStyleSheet(style)

    def eval_igual(self):  # Método que verifica o que está na tela e mostra o resultado.
        try:
            self.display.setText(str(eval(self.display.text())))
            # 'eval' caucula o texto da tela (self.display.text) e retorna 'str',
            # que é recebido por 'self.display.setText' que coloca na tela.

        except Exception as error:
            self.display.setText('Operação inválida.')


def run_white():
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()   


if __name__ == '__main__':
        qt = QApplication(sys.argv)
        calc = Calculadora()  # Instanciando a calculadora.
        calc.show()
        qt.exec_()        
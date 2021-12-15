from qt_core import *

class ContatoPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/clientes_page.ui')
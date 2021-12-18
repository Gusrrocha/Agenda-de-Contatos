from controller.criar_contato_page import CriarContato
from qt_core import *
from controller.contatos_page import ContatosPage
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        # evento da tabela
        self.show_contatos_page()

        #  evento do botão novo contato
        self.novo_contato.clicked.connect(self.show_criar_contato)
        self.contatos_btn.clicked.connect(self.show_contatos_page)

    def show_criar_contato(self, contato=None):
        self.painel.insertWidget(1, CriarContato(self, contato))
        self.painel.setCurrentIndex(1)

    def show_contatos_page(self):
        self.painel.insertWidget(0, ContatosPage(self))
        self.painel.setCurrentIndex(0)
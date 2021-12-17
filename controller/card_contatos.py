from qt_core import *
from assets.color import getColor
class CardContatos(QWidget):
    def __init__(self, contato):
        super().__init__()
        uic.loadUi('view/card_contatos.ui', self)

        self.icon.setText(contato.nome[0])
        self.nome.setText(contato.nome +' '+contato.sobrenome)
        self.email.setText(contato.email)
        self.telefone.setText(contato.telefone)

        # determina o estilo do label
        cor = getColor()
        style_sheet = f'border: 3px solid {cor}; border-radius: 25px; background-color: {cor};'
        self.icon.setStyleSheet(style_sheet)
    


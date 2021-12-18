from qt_core import *
from model.contatos import Contatos
import model.contato_dao as contato_dao
from assets.color import getColor
class CriarContato(QWidget):
    def __init__(self, mainWindow, contato=None):
        super().__init__()
        uic.loadUi('view/criar_contato_page.ui', self)
        self.mainWindow = mainWindow
        self.contato = contato
        if contato != False:
            self.carrega_contato()

        self.fechar.clicked.connect(self.fechar_page)
        self.salvar.clicked.connect(self.salvar_contato)

          # estilo do favorito
        self.fav.setStyleSheet("QCheckBox::indicator {width: 30px;height: 30px;}"
                               "QCheckBox::indicator:checked {image: url(assets/icons/star-unfilled.png);}"
                               "QCheckBox::indicator:unchecked {image: url(assets/icons/star-filled.png);}")

    def fechar_page(self):
        self.mainWindow.painel.setCurrentIndex(0)

    def carrega_contato(self):
        self.nome_label.setText(self.contato.nome +' '+ self.contato.sobrenome)
        self.name.setText(self.contato.nome)
        self.surname.setText(self.contato.sobrenome)
        self.company.setText(self.contato.emp)
        self.cargo.setText(self.contato.cargo)
        self.email.setText(self.contato.email)
        self.telefone.setText(self.contato.telefone)
        self.obs.setText(self.contato.obs)
        self.fav.setChecked(self.contato.favorito)

        cor = getColor()
        style_sheet = f'border: 3px solid {cor}; border-radius: 25px; background-color: {cor};'
        self.img.setStyleSheet(style_sheet)
        if self.contato.nome != " ":
            self.img.setText(self.contato.nome[0])

    def salvar_contato(self):
        nome = self.name.text()
        sobrenome = self.surname.text()
        emp = self.company.text()
        cargo = self.cargo.text()
        email = self.email.text()
        telefone = self.telefone.text()
        obs = self.obs.text()
        fav = int(self.fav.isChecked())
        
        if self.contato != False: # edição
            editado = Contatos(self, nome, sobrenome, emp, cargo, email, telefone, obs, fav)

            contato_dao.update(editado)
        else: # uma criação
            # cria novo objeto
            novo = Contatos(None, nome, sobrenome, emp, cargo, email, telefone, obs, fav)

            # insere no banco de dados
            contato_dao.insert(novo)

        #depois de salvar no banco
        # carrega os dados no mainwindow
        self.mainWindow.show_contatos_page()


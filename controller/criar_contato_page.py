from qt_core import *
from model.contatos import Contatos
import model.contato_dao as contato_dao
class CriarContato(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/criar_contato_page.ui', self)
        self.mainWindow = mainWindow
        self.fechar.clicked.connect(self.fechar_page)
        self.salvar.clicked.connect(self.salvar_contato)

    def fechar_page(self):
        self.mainWindow.painel.setCurrentIndex(0)

    def salvar_contato(self):
        nome = self.name.text()
        sobrenome = self.surname.text()
        emp = self.company.text()
        cargo = self.cargo.text()
        email = self.email.text()
        telefone = self.telefone.text()
        obs = self.obs.text()
        fav = 0
        
        # cria novo objeto
        novo = Contatos(None, nome, sobrenome, emp, cargo, email, telefone, obs, fav)

        # insere no banco de dados
        contato_dao.insert(novo)

        #depois de salvar no banco
        # carrega os dados no mainwindow
        self.mainWindow.show_contatos_page()
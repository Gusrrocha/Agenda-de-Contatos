class Contatos():
    def __init__(self, id, nome, sobrenome, emp, cargo, email, telefone, obs, favorito, deletado=0): # atribuir um valor a uma varíavel no init é o mesmo que informar seu valor padrão em caso de não existência
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.emp = emp
        self.cargo = cargo
        self.email = email
        self.telefone = telefone
        self.obs = obs
        self.favorito = favorito
        self.deletado = deletado

    def getContato(self):
        return [self.nome, self.sobrenome, self.emp, self.cargo, self.email, 
                self.telefone, self.obs, self.favorito]

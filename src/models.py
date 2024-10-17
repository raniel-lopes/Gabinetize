class Eleitor:
    def __init__(self, nome, cpf, endereco, telefone, secao, zona, data_nascimento, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.secao = secao
        self.zona = zona
        self.data_nascimento = data_nascimento
        self.email = email

    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Endereço: {self.endereco}\n"
            f"Telefone: {self.telefone}\n"
            f"Seção: {self.secao}\n"
            f"Zona: {self.zona}\n"
            f"Data de Nascimento: {self.data_nascimento}\n"
            f"E-mail: {self.email}\n"
        )
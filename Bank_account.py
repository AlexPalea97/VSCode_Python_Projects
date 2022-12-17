class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto 


class ContoCorrente(Conto):
    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
        self.__saldo = importo

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo 

    def descrizione(self):
        print(self.nome, self.conto, self.__saldo)

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)


class GestoreContoCorrente:
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)


customer1 = ContoCorrente('Alex', 'under30', 5000)
customer2 = ContoCorrente('John', 'under40', 7500)
customer3 = ContoCorrente('Alice', 'under25', 3000)

customer1.descrizione()
customer2.preleva(500)
customer3.deposita(300)
customer2.descrizione()
customer3.descrizione()

customer1.saldo = 8000
customer1.descrizione()

GestoreContoCorrente.bonifico(customer1, customer3, 250)
customer1.descrizione()
customer3.descrizione()
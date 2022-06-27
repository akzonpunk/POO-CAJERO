class Cajero:
    monto=2000
    print('BIENVENIDO ATM')
    def operaciones(self):
        self.opcion = int(input('''
        ------------------------
             INDIQUE QUE OPERACION DESEA REALIZAR..
        1.DEPOSITO A CUENTA
        2.RETIRO DE EFECTIVO
        3.CONSULTAR BALANCE
        4.SALIR'''))
        self.control=0
        while self.control==o:
          if self.opcion==1:
                self.depositar()
            elif self.opcion==2:
                self.retirar()
            elif self.opcion==3:
                self.consultarbalance()
            elif self.opcion==4:
                self.control=1
                self.salir()
            else:
                print('opcion no valida;intente de nuevo'
                self.operaciones()


    def depositar(self):
        self.deposito = int(input('indique la cantidad a depositar..'))
        self.monto=self.monto + self.deposito
        self.consultarbalance()

    def retirar(self):
        self.retiro = int(input('indique la cantidad a retirar..'))
        self.control = 0
        while self.control==0:
            if self.retiro > self.monto:
                print('''usted no cuenta con saldo suficiente para hacer este retiro
                por favor intente de nuevo con otra opcion..
                ----------------------------------------''')
                self.retiro = int(input('indique la cantidad a retirar..'))
        elif self.retiro<=self.monto:
            self.monto=self.monto-self.retiro
            self.control=1
            print('cantidad retirada:',self.retiro)
            self.consultabalance()

    def consultarbalance(self):
        print('su balance disponible es:', self.monto)
        print('Desea realizar otra operacion?')
    def salir(self):
        print('---------------')
        print('VUELVA PRONTO GRACIAS POR SU PREFERENCIA')
        print('---------------')
ejecucion = cajero()
ejecucion.operaciones()
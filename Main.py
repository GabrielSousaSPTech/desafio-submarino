import unittest



class Submarino:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.bussola = ['Norte', 'Leste', 'Sul', 'Oeste']
        self.direcao = self.bussola[0]
        
    def clearCoordenada (self):
       self.__init__()

    def atribuirCoordenada (self, comando =''):
        
        self.clearCoordenada()
        for comando_atual in comando.upper():
            posicaoAtual = ""
           
            if(comando_atual != "M" and comando_atual != "U" and comando_atual !="D"):
                posicaoAtual = comando_atual
                indice = self.bussola.index(self.direcao)

                if posicaoAtual == "R":
                    self.direcao = self.bussola[(indice + 1) % 4]
                elif posicaoAtual == "L":
                    self.direcao = self.bussola[(indice - 1) % 4]
                
            elif(comando_atual == "M"):
                if(self.direcao == "Norte"):
                    self.y +=1
                elif(self.direcao == "Sul"):
                    self.y -=1
                elif(self.direcao == "Leste"):
                    self.x +=1
                elif(self.direcao == "Oeste"):
                    self.x -=1
            elif(comando_atual == "U" and self.z < 0):
                
                self.z +=1
            elif(comando_atual == "D"):
                
                self.z -=1
        return f"{self.x} {self.y} {self.z} {self.direcao.upper()}"
    
        

class SubmarinoTest(unittest. TestCase):
    def testCoordenada(self):
        sub = Submarino()
        self.assertEqual('0 0 0 NORTE', sub.atribuirCoordenada())
        self.assertEqual('0 0 -1 NORTE', sub.atribuirCoordenada("D"))
        self.assertEqual('0 0 0 NORTE', sub.atribuirCoordenada("U"))
        self.assertEqual('0 0 0 OESTE', sub.atribuirCoordenada("L"))
        self.assertEqual('0 0 0 LESTE', sub.atribuirCoordenada("R"))
        self.assertEqual('2 3 -2 SUL', sub.atribuirCoordenada("RMMLMMMDDLL"))
        self.assertEqual('-1 2 0 NORTE', sub.atribuirCoordenada("LMRDDMMUU"))
    

if __name__ == '__main__':
    unittest.main()
import unittest

class Submarino (object):
    x = 0
    y = 0
    z = 0
    direcao = "Norte"
    def atribuirCoordenada (self, comando):
        
        for comando_atual in comando:
            posicaoAtual
            comando_atual
            if(comando_atual != 'M'):
                posicaoAtual = comando_atual
                if(self.direcao =="Norte" & posicaoAtual == "R"):
                    self.direcao = "Leste"
                if(self.direcao == "Norte" & posicaoAtual == "L"):
                    self.direcao = "Oeste"
                

            

class SubmarinoTest(unittest. TestCase):
    def testFoo(self):
        sub = Submarino
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
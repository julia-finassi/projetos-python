# Simulador de dados que mostra números aleatórios de 1 a 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor? '
        # layout dos botões e frase
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]



    def Iniciar(self):
        # janela para colocar layout
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler valores da tela
        self.eventos, self.valores = self.janela.Read()
        resposta = input(self.mensagem)
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.gerarValorDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Game over!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta!')

    def gerarValorDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
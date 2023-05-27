from PySimpleGUI import PySimpleGUI as sg
from tela_deposito import tela_deposito
from tela_saque import tela_saque
from tela_extrato import tela_extrato

saldo = 0
limite = 50000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def atualizar_saldo(valor):
    global saldo
    saldo += valor

def registrar_transacao(transacao):
    global extrato
    extrato += transacao

def tela_principal():
    layout = [
        [sg.Text('Bem-vindo(a) ao seu banco.', font=('Helvetica', 20))],
        [sg.Text(f'Saldo: R$ {saldo:.2f}', font=('Helvetica', 12), key='-SALDO-')],
        [
            sg.Button('Depositar', key='Depositar', size=(15, 2), button_color=('red', 'black')),
            sg.Button('Sacar', key='Sacar', size=(15, 2), button_color=('red', 'black'))
        ],
        [
            sg.Button('Extrato', key='Extrato', size=(15, 2), button_color=('red', 'black')),
            sg.Button('Sair', key='Sair', size=(15, 2), button_color=('red', 'black'))
        ]
    ]

    window = sg.Window('Tela de Login', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break

        elif event == 'Depositar':
            tela_deposito(atualizar_saldo, registrar_transacao)
            sg.popup('Depósito realizado com sucesso!', title='Sucesso!')

        elif event == 'Sacar':
            tela_saque(atualizar_saldo, registrar_transacao, saldo, limite, numero_saques, LIMITE_SAQUES)
            sg.popup('Saque realizado com sucesso!', title='Sucesso!')

        elif event == 'Extrato':
            tela_extrato(extrato, saldo)

        # Atualiza o valor do saldo na tela principal
        window['-SALDO-'].update(f'Saldo: R$ {saldo:.2f}')

    window.close()

tela_principal()

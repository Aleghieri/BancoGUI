from PySimpleGUI import PySimpleGUI as sg

def tela_deposito(atualizar_saldo, registrar_transacao):
    layout = [
        [sg.Text('Tela de Depósito')],
        [sg.Input(key='-VALOR-')],
        [sg.Button('Depositar', key='Depositar')],
        [sg.Button('Voltar', key='Voltar')]
    ]

    window = sg.Window('Tela de Depósito', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            break

        elif event == 'Depositar':
            valor = float(values['-VALOR-'])
            if valor > 0:
                atualizar_saldo(valor)
                registrar_transacao(f"Depósito: R$ {valor:.2f}\n")

    window.close()

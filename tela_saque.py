from PySimpleGUI import PySimpleGUI as sg

def tela_saque(atualizar_saldo, registrar_transacao, saldo, limite, numero_saques, LIMITE_SAQUES):
    layout = [
        [sg.Text('Tela de Saque')],
        [sg.Input(key='-VALOR-')],
        [sg.Button('Sacar', key='Sacar')],
        [sg.Button('Voltar', key='Voltar')]
    ]

    window = sg.Window('Tela de Saque', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            break

        elif event == 'Sacar':
            valor = float(values['-VALOR-'])
            if valor > 0:
                if valor > saldo:
                    sg.popup('Operação falhou! Você não tem saldo suficiente.')
                elif valor > limite:
                    sg.popup('Operação falhou! O valor do saque excede o limite.')
                elif numero_saques >= LIMITE_SAQUES:
                    sg.popup('Operação falhou! Número máximo de saques excedido.')
                else:
                    atualizar_saldo(-valor)
                    registrar_transacao(f"Saque: R$ {valor:.2f}\n")
                    numero_saques += 1

    window.close()

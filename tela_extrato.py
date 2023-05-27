from PySimpleGUI import PySimpleGUI as sg

def tela_extrato(extrato, saldo):
    layout = [
        [sg.Text('Tela de Extrato')],
        [sg.Multiline(extrato, size=(30, 10), disabled=True)],
        [sg.Text(f"Saldo: R$ {saldo:.2f}")],
        [sg.Button('Voltar', key='Voltar')]
    ]

    window = sg.Window('Tela de Extrato', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            break

    window.close()


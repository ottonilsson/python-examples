import PySimpleGUI as sg # PySimpleGUI library


sg.theme('Reddit')   # Window theme


# Window layout
def main_window():
    layout = [  [sg.Text('== INPUT ==', pad=(5, 0))],
                [sg.Text('Input text:'), sg.InputText(key='-IN-')],
                [sg.Button('OK', pad=(5, 5), bind_return_key=True), sg.Button('Cancel')],
                [sg.Text('== OUTPUT ==', pad=(5, 5))],
                [sg.Multiline(size=(88, 20), font='Courier 10', key='-OUT-' + sg.WRITE_ONLY_KEY)],
                [sg.Button('Clear', pad=(5, 5))]]
    return sg.Window('Main window', layout) # Creates window and adds title


def main():
    window = main_window()

    # Event Loop; processing "events" and get "values" from inputs
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED: # if user closes the window
            break

        elif event == 'OK': # when OK-button is pressed
            return_value = values['-IN-']
            window['-IN-'].update('') # clear input window
            window['-OUT-' + sg.WRITE_ONLY_KEY].print(return_value) # submit input value
        elif event == 'Cancel': # when Cancle-button is pressed
            window['-IN-'].update('') # clear input window
        elif event == 'Clear': # when Clear-button is pressed
            window['-OUT-' + sg.WRITE_ONLY_KEY].update('') # clear output window

    window.close()


if __name__ == '__main__':
    main() # entry point of program
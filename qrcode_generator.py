import qrcode
import PySimpleGUI as sg
import re
import pyautogui
import os


# checks if input is URL
def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    return re.match(regex, string)

# QR Code Colors
colors = ["Black","Blue","Red", "Green"]

# opens up another terminal window with text and a button
layout = [[sg.Text("Input a QR Code Link and Image Name")], 
          [sg.Text("QR CODE LINK"), sg.InputText(do_not_clear=False)],
          [sg.Text("QR IMAGE NAME"), sg.InputText(do_not_clear=False)],
          [sg.Text("Select a QR Code color"), sg.Combo(colors, default_value=colors[0], enable_events=True, readonly=True, key='COLOR')],
          [sg.Button("CREATE"), sg.Button("CLOSE")]]

# Create the window
window = sg.Window("Windows QR Code Generator", layout)

# Create an event loop
while True:
    event, values = window.read()

    # End program if user closes window or 
    # presses the OK button
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

    if (event == "CREATE" and values[0] and values[1]): 
        if Find(values[0]):
            qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

            # holds QR code URL
            qr.add_data(values[0])

            qr.make(fit=True)


            img = qr.make_image(fill_color = values["COLOR"],
                                back_color = 'white')

            # location and file qrcode will save as
            # forward slashes for directory links
            path = os.path.join(os.path.expanduser('~'), 'Desktop', values[1] + '.png')
            img.save(path)

            values[0] = ''
            values[1] = ''
        else:
            pyautogui.alert("Please submit a valid URL for the QR Code :)",title="Oh No!")

window.close()
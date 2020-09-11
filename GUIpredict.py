import PySimpleGUI as sg
import os.path
from playsound import playsound
from NNpredict import predict

file_list_column = [
    [
        sg.Text("Choose a file top predict"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"),
    ],
]

sound_viewer_column = [
    [sg.Text("Choose a song to predict from")],
    [sg.Text("", size=(60, 1), key="-TOUT-")],
    [sg.Button("Play"), sg.Button("Predict")],
    [sg.Text("Result:", size=(60, 1), key="-RES-")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(sound_viewer_column),
    ]
]

window = sg.Window("NN Prediction", layout)
filename = None

while True:
    event, values = window.Read()

    if event in (None, "Exit"):
        break

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]

        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".wav",))
        ]
        window.Element("-FILE LIST-").Update(fnames)

    if event == "-FILE LIST-":
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            window.Element("-TOUT-").Update(filename)
        except:
            pass

    if event == "Play":
        playsound(filename)

    if event == "Predict":
        prediction = predict(filename)
        window.Element("-RES-").Update("Result: " + str(prediction))
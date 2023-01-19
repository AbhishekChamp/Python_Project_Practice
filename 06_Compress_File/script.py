import PySimpleGUI as sg


def widget(file_type):
    """Creating label, input, choose button"""
    if file_type ==  'Compress':
        label = sg.Text('Select files to compress:')
    elif file_type == 'Destination':
        label = sg.Text('Select destination folder:')
    input = sg.Input()
    choose_button = sg.FilesBrowse("Choose")
    
    return [label, input, choose_button]


compress = widget('Compress')
destination = widget('Destination')
compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[compress], [destination], [compress_button]])

window.read()
window.close()
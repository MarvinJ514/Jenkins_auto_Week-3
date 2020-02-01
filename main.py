###SystemInfo Program
#Created: 2020-01-31

import system_query
import PySimpleGUI
import pint 
import psutil
import platform


system_info = system_query.query_all()
system_info2 = platform.platform()
cpu_info = platform.processor()
machine_info = platform.machine()
ram_info = str(((system_info['ram'])['total'])/(1024*1024*1024))

#For testing purposes
#print(system_info['host'])
#print(system_info2)
#print(machine_info)
#print(cpu_info)
#print(((system_info['ram'])['total'])/(1024*1024*1024))

PySimpleGUI.theme('DarkAmber')
layout = [
    [PySimpleGUI.Text('Hostname = ' + system_info['host'])],
    [PySimpleGUI.Text('OS = ' + system_info['os'])],
    [PySimpleGUI.Text('Platform = ' + machine_info)],
    [PySimpleGUI.Text('CPU = ' + cpu_info)],
    [PySimpleGUI.Text('Available RAM = ' + ram_info)],
    [PySimpleGUI.SimpleButton('OK')]]

window = PySimpleGUI.Window('System Info', layout)

while True:
    event = window.read()
    if event in (None,'OK'):
        break
    exit()

window.close()

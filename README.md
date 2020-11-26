# IIR_application
Using accelerometer sensor and Arduino to control a game.

## Prerequisite
1. Python

Check the following webpage for instructions on how to install latest version of python:
https://www.python.org/downloads/

2. pyFirmata2

Check the following webpage for instructions on how to install pyFirmata2:
https://pypi.org/project/pyFirmata2/

3. pynput (Controller Library)

On terminal, install pynput with pip or pip3. 
```
pip install pynput
```
or
```
pip3 install pynput
```
*Reference resource: https://pypi.org/project/pynput/*

## How to run the Controller
1. Change Directory to a clone of this project.
```
cd IIR_application
```
2. Run the realtime_iir_main.py on the terminal.
```
python realtime_iir_main.py
```
or
```
python3 realtime_iir_main.py
```

## How to open the Demo Dinosaur game in browser
1. Use terminal to access the game directory(webGL format file).
```
cd IIR_application/Dinosaur_trial1
```
2. Use terminal to run http server at port 8000. Keep the terminal open (Exit shortcut: ctrl+c).
```
python -m http.server --cgi 8000
```
or
```
python3 -m http.server --cgi 8000
```
3. On a web browser, run localhost port 8000.
```
http://localhost:8000/
```
or
```
http://0.0.0.0:8000/
```

### Notes
You can use this controller on any other custom/pre-existing games. However, please make sure the key pressed in the controller(realtime_iir_main.py) is correspond to the game you want to play.

![Alt text](https://github.com/Lilypads/IIR_application/blob/main/game_preview.png)
![Alt text](https://github.com/Lilypads/IIR_application/blob/main/circuit_diagram.png)

# IIR_application
Using accelerometer sensor and Arduino to control a game.

Have a look at our video explaining what we did and filtering results: https://youtu.be/T_xc3NxIb94

## Prerequisite
1. Python

Check the following webpage for instructions on how to install latest version of python:
https://www.python.org/downloads/

2. pyFirmata2

Check the following webpage for instructions on how to install pyFirmata2:
https://pypi.org/project/pyFirmata2/

3. pynput (Keyboard Controller Library)

On a terminal, install pynput with pip or pip3. 
```
pip install pynput
```
or
```
pip3 install pynput
```
*Reference resource: https://pypi.org/project/pynput/*

4. Arduino board and accelerometer wired as in the __circuit_diagram__ image above

*You might need to change PORT number in the __realtime_iir_main.py__ script to the corresponding Arduino port on your PC.*

## How to run the game controller
1. Change Directory to a clone of this project in your local file system.
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
There should be 2 plots showing up. One is the unfiltered data. The other one is the filtered data. Keep this terminal running when you play.

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
For this demo game, shake accelerometer in z-axis to jump. Try to avoid the spikes.

### Notes
You can use this controller on any other custom/pre-existing games. However, please make sure the key pressed in the controller(realtime_iir_main.py) is correspond to the game you want to play.

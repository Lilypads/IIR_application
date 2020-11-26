# IIR_application
Using sensor to control a game.

## Prerequisite
1. Python
https://www.python.org/downloads/

2. Pynput controller library

```
pip install pynput
```
or
```
pip3 install pynput
```
## How to open the game in browser
1. Use terminal to access the game directory(webGL format file).
```
cd IIR_application/Dinosaur_trial1
```
2. Use terminal to run http server at port 8000. Keep the terminal open. (Exit shortcut: ctrl+c)
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

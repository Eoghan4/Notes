# NotesGPT
Uses ChatGPT to screenshot lecture slides and convert them into concise notes in markdown format.

## Prerequisits
Tesseract is needed. It can be downlaoded from https://github.com/UB-Mannheim/tesseract/wiki

```bash
pip install pytesseract
```

PILLOW, Pyautogui, pyperclip and Keyboard are also required.

```bash
pip install pyperclip
pip install Pillow
pip install pyautogui
pip install keyboard
```

For ChatGPT connection, the OpenAI module is needed.
```bash
pip install openai
```

## Using the Program
Press ']' to select an area to screenshot, and an alert will appear once the notes have been generated and coppied to your clipboard.
Just press 'Ctrl + V' to paste into your prefered note-taking app!
Press 'esc' to close the program.

## Important Info
After pressing ']' you will need to click and drag over the area of the screen you want to take a screenshot of.
Press 'esc' to close.
Make sure to enter your OpenAI key and info into the AI_Request.py file at lines 8, 9 and 10.

import pyautogui as gui, keyboard, time, pyperclip
import AI_Request, Image_to_Text, Screenshot

def main():
    while not keyboard.is_pressed("esc"):
        if keyboard.is_pressed("]"):
            pyperclip.copy("")
        
            text = Image_to_Text.image_to_text(Screenshot.screenshot())
            result = AI_Request.ai_request(text)
            gui.alert("Your Notes have been copied to your clipboard.", "Notes Taken!")
            
            pyperclip.copy(result)
            time.sleep(0.1)
            
    if gui.confirm("Close Program?") != 'OK':
        main()

if __name__ == "__main__":
    main()
#This code was mostly made by AI (Chatgtp)
#The only reason i did this was to show how easy it is to get ai to make some sort of cheat for games
#To make this custom for other guns change the self.patterns, This is one thing the ai isnt able to do for you on a gun per gun basis

#If it doesnt work after running it once, try open it again as it might have needed to install stuff
#to turn it on and off use the up arrow


#The pattern was made to work for the gun "Fcar"

#EdenFails
import threading
import time
from pynput import mouse, keyboard

def main():
    print("Script is loading, Please wait! After a moment press up arrow and click to see if it is enabled!")

def install_pywin32():
    try:
        from pip._internal import main as pipmain
        pipmain(["install", "--user", "pywin32"])
        print("pywin32 installed successfully. Please reopen the python script to make it work")
    except Exception as e:
        print(f"Error installing pywin32: {e}")

try:
    import win32api
    main()  
except ImportError:
    print("win32api not found. Installing pywin32...")

    install_thread = threading.Thread(target=install_pywin32)
    install_thread.start()

    timeout = 60  
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            import win32api
            install_thread.join()  
            main() 
            break  
        except ImportError:
            pass 
    else:
        print("Timeout reached. Installation unsuccessful.")



class CursorController:
    def __init__(self):
        self.shooting = False
        self.move_cursor = False
        self.stop_pattern = False
        self.pattern = [(0, 0), (0, 7), (0, 6), (0, 6), (0, 6), (0, 6), (0, 7), (0, 7), (0, 7), (0, 9), (0, 9), (0, 9), (-3, 9), (-3, 11), (-3, 12), (-3, 12), (0, 12), (-3, 12), (-3, 12), (-3, 14), (-3, 14), (-3, 12), (-3, 8), (-3, 8), (-2, 8), (-1, 8), (-1, 8), (-2, 4), (-2, 2), (-1, 4), (-2, 2), (-2, 1), (-1, 2), (-1, 4),(0, 3), (0, 2), (-1, 2),(0, 2), (-1, 2), (-1, 2),(-1, 2), (-1, 1), (0, 2),(-1, 3), (-1, 5), (-1, 2),(-1, 1), (0, 3), (-2, 4),(0, 3), (1, 2), (-1, 1),(0, 2), (-1, 2), (0, 2),(0, 3), (0, 2), (0, 1),(0, 2), (1, 2), (1, 1),(1, 2), (-1, 2), (0, 3),(0, 1), (-1, 2), (0, 2),(0, 2), (0, 2), (0, 3),(0, 2), (-1, 1), (0, 2),(0, 2), (-1, 5)]  # Extend the pattern
        #if you wish to change the pattern for other guns
        #change the self.pattern
        #how it works (a,b)
        #a is -left and +right
        #b is -up and +down
        # it itterates from the start to the end and moves the mouse position

        self.interval = 0.03 # Dont change this value as it seems to be fine
        self.mouse_speed = 1.0  # Dont change this value as it seems to be fine~

    def move_cursor_pattern(self):
        self.stop_pattern = False
        for x, y in self.pattern:
            if not self.shooting or not self.move_cursor or self.stop_pattern:
                break  
            win32api.mouse_event(1, int(x * self.mouse_speed), int(y * self.mouse_speed), 0, 0)
            time.sleep(self.interval)  


    def stop_pattern_execution(self):
        self.stop_pattern = True

    def toggle_move_cursor(self):
        self.move_cursor = not self.move_cursor

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            cursor_controller.shooting = True
            if cursor_controller.move_cursor:
                cursor_thread = threading.Thread(target=cursor_controller.move_cursor_pattern)
                cursor_thread.start()
        else:
            cursor_controller.shooting = False
            cursor_controller.stop_pattern_execution()

def on_key_release(key):
    if key == keyboard.Key.up:
        cursor_controller.toggle_move_cursor()


cursor_controller = CursorController()
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()
keyboard_listener = keyboard.Listener(on_release=on_key_release)
keyboard_listener.start()
mouse_listener.join()
keyboard_listener.join()
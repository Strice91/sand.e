from pynput.keyboard import Key, Listener

class KeyConroller:

    def __init__(self):
        self.v = "S"
        self.w = "S"
        self.io = True

    def on_press(self, key):
        if(key == Key.up):
            self.v = "D"
        if(key == Key.down):
            self.v = "R"
        if(key == Key.left):
            self.w = "L"
        if(key == Key.right):
           self.w = "R"

    def on_release(self, key):
        if key == Key.esc:
            self.v = "S"
            self.w = "S"
            self.io = False
            return False
    
        if(key == Key.space):
            self.v = "S"
            self.w = "S"
        if(key == Key.up):
            self.v = "S"
        if(key == Key.down):
            self.v = "S"
        if(key == Key.left):
            self.w = "S"
        if(key == Key.right):
           self.w = "S"

    def drive(self):
        # Collect events until released
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    
    k = KeyConroller()
    k.drive()
    print("test")
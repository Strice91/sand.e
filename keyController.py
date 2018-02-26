from pynput.keyboard import Key, Listener

class KeyConroller:

    def __init__(self):
        self.v = "s"
        self.w = "s"
        self.io = True

    def on_press(self, key):
        if(key == Key.up):
            self.v = "d"
        if(key == Key.down):
            self.v = "b"
        if(key == Key.left):
            self.w = "l"
        if(key == Key.right):
           self.w = "r"

    def on_release(self, key):
        if key == Key.esc:
            self.v = "s"
            self.w = "s"
            self.io = False
            return False
    
        if(key == Key.space):
            self.v = "s"
            self.w = "s"
        if(key == Key.up):
            self.v = "s"
        if(key == Key.down):
            self.v = "s"
        if(key == Key.left):
            self.w = "s"
        if(key == Key.right):
           self.w = "s"

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
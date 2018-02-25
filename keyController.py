from pynput.keyboard import Key, Listener

class KeyConroller:

    def __init__(self):
        self.v = 0
        self.w = 0
        self.io = True

    def on_press(self, key):
        if(key == Key.up):
            self.v = 100
        if(key == Key.down):
            self.v = -100
        if(key == Key.left):
            self.w = -100
        if(key == Key.right):
           self.w = 100

    def on_release(self, key):
        if key == Key.esc:
            self.v = 0
            self.w = 0
            self.io = False
            return False
    
        if(key == Key.space):
            self.v = 0
            self.w = 0
        if(key == Key.up):
            self.v = 0
        if(key == Key.down):
            self.v = 0
        if(key == Key.left):
            self.w = 0
        if(key == Key.right):
           self.w = 0

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
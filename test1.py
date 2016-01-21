from kivy.app import App
from kivy.uix.button import Button

class TutorialApp(App):
    def build(self):
        return Button()

if __name__=="main":
    TutorialApp().run()
    
    
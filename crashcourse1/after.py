

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView

class TutorialApp(App):


    
    def build(self):
        f = FloatLayout()
        b = Button(pos_hint={'x': 0.5, 'center_y': .5},text='Hello world', font_size=14)
        s = Scatter()
        l = Label(text="Hello!",font_size=150)
        
        def select_to(*args):
            try:
                print args[1][0]
            except:
                pass
    
        fi = FileChooserIconView()

        f.add_widget(s)        
        s.add_widget(l)
        l.add_widget(b)
        
        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)
            fi.bind(on_selection=select_to)
            f.add_widget(fi)
        b.bind(on_press=callback)
        return f

if __name__ == "__main__":
    TutorialApp().run()

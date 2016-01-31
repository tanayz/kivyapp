from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

class TutorialApp(App):
    
    def change_label_colour(self, *args):
        colour = [random.random() for i in xrange(3)] + [1]
        label = self.ids['my_label']
        label.color = colour
        
    def build(self):

        b = BoxLayout(orientation='vertical')
        t = TextInput(font_size=20,size_hint_y=None,height=200,on_text=self.change_label_colour)
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello!",font_size=50,id='my_label')

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t)
        b.add_widget(f)
        t.bind(text=l.setter('text'))
        return b
#if __name__=="main":

TutorialApp().run()
    
    
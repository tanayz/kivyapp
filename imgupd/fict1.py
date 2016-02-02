from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView

class Imglayout(FloatLayout):

    def __init__(self,**args):
        super(Imglayout,self).__init__(**args)

        with self.canvas.before:
            Color(0,0,0,0)
            self.rect=Rectangle(size=self.size,pos=self.pos)

        self.bind(size=self.updates,pos=self.updates)
    def updates(self,instance,value):
        self.rect.size=instance.size
        self.rect.pos=instance.pos
############################################# Newly added #####################################
    def select_to(self,*args):
        try:
            print args[1][0]
            iw = Image.open(args[1][0])
            iw.save('Yellow_Rose.jpg')
            gray = iw.convert('1')
            gray.save('Yellow_Rose.jpg')
            self.img3.source = 'Yellow_Rose.jpg'
            self.img4.source = 'Yellow_Rose.jpg'
            self.img.source = 'Yellow_Rose.jpg'
            self.img.reload()
            self.img3.reload()
            self.img4.reload()
        except:
            pass
###############################################################################################

class MainTApp(App):

    im=Image(source='phase.jpg')
    def build(self):
        root = BoxLayout(orientation='vertical')
        c = Imglayout()
        root.add_widget(c)
        self.im.keep_ratio= False
        self.im.allow_stretch = True        
        cat=Button(text="Categories",size_hint=(1,.07))
        cat.bind(on_press=self.callback)        
        c.add_widget(self.im)
        root.add_widget(cat);       
        return root

    def callback(self,value):
        self.im.source='Yellow_Rose.jpg'


if __name__ == '__main__':
    MainTApp().run()

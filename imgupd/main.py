from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from PIL import Image
#from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
<RootWidget>:
    manager:manager
    img:img
    img3:img3
    lab:lab
    do_default_tab:False
    ScreenManager:
        id:manager
        Screen:
            id:sc1
            name:'Load Img'
            FileChooserIconView
                canvas.before:
                    Color:
                        rgb:0.5,0.4,0.5
                    Rectangle:
                        pos:self.pos
                        size:self.size
                on_selection:root.select_to(*args)
        Screen:
            id:sc2
            name:'Image'
            FloatLayout:
                Button:
                    id:lab
                    pos_hint:{'right':0.55,'top':1}
                    size_hint:0.15,0.1
            RelativeLayout:
                Image:
                    id:img
                    on_touch_down:str('Relative:{}'.format(args[1].pos))
                    pos_hint:{"left":1,'bottom':1}
                    size_hint:0.5,1
                    allow_stretch:True                  
            RelativeLayout:
                Image:
                    id:img3
                    pos_hint:{"right":1,'bottom':1}
                    size_hint:0.5,1
                    allow_stretch:True

            
    ''')

class RootWidget(TabbedPanel):
    manager = ObjectProperty(None)
    def on_touch_up(self,touch):
        if not self.img3.collide_point(*touch.pos):
            return True
        else:
            self.lab.text = 'Pos:(%d,%d)' %(touch.x,touch.y)
            return True
    def switch_to(self,header):
        self.manager.current = header.screen
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header
        
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
        
    def update_touch_label(self,label,touch):
         label.text = 'Pos:(%d,%d)' %(touch.x,touch.y)
         label.texture_update()
         label.pos = touch.pos()
         label.size = label.texture_size[0]+20,label.texture_size[1]+20
         
class MainApp(App):
    title = 'Screen Widget'
    def build(self):
        return RootWidget()
    def on_pause(self):
        return True

if __name__ == '__main__':
    MainApp().run()
import kivy
kivy.require('1.0.6')

from kivy.app import App

from kivy.uix.filechooser import FileChooserIconView, FileChooserListView


#class Showcase(FloatLayout):
#    pass
#
#
#class KivyImageScatter(Scatter):
#    pass
#
#
#class ButtonsScatter(Scatter):
#    pass


class ShowcaseApp(App):

    def show_filechooser_icon(self):
        return FileChooserIconView()

    def show_filechooser_list(self):
        return FileChooserListView()


if __name__ in ('__main__', '__android__'):
    ShowcaseApp().run()

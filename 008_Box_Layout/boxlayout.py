#stack items horizontally or vertically

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


#Design our .kv design file
Builder.load_file('box.kv')

class MyLayout(Widget):


    pass
class AwesomeApp(App):
    def build(self):
        return MyLayout()
if __name__ == '__main__':
    AwesomeApp().run()

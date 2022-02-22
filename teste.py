from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
#from kivymd.uix.menu import MDDropdownMenu,MDDropdownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivy.properties import StringProperty
import os

class PongGame(MDFloatLayout):
    def on_kv_post(self, base_widget):
        menu_items = [
            {
                "text": f"Editar",
                "left_icon": "pencil",
                "viewclass": "Item",
                "on_release": lambda x=f"Item {1}": self.menu_callback(x),
            },
            {
                "text": f"Remover",
                "left_icon": "sticker-remove-outline",
                "viewclass": "Item",
                "on_release": lambda x=f"Item {2}": self.menu_callback(x),
            }
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=3,
            position="center",
            border_margin=0,
            ver_growth = "down",
            max_height=100,
            hor_growth = "right",
        )
    def menu_callback(self, text_item):
        print(text_item)
    def callback(instance):
        print('The button is being pressed')
    
    def build(self):
        return Builder.load_file("note.kv")

    def open_menu(self,btn,menu):
        menu.caller = btn
        menu.open()

class Item(OneLineAvatarIconListItem):
    left_icon = StringProperty()
    right_text = StringProperty()


class Note_app(MDApp):
    
    def build(self):
        
        self.theme_cls.theme_style = "Dark"
        return PongGame()


if __name__ == '__main__':
    Note_app().run()


from cgitb import text
from logging import root

from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout,BoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDFlatButton,MDRaisedButton,MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
import os

class PongGame(MDFloatLayout):
    
    def build(self):
        return Builder.load_file("note.kv")

   
    
class Item(OneLineAvatarIconListItem,MDBoxLayout):
    left_icon = StringProperty()

class Table(MDBoxLayout):
    table_name = StringProperty("Mesa")
    
    dialog = None
    def on_kv_post(self, base_widget):
        menu_items = [
            {
                "text": f"Editar",
                "left_icon": "pencil",
                "viewclass": "Item",
                "on_release": lambda x=f"edit": self.menu_callback(x),
            },
            {
                "text": f"Remover",
                "left_icon": "sticker-remove-outline",
                "viewclass": "Item",
                "on_release": lambda x=f"remove": self.menu_callback(x),
            }
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=2.9,
            #position="center",
            border_margin=1,
            ver_growth = "down",
            max_height=100,
            hor_growth = "right",
        )
    def menu_callback(self, text_item):
        if text_item == "edit":
            if not self.dialog:
                self.dialog = MDDialog(
                    title="Novo Nome",
                    type="custom",
                    buttons=[
                        MDFlatButton(
                            text="CANCEL",
                            theme_text_color="Custom",
                            text_color=(1,1,1,1),
                            on_release= lambda x: self.closeDialog()
                        ),
                        MDFlatButton(
                            text="UPDATE",
                            theme_text_color="Custom",
                            text_color=(1,1,1,1),
                            on_release = lambda x:self.grabText()
                        ),
                    ],
                    content_cls=Content(),

                )
            self.dialog.open()
            #print(self.menu.caller.parent.table_name)
        if text_item == "remove":
            
            self.remove_widget(self.parent.children[0])
            print(self.parent.children[0])
            for obj in self.parent.children:
                if isinstance(obj, MDRaisedButton):
                    print(obj)
    def grabText(self):
        for obj in self.dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                self.menu.caller.parent.table_name = obj.text
        self.dialog.dismiss()
        self.menu.dismiss()

    def closeDialog(self):
        
        self.dialog.dismiss()
        self.menu.dismiss()

    def open_menu(self,btn,menu):
        menu.caller = btn
        menu.open()
    def process(self,teste):
        print(self.children,teste)

class Content(BoxLayout):
    pass
class Add_table(BoxLayout):
    pass
class Main_box(MDGridLayout):
    
    def add_table(self):
        obj = self.children[0]
        if isinstance(obj, Add_table):
            print(obj)
            self.remove_widget(obj)
        
        self.add_widget(Table())
        self.add_widget(Add_table())
    
    
class Note_app(MDApp):
    
    def build(self):
        
        self.theme_cls.theme_style = "Dark"
        return PongGame()


if __name__ == '__main__':
    Note_app().run()

#icon: plus-circle
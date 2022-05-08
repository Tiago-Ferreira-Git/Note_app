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

table_number = 0
class PongGame(MDFloatLayout):
    
    def build(self):
        return Builder.load_file("note.kv")

   
    
class Item(OneLineAvatarIconListItem,MDBoxLayout):
    left_icon = StringProperty()

class Table(MDBoxLayout):
    
    global table_number
    print(table_number)
    dialog = None
    table_name = StringProperty("Mesa " + str(table_number))
    
    def on_kv_post(self, base_widget):
        menu_items = [
            {
                "text": f"Editar",
                "left_icon": "pencil",
                "viewclass": "Item",
                "on_release": lambda x=f"edit": self.menu_callback(x,self.table_name),
            },
            {
                "text": f"Remover",
                "left_icon": "sticker-remove-outline",
                "viewclass": "Item",
                "on_release": lambda x=f"remove": self.menu_callback(x,self.table_name),
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
    def menu_callback(self, text_item,table_name):
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
            obj = self.parent.children
            #print(obj)
            for objects in obj:
                #print(objects)
                if isinstance(objects, Table):
                   #self.remove_widget(obj)
                    if objects.table_name == table_name:

                       self.parent.remove_widget(objects)

                    #print(objects.table_name,table_name)
            
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
        global table_number
        
        
        obj = self.children[0]
        if isinstance(obj, Add_table):
            print(obj)
            self.remove_widget(obj)
        if table_number < 12:
            table_number += 1
        else:
            table_number = 1
        print(table_number)
        print(self.children)
        self.add_widget(Table())
        self.add_widget(Add_table())
        self.children[1].table_name = "Mesa " + str(table_number)
    
    
class Note_app(MDApp):
    
    def build(self):
        
        self.theme_cls.theme_style = "Dark"
        return PongGame()


if __name__ == '__main__':
    Note_app().run()

#icon: plus-circle
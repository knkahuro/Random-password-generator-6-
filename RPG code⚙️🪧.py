#k3nny
#09/04/24

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
import random
import string

class PasswordGenerator(BoxLayout):
    def generate_password(self, *args):
#randomly selects letters from the alphabets and numbers in a range of 6
        characters = string.ascii_letters + string.digits
        self.password = ''.join(random.choice(characters) for i in range(6))
        self.password_label.text = "Generating password..."
#create a time-gap when printing so that it looks more realistic
        Clock.schedule_once(self.display_password, 1.5)

    def display_password(self, dt):
        self.password_label.text = self.password
        Clipboard.copy(self.password)
        self.show_popup("Password Copied", "The password has been\n copied to your clipboard.")

    def show_popup(self, title, message):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def __init__(self, **kwargs):
        super(PasswordGenerator, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20

#creating a welcome message
       self.welcome_label = Label(text="Welcome to the Random Password Generator!", font_size=24)
        self.add_widget(self.welcome_label)

        self.password_label = Label(text="", font_size=36)
        self.add_widget(self.password_label)

#customizing the button
        self.generate_button = Button(text="Generate", on_press=self.generate_password, size_hint=(None, None), size=(700, 200))
        self.add_widget(self.generate_button)

class PasswordGeneratorApp(App):
    def build(self):
        self.title = "Random Password Generator"
        self.icon = "icon.png"
        return PasswordGenerator()

if __name__ == '__main__':
    PasswordGeneratorApp().run()

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from functions import *
from kivy.core.window import Window
import sys
class MyGrid(GridLayout):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #sets dimension
        self.cols = 1
        self.rows = 2

        self.history = TextInput(height=Window.size[1] * 0.9, size_hint_y=None)
        self.add_widget(self.history)

        self.new_message = TextInput(width=Window.size[0] * 0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Enter")

        self.send.bind(on_press=self.send_message)

        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)



    def send_message(self, _):
        print(self.new_message.text)

        user_response = self.new_message.text
        user_response = user_response.lower()
        if user_response != "quit":
            if user_response in GREETINGS:
                print(greeting(user_response))
                #1 way to write chat history
                #appends each string and new line

                self.history.text += 'You: ' + self.new_message.text + '\n'
                self.history.text += 'Chatbot: ' + greeting(user_response) + '\n'
            else:
                #note does not work with non char
                print("Chatbot: " + get_response(user_response))
                self.history.text += 'You: ' + self.new_message.text + '\n'
                self.history.text += 'Chatbot: ' + get_response(user_response) + '\n'
        else:
            sys.exit()
            #stops the entire program when quit

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()







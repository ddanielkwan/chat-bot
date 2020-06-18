import random
import tkinter as tk
from functions import *
root = tk.Tk(className="Chatbot")
user_input = tk.Entry(root)
#test
user_input.pack()



root.geometry("700x700")
def main():
   
    user_response = user_input.get()
    user_response = user_response.lower()
    if user_response != "quit":
        if user_response in GREETINGS:
            print(greeting(user_response))
        else:
            print("Chatbot: " + get_response(user_response))
            
    else:
        status = False
        print("Chatbot: bye")
    output.config(text=get_response(user_response))
    return




root.bind('<Return>', main)

button = tk.Button(root, text="Enter", command=main)
button.pack()

output = tk.Label(root, text='')
output.pack()

tk.mainloop()
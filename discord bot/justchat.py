from chat import *

def main():
    status = True
    while status:
        user_response = input()
        user_response = user_response.lower()
        if user_response != "quit":
            if user_response in GREETINGS:
                print(greeting(user_response))
            else:
                print("Chatbot: " + get_response(user_response))
                
        else:
            status = False
            print("Chatbot: bye")
        
    return
main()
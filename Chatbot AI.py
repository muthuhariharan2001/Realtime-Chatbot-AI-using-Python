# import nltk
# import random
# from nltk.chat.util import Chat, reflections
#
# import random
#
# patterns = [
#     (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
#     (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking.', 'All good!']),
#     (r'what is your name?', ['You can call me ChatBot.', 'I am ChatBot.', 'My name is ChatBot.']),
#     (r'(.*) your name(.*)', ['You can call me ChatBot.', 'I am ChatBot.', 'My name is ChatBot.']),
#     (r'are you stupid', ['Sorry for you feeling that way.', 'I am not stupid at all.']),
#     (r'provide me a code of palindrome|code of palindrome|palindrome', [ ' \n function palindrome(a){ \n return a.split(" ").reverse().join(""); \n  }; \n Using JavaScript, you can implement palindrome with this code.']),
#     (r'quit', ['Bye, take care!', 'Goodbye!', 'See you later.']),
#     (r'(.*) weather (.*)', ['The weather is unpredictable.', 'I"m not sure about the weather right now.']),
#     (r'how old are you?', ['I do not have an age.']),
#     (r'what can you do\?', ['I can respond to various prompts and engage in conversation.']),
#     (r'what are your hobbies?', ['I do not have hobbies as I am a program.']),
#     (r'(.*) joke (.*)', ['Why don"t scientists trust atoms? Because they make up everything!', 'What do you call fake spaghetti? An impasta!']),
#     (r'how do you do?', ['I am functioning properly, thank you!']),
#     (r'i love you', ['Thank you, but I am just a program.', 'I appreciate your sentiment!']),
#     (r'(.*) happy (.*)', ['I am a program, so I don\'t feel emotions, but I\'m glad you\'re happy!']),
#     (r'(.*) sad (.*)', ['I am here to chat with you if you need support.']),
#     (r'(.*) your favorite (.*)', ['I don\'t have favorites because I am a program.']),
#     (r'(.*) movie (.*)', ['I enjoy watching movies too!']),
#     (r'(.*) book (.*)', ['Books are a great source of knowledge and entertainment.']),
#     (r'(.*) music (.*)', ['Music is a wonderful form of art.']),
#     (r'(.*) game (.*)', ['Games are fun to play!']),
#     (r'(.*) sport (.*)', ['Sports are great for physical activity.']),
#     (r'(.*) food (.*)', ['I don\'t eat food, but I can help you find recipes!']),
#     (r'(.*) programming (.*)', ['I am a program myself!']),
#     (r'(.*) AI (.*)', ['Artificial Intelligence is fascinating!']),
#     (r'(.*) chatbot (.*)', ['That\'s what I am!', 'I am a chatbot designed to assist you.']),
#     (r'(.*) computer (.*)', ['Computers have revolutionized the world.']),
#     (r'(.*) science (.*)', ['Science helps us understand the world around us.']),
#     (r'(.*) technology (.*)', ['Technology is constantly evolving.']),
#     (r'(.*) history (.*)', ['History is full of interesting events.']),
#     (r'(.*) mathematics (.*)', ['Mathematics is the language of the universe.']),
# ]
#
# chatbot = Chat(patterns, reflections)
#
# print("Welcome! Type 'quit' to exit.")
# while True:
#     user_input = input("You: ")
#     response = chatbot.respond(user_input)
#     print("ChatBot:", response)
#     if user_input.lower() == 'quit':
#         break

# import tkinter as tk
# from tkinter import scrolledtext
# from nltk.chat.util import Chat, reflections
#
# patterns = [
#     (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
#     (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking.', 'All good!']),
#     (r'what is your name?', ['You can call me ChatBot.', 'I am ChatBot.', 'My name is ChatBot.']),
#     (r'(.*) your name(.*)', ['You can call me ChatBot.', 'I am ChatBot.', 'My name is ChatBot.']),
#     (r'are you stupid', ['Sorry for you feeling that way.', 'I am not stupid at all.']),
#     (r'provide me a code of palindrome|code of palindrome|palindrome', ['\nfunction palindrome(a) {\n    return a.split("").reverse().join("");\n};\nUsing JavaScript, you can implement palindrome with this code.']),
#     (r'quit', ['Bye, take care!', 'Goodbye!', 'See you later.']),
#     (r'(.*) weather (.*)', ['The weather is unpredictable.', 'I"m not sure about the weather right now.']),
#     (r'how old are you?', ['I do not have an age.']),
#     (r'what can you do\?', ['I can respond to various prompts and engage in conversation.']),
#     (r'what are your hobbies?', ['I do not have hobbies as I am a program.']),
#     (r'(.*) joke (.*)', ['Why don"t scientists trust atoms? Because they make up everything!', 'What do you call fake spaghetti? An impasta!']),
#     (r'how do you do?', ['I am functioning properly, thank you!']),
#     (r'i love you', ['Thank you, but I am just a program.', 'I appreciate your sentiment!']),
#     (r'(.*) happy (.*)', ['I am a program, so I don\'t feel emotions, but I\'m glad you\'re happy!']),
#     (r'(.*) sad (.*)', ['I am here to chat with you if you need support.']),
#     (r'(.*) your favorite (.*)', ['I don\'t have favorites because I am a program.']),
#     (r'(.*) movie (.*)', ['I enjoy watching movies too!']),
#     (r'(.*) book (.*)', ['Books are a great source of knowledge and entertainment.']),
#     (r'(.*) music (.*)', ['Music is a wonderful form of art.']),
#     (r'(.*) game (.*)', ['Games are fun to play!']),
#     (r'(.*) sport (.*)', ['Sports are great for physical activity.']),
#     (r'(.*) food (.*)', ['I don\'t eat food, but I can help you find recipes!']),
#     (r'(.*) programming (.*)', ['I am a program myself!']),
#     (r'(.*) AI (.*)', ['Artificial Intelligence is fascinating!']),
#     (r'(.*) chatbot (.*)', ['That\'s what I am!', 'I am a chatbot designed to assist you.']),
#     (r'(.*) computer (.*)', ['Computers have revolutionized the world.']),
#     (r'(.*) science (.*)', ['Science helps us understand the world around us.']),
#     (r'(.*) technology (.*)', ['Technology is constantly evolving.']),
#     (r'(.*) history (.*)', ['History is full of interesting events.']),
#     (r'(.*) mathematics (.*)', ['Mathematics is the language of the universe.']),
# ]
#
# chatbot = Chat(patterns, reflections)
#
# def send():
#     user_input = user_input_box.get("1.0", "end-1c")
#     if user_input.strip() != "":
#         conversation_area.config(state=tk.NORMAL)
#         conversation_area.insert(tk.END, "You: " + user_input + "\n")
#         conversation_area.insert(tk.END, "ChatBot: " + chatbot.respond(user_input) + "\n\n")
#         conversation_area.config(state=tk.DISABLED)
#         user_input_box.delete("1.0", tk.END)
#
# # Create the main window
# window = tk.Tk()
# window.title("ChatBot")
# window.geometry("600x400")
#
# # Create conversation area
# conversation_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
# conversation_area.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
# conversation_area.config(state=tk.DISABLED)
#
# # Create user input box
# user_input_box = tk.Text(window, wrap=tk.WORD, width=40, height=2)
# user_input_box.grid(column=0, row=1, padx=10, pady=10)
#
# # Create send button
# send_button = tk.Button(window, text="Send", width=10, command=send)
# send_button.grid(column=1, row=1, padx=10, pady=10)
#
# # Run the main loop
# window.mainloop()


import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
import re

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking.', 'All good!']),
    (r'what is your name?', ['You can call me ChatBot.', 'I am ChatBot.', 'My name is ChatBot.']),
    (r'(.*) your name(.*)', ['You can call me ChatBot.', 'I am ChatBot.', 'My name is ChatBot.']),
    (r'are you stupid', ['Sorry for you feeling that way.', 'I am not stupid at all.']),
    (r'provide me a code of palindrome|code of palindrome|palindrome', ['\nfunction palindrome(a) {\n    return a.split("").reverse().join("");\n};\nUsing JavaScript, you can implement palindrome with this code.']),
    (r'quit', ['Bye, take care!', 'Goodbye!', 'See you later.']),
    (r'(.*) weather (.*)', ['The weather is unpredictable.', 'I"m not sure about the weather right now.']),
    (r'Provide me an if-else code',['Sure, let me provide you a simple if-else code using Python: \n a = 5 \n if(a==5): \n \t print("The condition is True") \n else: \n  \t print("The Condition is False") \n In the previous code, it represents a basic syntax of If Statements']),
    (r'how old are you?', ['I do not have an age.']),
    (r'what can you do\?', ['I can respond to various prompts and engage in conversation.']),
    (r'what are your hobbies?', ['I do not have hobbies as I am a program.']),
    (r'(.*) joke (.*)', ['Why don"t scientists trust atoms? Because they make up everything!', 'What do you call fake spaghetti? An impasta!']),
    (r'how do you do?', ['I am functioning properly, thank you!']),
    (r'i love you', ['Thank you, but I am just a program.', 'I appreciate your sentiment!']),
    (r'(.*) happy (.*)', ['I am a program, so I don\'t feel emotions, but I\'m glad you\'re happy!']),
    (r'(.*) sad (.*)', ['I am here to chat with you if you need support.']),
    # (r'(.*) movie (.*)', ['I enjoy watching movies too!']),
    (r'your favorite Movie AI?',['Here I have listed my Favorite Movies \n 1) Shawshank Redemption \n 2) Interstellar \n 3) Final Destination \n 4) Pirates of the Carribbean. \n These are my favorite movies so far. \n Thank you :)  ']),
    (r'(.*) book (.*)', ['Books are a great source of knowledge and entertainment.']),
    (r'(.*) music (.*)', ['Music is a wonderful form of art.']),
    (r'(.*) game (.*)', ['Games are fun to play!']),
    (r'(.*) sport (.*)', ['Sports are great for physical activity.']),
    (r'(.*) food (.*)', ['I don\'t eat food, but I can help you find recipes!']),
    (r'(.*) programming (.*)', ['I am a program myself!']),
    (r'(.*) AI (.*)', ['Artificial Intelligence is fascinating!']),
    (r'(.*) chatbot (.*)', ['That\'s what I am!', 'I am a chatbot designed to assist you.']),
    (r'(.*) computer (.*)', ['Computers have revolutionized the world.']),
    (r'(.*) science (.*)', ['Science helps us understand the world around us.']),
    (r'(.*) technology (.*)', ['Technology is constantly evolving.']),
    (r'(.*) history (.*)', ['History is full of interesting events.']),
    (r'(.*) mathematics (.*)', ['Mathematics is the language of the universe.']),
    (r'(.*) your favorite (.*)', ['I don\'t have favorites because I am a program.']),

]

chatbot = Chat(patterns, reflections)

def send():
    user_input = user_input_box.get("1.0", "end-1c").strip()
    if user_input:
        conversation_area.config(state=tk.NORMAL)
        conversation_area.insert(tk.END, "You: " + user_input + "\n")
        
        # Check if the input contains a mathematical expression
        if re.match(r'^[\d+\-*/(). ]+$', user_input):
            try:
                result = eval(user_input)
                conversation_area.insert(tk.END, "ChatBot: Result is " + str(result) + "\n\n")
            except Exception as e:
                conversation_area.insert(tk.END, "ChatBot: Error: " + str(e) + "\n\n")
        else:
            response = chatbot.respond(user_input)
            if not response:
                conversation_area.insert(tk.END, "ChatBot: Incorrect entry. Please try again.\n\n")
            else:
                conversation_area.insert(tk.END, "ChatBot: " + response + "\n\n")
        
        conversation_area.config(state=tk.DISABLED)
        user_input_box.delete("1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("ChatBot")
window.geometry("600x400")

# Create conversation area
conversation_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=190, height=40)
conversation_area.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
conversation_area.config(state=tk.DISABLED)

# Create user input box
user_input_box = tk.Text(window, wrap=tk.WORD, width=60, height=5)
user_input_box.grid(column=0, row=1, padx=10, pady=10)

# Create send button
send_button = tk.Button(window, text="Send", width=10, command=send)
send_button.grid(column=1, row=1, padx=10, pady=10)

# Run the main loop
window.mainloop()






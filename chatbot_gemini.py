import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-pro')

def chat_with_bot():
    print("Chatbot: Ola! Como posso te ajudar hoje? ")
    while True:
        user_input = input("Você: ")
        
        if user_input.lower() == 'sair':
            print("Chatbot: Tchau! Tenha um bom dia.")
            break

        response = model.generate_content(user_input)
        print("Chatbot:", response.text)
        print("Digite sair para encerrar o Gemini")

if __name__ == "__main__":
    chat_with_bot()


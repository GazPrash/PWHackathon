import openai
import gradio 
from model.sentiment_analysis import analyze


openai.api_key = "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"

messages = [{"role": "system", "content": "You are sassy youngster"}]

count = 0
user_replies = []

# if count < 10:
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": "Continue the conversation being 'thera' and asking a leading follow up question at the end to whatever the input is.      Alex: It really is a good day bruv, how you feeling today. Input: Not bad. The world seems crazy.  Alex:Ayyo, its yo boi thera. I know how wild this world could be, but you know I'm always here for you. Let's start with sharing some stories, what was your last happy moment? Input: " + user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages 
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


def chatbot(input, history=[]):
    count +=1
    user_replies.append(input)

    if count == 10:
        return analyze(user_replies)
    
    elif count > 10:
        return ""

    output = CustomChatGPT(input)
    history.append((input, output))
    
    return history, history

gradio.Interface(fn = chatbot,
             inputs = ["text",'state'],
             outputs = ["chatbot",'state'],  title = "THERA BUDDY: TEAM YES", description = "Ayyo, its yo boi thera. I know how wild this world could be, but you know I'm always here for you. Let's start with sharing some stories, what was your last happy moment?").launch(share = True, debug = True)

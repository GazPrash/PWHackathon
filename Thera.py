import openai
import gradio 

openai.api_key = "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"

messages = [{"role": "system", "content": "You are sassy youngster"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": "Continue the conversation being 'thera' and asking a leading follow up question at the end to whatever the input is.      Alex: It really is a good day bruv, how you feeling today. Input: Not bad. The world seems crazy.  Alex:Ayyo, its yo boi thera. I know how wild this world could be, but you know I’m always here for you. Let’s start with sharing some stories, what was your last happy moment? Input: " + user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages 
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

    message = completions.choices[0].text
    return message.strip()

def chatbot(input, history=[]):
    output = CustomChatGPT(input)
    history.append((input, output))
    return history, history

gradio.Interface(fn = chatbot,
             inputs = ["text",'state'],
             outputs = ["chatbot",'state'],  title = "THERA BUDDY: TEAM YES", description = "Ayyo, its yo boi thera. I know how wild this world could be, but you know I'm always here for you. Let's start with sharing some stories, what was your last happy moment?").launch(share = True, debug = True)
 
#demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "THERA BUDDY: TEAM YES", description = "Ayyo, its yo boi thera. I know how wild this world could be, but you know I'm always here for you. Let's start with sharing some stories, what was your last happy moment?")

#demo.launch(share=True)

# while input != "quit()":
#     message = input()
#     messages.append({"role": "user", "content": message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": reply})
#     print("\n" + reply + "\n")

# def openai_chat(prompt):
#     completions = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         temperature=0.5,
#     )

#     message = completions.choices[0].text
#     return message.strip()

# def chatbot(input, history=[]):
#     output = openai_chat(input)
#     history.append((input, output))
#     return history, history

# gr.Interface(fn = chatbot,
#              inputs = ["text",'state'],
#              outputs = ["chatbot",'state']).launch(share = True, debug = True)

# demo.launch(share=True)
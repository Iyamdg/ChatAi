import openai
import gradio as gr

openai.api_key = ""
messages = []

def CustomChatGPT(user_input):
    if not messages:
        messages.append({"role": "system", "content": "You are a computer assistant"})
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Custom CSS for Morgan State University colors
css = """
body { background-color: #FFA500; } 
.textbox, button { background-color: #003366; color: white; }
"""

with gr.Blocks(css=css) as demo:
    gr.Markdown("# COSC AI Chatbot - Morgan State University")
    gr.Markdown("Interact with our AI assistant!")
    with gr.Row():
        input_text = gr.Textbox(label="Your Message", placeholder="Type your message here...")
        output_text = gr.Textbox(label="AI Response", interactive=False)
    gr.Button("Send").click(
        fn=CustomChatGPT,
        inputs=input_text,
        outputs=output_text
    )

demo.launch(share=True)

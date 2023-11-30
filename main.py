import openai
import gradio as gr
import csv
import sys

openai.api_key = "sk-QkKEJ0Xujvy9zm60UTmcT3BlbkFJZlZUTIBE5Vz5a50a9U"

csv_file_path = r"C:\Users\gmann\Downloads\data.csv"

def read_csv_data(file_path):
    data = {}
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_input = row['User Input'].strip().lower()
                assistant_reply = row['Assistant Reply'].strip()
                data[user_input] = assistant_reply
    except Exception as e:
        print(f"Error reading CSV file: {e}", file=sys.stderr)
    return data

data = read_csv_data(csv_file_path)

messages = []

def CustomChatGPT(user_input):
    user_input_lower = user_input.strip().lower()
    if user_input_lower in data:
        return data[user_input_lower]

    if not messages:
        messages.append({"role": "system", "content": "You are a computer assistant"})
    messages.append({"role": "user", "content": user_input})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
    except Exception as e:
        print(f"Error with OpenAI response: {e}", file=sys.stderr)
        return "An error occurred while generating a response."
    return ChatGPT_reply

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

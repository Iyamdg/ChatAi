## COSC AI Chatbot - Morgan State University
### Overview
The COSC AI Chatbot is a specialized chatbot designed to assist computer science students at Morgan State University. Utilizing OpenAI's GPT-3.5 model, this chatbot aims to provide quick, relevant, and interactive responses to a variety of queries related to computer science topics. Integrated into a user-friendly web interface with Gradio, the chatbot is easily accessible for students seeking assistance or information.

### Features
- OpenAI GPT-3.5 Integration: Leverages the advanced natural language processing capabilities of GPT-3.5.
- Interactive Web Interface: A simple and intuitive Gradio-based interface for user interactions.
- Custom Styling: Themed with Morgan State University's colors to provide a familiar and engaging user experience.
- Persistent Conversation: Maintains the context of the conversation within a session for coherent dialogue.

### Requirements
- Python 3.x
- Gradio
- OpenAI API Key

## Installation
Before running the chatbot, ensure you have Python installed on your system. Then, install the required packages using pip:

bash
pip install gradio openai

### Configuration
API Key: You need to obtain an API key from OpenAI. Replace the openai.api_key value in the script with your actual API key.

Custom Styling: The current CSS is themed for Morgan State University. You can modify the CSS in the script to customize the appearance.

### Usage
To run the chatbot, execute the provided Python script:
python chatbot_script.py

This will start a local web server and the Gradio interface will be accessible through your web browser.

## User Guide
Starting the Chat: Simply type your question or message in the input textbox and press the "Send" button.

Conversation Context: The chatbot remembers the context of the conversation within a session, so you can ask follow-up questions.

Ending the Session: Close the browser tab or stop the Python script to end the session.
### Customization
Model Customization: You can change the model used by modifying the model parameter in the openai.ChatCompletion.create() function.

UI Customization: Modify the CSS in the script to change the look and feel of the chatbot interface.
### Support
For issues, questions, or contributions, please submit an issue on the project repository (if available).





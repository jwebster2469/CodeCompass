import sys
import os

# Get the directory where the current file (main.py) is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of codecompasslib
project_root = os.path.dirname(os.path.dirname(current_dir))

# Add the parent directory of codecompasslib to the Python path
sys.path.insert(0, project_root)

"""
The entry point of application that brings everything together and runs the chatbot.
"""
from codecompasslib.chatbot.secrets_manager import load_openai_key, load_github_token, load_assistant_instructions
from codecompasslib.chatbot.chatbot_management import initialize_client, create_assistant, load_tools, retrieve_assistant, run_chatbot

# Load secrets
openAI_key = load_openai_key(file_path='./secrets/openAI_key')
github_token = load_github_token(file_path='./secrets/github_token')

# Initialize the OpenAI client
client = initialize_client(openAI_key)

# Create an assistant
"""
instructions = load_assistant_instructions(file_path='secrets/instructions')
new_assistant = create_assistant(
    client=client,
    name="CodeCompass",
    instructions=instructions,
    model="gpt-3.5-turbo-0125",
    tools=load_tools('chatbot/tools.json'))
"""

# Retrieve assistant
assistant = retrieve_assistant(client, 'asst_cibfhJsvFEKbAo7EmaS34oQD')

# Run the chatbot
run_chatbot(client, assistant=assistant)
import os
from datetime import datetime

# Define the path to the log file dynamically based on project directory
PROJECT_DIR = r"C:\Users\Admin\PycharmProjects\social_cue\little_compass"
LOG_FILE_PATH = os.path.join(PROJECT_DIR, "logs", "conversation_log.txt")  # Saves to 'logs' folder

def log_conversation(user_message, bot_reply, latest_user_message=False):
    # Ensure the directory for the log file exists
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

    # Open the log file and append the conversation with utf-8 encoding
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as file:
        # Add a timestamp for better tracking
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Timestamp: {timestamp}\n")

        # Mark the latest user message with a special marker (if applicable)
        if latest_user_message:
            file.write(f"User (LATEST): {user_message}\n")
        else:
            file.write(f"User: {user_message}\n")

        # Write the bot's response
        file.write(f"Bot: {bot_reply}\n\n")

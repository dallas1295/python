from google import genai
from google.genai import types
from dotenv import load_dotenv
from datetime import datetime
import signal
import json
import os
import sys

load_dotenv()

# Set API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.api_key = api_key
client = genai.Client()

active = True

chat_history = []


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n\nChat interrupted! Saving history...")
    save_chat_history()
    print("Goodbye!")
    sys.exit(0)


def save_chat_history():
    """Save chat history to JSON file"""
    if chat_history:
        with open("chat_log.json", "w") as f:
            json.dump(chat_history, f, indent=2)
        print(f"Chat saved to chat_log.json with {len(chat_history)} messages")


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

print("Chat is beginning")
print("Press Ctrl+C to exit chat and save history")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() in ["qq", "cc"]:
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_budget=0
            ),  # Disables thinking
        ),
    )

    chat_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_prompt": user_prompt,
        "response": response.text,
    }

    chat_history.append(chat_entry)
    print(f"AI: { response.text }\n")

# Save chat history on normal exit
save_chat_history()

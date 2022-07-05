from flask import Flask, request, render_template  # Подключить Фласк
from datetime import datetime
import json

app = Flask(__name__)

MESSAGES_FILENAME = "messages_file.json"  # Имя файла с сообщенями


def load_messages():
    with open(MESSAGES_FILENAME, 'r') as message_file:
        return json.load(message_file)["messages"]


all_messages = load_messages()


def save_messages():
    message_file = open(MESSAGES_FILENAME, "w")
    data = {
        "messages": all_messages
    }
    json.dump(data, message_file)


def add_message(sender, text):
    new_message = {
        "text": text,
        "sender": sender,
        "time": datetime.now().strftime("%H:%M"),  # "часы:минуты"
    }

    all_messages.append(new_message)
    save_messages()


def print_all():
    for msg in all_messages:
        print(f'[{msg["sender"]}]: {msg["text"]} / {msg["time"]}')


@app.route("/")
def main_page():
    return "Hello, welcome to SkillChatServer5000"


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@app.route("/send_message")
def send_message():
    text = request.args["text"]
    name = request.args["name"]
    add_message(name, text)
    return "ok"


@app.route("/chat")
def chat():
    return render_template("form.html")


app.run()

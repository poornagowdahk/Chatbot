#importing needed libraries.
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time
import plotly.express as px

app = Flask(__name__,template_folder='templates')
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
#train the chatter bot for english
trainer.train("chatterbot.corpus.english")
# Train based on english greetings corpus
# trainer.train("chatterbot.corpus.english.greetings")

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
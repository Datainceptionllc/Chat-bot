#!/usr/bin/env python
# coding: utf-8

# In[1]:


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# In[2]:


pip install chatterbot chatterbot_corpus


# In[3]:


pip install spacy


# In[4]:


pip install sqlalchemy


# In[5]:


pip install chatterbot2


# In[6]:


# Importing chatterbot
from chatterbot import ChatBot


# In[7]:


# Create object of ChatBot class
chatbot = ChatBot('DataBot')


# In[8]:


# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now, let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )


# In[9]:


response = chatbot.get_response("How are you?")
print(response)


# In[10]:


from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# In[11]:


#Flask initialisation
app = Flask(__name__)


# In[12]:


@app.route("/")
def index():
    render_template("index.html")


# In[13]:


@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = chatbot.get_response(msg)
    return response


# In[14]:


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:





![](/images/pulp_trav_sam)


Description: You've been web-scrapping and querying databases for data. Now you will be the data provider 🎉.

For that, you will create your own API. This API will be able to receive information, store it, or serve it when needed.

In this project, you will practice:

Flask (API creation)
SQL
NLTK (sentiment analysis)


## Project Goals

Main goal: Create an API that:

Serves information to clients (in response to their GET requests).
Receives data from your clients (via their POST requests) and saves it to your own database.
Remember, YOU (your API) are the server, and clients send GET or POST requests to you.

(L0🤔) Design the structure of your own database depending on the type of info you want to store.
(L1🧐) Write an API using flask to receive chat messages and store them in a database (mysql).
(L2🥳) Read and serve data from the chats database using different endpoints.
(L3🤭) Extract the emotional value of messages per user/chats and make it queryable through an endpoit.
(L4🔥) Do it real, use slack API to get messages and analyze the messages of our data-bootcamp channel.
https://api.slack.com/


## Example's - API Endpoints

# 1. Endpoints GET
(GET) /users Returns every user in the database.

(GET) /messages Returns every message sent in every chat.

(GET) /<chat_name>/<user> Returns every message sent in a given chat.

# 2. Endpoint POST
(POST) /chat/<chat_id> Creates a chat

(POST) /chat/<chat_id>/adduser Adds a user to a chat.

(POST) /chat/<chat_id>/message Adds a message from a user to a given chat.

# Links - API dev in python
[https://bottlepy.org/docs/dev/]
[https://www.getpostman.com/]

# Links - NLP & Text Sentiment Analysis
[https://www.nltk.org/]
[https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]
[https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk]
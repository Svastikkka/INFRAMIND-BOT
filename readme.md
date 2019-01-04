#bot_Project
## Bot with interactive UI using simple web socket server 
### Description of files

* Chatbot_train.py file trains the data available in the data folder. Once it is trained , the result will be stored as db.sqlite.
* server.py sends back message to the client.
* Chatbot.py uses this db.sqlite to generate responses for user queries.

### How to run
* Once you downloaded this project , Make sure you install the python packages mentioned in requirement.txt.
* Go to Bot_Project directory and run python server.py.
* Above step will open the server. Now right click the index.html page and open with brower. You will be able to see the chat window where you can start the conversation and test.

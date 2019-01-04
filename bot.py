from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def get_response(usrText):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
	
	
	
	
    bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip()!= 'News':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)

        if usrText.strip()== 'News':
            return('<input type="text" placeholder="Search news" class="aa-input" style="width:100%; background:transparent "  style="width:50%;"> <input type="submit" class="aa-button" Style="width:100%;background-color: #ff4081;color: white;" value="submit">')
            break

        

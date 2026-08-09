import uuid
# CREATE A DEFAULT CHAT 
def create_new_chat(conversations : dict) -> str :
    chat_id = str(uuid.uuid4())

    conversations[chat_id] = {
        "title" : "New Chat" ,
        "messages" : []    # list of dictionaries 
    }

    return chat_id


def add_message(conversation : dict , chat_id : str , role : str , content: str) -> None : 
    conversation[chat_id]["messages"].append(
        {
            "role" : role ,
            "content" : content 
        }
    )

def update_chat_title(conversations: dict, chat_id :  str, new_title: str) -> None:
    conversations[chat_id]["title"] = new_title   
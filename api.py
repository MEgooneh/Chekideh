# CONFIG YOUR API HERE : 
RATE_LIMIT = 20 # sleeping time for openai per minute limitation
TOKEN_LIMIT = 0 # token limit per message 0=inf
MODEL = 'gpt-3.5-turbo'

import openai, os, time

# Getting OpenAI API key from the evnironmental variables

openai.api_key =  os.getenv("OPENAI_API_KEY")

# make content in openai required format
def create_message(role , content) : 
    return {"role" : role , "content" : content}



def send_message(message , token_limit=TOKEN_LIMIT , time_limit_rate=RATE_LIMIT) : 
    """
    Sending the request to api
    """    
    
    context = [create_message("user" , message)]

    # connecting to Openai
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=context,
    )
    # just for debugging in terminal
    print(f"""
          #######################
          {message}
          #######################
          -----------------------------
          {response.choices[0].message["content"]}
    """)
    time.sleep(time_limit_rate)
    # returning the response as a string
    return response.choices[0].message["content"]

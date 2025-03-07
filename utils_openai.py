import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

def retorna_resposta_modelo(mensagens, 
                            modelo = 'gpt-4o-mini', 
                            stream=False):
    response=client.chat.completions.create(
        messages=mensagens,
        model=modelo,
        temperature=0,
        stream=stream
    )
    return response
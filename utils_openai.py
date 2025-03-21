import openai

import requests
from PIL import Image
import time
import os

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

def retorna_imagem(prompt,
                   modelo='dall-e-3'
                   ):
    resposta_imagem=client.images.generate(model=modelo,
                                prompt=prompt,
                                size='1024x1024',
                                quality = 'standard',
                                style = 'natural',
                                n=1
                            )
    
    # Obtém a URL da imagem gerada
    if resposta_imagem and resposta_imagem.data and len(resposta_imagem.data) > 0:
        image_url = resposta_imagem.data[0].url
    else:
        return None  # Se a resposta não contém imagem, retorna None

 # Criar um nome único para a imagem (timestamp)
    pasta_imagens = "D:/Python/Projetos/MyChat/imagens/"
    nome_arquivo = os.path.join(pasta_imagens, f"AIgenerator_{int(time.time())}.jpg")

    # Baixa e salva a imagem com um nome único
    img_data = requests.get(image_url).content
    with open(nome_arquivo, 'wb') as f:
        f.write(img_data)

    return nome_arquivo  # Retorna o caminho local da imagem salva

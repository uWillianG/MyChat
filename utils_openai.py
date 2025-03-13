import openai
import requests
from PIL import Image

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
                   nome_arquivo,
                   modelo='dall-e-3'
                   ):
    resposta_imagem=client.images.generate(model=modelo,
                                prompt=prompt,
                                #'Você é um gerador de imagens, \
                                #realize a geração conforme a solicitação do usuário: {solicitacao_imagem}',
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

    # Baixa e salva a imagem
    img_data = requests.get(image_url).content
    with open(nome_arquivo, 'wb') as f:
        f.write(img_data)

    return image_url  # Retorna a URL correta da imagem gerada


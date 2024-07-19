import os

import openai


def get_car_ai_bio(model, brand, year):
    prompt = f'''
    Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres.
    Fale características específicas desse modelo de carro.
    '''
    openai.api_key = os.getenv('OPENAI_API_KEY')

    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # ou o modelo adequado
            messages=[
                {"role": "system", "content": "Você é um assistente de vendas de carros."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return("Descrição indisponível.")

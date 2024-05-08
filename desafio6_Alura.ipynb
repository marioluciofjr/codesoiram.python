"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
import google.generativeai as genai

genai.configure(api_key="SUA_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
  path = Path(pathname)
  hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
  try:
    existing_file = genai.get_file(name=hash_id)
    return [existing_file]
  except:
    pass
  uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
  return [uploaded_files[-1]]

prompt_parts = [
  "input: ",
  *upload_if_needed("COPIE E COLE O NOME E A EXTENSÃO DA IMAGEM QUE FEZ UPLOAD NO GOOGLE COLAB. Exemplo: "Teste.png""),
  "input 2: Escolha uma métrica da imagem e explique com um exemplo prático",
  "output: Métrica: Engajamento Total\nExemplo: um post de um perfil pessoal no LinkedIn teve 150 reações, 45 comentários e 15 compartilhamentos. Isso deu um Engajamento Total de 210.",
  "input: ",
  *upload_if_needed("COPIE E COLE O NOME E A EXTENSÃO DA IMAGEM QUE FEZ UPLOAD NO GOOGLE COLAB. Exemplo: "Teste.png""),
  "input 2: Escolha uma métrica da imagem e explique detalhadamente com um exemplo prático",
  "output: Métrica: NPS (Net Promoter Score)\nExemplo: Imagine uma farmácia que deseja medir o NPS através de pesquisas de satisfação online após a compra do cliente. A pesquisa contém apenas uma pergunta principal:\n\nEm uma escala de 0 a 10, qual a probabilidade de você recomendar nossa farmácia para amigos e familiares?\n\nRespostas dos clientes:\n\n10 Promotores (20%): clientes que respondem com 9 ou 10 e são considerados promotores da farmácia. Eles provavelmente comprarão novamente e recomendarão a outros.\n7-8 Passivos (45%): clientes neutros que respondem com 7 ou 8. Eles podem ou não comprar novamente no futuro, mas não são propensos a recomendar ativamente a farmácia.\n0-6 Detratores (35%): clientes insatisfeitos que respondem com 6 ou menos. Eles provavelmente não comprarão novamente e podem espalhar comentários negativos sobre a farmácia.\nCálculo do NPS:\n\nPorcentagem de Promotores: 20%\nPorcentagem de Detratores: 35%\nSubtraia a porcentagem de Detratores da porcentagem de Promotores: 20% - 35% = -15%\nNPS da farmácia: -15%\n\nInterpretação:\n\nUm NPS de -15% indica que a farmácia tem mais detratores do que promotores. Isso significa que a maioria dos clientes que responderam à pesquisa não recomendariam a farmácia para outras pessoas.",
  "input: ",
  *upload_if_needed("COPIE E COLE O NOME E A EXTENSÃO DA IMAGEM QUE FEZ UPLOAD NO GOOGLE COLAB. Exemplo: "Teste.png""),
  "input 2: Escolha uma métrica da imagem e explique detalhadamente com um exemplo prático",
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)
for uploaded_file in uploaded_files:
  genai.delete_file(name=uploaded_file.name)

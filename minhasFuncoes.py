def api(secret: str):
  from google.colab import userdata
  import os

  api_key = userdata.get(secret)
  os.environ["GOOGLE_API_KEY"] = api_key

  print("API configurada")

def energy():
  # Importando os pacotes necessários
  from ecologits import EcoLogits
  from google import genai
  
  client = genai.Client(api_key=api_key)
  
  # Iniciando o Ecologits
  EcoLogits.init(providers=["google_genai"])
  
  # Função do cálculo de consumo de energia e pegada de carbono
  
  def consumo_ai(prompt: str, model_name: str):
    response = client.models.generate_content(
    model=model_name,
    contents=f"{prompt}"
  )
  
    impacts = response.impacts
  
    resultado = (
      f"### Resumo de Impacto para {model_name}\n\n"
      f"ENERGIA:\n"
      f"  - Mínimo: {impacts.energy.value.min:.2f} {impacts.energy.unit}\n"
      f"  - Máximo: {impacts.energy.value.max:.2f} {impacts.energy.unit}\n\n"
      f"GWP (PEGADA DE CARBONO):\n"
      f"  - Mínimo: {impacts.gwp.value.min:.2f} {impacts.gwp.unit}\n"
      f"  - Máximo: {impacts.gwp.value.max:.2f} {impacts.gwp.unit}\n"
  )
    print(resultado)

  modelo_um = "gemini-2.5-flash"
  modelo_dois = "gemini-2.5-pro"
  
  prompt = input("Coloque aqui o seu prompt: ")
  
  consumo_ai(prompt, modelo_um)
  consumo_ai(prompt, modelo_dois)

def corrigir_valor_inflacao():
  import pandas as pd
  import requests as rq

  # Fiz uma requisição de dados no site do Ipeadata para ler o HTML
  pegarDados = rq.get("http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=36482&module=M")
  dados = pd.read_html(pegarDados.text)
  ipca = dados[2]

  # Filtrei os dados para o início do Plano Real
  ipca = ipca.loc[181:ipca.index[-1]]

  # Reordenei o índice
  ipca = ipca.set_index(ipca.index - 181)

  # A coluna 0 se chamará 'Mês' e coluna 1 se chamará 'Índice'
  ipca.rename(columns={0: 'Mês', 1: 'Índice'}, inplace=True)

  try:
    # Informação do ano inicial e do mês inicial para pegar o valor do índice respectivo
    ano_inicial = input("Insira o ano inicial entre 1995 e 2025: ")
    mês_inicial = input("Insira o mês inicial (Coloque o zero na frente dos meses anteriores a outubro): ") # Coloque o zero na frente de janeiro a setembro

    data_inicial = str(ano_inicial+"."+mês_inicial)
    data_inicial

    indice_inicial = ipca.loc[ipca.index == ipca.index[ipca.Mês == data_inicial].values[0]-1, 'Índice'].values[0]
    indice_inicial = float(indice_inicial.replace('.', '').replace(',','.'))
    indice_inicial

    # Informação do ano final e do mês final para pegar o valor do índice respectivo
    ano_final = input("Insira o ano final entre 1995 e 2025: ")
    mês_final = input("Insira o mês final (Coloque o zero na frente dos meses anteriores a outubro): ") # Coloque o zero na frente de janeiro a setembro
  
    data_final = str(ano_final+"."+mês_final)
    data_final
  
    indice_final = ipca.loc[ipca.index == ipca.index[ipca.Mês == data_final].values[0], 'Índice'].values[0]
    indice_final = float(indice_final.replace('.', '').replace(',','.'))
    indice_final
  
    # Valor a ser corrigido pela Inflação
  
    valor = int(input("Insira o valor a ser corrigido: "))
  
    # Cálculo da Correção
  
    calc = round(float(valor * (indice_final/indice_inicial)),2)
    print("O valor corrigido pela inflação no período é de R$ "+ str(calc))

  except IndexError:
    print("O índice não existe na lista, tente novamente")

def media_ponderada():
  # importe as bibliotecas pandas e numpy
  import pandas as pd
  import numpy as np
  
  # gere uma lista vazia para colocar as notas
  lista_de_notas = [ ] 
  
  # estipule o total de notas que serão inseridas posteriormente
  notas_range = int(input("Total de Notas : ")) 
  
  # nessa estrutura de repetição você colocará nota por nota 
  for i in range(0, notas_range): 
      notas = float(input("Digite uma Nota: "))
      lista_de_notas.append(notas) 
  
  # gere uma lista vazia para colocar os pesos
  lista_de_pesos = [ ] 
  
  # um peso para cada nota
  pesos_range = notas_range 
  
  # nessa estrutura de repetição você colocará peso por peso  
  for i in range(0, pesos_range): 
      pesos = float(input("Digite um Peso: "))
      lista_de_pesos.append(pesos)
  
  # crie um dicionário com as notas e os pesos utilizando o pandas
  notas_pesos = pd.DataFrame.from_dict({"Notas": lista_de_notas,
                                        "Pesos": lista_de_pesos})
  
  # calcule a média ponderada utilizando o numpy
  media_ponderada = np.average(a= notas_pesos["Notas"], 
                               weights= notas_pesos["Pesos"])
  
  # mostre o resultado
  print("A Média Ponderada é: ", media_ponderada)

def qrcode(texto: str):
  # 1ª etapa: Instale a biblioteca "qrcode"
  # !pip install -qU qrcode
  
  # 2ª etapa: importe a biblioteca
  import qrcode
  
  # 3ª etapa: Escolha o que o seu qrcode vai direcionar. Neste exemplo, eu utilizei um site.
  imagem_qrcode = qrcode.make(texto)
  
  # 4ª etapa: Gere o arquivo de imagem. A extensão você pode mudar no lugar de ".png"
  imagem_qrcode.save("qrcode.png")

def tabuada_cardinal_ordinal():
  # Instale a biblioteca num2words
  # !pip install -qU num2words

  # Importe o pacote necessário
  from num2words import num2words

  # Insira qual a tabuada que você quer. Ou seja, se você inserir o número 2, por exemplo, isso quer dizer que deseja a tabuada do 2. 
  tabuada = int(input("Digite a tabuada: "))

  # Insira a quantidade a ser multiplicada pela tabuada definida no passo anterior.
  quantidade_max = int(input("Digite a quantidade máxima multiplicada: "))

  # espaço no código.
  print("\n")

  # máximo de multiplicações.
  range_max = tabuada * quantidade_max + 1

  # contagem das linhas.
  counter = 0

  # estrutura de repetição para formar a tabuada.
  for i in range(tabuada, range_max, tabuada):
      counter = counter + 1
      print(tabuada, "*", counter, "= ", i)
      num_ptbr = num2words(i, lang="pt-br")
      print(f"Resultado em Cardinal: {num_ptbr}")
      num_ptbr_ord = num2words(i, lang="pt-br", to="ordinal")
      print(f"Resultado em Ordinal: {num_ptbr_ord}\n")

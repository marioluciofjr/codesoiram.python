import streamlit as st
import os
import google.generativeai as genai
from google.colab import userdata
import pdfquery

def analisar_perfil(api_key, pdf_path):
    """
    Analisa um perfil do LinkedIn a partir de um arquivo PDF, utilizando o modelo Gemini.

    Args:
        api_key (str): A chave da API do Google Generative AI.
        pdf_path (str): O caminho para o arquivo PDF do perfil do LinkedIn.

    Returns:
        str: O texto com a análise do perfil do LinkedIn.
    """

    genai.configure(api_key=api_key)

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest",
        safety_settings=safety_settings,
        generation_config=generation_config,
        system_instruction="""Você vai atuar como uma pessoa especialista em análise de perfis do LinkedIn, 
        tendo como propósito ajudar as pessoas a se posicionarem melhor nessa rede social e serem notadas por pessoas recrutadoras de emprego.""",
    )

    # Extract text from PDF
    pdf = pdfquery.PDFQuery(pdf_path)
    pdf.load()
    pdf_content = pdf.pq("LTTextLineHorizontal").text()

    # Create the chat session
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Com base no arquivo, siga os seguintes passos: ",
                    pdf_content,
                    "1. Analise o documento e atribua uma nota de 0 a 10 com base no que as pessoas recrutadoras costumam observar em um perfil do LinkedIn.",
                    "2. Destaque 5 pontos positivos do meu perfil.",
                    "3. Sugira 5 pontos que devo melhorar.",
                    "4. Forneça uma lista de 5 tipos de vagas que fariam mais sentido para o meu perfil, a partir da análise que realizou no primeiro passo.",
                ],
            },
            {
                "role": "model",
                "parts": [
                    """## Análise do Perfil LinkedIn\n\n**1. Nota:** 6/10\n\n**Justificativa:** O perfil demonstra um bom histórico profissional, 
                    com destaque para a experiência em marketing de conteúdo e gestão de LinkedIn. Entretanto, algumas falhas na estrutura e 
                    na linguagem impedem que o perfil seja ainda mais atraente para recrutadores.\n\n**2. Pontos Positivos:**\n\n* **Experiência Relevante:** 
                    Demonstra um histórico profissional diversificado com foco em áreas como marketing de conteúdo, gestão de LinkedIn, planilhas e vendas.\n* 
                    **Especialização em Marketing de Conteúdo:** O destaque para \"Prazo Certo®\" como uma \"eugência\" que combina marketing de conteúdo, design, 
                    ciência de dados e gestão do tempo demonstra um diferencial interessante.\n* **Portfólio Online:** A inclusão de links para o site, GitHub e LinkedIn  
                    permite que recrutadores acessem exemplos do seu trabalho.\n* **Foco em Resultados:** Quantifica resultados alcançados em cada experiência profissional, 
                    como o número de empresas atendidas, conteúdos publicados e metas batidas.\n* **Boa Apresentação:** O perfil é organizado e apresenta informações relevantes 
                    de forma clara e concisa.\n\n**3. Pontos a Melhorar:**\n\n* **Foto de Perfil:** A foto atual não transmite profissionalismo e impacto. Uma foto profissional e 
                    de alta qualidade é fundamental para causar boa primeira impressão.\n* **Resumo:** O resumo precisa ser mais conciso e focado em seus principais diferenciais. 
                    Explore mais os resultados e impactos que você gerou e use palavras-chave relevantes para a área.\n* **Linguagem:** Utilize uma linguagem mais profissional e 
                    evite expressões informais como \"eugência\" e \"Pode chamar\".\n* **Habilidades:** Incluir mais habilidades relevantes para o mercado, com foco em áreas como SEO, 
                    marketing digital, gestão de redes sociais, análise de dados e  ferramentas de design. \n* **Recomendações:** Buscar recomendações de clientes e ex-colegas para 
                    fortalecer seu perfil e adicionar credibilidade.\n\n**4. Sugestões de Vagas:**\n\n* **Especialista em Marketing de Conteúdo:** Criar conteúdo para blogs, websites, 
                    mídias sociais e outras plataformas digitais.\n* **Gestor de Redes Sociais:** Criar e implementar estratégias de marketing digital para redes sociais, 
                    com foco em LinkedIn.\n* **Analista de Marketing Digital:** Analisar dados, desenvolver campanhas e estratégias de marketing digital, incluindo conteúdo, 
                    SEO, e publicidade online.\n* **Freelancer de Marketing e Comunicação:** Oferece serviços de redação, edição, criação de conteúdo e gestão de redes sociais 
                    para diferentes empresas e clientes.\n* **Consultor de LinkedIn:** Assessorar empresas e profissionais na criação de perfis de LinkedIn eficazes, 
                    desenvolvimento de estratégias de networking e geração de leads.\n\n**Dicas Adicionais:**\n\n* **Atualize o perfil regularmente:** 
                    Inclua novas habilidades, projetos e experiências relevantes.\n* **Participe de grupos do LinkedIn:** 
                    Conecte-se com outros profissionais da sua área, participe de discussões e compartilhe conteúdo.\n* **Interaja com outros perfis:** 
                    Curta, comente e compartilhe conteúdo relevante.\n* **Use palavras-chave:** Inclua palavras-chave que descrevam suas habilidades, 
                    áreas de atuação e objetivos profissionais.\n\nCom estas dicas e a análise do seu perfil, você estará melhor preparado para destacar-se no 
                    LinkedIn e alcançar seus objetivos profissionais. \n""",
                ],
            },
        ]
    )

    response = chat_session.send_message("Execute o passo a passo a partir do documento compartilhado")
    return response.text

# Streamlit web app
st.title("Analisador de Perfil do LinkedIn")

api_key = st.text_input("Insira sua chave da API do Google Generative AI", type="password")
pdf_file = st.file_uploader("Carregue seu arquivo PDF do LinkedIn", type=["pdf"])

if api_key and pdf_file:
    # Save the PDF file to disk
    pdf_path = "perfil.pdf"
    with open(pdf_path, "wb") as f:
        f.write(pdf_file.read())

    # Analyze the profile
    analysis = analisar_perfil(api_key, pdf_path)

    # Display the analysis
    st.markdown(analysis)
    st.success("Análise do perfil concluída!")

    # Remove the PDF file after analysis
    os.remove(pdf_path)

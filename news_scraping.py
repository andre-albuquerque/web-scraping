import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import mysql.connector
import os
import random

print('Iniciando scraping do site G1. Isto pode demorar um pouco...')

# opções do método Selenium | --headless não abre nagevador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

#variáveis de ambiente com os caminhos na plataforma heroku para o google chrome e google driver
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")    
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

#abrir o site g1.globo
driver.get("https://g1.globo.com/")

# botão 'veja mais' do site G1
element = driver.find_element_by_xpath("//*[@id='feed-placeholder']/div/div/div[3]/a")
# loop para dar scroll na página e clicar no botão 'veja mais'
for j in range (3):
    for i in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5) #Aguardando 5 segundos para ter todos os dados carregados
    element.click()
# obter o html do site com o BeautifulSoup
site_g1 = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
print('Buscando notícias e salvando em lista...')
# Busca todas as notícias na página principal
noticias = site_g1.find_all('div', attrs={'class': "feed-post-body"})
lista_noticias_g1 = []

# Loop para obter todos os elementos de cada notícia
for noticia in noticias:    
    dados_noticias = []

    titulo = noticia.find('div', attrs={'class': 'feed-post-body-title gui-color-primary gui-color-hover'})   
    img = noticia.find('img', attrs={'class':'bstn-fd-picture-image'})
    link = noticia.find('div', attrs={'class':'_b'}).find('a')
    resumo = noticia.find('div', attrs={'class':'feed-post-body-resumo'})
    tempo = noticia.find('span', attrs={'class':'feed-post-datetime'})
    fonte = "G1"
    dados_noticias.append(titulo.text) 

    if (resumo):
        dados_noticias.append(resumo.text)
    else:
        dados_noticias.append("")

    try:
        dados_noticias.append(tempo.text)
    except:
        dados_noticias.append("")
    dados_noticias.append(fonte)

    dados_noticias.append(link['href'])

    try:
        dados_noticias.append(img['src'])
    except: 
        dados_noticias.append("")

    lista_noticias_g1.append(dados_noticias)

# scraping do google news
print('Iniciando scraping do site Google News...')
# acessa o site do Google News
html = requests.get("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYQjBMVUpTR2dKQ1VpZ0FQAQ?hl=pt-BR&gl=BR&ceid=BR%3Apt-419")
# obtem o html do site
site_gnews = BeautifulSoup(html.content, "html.parser")
print('Buscando notícias e salvando em lista...')
# obtem todas as noticias do tipo 1 
noticias_1 = site_gnews.find_all('div', attrs={'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'})

lista_noticias_gnews = []
# Loop para obter todos os elementos de cada notícia
for noticia in noticias_1:
    dados_noticias_1 = []
    titulo = noticia.find('a', attrs={'class':'DY5T1d RZIKme'}).text
    subtitulo = ""
    tempo = noticia.time
    link = noticia.a['href']
    img = noticia.img
    fonte = noticia.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
    # condição para evitar notícias repetidas no banco de dados
    if fonte == 'G1':
        continue
    else:
        dados_noticias_1.append(titulo)    
        dados_noticias_1.append(subtitulo)
        try:
            dados_noticias_1.append(tempo.text)
        except:
            dados_noticias_1.append("")
        dados_noticias_1.append(fonte)
        if len(link) > 140:
            continue
        else:
            dados_noticias_1.append('https://news.google.com' + link[1:])
        dados_noticias_1.append(img['src'])

        lista_noticias_gnews.append(dados_noticias_1)
        
# obtem todas as notícias do tipo 2
noticias_2 = site_gnews.find_all('div', attrs={'class':'NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc'})
# Loop para obter todos os elementos de cada notícia
for noticia in noticias_2:
    dados_noticias_2 = []
    titulo = noticia.find('a', attrs={'class':'DY5T1d RZIKme'}).text
    subtitulo = ""
    tempo = noticia.time
    link = noticia.a['href']
    img = noticia.img
    fonte = noticia.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
    # condição para evitar notícias repetidas no banco de dados
    if fonte == 'G1':
        continue
    else:       
        dados_noticias_2.append(titulo)
        dados_noticias_2.append(subtitulo)    
        try:
            dados_noticias_2.append(tempo.text)
        except:
            dados_noticias_2.append("")
        dados_noticias_2.append(fonte)
        if len(link) > 140:
            continue
        else:
            dados_noticias_2.append('https://news.google.com' + link[1:])
        dados_noticias_2.append(img['src'])

        lista_noticias_gnews.append(dados_noticias_2)

# salvando no banco de dados
print('Importando listas para o banco de dados...')

#variáveis de ambiente com os dados para se conectar ao banco de dados MySQL no AWS
host = os.environ.get("host")
user= os.environ.get("user")
password = os.environ.get("password")
database = os.environ.get("database")

#Comandos para conectar e criar o database e a tabela no MySQL se não existir
mydb = mysql.connector.connect(
host=host,
user=user,
passwd=password,
database=database
)

mycursor = mydb.cursor()

# criar a tabela no banco de dados
tabela_news = """CREATE TABLE IF NOT EXISTS news (id INT PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(255), subtitulo VARCHAR(255), tempo VARCHAR(100), 
                fonte VARCHAR(255), link VARCHAR(1000), img VARCHAR(500))"""

# garantir que o auto incremento seja iniciado no número 1
tabela_news_2 = """SET @@auto_increment_increment=1"""

mycursor.execute(tabela_news)
mycursor.execute(tabela_news_2)

# apagando conteúdos anteriores nas tabelas para evitar noticias antigas ou repetidas
mycursor.execute("TRUNCATE TABLE news") 
# comando SQL para inserir os elementos das notícias nas tabelas
comando_sql_news = """INSERT INTO news (titulo, subtitulo, tempo, fonte, link, img)
                        VALUES (%s, %s, %s, %s, %s, %s)"""

dados_g1  = lista_noticias_g1       
dados_gnews = lista_noticias_gnews  

#junta as listas de noticias
dados_total = dados_g1 + dados_gnews

#embaralha a ordem para obter lista de notícias com fontes sortidas
dados_shuffle = random.sample(dados_total, len(dados_total))

#executa o comando para o banco de dados
mycursor.executemany(comando_sql_news, dados_shuffle)
mydb.commit()

# fechando conexão com banco de dados
mydb.close()

print('Processo finalizado!')

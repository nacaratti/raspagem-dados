import requests
import bs4


url = '***site que deseja fazer a busca***'

requisicao = requests.get(url)

pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")

lista_noticias = pagina.find_all("a", class_= "tipo da classe utilizada")

for noticia in lista_noticias:
    print(noticia.text)
    print(noticia.get("href"))
    print("---------------------------")

print(len(lista_noticias))
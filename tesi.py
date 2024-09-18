import requests
from bs4 import BeautifulSoup

# URL base
BASE_URL = "http://localhost/tesi"

# Iniciar uma sessão para manter os cookies entre as requisições
session = requests.Session()

# Fazer o login
login_data = {
    "username": "admin",
    "password": "12345"
}
response = session.post(BASE_URL + "/login.php", data=login_data)

# Se o login foi bem-sucedido, prosseguir para a página de boas-vindas
if "success" in response.text:
    response = session.get(BASE_URL + "/welcome.php")
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar todos os nomes que têm a cor vermelha associada
    rows = soup.find_all("tr")[1:]  # [1:] para pular o cabeçalho da tabela
    red_names = [row.find_all("td")[0].text for row in rows if "red" in row.find_all("td")[1].text]
    
    # Imprimir os nomes vermelhos
    for name in red_names:
        print(name)
else:
    print("Falha no login!")

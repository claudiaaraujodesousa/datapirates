import requests
from bs4 import BeautifulSoup
import re

# def get_brcep(UF):
#     # Getting data
#     session = requests.session()

#     payload = "UF="+UF+"&Localidade="

#     r = session.request("POST", "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm", payload)

#     content = r.text
    
#     print(content)
#     # Parsing
#     # soup = BeautifulSoup(content)
#     # #print(soup)
#     # items = soup.find_all('table')[0].find_all('td')

#     # # # Returning data
#     # print(items)

# cep = get_brcep("AM")


reqUrl = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/x-www-form-urlencoded" 
}

payload = "UF=AM&Localidade="

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)
from time import sleep
import requests 
from bs4 import BeautifulSoup
import re

async def get_brcep(UF):
    reqUrl = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

    headersList = {
     "Accept": "*/*",
     "User-Agent": "",
     "Content-Type": "application/x-www-form-urlencoded" 
    }

    payload = "UF="+UF+"&Localidade="

    response = await requests.request("POST", reqUrl, data=payload,  headers=headersList)

    print(response.text)

def main():
    get_brcep("AM")

from bs4 import BeautifulSoup
import requests
import re

def clean_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Retire les balises inutiles
    for script in soup(["script", "style"]):
        script.extract()
    
    # Récupère le texte brut
    text = soup.get_text()
    
    # Supprime les espaces en trop et nettoie le texte
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

url = "https://reveblanc.fr"
cleaned_text = clean_text_from_url(url)
print(cleaned_text)


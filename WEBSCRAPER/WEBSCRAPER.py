# Importar las bibliotecas necesarias.
from bs4 import BeautifulSoup
import requests

# Definir la URL del sitio web que deseas analizar.
url = 'https://www.ibm.com/security/artificial-intelligence' 

# Realizar una solicitud HTTP al sitio web y obtén el contenido de la página.
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("La solicitud HTTP fue exitosa.")
else:
    print("Error al realizar la solicitud HTTP. Código de estado:", response.status_code)

# Obtener el contenido de la página
content = response.content
print("Contenido de la página:", content)


# Crear un objeto BeautifulSoup y pasa el contenido de la página y el parser que deseas utilizar.
soup = BeautifulSoup(response.content, 'html.parser')

# Utilizar los métodos de BeautifulSoup para navegar y extraer los datos que se desean.
# Se obtienen todos los enlaces de la página. 
links = soup.find_all('a')
for link in links:
    
    # Imprimir el atributo 'href' de cada enlace. 
    print(link.get('href')) 

# Encontrar todos los elementos <a> en la página web y almacenarlos en la variable links. 
links = soup.find_all('a')

# Imprimir el número de enlaces encontrados utilizando una f-string. 
print(f"Se encontraron {len(links)} enlaces.")

# Iterar sobre la lista de enlaces y mostrar la URL de cada enlace. 
for link in links:
    print(link.get('href'))
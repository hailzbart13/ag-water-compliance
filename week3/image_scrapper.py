import urllib.request
from bs4 import BeautifulSoup
import ssl
import urllib.parse
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'https://www.gamesindustry.biz/are-video-games-really-more-expensive'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img')
for img in images:
    src = img.get('src')
    full_url = urllib.parse.urljoin(url, src)
    print(full_url)

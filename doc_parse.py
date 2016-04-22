from lxml.html import parse
import urllib.request

parsed = parse(urllib.request.urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
print(parsed)
doc = parsed.getroot()
print(doc)
links = doc.findall('.//a')
print(links[15:20])
lnk = links[28]
print(lnk.get('href'))
print(lnk.text_content())
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
print(urls[-10:])
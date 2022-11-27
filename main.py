import requests
from bs4 import BeautifulSoup as bs
import os
from PyPDF2 import PdfMerger
from PIL import Image


def create_directory():
    pass


def get_name():
    url = 'https://manga-terra.com/manga/hajime-no-ippo'
    response = requests.get(url)
    html = response.content
    soup = bs(html, 'html.parser')
    data = soup.find('div', class_='col-12 col-lg-6 py-3 col-chapter')
    data1 = data.find('h5')
    print(data1.getText()[1:14])
    return data1.getText()[1:14]


def manga_validation():
    url = 'https://manga-terra.com/manga/hajime-no-ippo'
    response = requests.get(url)
    html = response.content
    soup = bs(html, 'html.parser')
    link = soup.find('div', class_='col-12 col-lg-6 py-3 col-chapter')
    link1 = link.find('a')

    return link1


def downloader():
    page = 1
    while page <= 14:
        url = f"https://manga-terra.com/book/91555/{page}"
        response = requests.get(url)
        html = response.content
        soup = bs(html, 'html.parser')
        formats_on_page = soup.findAll("img")

        if page < 10:
            with open(fr"./Hajime no Ippo/0{page}.jpg", 'wb') as pag:
                  for e in formats_on_page:
                        print(e['src'])
                        down = requests.get(f"{e['src']}")
                        pag.write(down.content)
            page += 1
        else:
            with open(fr"./Hajime no Ippo/{page}.jpg", 'wb') as pag:
                  for e in formats_on_page:
                        print(e['src'])
                        down = requests.get(f"{e['src']}")
                        pag.write(down.content)
            page += 1

    transform_in_pdf()


def transform_in_pdf():
    files = os.listdir(r'.\Hajime no Ippo')

    for i in files:
        if i.split('.')[-1] == 'jpg':
            im = Image.open(fr'./Hajime no Ippo/{i}')
            im.save(fr'./Hajime no Ippo/{i[:-4]}' + ".pdf", resolution=100.0)
            os.remove(fr'./Hajime no Ippo/{i}')
    merge_pdf()


def merge_pdf():
    merger = PdfMerger()
    for pdf in os.listdir(r'.\Hajime no Ippo'):
        if pdf.split('.')[-1] == 'pdf':
            merger.append(fr'.\Hajime no Ippo\{pdf}')
    name = get_name()
    merger.write(fr".\Hajime no Ippo\{name}.pdf")
    merger.close()
    for pdf in os.listdir(r'.\Hajime no Ippo'):
        if pdf.split('.')[-1] == 'pdf' and pdf != f"{name}.pdf":
            os.remove(fr'./Hajime no Ippo/{pdf}')


downloader()

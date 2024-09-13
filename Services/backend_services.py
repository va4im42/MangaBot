import requests
from Class import Manga

url = "https://localhost:7034"

headers = {
    'User-Agent': 'Mozilla/5.0',
    # 'Host': 'localhost',
    'accept': 'text/plain'
}

def mangalist(MangaName) -> list[Manga]:

    params = {
        'name': MangaName  
    }

    response = requests.get(url+"/api/Manga/Search", params=params, headers=headers, verify=False)
    manga_list = list()
    print(response.json())

    if response.status_code == 200:
        # Вывод данных ответа в формате JSON
        data = response.json()

        # mangas = data.get([])
        
        for i in data:
            manga = Manga.Manga(i.get('names'), "https://2.readmanga.ru"+i.get('link'), i.get('thumbnail'))    
            #manga_name = manga.get('names')
            #manga_link = url+manga.get('link')
            #manga_pic = manga.get('thumbnail')
            print(f"Name: {manga.name}, Сылка: {manga.link}, Pic: {manga.img}")
            manga_list.append(manga)
        return(manga_list)
    else:
        print((f"Ошибка: {response.status_code}"))
        manga_list.append(Manga.Manga("Ошибка", response.status_code, ":("))
        return(manga_list)


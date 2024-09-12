import requests
from Class import Manga

url = "https://localhost:7034"

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Host': 'https://localhost:7034'
}

def mangalist(MangaName):

    params = {
        'name': MangaName  
    }

    response = requests.get(url+"/api/Manga/Search", params=params, headers=headers, verify=False)

    if response.status_code == 200:
        # Вывод данных ответа в формате JSON
        data = response.json()

        mangas = data.get([])
        manga_list =[]

        for i in mangas:
            manga = Manga.Manga(i.get('names'), url+i.get('link'), i.get('thumbnail'))    
            #manga_name = manga.get('names')
            #manga_link = url+manga.get('link')
            #manga_pic = manga.get('thumbnail')
            print(f"Name: {manga.name}, Сылка: {manga.link}, Pic: {manga.img}")
            manga_list.append(manga)
            

        return(manga_list)
    else:
        print((f"Ошибка: {response.status_code}"))
        return(f"Ошибка: {response.status_code}")


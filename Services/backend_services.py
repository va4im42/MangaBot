import requests
from Class import Manga

url = "https://2.readmanga.ru"

headers = {
    'User-Agent': 'Mozilla/5.0',  # Возможно, сервер требует идентификацию клиента
    # Если требуется авторизация, можно добавить ее здесь
    # 'Authorization': 'Bearer your_token_here'
}

def mangalist(MangaName):

    params = {
        'query': MangaName,
        'types': 'CREATION',
        'types': 'FEDERATION_MANGA_SUBJECT'
    }

    response = requests.get(url+"/search/suggestion", params=params, headers=headers)

    if response.status_code == 200:
        # Вывод данных ответа в формате JSON
        data = response.json()

        mangas = data.get('suggestions', [])
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


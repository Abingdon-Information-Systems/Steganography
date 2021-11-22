from imgurpython import ImgurClient
import random

client_id = 'f67bde9410b59a1'
client_secret = '788d83f23980e9f1aa7ae37fc9103f28baa5eb07'

client = ImgurClient(client_id, client_secret)


def getRandomImage():
    while True:
        page = random.randint(0, 10)
        items = client.memes_subgallery(sort='viral', page=page, window='month')
        imagelist = []
        print(len(items))
        for (i, item) in enumerate(items):
            link = item.link
            if link[-4:] == ".png":
                print(i)
                imagelist.append(link)
                yield link

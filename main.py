import requests
from yadisk import Yadisk
import urllib


class VK:
    def __init__(self, ttoken, user_id, version='5.131'):
        self.token = ttoken
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def get_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'access_token': ttoken,
            'v': 5.131,
            'album_id': 'profile',
            'extended': 1
        }
        resp = requests.get(url, params=params).json()
        for idx, alb in enumerate(resp['response']['items']):
            for img in alb['sizes']:
                if img['type'] == 'w':
                    urllib.request.urlretrieve(img['url'], f'image.jpg')
                    ya.upload_file_to_disk(f'test/image_{idx}.jpg', f'image.jpg')


if __name__ == '__main__':
    ya = Yadisk(token="AQAAAABZ1l9vAADLW2o_p71eAERDs7EdDJ6e3iI")
    ttoken = 'vk1.a.aNqIqjDwTwy-2o0QQeSVrgWbCUzvLQjqsyZynaLBorSSaVUG84JE-riCqiVR-r_BsDz8uUBTnwNF8VQnMCssTDdprhNqakzOqAkPE2fku-sW2YECTStco-YxD-j008-1cwW7snKJzpiBR8Q8yK3sIJkYBA9KXbbhtvO8xf21Cx99fuwwHCXQjzjnFybq86dX'
    user_id = '741761650'
    vk = VK(ttoken, user_id)
    vk.get_photos()

from pprint import pprint
from rocketchat.api import RocketChatAPI
from rocketchat_API.rocketchat import RocketChat

api = RocketChatAPI(settings={'username': 'Yongchin', 'password': 'yongchin1995',
                              'domain': 'https://chat.rgwit.be'})



api.delete_public_room('vector-test-api')

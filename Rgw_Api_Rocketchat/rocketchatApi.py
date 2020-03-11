from pprint import pprint
from rocketchat.api import RocketChatAPI
from rocketchat_API.rocketchat import RocketChat

api = RocketChatAPI(settings={'username': 'Kevin', 'password': 'Rgwit,912',
                              'domain': 'https://chat.rgwit.be'})
#get information
api.get_my_info()

#send message to room
api.send_message('test', 'GENERAL')

#send dm
api.send_message('test', '@yongchin')

#
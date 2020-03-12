from rocketchat.calls.chat.send_message import SendMessage
from rocketchat.calls.channels.get_public_rooms import GetPublicRooms
from rocketchat.calls.groups.get_private_rooms import GetPrivateRooms
from rocketchat.calls.channels.get_room_info import GetRoomInfo
from rocketchat.calls.groups.get_private_room_info import GetPrivateRoomInfo
from rocketchat.calls.groups.get_room_id import GetRoomId
from rocketchat.calls.groups.set_room_topic import SetRoomTopic
from rocketchat.calls.channels.get_history import GetRoomHistory
from rocketchat.calls.groups.get_private_room_history import GetPrivateRoomHistory
from rocketchat.calls.channels.create_public_room import CreatePublicRoom
from rocketchat.calls.channels.delete_public_room import DeletePublicRoom
from rocketchat.calls.auth.get_me import GetMe
from rocketchat.calls.users.get_users import GetUsers
from rocketchat.calls.users.get_user_info import GetUserInfo
from rocketchat.calls.users.create_user import CreateUser
from rocketchat.calls.users.delete_user import DeleteUser
from rocketchat.calls.groups.upload_file import UploadFile
from rocketchat.calls.im.create_room import CreateImRoom
from rocketchat.calls.im.open_room import OpenImRoom
from rocketchat.calls.im.close_room import CloseImRoom
from rocketchat.calls.im.get_rooms import GetImRooms
from rocketchat.calls.im.get_history import GetImRoomHistory
from datetime import datetime
import anki_vector
from pprint import pprint
from rocketchat.api import RocketChatAPI
from rocketchat_API.rocketchat import RocketChat

class RocketChatAPI(object):
    settings = None

    def get_private_rooms(self, **kwargs):
        """
        Get a listing of all private rooms with their names and IDs
        """
        return GetPrivateRooms(settings=self.settings, **kwargs).call(**kwargs)

    def get_my_info(self, **kwargs):
        return GetMe(settings=self.settings, **kwargs).call(**kwargs)

    api = RocketChatAPI(settings={'username': 'Kevin', 'password': 'Rgwit,912',
                              'domain': 'https://chat.rgwit.be'})

    api.get_my_info()

# anki-vector-rgw

in the Scripts folder there are scripts that can be found for different use cases. Like for example a pong game, a script for getting the camera on Vector's face and a script that will make vector fetch his cube.

## Table of contents
* [Team](#Team)
* [Step installation and connexion](#Step_connexion_and_setting)
  * [Mac OS / OSX](#Install_macOS)
  * [Source](#Source)
* [Script audio](#Script_audio)


## Team

- [Yong Chin Zhuang](https://github.com/yongchin95)
- [Kevin Schrader](https://github.com/kevinschrader)

## Step_connexion_and_setting

### Install_macOS 
Install Homebrew: brew update   
Install the latest version on Python 3: brew install python 3   
Install SDK: python3 -m pip install --user anki_vector   
Upgrade SDK: python3 -m pip install --user --upgrade anki_vector   
Configure anki vector: python3 -m anki_vector.configure
### Source
[installation](https://developer.anki.com/vector/docs/install-macos.html)   
[getting started](https://developer.anki.com/vector/docs/getstarted.html)

### Script_audio

the format audio file must be dowlaoad in   
*.wav   
*16 bit  
*8000Hz   
*1 channel    

## Rocket.chat API

*pip install rocket-python  

####

code: from rocketchat.api import RocketChatAPI   
      api = RocketChatAPI(settings={'username': '...', 'password': '...',
                              'domain': 'https://...'})

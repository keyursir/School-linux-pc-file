from kivy.uix.accordion import ListProperty
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.textinput import Texture
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from firebase import firebase
firebase = firebase.FirebaseApplication("https://abhay-121-default-rtdb.firebaseio.com/", None)
import socket

import sys
from kivy.core.video import Video
album_url = "https://www.jiosaavn.com/album/brahmastra-original-motion-picture-soundtrack/xq4v9ZFC9iA_"


from kivymd.uix.dialog import MDDialog

from PIL import Image
import time
from kivy.uix.image import Image, AsyncImage, CoreImage
from mutagen.id3 import ID3
from kivymd.toast import toast
import random

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatIconButton, MDIconButton, MDFlatButton, MDFloatingActionButton, MDTextButton
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager,FadeTransition
from kivy.clock import Clock
from kivy.uix.label import Label
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.taptargetview import MDTapTargetView
import cv2
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.video import Video
from kivy.uix.behaviors import ButtonBehavior
from kivy.factory import Factory
from kivy.uix.button import Button
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.behaviors import TouchBehavior
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.filemanager import MDFileManager
from kivy.core.text import LabelBase
from kivymd.uix.list import IRightBodyTouch,MDList, ThreeLineAvatarIconListItem,ThreeLineAvatarListItem,ImageLeftWidget,ThreeLineIconListItem,OneLineListItem,OneLineAvatarIconListItem,TwoLineAvatarIconListItem,IconLeftWidget, TwoLineAvatarListItem, OneLineAvatarListItem
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.spinner import MDSpinner
from kivy.network.urlrequest import UrlRequest
import os
from PIL import Image as PILimage
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
import time
from kivymd.uix.bottomsheet import MDListBottomSheet
#from kvdroid.tools.audio import Player
from kivymd.uix.pickers import MDTimePicker
from kivy.graphics.texture import Texture
from kivymd.uix.label import MDIcon
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
#from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
#from kivy.uix.screenmanager.WipeTransition import WipeTransition
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.fitimage import FitImage
import requests
from kivy.loader import Loader
import sys
import base64
import json
import os
import io
from kivymd.uix.tab import MDTabsBase
from kivy.utils import platform
from contextlib import closing
from threading import Thread

    


#__call=search.getPlaylistResults

album_details_base_url = "https://www.jiosaavn.com/api.php?__call=content.getAlbumDetails&_format=json&cc=in&_marker=0%3F_marker=0&albumid="

lyrics_base_url = "https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&ctx=web6dot0&api_version=4&_format=json&_marker=0%3F_marker%3D0&lyrics_id="
    
search_base_url = "https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&cc=in&includeMetaTags=1&query="

homedata = "www.jiosaavn.com/api.php?_format=json&_marker=0&api_version=4&ctx=web6dot0__call=webapi.getLaunchData"

song_details_base_url = "https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids="
playlist_details_base_url = "https://www.jiosaavn.com/api.php?__call=webapi.get&token={}&type=playlist&p=1&n=20&includeMetaTags=0&ctx=web6dot0&api_version=4&_format=json&_marker=0"



album_ids = {
  "Sita-Raman":"iR05Wcpk,G0_",
  }

album_image = {
  "iR05Wcpk,G0_":"https://c.saavncdn.com/863/Sita-Ramam-Hindi-Original-Motion-Picture-Soundtrack-Hindi-2022-20220905152715-500x500.jpg"
  }

playlist_ids = {
  "Weekly Top JioTunes" : "znKA,YavndBuOxiEGmm6lQ__",
  "Trending Today":"EzSEwcZfOoB5b0dfvYvasw__",
  "Hindi - Weekly Top Songs" : "8MT-LQlP35c_",
  "Hindi - Top Jio Tunes":"AZNZNH1EwNjfemJ68FuXsA__",
  "English Top Songs" : "LdbVc1Z5i9E_",
  "English - Top JioTunes" : "xXiMISqMjsrfemJ68FuXsA__",
  "Punjabi - Weekly Top Songs":"W6DUe-fP3X8_",
  "Trending":"I3kvhipIy73uCJW60TJk1Q__",
  "Punjabi - Top JioTunes":"mzDerWPsSwiO0eMLZZxqsA__",
  "Latest Punjabi Hits":"T,w3Z-u7t6A_",
  "VYRL Top 20":"zvYYPLOvojJFo9wdEAzFBA__",
  "Haryanvi - Weekly Top Songs" :"ar5lExlDmbwwkg5tVhI3fw__",
  "Haryanvi - Top JioTunes":"xgyTegenCljc1EngHtQQ2g__",
  }
  
 

playlist_images = {
    "8MT-LQlP35c_" : "http://c.saavncdn.com/editorial/wt15-49_20210101173527.jpg?bch=1609524330",
    "znKA,YavndBuOxiEGmm6lQ__" : "https://pli.saavncdn.com/44/90/101334490.jpg?bch=1486377541",
    "EzSEwcZfOoB5b0dfvYvasw__":"https://c.saavncdn.com/editorial/RomanticHits2022Hindi_20221207061952.jpg?bch=1670396010",
    "AZNZNH1EwNjfemJ68FuXsA__" : "https://c.saavncdn.com/editorial/TopJioTunesHindi_20200721161337.jpg?bch=1610064389",
    "I3kvhipIy73uCJW60TJk1Q__":"https://c.saavncdn.com/editorial/logo/charts_TrendingToday_183360_20220107111716.jpg?bch=1502438867",
    "LdbVc1Z5i9E_" : "http://c.saavncdn.com/editorial/wt15-7386899_20210101134203.jpg?bch=1609510327",
    "xXiMISqMjsrfemJ68FuXsA__" : "https://c.saavncdn.com/editorial/TopJioTunesEnglish_20181220070458.jpg",
    "W6DUe-fP3X8_" : "https://c.saavncdn.com/editorial/wt15-2676373_20201225140344.jpg?bch=1608935628",
    "mzDerWPsSwiO0eMLZZxqsA__" : "https://c.saavncdn.com/editorial/TopJioTunesPunjabi_20181220084041.jpg?bch=1610064899",
    "T,w3Z-u7t6A_" : "https://c.saavncdn.com/editorial/LatestPunjabiHits_20201128085206.jpg?bch=1606555342",
    "zvYYPLOvojJFo9wdEAzFBA__" : "https://c.saavncdn.com/editorial/VYRLTop20_20200929074344.jpg?bch=1605790299",
    "ar5lExlDmbwwkg5tVhI3fw__" : "https://c.saavncdn.com/editorial/wt15-157145953_20210101135104.jpg?bch=1609539668",
    "xgyTegenCljc1EngHtQQ2g__" : "https://c.saavncdn.com/editorial/TopJioTunesHaryanvi_20181220085019.jpg?bch=1610064088",
}


class abhay(TwoLineAvatarIconListItem):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class HoverButton(Button, HoverBehavior):
    background = ListProperty((71/255, 104/255, 237/255, 1))
    def on_enter(self):
        self.background = (251/255, 104/255, 23/255, 1)
        Animation(size_hint= (.6, .1), d=.3).start(self)

    def on_leave(self):
        self.background = (71/255, 104/255, 237/255, 1)
        Animation(size_hint= (.5, .1), d=.3).start(self)

class Videos(Video):
    pass

class MainApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    last_screen = []
    exit = "0"
    
    
    #win_size = min(Window.size)
    
    def build(self):
        screen = Builder.load_file("login.kv")
        #self.capture = cv2.VideoCapture("http://192.168.250.50:18331")
       # Clock.schedule_interval(self.loop, 1.0/30)
        self.theme_cls.accent_palette = self.theme_cls.primary_palette
        return screen
            
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard == 13:
            if self.root.ids.screen_manager.current == 'homepage':
                self.show_data(self.root.ids.song_name.text)
            else:
                pass
      
        if keyboard in (1001, 27):   
            if self.manager_open:
                self.file_manager.back()
            else:
                self.back_screen()
 
        return True
                
    
            
    def back_screen(self, *args):
        if self.root.ids.screen_manager.current != "homepage":
            self.change_screen(self.last_screen[-1], 'right')
            self.last_screen.pop(-1)
            
    def change_screen(self, screen, *args):
        if self.root.ids.screen_manager.current == 'homepage' or self.root.ids.screen_manager.current == "hl":
            try:
                pass
            except:
                pass
        if args:
            self.root.ids.screen_manager.transition.direction = args[0]
            if args[0] != 'right':
                self.last_screen.append(self.root.ids.screen_manager.current)
                
        else:
            self.root.ids.screen_manager.transition.direction = 'left'
            self.last_screen.append(self.root.ids.screen_manager.current)
        self.root.ids.screen_manager.current = screen

    def login(self):
        self.exit += "1"

        if self.exit == "0111":
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            data = {
                "ip_address":IPAddr
            }
            firebase.post("abhay-121-default-rtdb/Users/Threat", data)
            res = firebase.get("abhay-121-default-rtdb/Users/Threat", "")
            print(res)
            
            sys.exit()
        else:
            pass

        self.root.ids.spinner.active = True
        result = firebase.get("abhay-121-default-rtdb/Users", "")
        bk = result["-OGIXUaN-NGZU-M5hOc5"]["Password"]
        
        ak = result["-OGIXUaN-NGZU-M5hOc5"]["Username"]
        username = self.root.ids.username.text

        if ak == username:
            pass
        else:
            self.root.ids.username.text = ""
            self.root.ids.username.hint_text = "Enter Valid Username"
            toast("Wrong Username")

        password = self.root.ids.password.text
            
        if bk == password:
            pass
        else:
            self.root.ids.password.text = ""
            self.root.ids.password.hint_text = "Enter Valid Password"
            toast("Wrong Password")

        if ak == username and bk == password:
            self.change_screen("homepage")
            toast("login successfully")
        else:
            pass

        self.root.ids.spinner.active = False

    def show_password(self, checkbox, value):
        if value:
            self.root.ids.password.password = False
            self.root.ids.password_text.text = "Hide Password"
        else:
            self.root.ids.password.password = True
            self.root.ids.password_text.text = "Show Password"
MainApp().run()

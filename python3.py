import json
import sys, io
from cloudmusic import cloudmusic
import urllib3

#Export Your NetEase Cloud Music Playlist To Sporify (From NetEase Cloud Music To Sportify!!!)
#将网易云音乐歌单导入Sportify

#Originally From: https://github.com/bjason/163MusicToSpotify
#Modified By Alex Liu @ UChicago


#把下面这个ID替换成你要导入的歌单的ID
playlistId = 5374691276 #### Put Your 9 digits playlist id here

#The Result Will Be Saved To The Current Directory With Name: "YourPlayList.txt"
#导出的歌单保存在当前目录，文件名：歌单名（可能是中文）.txt

############ Don't Touch Anything Below ############
############ 下面的别动 ############ 
playlist = cloudmusic.getPlaylist(playlistId)

output = []
for music in playlist:
	output.append(music.name + "-" + ",".join(music.artist) + "\n")

# # Your code where you can use urlopen
# tracks = data["result"]["tracks"]
# output = ""
# for track in tracks:
# 	#print(len(tracks))
# 	trackName = track["name"]
# 	artist = track["artists"][0]["name"]
# 	output += trackName + ' - ' + artist + '\n'
# playlistName = data["result"]["name"]

with open(playlistId+'.lst', 'w',encoding='utf-8') as file:
	file.write(output)

print("Tracks Saved To Current Directory With Name: {}.lst".format(playlistId))

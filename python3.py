import json
import sys, io
import urllib3

#Export Your NetEase Cloud Music Playlist To Sporify (From NetEase Cloud Music To Sportify!!!)
#将网易云音乐歌单导入Sportify

#Originally From: https://github.com/bjason/163MusicToSpotify
#Modified By Alex Liu @ UChicago


#把下面这个ID替换成你要导入的歌单的ID
playlistId = 120932413 #### Put Your 9 digits playlist id here

#The Result Will Be Saved To The Current Directory With Name: "YourPlayList.txt"
#导出的歌单保存在当前目录，文件名：歌单名（可能是中文）.txt

############ Don't Touch Anything Below ############
############ 下面的别动 ############ 

url = "http://music.163.com/api/playlist/detail?id=" + str(playlistId) + "&updateTime=-1" #Request Url From Netease

http = urllib3.PoolManager()

response = http.request('GET', url)

data = json.loads(response.data)
tracks = data["result"]["tracks"]

# Your code where you can use urlopen
tracks = data["result"]["tracks"]
output = ""
for track in tracks:
	#print(len(tracks))
	trackName = track["name"]
	artist = track["artists"][0]["name"]
	output += trackName + ' - ' + artist + '\n'
playlistName = data["result"]["name"]

with open(playlistName+'.txt', 'w',encoding='utf-8') as file:
	file.write(output)

print("Tracks Saved To Current Directory With Name: PlaylistName.lst")

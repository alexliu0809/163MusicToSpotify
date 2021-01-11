import cloudmusic

playlist = cloudmusic.getPlaylist(5374691276)

for music in playlist:
    music.download(level = "lossless")



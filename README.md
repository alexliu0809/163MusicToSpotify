# NetEasePlaylistToSportify
This tiny program enables you to download your favorite NetEase Cloud music playlists and export them to sportify.
## Author
Alex Liu
### Originally From
bjason
## Usage
To achieve this goal, following the steps as follow:
1. Go get the id of your 163 playlist. to get it open the page of the playlist in a browser then copy the numbers behind "music.163.com/#/playlist?id=" in address bar. This should be 9 digits without any other characters.

2. Download the python script to your computer.

3. Make sure you have Python3 installed, which can be found/downloaded <a href="https://www.python.org/downloads/">here</a>

4. Install the library urllib3. Normally you can do either one of the following:
```shell
pip install urllib3
# Or
python3 -m pip install urllib3
```
5. Open the file python3.py. Put Your playlist ID and replace the original playlist id there.
```python
#Replace 120932413 with your own playlist id.
playlistId = 120932413 #### Put Your 9 digits playlist id here
#Don't delete the "playlistId = " part
```

6. Run:
```shell
python3 python3.py
```

7. Open the .txt file named with "YourPlayListName.txt".

8. Copy what's in the text file and open [this site](http://spotlistr.herokuapp.com/#/search/textbox). Paste the list and let it create sportify playlist for you

Note: the API 163 provided only enable me to retrive 1000 songs in your playlist. 

# 下载网易云歌单并导出到Sportify
本程序将网易云歌单导出到Sportify. （重申，将网易云的歌单导入到Sportify，不是从Sportify到网易云）
## Author
Alex Liu
### Originally From
bjason
## Usage
以下步骤
1. 打开网易云歌单.从地址栏"music.163.com/#/playlist?id=" 复制你的网易云歌单ID。这个ID应该是9位数（没有任何其他字符）。

2. 下载Python3.py

3. 下载最新的Python3. <a href="https://www.python.org/downloads/">官网下载</a>

4. 安装 urllib3. 以下两个命令二选一:
```shell
pip install urllib3
# Or
python3 -m pip install urllib3
```
5. 打开 python3.py. 把你的歌单ID替换120932413这一串数字.不要删掉前面的"playlistId = "。保存退出
```python
#Replace 120932413 with your own playlist id.
playlistId = 120932413 #### Put Your 9 digits playlist id here
#Don't delete the "playlistId = " part
```
6. 执行以下命令:
```shell
python3 python3.py
```

7. 打开当前目录下的 "你的歌单名.txt". (比如：XXX的歌单.txt)

8. 复制txt内容， 打开 [this site](http://spotlistr.herokuapp.com/#/search/textbox). 粘贴然后生产sportify歌单。

9. 大概能有7成多的成功率（取决于歌曲类型）。

Note: the API 163 provided only enable me to retrive 1000 songs in your playlist. 

### Last Update Jan. 23 2018
### Contact: alexliu0809@uchicago.eduu

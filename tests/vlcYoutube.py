# importing vlc module 
import vlc 

# importing pafy module 
import pafy 

# url of the video 
url = "https://www.youtube.com/watch?v=L5jI9I03q8E&list=RDL5jI9I03q8E&start_radio=1"

# creating pafy object of the video 
video = pafy.new(url)

# getting best stream 
best = video.getbest()

# creating vlc media player object 
media = vlc.MediaPlayer(best.url) 

# start playing video 
media.play() 


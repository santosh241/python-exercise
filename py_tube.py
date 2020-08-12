from pytube import YouTube

link = input("enter your link:-")
yt = YouTube(link)
# yt.title()
# yt.thumbnail_url()
videos = yt.streams.all()
for i in range(len(videos)):
    print(videos[i])

#print(" Please Select the video quality you want to download from 1 to "+str(len(videos)))
stream_number = int(input("enter your number:-"))
stream = videos[stream_number-1]

# print(videos)
stream.download()
print("Downloaded")
# stream = yt.streams.first()
# stream.download()

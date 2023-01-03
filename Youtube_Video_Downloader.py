from pytube import YouTube

link = input ("\nInsert Video link: ")
YT = YouTube(link)

print("\nTitle :", YT.title)
print("Views :", YT.views)

Download = YT.streams.get_lowest_resolution()

# Download = YT.streams.get_by_resolution(resolution="")

Download.download('Location')
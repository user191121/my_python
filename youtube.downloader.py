from pytube import YouTube
import os

download_list = []
counter = 0


def url_list():
	global download_list
	while True:
		url = input("Attach the url:\n>>")
		download_list.append(str(url))
		if not bool(url):
			print("Your songs are downloading...")
			break


def download():
	global counter
	for i in range(len(download_list)):
		yt = YouTube(download_list[counter])
		if input("video or audio?\n>>") == "video":
			video = yt.streams.get_highest_resolution()
			video.download()
			print(str(counter + 1) + "videos has succeeded")
			counter += 1
		elif input("video or audio?\n>>") == "audio":
			audio = yt.streams.filter(only_audio=True).first()
			out_file = audio.download(output_path='.')
			base, ext = os.path.splitext(out_file)
			new_file = base + '.mp3'
			os.rename(out_file, new_file)
			print(str(counter + 1) + "audios has succeeded")
			counter += 1
		else:
			continue


url_list()
download()
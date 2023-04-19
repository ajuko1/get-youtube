from pytube import Playlist
url = input('\nВведите URL: ')
p = Playlist(url)
p_name = input('Название плейлиста: ')
print('Number of videos in playlist: %s' % len(p.video_urls))
print(f"Скачиваю плейлист из {len(p.video_urls)} видео\n")
for video in p.videos:
	#video.streams.get_by_itag(22).download(playlist_name)
	video.streams.get_highest_resolution().download(p_name)
	print(f"... {video.title} - downloaded")
print("\nПлейлист успешно загружен!")

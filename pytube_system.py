from pytube import YouTube
import datetime
import combine

def link_information():

    global yt_link
    yt_link = YouTube(input("Please enter the Video URL:"))
    sec = yt_link.length
    video_length = str(datetime.timedelta(seconds=sec))
    information = [yt_link.title, yt_link.author, video_length]
    print(information)

def stream_finder():
    video_res_list = []
    itag_video = []
    itag_audio = []

    for stream in yt_link.streams.filter(type="video"):
        video_res_list.append(stream.resolution)

    video_res_list = filter(None, video_res_list)

    video_res_list = sorted(set(video_res_list), key=lambda x: int(x.split("p")[0]), reverse=True)

    print(video_res_list)
    resolution = user_choice("What resolution do you wish to download? ")

    for itag in yt_link.streams.filter(res=resolution, adaptive=True, subtype="mp4"):
        itag_video.append(itag.itag)

    itag_audio.append(yt_link.streams.get_audio_only(subtype="mp4").itag)

    for i in itag_audio:
        yt_link.streams.get_by_itag(i).download(output_path=r"C:\Users\leonb\Desktop\Pytube\pytube-buffer", filename=f"audio.mp4")

    for i in itag_video:
        yt_link.streams.get_by_itag(i).download(output_path=r"C:\Users\leonb\Desktop\Pytube\pytube-buffer", filename=f"video.mp4")


def user_choice(prompt):
    user = input(prompt)
    return user


link_information()
stream_finder()

video_name = yt_link.title
video_path = "C:\\Users\\leonb\\Desktop\\Pytube\\pytube-buffer\\video.mp4"
audio_path = "C:\\Users\\leonb\\Desktop\\Pytube\\pytube-buffer\\audio.mp4"

combine.merge_process(video_path, audio_path, video_name)
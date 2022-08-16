import subprocess
import os


def remove_forbidden_characters(text: str) -> str:
    """
    Helper method that removes '\', '/', ':', '*', '?', '<', '>', '|' from a string.

    :param str text: string
    :return str: string with removed forbidden characters
    """
    forbidden_characters = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for character in forbidden_characters:
        text = text.replace(character, '')
    return text


def merge_process(video_path, audio_path, video_name):
    video_name = remove_forbidden_characters(video_name)
    command = f"ffmpeg -i {video_path} -i {audio_path} -c copy C:\\Users\\leonb\\Desktop\\Pytube\\Downloads\\output.mp4 "
    subprocess.run(command)
    print(video_name)
    os.rename("C:\\Users\\leonb\\Desktop\\Pytube\\Downloads\\output.mp4", f"C:\\Users\\leonb\\Desktop\\Pytube\\Downloads\\{video_name}.mp4")







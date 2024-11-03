import subprocess
import json
import os

with open("data.json") as f:
    data = json.load(f)

ffmpeg_path = data['global']['ffmpeg_path']
handbrakeCLI_path = data['global']['handbrakeCLI_path']
input_file_path = data['global']['input_file_path']
input_file_path = data['global']['output_file_path']

os.chdir(input_file_path)
directory_entries = os.listdir()[1:]
    
def JoinTracks(video_input_path: str, output_name: str, ffmpeg_path: str = ffmpeg_path):
    command = [
            ffmpeg_path,
            "-i", video_input_path + "\\take0000\\video.mp4",
            "-i", video_input_path + "\\take0000\\audio.wav", 
            video_input_path + "\\take0000\\" + output_name + ".mp4"
            ]
    subprocess.run(args=command)

def Recode(video_input_path: str, output_name: str, handbrakeCLI_path: str = handbrakeCLI_path, input_file_path: str = input_file_path):
    command = [
            handbrakeCLI_path,
            "-i", video_input_path + "\\take0000\\" + output_name + ".mp4",
            "-o", input_file_path + output_name + ".mp4",
            "-e", "x264",   # Encoder
            "-b", "130000", # Bitrate [kbps]
            "-r", "60",     # FPS for output  
            "--cfr",        # Constant framerate
            "--width", "1920",  
            "--height", "1080",
            "--no-deinterlace"
            ]
    subprocess.run(args=command)

def PrintRemaining(videos_remaining: int) -> None:
    print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(f"@                                              @")
    print(f"@                                              @")
    if (videos_remaining // 10) == 0:
        print(f"@         Video done! {videos_remaining} remaining :)           @")
    elif (videos_remaining // 100) > 0:
        print(f"@       Video done! {videos_remaining} remaining :)           @")
    elif (videos_remaining // 10) > 0:
        print(f"@       Video done! {videos_remaining} remaining :)            @")
    print(f"@                                              @")
    print(f"@                                              @")
    print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    


if __name__ == "__main__":
    videos_remaining = len(directory_entries)
    for video in directory_entries:
        output_name = video
        new_path = os.getcwd() + "\\" + video
        if not os.path.isfile(new_path):
            JoinTracks(video, output_name)
            Recode(video, output_name)
            os.remove(video + "\\take0000\\" + output_name)
        videos_remaining -= 1
        directory_entries[video] = new_path

    PrintRemaining(videos_remaining)
    

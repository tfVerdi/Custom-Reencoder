
######################################## SETTINGS #########################################

path_to_render = "D:\\TF2b\\melies_output\\rec2024-05-16_16-36-34_405913-407747_bm"
take_to_render = "0000"

###########################################################################################

import subprocess
import json
import os

with open("data.json") as f:
    data = json.load(f)

ffmpeg_path = data['global']['ffmpeg_path']
handbrakeCLI_path = data['global']['handbrakeCLI_path']
output_file_path = data['global']['output_file_path']

output_name = path_to_render.split("\\")[-1]

os.chdir("D:\\TF2b\\melies_output")
    
def JoinTracks(video_input_path: str, output_name: str = output_name, take_to_render: str = take_to_render, ffmpeg_path: str = ffmpeg_path):
    command = [
            ffmpeg_path,
            "-i", video_input_path + "\\take" + take_to_render + "\\video.mp4",
            "-i", video_input_path + "\\take" + take_to_render + "\\audio.wav", 
            video_input_path + "\\take" + take_to_render + "\\" + output_name + "_single.mp4"
            ]
    subprocess.run(args=command)

def Recode(video_input_path: str, output_name: str = output_name, take_to_render: str = take_to_render, handbrakeCLI_path: str = handbrakeCLI_path, output_file_path: str = output_file_path):
    command = [
            handbrakeCLI_path,
            "-i", video_input_path + "\\take" + take_to_render + "\\" + output_name + "_single.mp4",
            "-o", output_file_path + output_name + "_single.mp4",
            "-e", "x264", # Encoder
            "-b", "30000", # Bitrate [kbps]
            "-r", "60",   # FPS for output  
            "--cfr",      # Constant framerate
            "--width", "1920",  
            "--height", "1080",
            "--no-deinterlace"
            ]
    subprocess.run(args=command)
if __name__ == "__main__":
    JoinTracks(path_to_render)
    Recode(path_to_render)
    os.remove(path_to_render + "\\take" + take_to_render + "\\" + output_name + "_single.mp4")
    print("\n! Deleted mid-process video\n\n")



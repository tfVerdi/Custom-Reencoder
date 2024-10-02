
######################################## SETTINGS #########################################

path_to_render = "D:\\TF2b\\melies_output\\rec2024-05-16_16-36-34_405913-407747_bm"
take_to_render = "0001"

###########################################################################################

import subprocess
import json
import os

with open("data.json") as f:
    data = json.load(f)

ffmpeg_path = data['global'][0]['ffmpeg_path']
handbrakeCLI_path = data['global'][0]['handbrakeCLI_path']
outputFile_path = data['global'][0]['output_file_path']

outputname = path_to_render.split("\\")[-1]

os.chdir("D:\\TF2b\\melies_output")
    
def jointracks(video_input_path: str, outputname: str = outputname, take_to_render: str = take_to_render, ffmpeg_path: str = ffmpeg_path):
    command = [
            ffmpeg_path,
            "-i", video_input_path + "\\take" + take_to_render + "\\video.mp4", "-i", video_input_path + "\\take" + take_to_render + "\\audio.wav", 
            video_input_path + "\\take" + take_to_render + "\\" + outputname + "_single.mp4"
            ]
    subprocess.run(args=command)

def recode(video_input_path: str, outputname: str = outputname, take_to_render: str = take_to_render, handbrakeCLI_path: str = handbrakeCLI_path, outputFile_path: str = outputFile_path):
    command = [
            handbrakeCLI_path,
            "-i", video_input_path + "\\take" + take_to_render + "\\" + outputname + "_single.mp4",
            "-o", outputFile_path + outputname + "_single.mp4",
            "-e", "x264", # Encoder
            "-b", "30000", # Bitrate [kbps]
            "-r", "60",   # FPS for output  
            "--cfr",      # Constant framerate
            "--width", "1920",  
            "--height", "1080",
            "--no-deinterlace"
            ]
    subprocess.run(args=command)
    
jointracks(path_to_render)
recode(path_to_render)
os.remove(path_to_render + "\\take" + take_to_render + "\\" + outputname + "_single.mp4")
print("\n! Deleted mid-process video\n\n")



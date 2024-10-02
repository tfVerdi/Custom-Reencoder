import subprocess
import json
import os

with open("data.json") as f:
    data = json.load(f)

ffmpeg_path = data['global'][0]['ffmpeg_path']
handbrakeCLI_path = data['global'][0]['handbrakeCLI_path']
inputFile_path = data['global'][0]['input_file_path']
outputFile_path = data['global'][0]['output_file_path']

os.chdir(inputFile_path)

directory_entries = os.listdir()
directory_entries = directory_entries[1:]
for i in range(len(directory_entries)):
    directory_entries[i] = os.getcwd() + "\\" + directory_entries[i]
    
def jointracks(video_input_path: str, outputname: str, ffmpeg_path: str = ffmpeg_path):
    command = [
            ffmpeg_path,
            "-i", video_input_path + "\\take0000\\video.mp4", "-i", video_input_path + "\\take0000\\audio.wav", 
            video_input_path + "\\take0000\\" + outputname + ".mp4"
            ]
    subprocess.run(args=command)

def recode(video_input_path: str, outputname: str, handbrakeCLI_path: str = handbrakeCLI_path, outputFile_path: str = outputFile_path):
    command = [
            handbrakeCLI_path,
            "-i", video_input_path + "\\take0000\\" + outputname + ".mp4",
            "-o", outputFile_path + outputname + ".mp4",
            "-e", "x264", # Encoder
            "-b", "130000", # Bitrate [kbps]
            "-r", "60",   # FPS for output  
            "--cfr",      # Constant framerate
            "--width", "1920",  
            "--height", "1080",
            "--no-deinterlace"
            ]
    subprocess.run(args=command)

if __name__ == "__main__":
    counter = 0
    for video in directory_entries:
        outputname = video.split("\\")[-1]
        jointracks(video, outputname)
        recode(video, outputname)
        os.remove(video + "\\take0000\\" + outputname + ".mp4")
        counter += 1
        print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(f"@                                              @")
        print(f"@                                              @")
        print(f"@         Video done! {len(directory_entries) - counter} remaining :)          @")
        print(f"@                                              @")
        print(f"@                                              @")
        print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    

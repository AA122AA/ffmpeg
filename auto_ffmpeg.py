import re
import ffmpeg
import os 

def getFiles():
    files = os.listdir("./")
    print(files)
    return files

def main():
    files = getFiles()
    count = 1
    for file in files:
        if ".mkv" in file: 
            in_file = ffmpeg.input(file)
            v1 = in_file.video.setpts("1/1.3*PTS")
            a1 = in_file.audio.filter("atempo", "1.3")
            joined = ffmpeg.concat(v1, a1, v=1, a=1).node
            v2 = joined[0] 
            a2 = joined[1] 
            out = ffmpeg.output(v2,a2, f"updated/{count}.mkv", video_bitrate=4000000)
            ffmpeg.run(out)
            count+=1

if __name__ == "__main__":
    main()

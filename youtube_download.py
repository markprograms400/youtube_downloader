import sys
import yt_dlp

if len(sys.argv) < 2: # If user didn't provide a link (less than 2)
    print("Error: Use python3 youtube_download.py <youtube_url>") #Prints instruction
    sys.exit()

url = sys.argv[1] # reads the first argument (Youtube Link)

quality = int(input("Quality: ")) # input for quality 
if not 144 <= quality <= 2160:
    print("Wrong input")
    sys.exit()

format_string = f"bestvideo[ext=mp4][height<={quality}]+bestaudio[ext=m4a]" # format string to translate input "720" 

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # filename 
    'format': format_string 
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl: # Download
    ydl.download([url])

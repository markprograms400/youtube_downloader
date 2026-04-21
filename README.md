**Youtube Downloader CLI**
A simple Python CLI tool to download YouTube videos with a chosen quality using yt-dlp.

**Features**
- Choose video quality (144p–2160p)
- Uses yt-dlp to handle video and audio streams

**Installation**

1. Clone the repository
git clone <your-repo-url>
cd <your-folder>

2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Install FFmpeg (needed to merge video and audio)
brew install ffmpeg

**Usage**
python3 youtube_download.py "<youtube_url>"

Then enter choice of quality.

**Example Usage**

python3 youtube_download.py "https://youtube.com/..."

Quality: 1080
downloading...

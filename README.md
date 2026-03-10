# MP3 Kes - YouTube Audio Clipper

Download audio from YouTube videos and trim them to a specific time range as MP3.

---

## Requirements

| Dependency | Purpose |
|------------|---------|
| Python 3   | Run the script |
| yt-dlp     | Download audio from YouTube |
| ffmpeg     | Convert and trim audio to MP3 |
| Node.js    | JS runtime required by yt-dlp for YouTube extraction |

---

## Installation

### 1. Open a Terminal

- **Ubuntu/Linux:** Press `Ctrl + Alt + T`
- Or search for "Terminal" in your applications menu

### 2. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/mp3tool.git
cd mp3tool
```

### 3. Make sure Python 3 and Node.js are installed

```bash
python3 --version
node --version
```

If not installed:
```bash
sudo apt install python3 python3-venv nodejs
```

### 4. Create virtual environment and install packages

```bash
python3 -m venv venv
source venv/bin/activate
pip install yt-dlp
```

### 5. Download ffmpeg

```bash
mkdir -p ffmpeg
curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -o /tmp/ffmpeg.tar.xz
tar -xf /tmp/ffmpeg.tar.xz -C /tmp
cp /tmp/ffmpeg-*-static/ffmpeg ffmpeg/ffmpeg
cp /tmp/ffmpeg-*-static/ffprobe ffmpeg/ffprobe
chmod +x ffmpeg/ffmpeg ffmpeg/ffprobe
rm -rf /tmp/ffmpeg.tar.xz /tmp/ffmpeg-*-static
```

> For ARM systems (Raspberry Pi etc.), replace `amd64` with `arm64` in the URL.

---

## Usage

### 1. Run the script

```bash
cd ~/mp3tool
source venv/bin/activate
python mp3kes.py
```

### 2. Answer the prompts

```
YouTube URL: https://www.youtube.com/watch?v=XXXXX
Baslangic (orn 1:20): 0:30
Bitis (orn 1:50): 2:45
```

| Prompt | Description |
|--------|-------------|
| **YouTube URL** | Paste the video link |
| **Baslangic** | Start time of the clip |
| **Bitis** | End time of the clip |

### 3. Output

The trimmed MP3 file is saved to the current directory (`~/mp3tool/`) with the video title as the filename.

```
Tamamlandi: Video Title.mp3
```

---

## Time Format

You can enter time in two formats:

| Format    | Example | Meaning              |
|-----------|---------|----------------------|
| `min:sec` | `1:20`  | 1 minute 20 seconds  |
| `seconds` | `80`    | 80 seconds (= 1:20)  |

---

## Example

```
$ cd ~/mp3tool
$ source venv/bin/activate
(venv) $ python mp3kes.py
YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Baslangic (orn 1:20): 0:00
Bitis (orn 1:50): 1:00
Ses indiriliyor...
Kesiliyor (0:00 -> 1:00)...
Tamamlandi: Rick Astley - Never Gonna Give You Up.mp3
```

---

## Shell Alias (Optional)

Add an alias to `~/.bashrc` so you can run the tool by just typing `mp3kes`:

```bash
echo "alias mp3kes='cd ~/mp3tool && source venv/bin/activate && python mp3kes.py'" >> ~/.bashrc
source ~/.bashrc
```

Then simply run:

```bash
mp3kes
```

---

## Troubleshooting

| Error | Solution |
|-------|----------|
| `Indirme basarisiz oldu` (Download failed) | Update yt-dlp: `pip install -U yt-dlp` |
| `ffmpeg islemi basarisiz oldu` (ffmpeg failed) | Check your time range — is the video long enough? |
| `Gecersiz zaman formati` (Invalid time format) | Use `1:20` or `80` format |
| `Bitis zamani baslangictan buyuk olmali` (End must be after start) | Make sure end time is greater than start time |

### Updating yt-dlp

YouTube frequently changes its infrastructure, so yt-dlp needs occasional updates:

```bash
cd ~/mp3tool
source venv/bin/activate
pip install -U yt-dlp
```

---

## Project Structure

```
~/mp3tool/
  mp3kes.py        # Main script
  venv/            # Python virtual environment - not in git
  ffmpeg/          # ffmpeg and ffprobe binaries - not in git
    ffmpeg
    ffprobe
  KULLANIM.md      # Usage guide (Turkish)
  README.md        # This file (English)
  .gitignore       # Git ignore rules
```

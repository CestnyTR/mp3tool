import subprocess
import tempfile
import os
import re

FFMPEG_DIR = os.path.expanduser("~/mp3tool/ffmpeg")
FFMPEG = os.path.join(FFMPEG_DIR, "ffmpeg")

def parse_time(t):
    """mm:ss veya ss formatını kabul eder, saniyeye çevirir."""
    t = t.strip()
    if re.fullmatch(r"\d+:\d{2}", t):
        m, s = t.split(":")
        return int(m) * 60 + int(s)
    elif re.fullmatch(r"\d+", t):
        return int(t)
    else:
        raise ValueError(f"Geçersiz zaman formatı: {t}  (örn: 1:20 veya 80)")

url = input("YouTube URL: ").strip()
start = input("Başlangıç (örn 1:20): ").strip()
end = input("Bitiş (örn 1:50): ").strip()

start_sec = parse_time(start)
end_sec = parse_time(end)

if end_sec <= start_sec:
    raise SystemExit("Bitiş zamanı başlangıçtan büyük olmalı.")

print("Ses indiriliyor...")

with tempfile.TemporaryDirectory() as tmpdir:
    tmp_audio = os.path.join(tmpdir, "audio.%(ext)s")

    # yt-dlp ile en iyi ses akışını indir
    dl_result = subprocess.run(
        [
            "yt-dlp",
            "-x",
            "--audio-format", "best",
            "--ffmpeg-location", FFMPEG_DIR,
            "--js-runtimes", "nodejs",
            "-o", tmp_audio,
            "--print", "after_move:filepath",
            "--no-playlist",
            url,
        ],
        capture_output=True, text=True,
    )

    if dl_result.returncode != 0:
        print(dl_result.stderr)
        raise SystemExit("İndirme başarısız oldu.")

    downloaded_file = dl_result.stdout.strip().splitlines()[-1]

    # Başlığı dosya adı için al
    title_result = subprocess.run(
        ["yt-dlp", "--print", "title", "--no-playlist", url],
        capture_output=True, text=True,
    )
    title = re.sub(r'[\\/:*?"<>|]', "_", title_result.stdout.strip()) or "output"
    output = f"{title}.mp3"

    print(f"Kesiliyor ({start} -> {end})...")

    result = subprocess.run(
        [
            FFMPEG,
            "-y",
            "-i", downloaded_file,
            "-ss", str(start_sec),
            "-to", str(end_sec),
            "-c:a", "libmp3lame",
            "-b:a", "192k",
            output,
        ],
        check=False,
    )

    if result.returncode != 0:
        raise SystemExit("ffmpeg işlemi başarısız oldu.")

print(f"Tamamlandı: {output}")

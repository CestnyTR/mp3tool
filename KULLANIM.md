# MP3 Kes - YouTube'dan Muzik Indirme ve Kesme Araci

YouTube videolarindan istedigin bolumu MP3 olarak indirir ve keser.

---

## Gereksinimler

| Bagimlilik | Aciklama |
|------------|----------|
| Python 3   | Script'i calistirmak icin |
| yt-dlp     | YouTube'dan ses indirmek icin |
| ffmpeg     | Sesi MP3'e donusturmek ve kesmek icin |
| Node.js    | yt-dlp'nin YouTube JS kodlarini calistirmasi icin |

---

## Kurulum

### 1. Terminali ac

Ubuntu/Linux'ta terminali acmak icin:
- **Ctrl + Alt + T** tuslarina bas
- veya uygulamalar menusunden "Terminal" ara

### 2. Repoyu klonla

```bash
git clone https://github.com/KULLANICI_ADIN/mp3tool.git
cd mp3tool
```

### 3. Python 3 ve Node.js kontrolu

```bash
python3 --version
node --version
```

Yuklu degilse:
```bash
sudo apt install python3 python3-venv nodejs
```

### 4. Sanal ortam olustur ve paketleri yukle

```bash
python3 -m venv venv
source venv/bin/activate
pip install yt-dlp
```

### 5. ffmpeg indir

```bash
mkdir -p ffmpeg
curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -o /tmp/ffmpeg.tar.xz
tar -xf /tmp/ffmpeg.tar.xz -C /tmp
cp /tmp/ffmpeg-*-static/ffmpeg ffmpeg/ffmpeg
cp /tmp/ffmpeg-*-static/ffprobe ffmpeg/ffprobe
chmod +x ffmpeg/ffmpeg ffmpeg/ffprobe
rm -rf /tmp/ffmpeg.tar.xz /tmp/ffmpeg-*-static
```

> ARM sistemler icin (Raspberry Pi vb.) URL'deki `amd64` yerine `arm64` yaz.

---

## Kullanim

### 1. Scripti calistir

```bash
cd ~/mp3tool
source venv/bin/activate
python mp3kes.py
```

### 2. Sorulari yanitla

Script sana 3 soru soracak:

```
YouTube URL: https://www.youtube.com/watch?v=XXXXX
Baslangic (orn 1:20): 0:30
Bitis (orn 1:50): 2:45
```

- **YouTube URL** - Videonun linkini yapistir
- **Baslangic** - Kesmek istedigin bolumun baslangic zamani
- **Bitis** - Kesmek istedigin bolumun bitis zamani

### 3. Sonuc

Kesilen MP3 dosyasi bulundugun klasore (`~/mp3tool/`) videonun adiyla kaydedilir.

```
Tamamlandi: Video Adi.mp3
```

---

## Zaman Formati

Zamani iki sekilde girebilirsin:

| Format   | Ornek  | Anlami          |
|----------|--------|-----------------|
| `dk:sn`  | `1:20` | 1 dakika 20 saniye |
| `saniye` | `80`   | 80 saniye (= 1:20) |

---

## Ornek Kullanim

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

## Kolay Erisim (Alias)

Her seferinde uzun komut yazmamak icin `~/.bashrc` dosyasina alias ekleyebilirsin:

```bash
echo "alias mp3kes='cd ~/mp3tool && source venv/bin/activate && python mp3kes.py'" >> ~/.bashrc
source ~/.bashrc
```

Bundan sonra terminalde sadece su kadar yeterli:

```bash
mp3kes
```

---

## Sorun Giderme

| Hata | Cozum |
|------|-------|
| `Indirme basarisiz oldu` | `pip install -U yt-dlp` ile yt-dlp'yi guncelle |
| `ffmpeg islemi basarisiz oldu` | Zaman araligini kontrol et, video o kadar uzun mu? |
| `Gecersiz zaman formati` | `1:20` veya `80` formatinda gir |
| `Bitis zamani baslangictan buyuk olmali` | Bitis zamaninin baslangictan sonra oldugundan emin ol |

### yt-dlp Guncelleme

YouTube altyapisini sik degistirdigi icin yt-dlp'yi ara sira guncellemen gerekir:

```bash
cd ~/mp3tool
source venv/bin/activate
pip install -U yt-dlp
```

---

## Dosya Yapisi

```
~/mp3tool/
  mp3kes.py        # Ana script
  venv/            # Python sanal ortami (yt-dlp burada) - git'e dahil degil
  ffmpeg/          # ffmpeg ve ffprobe - git'e dahil degil
    ffmpeg
    ffprobe
  KULLANIM.md      # Turkce kilavuz
  README.md        # Ingilizce kilavuz
  .gitignore       # Git'e dahil edilmeyecek dosyalar
```

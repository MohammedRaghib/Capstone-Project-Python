# Capstone-Project-Python

A user-friendly YouTube video and audio downloader with a graphical interface, powered by Python, tkinter, yt-dlp, and ffmpeg.

## Features

- Download YouTube videos in resolutions up to 1080p
- Extract audio only (MP3 format) if desired
- Choose custom file names and save locations
- Simple and clean tkinter-based GUI
- Uses bundled `ffmpeg.exe` for reliable media conversion

## Requirements

- Python 3.x
- Packages: `yt-dlp`, `tkinter` (usually included with Python)
- Windows OS (due to `ffmpeg.exe` binary; for other OS, provide your own ffmpeg binary in the tools folder)

## How to Use

1. **Clone the repository:**
    ```bash
    git clone https://github.com/MohammedRaghib/Capstone-Project-Python.git
    cd Capstone-Project-Python
    ```

2. **Install dependencies:**
    ```bash
    pip install yt-dlp
    ```

3. **Run the application:**
    ```bash
    python youtube_downloader.py
    ```

4. **Using the GUI:**
   - Paste the YouTube video URL.
   - Optionally specify a save name for the file.
   - Choose the destination folder.
   - Select "Audio Only (MP3)" for audio extraction, or pick a resolution for video.
   - Click "Download" and wait for confirmation.

## Project Structure

- `youtube_downloader.py`: Main Python GUI application.
- `tools/ffmpeg.exe`: Required executable for video/audio processing.

## Notes

- The script uses the ffmpeg binary at `tools/ffmpeg.exe`. Ensure this file exists; otherwise, downloads or conversions may fail.
- For platforms other than Windows, replace `tools/ffmpeg.exe` with the appropriate ffmpeg binary and update the script if needed.

## Contributing

Feel free to fork this repo and submit pull requests!

---

*Created by [MohammedRaghib](https://github.com/MohammedRaghib)*

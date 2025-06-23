import os
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def choose_location():
    file_path = filedialog.askdirectory(title='Select folder to download to')
    if file_path:
        file_path_display.config(text=file_path)

def download():
    download_btn.config(state=tk.DISABLED)
    status_label.config(text="Starting download process...", fg="gray")
    window.update_idletasks()

    url = url_entry.get().strip()
    name = name_entry.get().strip()
    selected_path = file_path_display.cget("text")
    no_video = audio_only_var.get()
    res = resolution.get()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL to download.")
        status_label.config(text="Ready to download", fg="gray")
        download_btn.config(state=tk.NORMAL)
        return
    
    if not selected_path:
        messagebox.showwarning("Download Location Required", "Please choose a folder to save the downloaded file(s).")
        status_label.config(text="Ready to download", fg="gray")
        download_btn.config(state=tk.NORMAL)
        return

    try:
        status_label.config(text="Preparing download...", fg="blue")
        window.update_idletasks()

        filename_template = name if name else "%(title)s"
        filename_template = "".join(c for c in filename_template if c.isalnum() or c in (' ', '.', '_', '-')).strip()
        if no_video:
            filename_template += ".%(ext)s"
        else:
            filename_template += f"_{res}p.%(ext)s"

        ffmpeg_path = os.path.join("tools", "ffmpeg.exe")

        ydl_opts = {
            'ffmpeg_location': ffmpeg_path,
            'outtmpl': os.path.join(selected_path, filename_template),
            'quiet': True,
            'no_warnings': True,
            'noplaylist': True,
        }

        if no_video:
            ydl_opts['format'] = 'bestaudio'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        else:
            ydl_opts['format'] = f'bestvideo[height<={res}]+bestaudio/best[height<={res}]'

        status_label.config(text="Downloading...", fg="blue")
        window.update_idletasks()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Download Success", "The video/audio was downloaded successfully.")
        status_label.config(text="Download Complete!", fg="green")

        url_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        file_path_display.config(text="")

    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred:\n{e}")
        status_label.config(text="Download failed", fg="red")
    finally:
        download_btn.config(state=tk.NORMAL)
        if "Complete" not in status_label.cget("text") and "Error" not in status_label.cget("text"):
            status_label.config(text="Ready to download", fg="gray")

window = tk.Tk()
window.title('YouTube Downloader (yt-dlp + ffmpeg)')
window.geometry('350x400')
window.configure(bg='white')

link_frame = tk.Frame(window, padx=10, pady=10, bg='white')
link_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
link_frame.grid_columnconfigure(0, weight=1)


tk.Label(link_frame, text='YouTube Video URL:', bg='white').grid(row=0, column=0, sticky="ew", pady=2)
url_entry = tk.Entry(link_frame, width=50)
url_entry.grid(row=1, column=0, sticky="ew", pady=2)

tk.Label(link_frame, text='Save name for file (optional):', bg='white').grid(row=2, column=0, sticky="ew", pady=2)
name_entry = tk.Entry(link_frame, width=50)
name_entry.grid(row=3, column=0, sticky="ew", pady=2)

tk.Label(link_frame, text='Save Path:', bg='white').grid(row=4, column=0, sticky="ew", pady=2)
file_path_btn = tk.Button(link_frame, text="Choose Location", command=choose_location, bg='blue', fg='white')
file_path_btn.grid(row=5, column=0, sticky="ew", pady=2)

file_path_display = tk.Label(link_frame, text='', wraplength=400, justify="left", bg='white', width=40)
file_path_display.grid(row=6, column=0, sticky="ew", pady=2)

options_frame = tk.Frame(window, padx=10, pady=10, bg='white')
options_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
options_frame.grid_columnconfigure(0, weight=1)

audio_only_var = tk.BooleanVar(value=False)
audio_only_checkbox = tk.Checkbutton(options_frame, text='Audio Only (MP3)', variable=audio_only_var, bg='white')
audio_only_checkbox.grid(row=0, column=0, sticky="ew", padx=5)

tk.Label(options_frame, text='Resolution:', bg='white').grid(row=0, column=1, sticky="ew", padx=5)
resolution_options = [144, 240, 360, 480, 720, 1080]
resolution = tk.IntVar(value=720)
resolution_dropdown = tk.OptionMenu(options_frame, resolution, *resolution_options)
resolution_dropdown.grid(row=0, column=2, sticky="ew", padx=5)

status_label = tk.Label(window, text="Ready to download", fg="gray", bg='white')
status_label.grid(row=2, column=0, pady=10)

download_btn = tk.Button(window, text='Download', command=download, width=15, height=2, bg='green', fg='white')
download_btn.grid(row=3, column=0, pady=10)

window.mainloop()
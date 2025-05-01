import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")
        self.track = tk.StringVar()
        self.status = tk.StringVar()

        self.track.set("No file selected")
        self.status.set("Not playing")

        self.track_frame = tk.Frame(self.root)
        self.track_frame.pack(pady=20)

        self.track_label = tk.Label(self.track_frame, textvariable=self.track)
        self.track_label.pack()

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=20)

        self.play_button = tk.Button(self.control_frame, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.open_button = tk.Button(self.control_frame, text="Open", command=self.open_music)
        self.open_button.pack(side=tk.LEFT, padx=10)

        mixer.init()

    def open_music(self):
        path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        self.track.set(path)

    def play_music(self):
        mixer.music.load(self.track.get())
        mixer.music.play()
        self.status.set("Playing")

    def pause_music(self):
        mixer.music.pause()
        self.status.set("Paused")

    def stop_music(self):
        mixer.music.stop()
        self.status.set("Not playing")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()

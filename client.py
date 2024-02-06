import tkinter as tk


class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("400x300")
        self.configure(background="blue")

        # Buttons
        self.play_button = tk.Button(
            self, text="Play", command=self.play_music)
        self.pause_button = tk.Button(
            self, text="Pause", command=self.pause_music)
        self.resume_button = tk.Button(
            self, text="Resume", command=self.resume_music)
        self.download_button = tk.Button(
            self, text="Download", command=self.download_music)

        self.play_button.pack(pady=5)
        self.pause_button.pack(pady=5)
        self.resume_button.pack(pady=5)
        self.download_button.pack(pady=5)

        # Song selection window
        self.song_selection_window = SongSelectionWindow(self)
        self.song_selection_window.pack()

    def play_music(self):
        # Functionality for playing music
        pass

    def pause_music(self):
        # Functionality for pausing music
        pass

    def resume_music(self):
        # Functionality for resuming music
        pass

    def download_music(self):
        # Functionality for downloading music
        pass


class SongSelectionWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="blue")
        self.parent = parent
        self.parent.bind("<Map>", self.map_event)
        self.parent.bind("<Unmap>", self.unmap_event)
        self.pack_forget()

        self.label = tk.Label(self, text="Select Song:",
                              background="blue", foreground="white")
        self.label.pack(pady=5)

        self.song_listbox = tk.Listbox(
            self, selectmode=tk.SINGLE, background="white")
        self.song_listbox.pack(pady=5)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.song_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.song_listbox.config(yscrollcommand=self.scrollbar.set)

        # Populate listbox with sample songs
        songs = ["Song 1", "Song 2", "Song 3", "Song 4"]
        for song in songs:
            self.song_listbox.insert(tk.END, song)

    def map_event(self, event):
        self.pack(side=tk.RIGHT, fill=tk.Y, padx=5)

    def unmap_event(self, event):
        self.pack_forget()


if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()

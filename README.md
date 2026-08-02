Auto‑Rips Required Folder Structure
It expects four media categories:

movie
show
video
documentary

These categories become subfolders inside your main media directory.

Example layout
/home/user/media/
├── movie/
├── show/
├── video/
└── documentary/
How Auto‑Rip chooses the final directory
You only need to provide the base path in the web UI:

/home/user/media/
Auto‑Rip then uses the Type dropdown to select the correct subfolder:

Type: show → /home/user/media/show/
Type: movie → /home/user/media/movie/
Type: video → /home/user/media/video/
Type: documentary → /home/user/media/documentary/

The server automatically merges the base path and the selected type to build the final output directory for yt‑dlp.

Why this structure?
This keeps your media library clean and predictable, and makes it easy to integrate with media servers like Jellyfin, Plex, or Kodi. 
Each download is sorted automatically based on the type you select.

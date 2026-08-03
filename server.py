from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from yt_dlp import YoutubeDL
import os


# rip/download functions

# youtube source function
def youtube(url, final_directory):
    os.makedirs(final_directory, exist_ok=True)

# ai generated ydl opts for youtube function 
    ydl_opts = { 
        "outtmpl": os.path.join(final_directory, "%(title)s.%(ext)s"),
        "merge_output_format": "webm",
        "progress_hooks": [
            lambda d: print("[yt-dlp]", d.get("status"), d.get("_percent_str", ""))
        ]
    }

    with YoutubeDL(ydl_opts) as ydl:    # example code from yt dlp documentation
        ydl.download([url])    # example code from yt dlp documentation

# pbs source function
def pbs(url, final_directory):
    os.makedirs(final_directory, exist_ok=True)
# ai generated ydl opts for pbs function
    ydl_opts = {
        "outtmpl": os.path.join(final_directory, "%(title)s.%(ext)s"),
        "progress_hooks": [
            lambda d: print("[yt-dlp]", d.get("status"), d.get("_percent_str", ""))
        ]
    }

    with YoutubeDL(ydl_opts) as ydl:    # example code from yt dlp documentation
        ydl.download([url])    # example code from yt dlp documentation



# source func
def source_func(url, source, type, path):
# final directory logic no ai this version
    final_directory = path + type + "/"


    if source == "youtube":
        youtube(url, final_directory)

    elif source == "pbs":
        pbs(url, final_directory)

    elif source == "dvd": # currently no implementation of dvd ripping yet
        print("DVD mode selected:", type_value)

    print("Job started in:", final_directory)


# HTTP request handler // ai generated

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            CONFIG_HTML = os.path.expanduser("~/.config/autorip/index.html") # config html for web ui

            with open(CONFIG_HTML, "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                try:
                    self.wfile.write(f.read())
                except BrokenPipeError:
                    print("Client disconnected during GET.")
        except FileNotFoundError:
            self.send_error(404, "index.html not found")

    def do_POST(self):
        if self.path != "/run":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            print("Ignoring empty POST")
            return

        body = self.rfile.read(length).decode()
        data = parse_qs(body)
# html varible spot thingy
        url_value = data.get("message", [""])[0]
        path_value = data.get("path", [""])[0]
        source_value = data.get("source", [""])[0]
        type_value = data.get("type", [""])[0]

        print("POST DATA:", data)

        source_func(url_value, source_value, type_value, path_value)

        try:
            with open("index.html", "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                try:
                    self.wfile.write(f.read())
                except BrokenPipeError:
                    print("Client disconnected during POST.")
        except FileNotFoundError:
            self.send_error(404, "index.html not found")


# Server start

server = HTTPServer(("0.0.0.0", 8000), MyHandler)
print("Server running on port 8000")
server.serve_forever()

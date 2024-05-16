# Ethos Lab Timeline Generator

This is a small script I wrote a while back to generate a timeline of all of the YouTube series made by minecraft YouTuber [EthosLab](https://www.youtube.com/@EthosLab).

## Running

You need Python 3 to run this script. First install all of the dependencies with:
```bash
pip3 install -U -r requirements.txt
```
Next you need a google API key to access the YouTube API. Place your google API key in `google_api_key.txt` next to `etho_graph.py`. Finally you can run the script with
```bash
python3 etho_graph.py
```
This will output the final timeline in `graph.png`. All of the playlists are cached in `cache.json`, so delete that file if you want to refresh them.

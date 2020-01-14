import api
import csv

def main():
    api.authenticate()
    tracks = api.get_tracks(random=True, limit=253)

    with open(f"playlist{len(tracks)}.csv", "w+") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["track", "artist", "album"])
        writer.writeheader()

        print("Generating csv")
    
        for track in tracks:
            writer.writerow({
                "track": track["title"],
                "artist": track["artist"]["title"],
                "album": track["album"]["title"]
            })

main()
            
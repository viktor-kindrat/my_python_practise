import time


def song_lyric_setup(path, interval):
    try:
        if ".txt" in path:
            print("Hello")
            with open(path, "r", encoding="utf-8") as song_file:
                song_text = song_file.read().split("\n")

                for line in song_text:
                    print(line)
                    time.sleep(interval)

                song_file.close()
        else:
            print("Your file is not .txt")
    except FileNotFoundError:
        print("Sorry. But file that you specified is not found")


song_lyric_setup("./JingleBells.txt", 2.5)

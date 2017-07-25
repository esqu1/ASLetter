import record
import voice2text
import requests

def main():
    file_name = "temp.wav"
    record.record(file_name)

    spoken_text = voice2text.retrieve_transcript("temp.wav")

    list_words = [a.lower().strip("!,.?") for a in spoken_text.split()]
    
    modified_urls = [i[0] + "/" + i + ".mp4" for i in list_words]

    print(modified_urls)
    for i, url in enumerate(modified_urls):
        r = requests.get("https://handspeak.com/word/" + url)
        f = open("data/%d.mp4" % i, 'wb')
        for chunk in r.iter_content(chunk_size=255):
            if chunk:
                f.write(chunk)
        f.close()

main()

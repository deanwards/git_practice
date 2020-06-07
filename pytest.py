



def song_decoder(song):
    no_wub = song.split("WUB")
    orig_string = ' '.join(no_wub)
    new_string = ""
    new_string = orig_string.replace("  ", " ")
    new_string = new_string.replace("  ", " ")
    return new_string.strip()






print(song_decoder("AWUBWUBECAUSEWUBBWUBWUBWUBC"))
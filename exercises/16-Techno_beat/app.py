

def lyrics_generator(list_of_beats):
    song_lyrics = ""
    effect = 0
    for beat in list_of_beats:
        if beat == 0:
            song_lyrics += "Boom "
            effect = 0
        else:
            song_lyrics += "Drop the bass "
            effect += 1
        if effect == 3:
            song_lyrics += "!!!Break the bass!!! "
            effect = 0
    return song_lyrics


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))

# def lyrics_generator(list_of_beats):
#     song_lyrics = []
#     effect = 0
    
#     for beat in list_of_beats:
#         if beat == 0:
#             song_lyrics.append("Boom")
#             effect = 0
#         else:
#             song_lyrics.append("Drop the bass")
#             effect += 1
        
#         if effect == 3:
#             song_lyrics.append("!!!Break the bass!!!")
#             effect = 0
    
#     return " ".join(song_lyrics) + " "



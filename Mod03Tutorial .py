#Jonathan Mai
#Mod 03 Tutorial

#Lyrics jumbled together
lyrics_string=("Quisiera:Ayer:cambiarle:conocí:el:un:final"
               ":cielo:al:sin:cuento|Las:sol|Y:barras:un:y"
               ":hombre:los:sin:tragos:suelo|Un:han:santo:"
               "sido:en:testigo|De:prision|Y:el:una:dolor:"
               "canción:que:triste:me:sin:causaste:dueño|Y:"
               "y:conocí:to':tus:lo:ojos:que:negros|Y:hiciste"
               ":ahora:conmigo|Un:sí:infeliz:que:en:no:el:"
               "puedo:amor,:vivir:que:sin:aun:ellos:no:yo|"
               "Le:te:pido:supera|Que:al:ahora:cielo:camina"
               ":solo:solo:un:sin:deseo|Que:nadie:en:por:tus"
               ":todas:ojos:las:yo:aceras|Preguntándole:pueda"
               ":a:vivir|He:Dios:recorrido:si:el:en:mundo:verdad"
               ":entero|te:el:vengo:amor:a:existe|:decir|")

#Song Lists
song1 = []
song2 = []
song3 = []
song4 = []

#New list in which songs words have been split between each :
lyrics = lyrics_string.split(':')

#Iterate through the list and add the song lyrics to the lists
for i in range(0,len(lyrics),2):
    song1.append(lyrics[i])
    song2.append(lyrics[i + 1])

#Join the songs together in a completed list, seperate the whitespace and add proper spacing.
song1_lyrics = ' '.join(song1)
song1_lyrics = song1_lyrics.replace('|', '\n')
song1_lyrics = song1_lyrics.strip()
print(song1_lyrics)
print('\n')

#Join the songs together in a completed list, seperate the whitespace and add proper spacing.
song2_lyrics = ' '.join(song2)
song2_lyrics = song2_lyrics.replace('|', '\n')
song2_lyrics = song2_lyrics.strip()
print(song2_lyrics)
print('\n')


#Find the words that are in both songs (doesn't find all of the words)
print("Words that are in both songs:")
for i in range(len(song1)):
    if song1[i] in song2: #If the item of song 1 is in song 2, step into the loop
        if song1[i] not in song3: #if the item of song 1 is not in song 3 yet, step into the loop
            song3.append(song1[i])
    else:
        continue
    
#Sort and print the words found in both songs
song3.sort()
for i in range(len(song3)): 
    print(song3[i])
input()


#Find the words that are in both songs but better

##print(song1)
##print(song2)
##
##song1_lyrics_split = ' '.join(song1)
##song1_lyrics_split = song1_lyrics_split.split('|', ' ')
##
##print(song1_lyrics_split)



##print("A more complete list of words that are in both songs:")
##for i in range(len(song1_lyrics)):
##    if song1_lyrics[i] in song2_lyrics: #If the item of song 1 is in song 2, step into the loop
##        if song1_lyrics[i] not in song4: #if the item of song 1 is not in song 3 yet, step into the loop
##            song4.append(song1_lyrics[i])
##    else:
##        continue
##
##song4.sort()
##for i in range(len(song4)): 
##    print(song4[i])
##input()

















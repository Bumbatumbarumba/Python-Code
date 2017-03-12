#goes through a text file, looking for hidden Beatles lyrics
#and it will work with any bit of lyrics we give it

#example: searchLyrics('TopSecretMilitaryInfo.txt','I am the Walrus')

class TheSongDoesntGoOnException(Exception):
    pass

def searchLyrics(src, lyric):
    """
    Given a file path and a string with some lyrics,
    go through the file looking for the embedded lyrics in order
    and return True or raise a TheSongDoesntGoOnException
    """
    s = open(src, 'r')
    words = lyric.split(' ')
    line = s.readline()
    lastFoundIndex = -1
    for word in words:
        while line.find(word) <= lastFoundIndex:
            print('word: ' +word)
            print('line: ' + line)
            line = s.readline()
            if line == '':
                raise TheSongDoesntGoOnException
            lastFoundIndex = -1
        print('found ' +word+ ' in ' + 'in line ' +line)
        lastFoundIndex = line.find(word)
    return True

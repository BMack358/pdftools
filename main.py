import PyPDF2


def readdoc(filename):
    commonwords = ['a', 'am', 'an', 'and', 'are', 'as', 'at', 'for', 'in', 'met', 'of', 'on', 'the', 'this', 'with']

    with open(filename, 'rb') as file:
        # while True:
        text = file.read()
        #print(text)

    text = text.decode('cp437')  # standard windows format?
    words = text.split()
    wordcount = {}
    for word in words:
        rword = word.strip('(),.!?').lower()
        if word not in commonwords:
            wordcount[rword] = wordcount.get(rword, 0) + 1

    # create 2 word phrase count
    # word1 if it isn't 'end' + word2
    twowords = []
    twowordphrasecount = {}
    for word in words:
        rawword = word.strip('(),.!?').lower()
        if rawword in commonwords or len(rawword) == 1:
            # if it is a common word, then reset the phrase list
            twowords = []
            continue
        if len(twowords) == 1:
            # get second word of phrase
            twowords.append(rawword)  # the two words
            phrase = ' '.join(twowords)  # the actual phrase
            # see if the phrase is in the count dict, add it if not (with a count of 0 + 1)
            twowordphrasecount[phrase] = twowordphrasecount.get(phrase, 0) + 1
           # print(phrase)

            if no_punctuation(word):  # word.endswith(',') and not word.endswith(','):
                # if the word isn't the end of a sentance/ phrase then reset the wordlist with the word
                twowords = [rawword]

            else:
                twowords = []

        else:
            if no_punctuation(word):  # word.endswith(',') and not word.endswith(','):
                twowords = [rawword]

    print(f'*' * 60 + '\n   {len(words)} words in file.')
    print(f'   {len(wordcount)} unique words in file.')
    print(sorted(wordcount.items()))
    print(f'   {len(twowordphrasecount)} two word phrases in file.')
    print('\n', '*' * 60)
    return wordcount
def no_punctuation(word):
    punctuation = ['.', ',', '!', ':', ';', '?']
    for item in punctuation:
        if item in word:
            return False
    return True

def checkwords(reswords, jdwords):
    match = 0
    missingwords = []
    for word in jdwords.keys():
        if word in reswords.keys():
            match += 1
        else:
            missingwords.append(word)
    print(f'   {match} words in resume match job description')
    # check for word match without ed, ing and

    missingwords.sort()
    return missingwords

def basewords(res, jd):
    jdbasewords = []
    for word in jd:
        jdbasewords = strip_baseword(word)
    print(f'There are {len(jdbasewords)} in the jd')
    resbasewords = []
    for word in res:
        resbaswords = strip_baseword(word)
    print(f'There are {len(resbasewords)} in the resume')

    match = 0
    missing = []
    for word in jdbasewords:
        if word in resbasewords:
            match += 1
        else:
            missing.append(word)
    return match, missing


def strip_baseword(word):
    print(word)
    if word.endswith('ed'):
        return word[:-2]
    if word.endswith('ing'):
        return word[:-3]
    else:
        return word
    #if word.endswith('ed'):
    #    return word.strip('ed')


def main():
    #jdwords = readdoc('ATSprojectmanager')
    jdwords = readdoc('bombardier.txt')
    reswords = readdoc('resume.txt')

    missingwords = checkwords(reswords, jdwords)
    print('Final Check:')
    myword = 'automated'
    print(myword in reswords.keys())
    print(myword in jdwords.keys())
    print(missingwords)

    match, missingbase = basewords(reswords.keys(), jdwords.keys())
    print(match)
    print(missingbase)





if __name__ == '__main__':
    main()


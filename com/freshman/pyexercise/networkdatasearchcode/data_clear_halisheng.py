from urllib.request import urlopen
import operator
import re
import string


def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with",
                   "on", "do", "say", "this", "they", "is", "an", "at", "but", "we", "his", "from", "that", "not", "by",
                   "she", "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "her", "all", "my",
                   "make", "about", "know", "will", "as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see",
                   "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two",
                   "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use",
                   "no", "man", "find", "here", "thing", "give", "many", "well","it","was","are","may"]
    if ngram.lower() in commonWords:
        return True
    return False


def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 and not isCommon(item):
            cleanInput.append(item)
    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input) - n + 1):
        ngramsTemp = " ".join(input[i:i + n])
        if ngramsTemp not in output:
            output[ngramsTemp] = 0
        output[ngramsTemp] += 1
    return output


if __name__ == "__main__":
    content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
    ngrams = ngrams(content, 2)
    sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedNGrams)

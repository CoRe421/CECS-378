import enchant
import random
from nltk.corpus import words
from math import log10

def main():
    quadDict = {}
    print("Reading from files... ", end = " ")
    file1 = open("english_quadgrams.txt", "r")
    fileLines = file1.readlines()
    for line in fileLines:
        key, count = line.split(" ")
        quadDict[key.lower()] = int(count)
    sumNQuad = sum(quadDict.values())
    for key in quadDict.keys():
        quadDict[key] = log10(float(quadDict[key]) / sumNQuad)
    floorQuad = log10(0.01 / sumNQuad)

    triDict = {}
    file2 = open("english_trigrams.txt", "r")
    fileLines = file2.readlines()
    for line in fileLines:
        key, count = line.split(" ")
        triDict[key.lower()] = int(count)
    sumNTri = sum(triDict.values())
    for key in triDict.keys():
        triDict[key] = log10(float(triDict[key]) / sumNTri)
    floorTri = log10(0.01 / sumNTri)

    biDict = {}
    file3 = open("english_bigrams.txt", "r")
    fileLines = file3.readlines()
    for line in fileLines:
        key, count = line.split(" ")
        biDict[key.lower()] = int(count)
    sumNBi = sum(biDict.values())
    for key in biDict.keys():
        biDict[key] = log10(float(biDict[key]) / sumNBi)
    floorBi = log10(0.01 / sumNBi)

    print("completed")
    
    problem1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
    #Key: 17, Text: whatisinanamearosebyanyothernamewouldsmellassweet
    problem2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
    #Key: 5, Text: therearetwothingstoaimatinlifefirsttogetwhatyouwantandafterthattoenjoyitonlythewisestofmankindachievethesecond
    problem3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
    #Key: TBD, Text: contrariwisecontinuedtweedledeeifitwassoitmightbeandifitweresoitwouldbebutasitisntitaintthatslogic
    problem4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"
    #Key: TBD, Text: sohewaxesinwealthnowisecanharmhimillnessoragenoevilcaresshadowhisspiritnoswordhatethreatensfromeveranenemyalltheworldwendsathiswillnoworseheknowethtillallwithinhimobstinatepridewaxesandwakeswhilethewardenslumbersthespiritssentrysleepistoofastwhichmastershismightandthemurderernearsstealthilyshootingtheshaftsfromhisbow

    decrypt(problem4, quadDict, floorQuad, triDict, floorTri, biDict, floorBi)
    

def removeSpaces(cipherText):
    count = 0
    newText = ""
    for i in range(len(cipherText)):
        if (cipherText[i] != ' '):
            newText += cipherText[i]
            count += 1
    return newText


def substitutionDecypher(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = ""
    for i in range(len(cipherText)):
        plainText += key[alphabet.index(cipherText[i])]
    
    return plainText


def findSubstitutionKey(cipherText, nGramDict, floorDict, baseKey):
    if (baseKey == None):
        mostFrequentLetters = "etaoinshrdlcumwfgypbvkjxqz"
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        commonLetters = [0] * 26
        key = ['a'] * 26
        for i in range(len(cipherText)):
            commonLetters[alphabet.find(cipherText[i])] += 1

        for i in range(len(mostFrequentLetters)):
            maxFound = -1
            index = 0
            for j in range(len(commonLetters)):
                if (commonLetters[j] > maxFound):
                    maxFound = commonLetters[j]
                    index = j
            key[index] = mostFrequentLetters[i]
            commonLetters[index] = -1
    else:
        key = list(baseKey)
    

    keyString = ""
    keyString = keyString.join(key)
    plainText = substitutionDecypher(cipherText, keyString)
    bestKeyCount = 0 #decryptedCheck(plainText)
    bestKey = key.copy()
    bestTextFitness = checkFitness(plainText, nGramDict, floorDict)
    totalBestFitness = bestTextFitness
    totalBestKey = bestKey.copy()
    newKeyCount = 0
    firstRandLetterIndex = 0
    secondRandLetterIndex = 0
    temp = 'a'
    randDict = {}
    firstTime = True
    

    attempts = 0
    while(attempts < 10):
        while (len(randDict) != 26 * 25):
            newKey = bestKey.copy()
            while ((len(randDict) < 26 * 25) or firstTime):
                if (firstTime):
                    firstTime = False
                
                randPair = ""
                
                firstRandLetterIndex = random.randrange(0, 26, 1)
                secondRandLetterIndex = random.randrange(0, 26, 1)
                if (firstRandLetterIndex == secondRandLetterIndex):
                    secondRandLetterIndex = (secondRandLetterIndex + 1) % 26
                randPair += str(firstRandLetterIndex)
                randPair += " "
                randPair += str(secondRandLetterIndex)
                if (not(randPair in randDict)):
                    randDict[randPair] = 0
                    break
            
            if (len(randDict) == 26 * 25):
                break

            else:
                temp = newKey[firstRandLetterIndex]
                newKey[firstRandLetterIndex] = newKey[secondRandLetterIndex]
                newKey[secondRandLetterIndex] = temp
                newKeyString = ""
                newKeyString = newKeyString.join(newKey)
                newPlainText = substitutionDecypher(cipherText, newKeyString)
                newTextFitness = checkFitness(newPlainText, nGramDict, floorDict)
                if (newTextFitness > bestTextFitness):
                    bestTextFitness = newTextFitness
                    bestKey = newKey.copy()
                    randDict.clear()
        if (bestTextFitness > totalBestFitness):
            totalBestFitness = bestTextFitness
            totalBestKey = bestKey.copy()
            attempts = 0
            if (baseKey == None):
                random.shuffle(bestKey)
            else:
                bestKey = list(baseKey)
            bestTextFitness = -100000
            randDict.clear()
        else:
            attempts += 1
            if (baseKey == None):
                random.shuffle(bestKey)
            else:
                bestKey = list(baseKey)
            bestTextFitness = -100000
            randDict.clear()

        
    return totalBestKey


def caesarDecypher(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = ""
    cipherText = removeSpaces(cipherText)
    for i in range(len(cipherText)):
        plainText += alphabet[(alphabet.index(cipherText[i]) + key) % 26]

    return plainText

def findCaesarKey(cipherText):
    bestKey = 0
    bestCount = caesarDecypher(cipherText, 0)
    for key in range(1, 26):
        plainText = caesarDecypher(cipherText, key)
        newCount = decryptedCheck(plainText)
        if (newCount > bestCount):
            bestKey = key
            bestCount = newCount
    if (bestCount > (len(cipherText) / 5)):
        return bestKey
    else:
        
        return None

    

def checkFitness(cipherText, nGramDict, floorDict):
    score = 0
    lengthKey = len(list(nGramDict.keys())[0])
    for i in range(len(cipherText) - (lengthKey - 1)):
        if (cipherText[i : i + lengthKey] in nGramDict):
            score += nGramDict[cipherText[i : i + lengthKey]]
        else :
            score += floorDict

    return score
    


def decryptedCheck(cipherText):
    count = 0
    longestWord = 12
    currentText = cipherText[0:longestWord]
    twoLetterWords = ["am", "an", "as", "at", "be", "by", "do", "go", "he", "if", "in", "is", "it", "me", "my", "of", "oh", "on", "or", "so", "to", "up", "us", "we"]
    lowerIndex = 0
    totalLettersChopped = 0;
    while (len(currentText) != 0):
        length = len(currentText) - 1
        i = length
        for i in range(length, -1, -1):
            if (len(currentText) > 2 and (currentText in words.words())):
                count += 1
                lowerIndex = i + totalLettersChopped + 1
                totalLettersChopped += len(currentText)
                if (lowerIndex + longestWord < len(cipherText)):
                    currentText = cipherText[lowerIndex: lowerIndex + longestWord]
                else:
                    currentText = cipherText[lowerIndex: len(cipherText)]
                break
            elif (currentText in twoLetterWords):
                count += 1
                lowerIndex = i + totalLettersChopped + 1
                totalLettersChopped += len(currentText)
                if (lowerIndex + longestWord < len(cipherText)):
                    currentText = cipherText[lowerIndex: lowerIndex + longestWord]
                else:
                    currentText = cipherText[lowerIndex: len(cipherText)]
                break
#            elif (currentText == "a" or currentText == "i"):
#                count += 1
#                lowerIndex = i + totalLettersChopped + 1
#                totalLettersChopped += len(currentText)
#                if (lowerIndex + longestWord < len(cipherText)):
#                    currentText = cipherText[lowerIndex: lowerIndex + longestWord]
#                else:
#                    currentText = cipherText[lowerIndex: len(cipherText)]
#                break
            else:
                currentText = currentText[0:i]
        lowerIndex = i + totalLettersChopped + 1
        if (i == 0 and (lowerIndex + longestWord < len(cipherText))):
            totalLettersChopped += 1
            currentText = cipherText[lowerIndex: lowerIndex + longestWord]
        elif (i == 0):
            totalLettersChopped += 1
            currentText = cipherText[lowerIndex: len(cipherText)]
    return count



def decrypt(cipherText, quadDict, floorQuad, triDict, floorTri, biDict, floorBi):
    print("Attempting decryption...")
    print()
    print("Before decryption: ", cipherText)
    print()
    cipherText = removeSpaces(cipherText)

    print("Checking for encryption using translation...")
    translationResult = findCaesarKey(cipherText)
    if (translationResult != None):
        print("Decryption successful using translation")
        print("Plain Text:")
        print(caesarDecypher(cipherText, translationResult))
        print("Final key:")
        print(translationResult)
        return
    else:
        print("Decryption using translation: Failed")

    print()
    print("Checking for encryption using substitution...")
    keyCount = 0
    plainText = ""
    finalGramKey = 0
    while(keyCount < (len(cipherText) / 5)):
        biGramKey = findSubstitutionKey(cipherText, biDict, floorBi, None)
        triGramKey = findSubstitutionKey(cipherText, triDict, floorTri, biGramKey)
        quadGramKey = findSubstitutionKey(cipherText, quadDict, floorQuad, triGramKey)
        quadGramKey1 = findSubstitutionKey(cipherText, quadDict, floorQuad, quadGramKey)
        quadGramKey2 = findSubstitutionKey(cipherText, quadDict, floorQuad, quadGramKey1)
        quadGramKey3 = findSubstitutionKey(cipherText, quadDict, floorQuad, quadGramKey2)
        finalGramKey = findSubstitutionKey(cipherText, quadDict, floorQuad, quadGramKey3)
        plainText = substitutionDecypher(cipherText, finalGramKey)
        keyCount = decryptedCheck(plainText)

    print("Decryption successful using substitution")
    print("Plain Text:")
    print(substitutionDecypher(cipherText, finalGramKey))
    print("Final key:")
    print(finalGramKey)
    return
    


main()

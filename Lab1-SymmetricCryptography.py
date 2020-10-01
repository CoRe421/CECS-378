import enchant
import random
from nltk.corpus import words

def main():
    problem1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
    #Key: 17, Text: whatisinanamearosebyanyothernamewouldsmellassweet
    problem2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
    #Key: 5, Text: therearetwothingstoaimatinlifefirsttogetwhatyouwantandafterthattoenjoyitonlythewisestofmankindachievethesecond
    problem3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
    #Key: TBD, Text: contrariwisecontinuedtweedledeeifitwassoitmightbeandifitweresoitwouldbebutasitisntitaintthatslogic
    problem4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"
    #Key: TBD, Text: sohewaxesinwealthnowisecanharmhimillnessoragenoevilcaresshadowhisspiritnoswordhatethreatensfromeveranenemyalltheworldwendsathiswillnoworseheknowethtillallwithinhimobstinatepridewaxesandwakeswhilethewardenslumbersthespiritssentrysleepistoofastwhichmastershismightandthemurderernearsstealthilyshootingtheshaftsfromhisbow
    print(problem1)
    #print(decryptedCheck(caesarDecypher(problem1, 16)))

    cipherText1 = removeSpaces(problem1)
    cipherText2 = removeSpaces(problem3)
    cipherText3 = removeSpaces(problem4)
    answer1 = substitutionDecypher(cipherText1, findSubstitutionKey(cipherText1))
    print()
    print(answer1)
    answer2 = substitutionDecypher(cipherText2, findSubstitutionKey(cipherText2))
    print()
    print(answer1)
    print(answer2)
    answer3 = substitutionDecypher(cipherText3, findSubstitutionKey(cipherText3))
    print()
    print(answer1)
    print(answer2)
    print(answer3)
    

def removeSpaces(cipherText):
    count = 0
    newText = ""
    for i in range(len(cipherText)):
        if (cipherText[i] != ' '):
            newText += cipherText[i]
            count += 1
    return newText

 
def decrypt(cipherText):
    cipherText = removeSpaces(cipherText)
    print("Before decryption: ", cipherText)
    for i in range(1, 26):
        print("Key: ", i, ", Plaintext: ", caesarDecypher(cipherText, i))
    return


def substitutionDecypher(cipherText, key):
    plainText = ""
    for i in range(len(cipherText)):
        plainText += key[key.index(cipherText[i])]
        
    return plainText


def findSubstitutionKey(cipherText):
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

    keyString = ""
    keyString = keyString.join(key)
    plainText = substitutionDecypher(cipherText, keyString)
    bestKeyCount = decryptedCheck(plainText)
    bestKey = key.copy()
    newKeyCount = 0
    firstRandLetterIndex = 0
    secondRandLetterIndex = 0
    temp = 'a'
    randDict = {"" : 0}
    
    while (bestKeyCount < len(cipherText) /  6):
        newKey = bestKey.copy()
        while (len(randDict) < 26 * 25):
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
            random.shuffle(bestKey)
            randDict.clear()   

        else:
            temp = newKey[firstRandLetterIndex]
            newKey[firstRandLetterIndex] = newKey[secondRandLetterIndex]
            newKey[secondRandLetterIndex] = temp
            newKeyString = ""
            newKeyString = newKeyString.join(newKey)
            newPlainText = substitutionDecypher(cipherText, newKeyString)
            newKeyCount = decryptedCheck(newPlainText)
            if (newKeyCount > bestKeyCount):
                bestKeyCount = newKeyCount
                bestKey = newKey
                randDict.clear()        
        
        
    return bestKey


def caesarDecypher(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = ""
    cipherText = removeSpaces(cipherText)
    for i in range(len(cipherText)):
        plainText += alphabet[(alphabet.index(cipherText[i]) + key) % 26]

    return plainText


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
#               break
            else:
                currentText = currentText[0:i]
        lowerIndex = i + totalLettersChopped + 1
        if (i == 0 and (lowerIndex + longestWord < len(cipherText))):
            totalLettersChopped += 1
            currentText = cipherText[lowerIndex: lowerIndex + longestWord]
        elif (i == 0):
            totalLettersChopped += 1
            currentText = cipherText[lowerIndex: len(cipherText)]
    print(count, end = " ")
    return count




main()

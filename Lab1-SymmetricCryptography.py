import enchant
import random
from nltk.corpus import words
from math import log10

def main():
    #Reads the files and creates dictionaries out of each of them.
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

    #Each problem for part 1 of the assignment.
    problem1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
    problem2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
    problem3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
    problem4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

    #Each phrase for part 2 of the assignment.
    part2Phrase1 = "He who fights with monsters should look to it that he himself does not become a monster. And if you gaze long into an abyss, the abyss also gazes into you."
    #Key: zyxwvutsrqponmlkjihgfedcba, Cipher: svdslurtsghdrgsnlmhgvihhslfowollpglrggszgsvsrnhvouwlvhmlgyvxlnvznlmhgvizmwrublftzavolmtrmglzmzybhhgsvzybhhzohltzavhrmglblf
    part2Phrase2 = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened."
    #Key: zyxwvutsrqponmlkjihgfedcba, Cipher: gsvivrhzgsvlibdsrxshgzgvhgszgruvevizmbylwbwrhxlevihvczxgobdszggsvfmrevihvrhulizmwdsbrgrhsvivrgdroormhgzmgobwrhzkkvzizmwyvivkozxvwybhlnvgsrmtvevmnlivyraziivzmwrmvckorxzyovgsvivrhzmlgsvigsvlibdsrxshgzgvhgszggsrhszhzoivzwbszkkvmvw
    part2Phrase3 = "Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off - then, I account it high time to get to sea as soon as I can."
    #Key: zyxwvutsrqponmlkjihgfedcba, Cipher: dsvmvevirurmwnbhvoutildrmttirnzylfggsvnlfgsdsvmvevirgrhzwznkwiraaobmlevnyvirmnbhlfodsvmvevirurmwnbhvourmelofmgzirobkzfhrmtyvulivxluurmdzivslfhvhzmwyirmtrmtfkgsvivziluvevibufmvizornvvgzmwvhkvxrzoobdsvmvevinbsbklhtvghfxszmfkkviszmwlunvgszgrgivjfrivhzhgilmtnlizokirmxrkovglkivevmgnvuilnwvoryvizgvobhgvkkrmtrmglgsvhgivvgzmwnvgslwrxzoobpmlxprmtkvlkovhszghluugsvmrzxxlfmgrgsrtsgrnvgltvgglhvzzhhllmzhrxzm

    #Prints the menu for the user
    print()
    print("What would you like to do?")
    print(" 1. Decrypt one of the base ciphers")
    print(" 2. Encrypt a text with a given substitution key / Decrpyt a given text with a given subsitution key")
    print(" 3. Exit")
    print()
    userInput = input()

    while (userInput != '3'):
        #If the user selects choice 1, another menu is printed.
        if (userInput == '1'):
            print("Which problem would you like do decypher?")
            print()
            print(" 1. Problem 1: ")
            print("   ", problem1)
            print()
            print(" 2. Problem 2:")
            print("   ", problem2)
            print()
            print(" 3. Problem 3:")
            print("   ", problem3)
            print()
            print(" 4. Problem 4:")
            print("   ", problem4)
            print()
            print(" 5. Back to menu")
            print()
            userInput = input()
            while (userInput != '5'):
                cipherText = ""
                
                #If the user selects choice 1, the set cipherText is set to problem 1.
                if (userInput == '1'):
                    cipherText = problem1
                    
                #If the user selects choice 1, the set cipherText is set to problem 2.
                elif (userInput == '2'):
                    cipherText = problem2
                    
                #If the user selects choice 1, the set cipherText is set to problem 3.
                elif (userInput == '3'):
                    cipherText = problem3
                    
                #If the user selects choice 1, the set cipherText is set to problem 4.
                elif (userInput == '4'):
                    cipherText = problem4

                #If the user selects none of the choices, the menu is reprinted.
                else:
                    print("Your input was not understood.")
                    print()
                    print("Which problem would you like do decypher?")
                    print()
                    print(" 1. Problem 1: ")
                    print("   ", problem1)
                    print()
                    print(" 2. Problem 2:")
                    print("   ", problem2)
                    print()
                    print(" 3. Problem 3:")
                    print("   ", problem3)
                    print()
                    print(" 4. Problem 4:")
                    print("   ", problem4)
                    print()
                    print(" 5. Back to menu")
                    print()
                    userInput = input()
                    continue

                #If a selection is chosen correctly, the function is called and the cipher is decrypted.
                decrypt(cipherText, quadDict, floorQuad, triDict, floorTri, biDict, floorBi)

                #After decryption, the menu is reprinted.
                print("Which problem would you like do decypher?")
                print()
                print(" 1. Problem 1: ")
                print("   ", problem1)
                print()
                print(" 2. Problem 2:")
                print("   ", problem2)
                print()
                print(" 3. Problem 3:")
                print("   ", problem3)
                print()
                print(" 4. Problem 4:")
                print("   ", problem4)
                print()
                print(" 5. Back to menu")
                print()
                userInput = input()

        #If the user selects choice 2, another menu is printed.                
        elif (userInput == '2'):
            print("Are you looking to:")
            print(" 1. Encrypt a text")
            print(" 2. Decrypt a given cipher")
            print(" 3. Back to menu")
            userInput = input()
            
            while (userInput != '3'):

                #If the user selects choice 1, another menu is printed.
                if (userInput == '1'):
                    print("Which phrase do you want to encrypt?: ")
                    print()
                    print(" 1. ", part2Phrase1)
                    print()
                    print(" 2. ", part2Phrase2)
                    print()
                    print(" 3. ", part2Phrase3)
                    print()
                    print(" 4. Back to menu.")
                    print()
                    userInput = input()
                    while (userInput != '4'):
                        plainText = ""

                        #If the user selects choice 1, the set plainText is set to phrase 1. 
                        if (userInput == '1'):
                            plainText = part2Phrase1

                        #If the user selects choice 1, the set plainText is set to phrase 2.
                        elif (userInput == '2'):
                            plainText = part2Phrase2

                        #If the user selects choice 1, the set plainText is set to phrase 3.
                        elif (userInput == '3'):
                            plainText = part2Phrase3
                            
                        #If the user selects none of the choices, the menu is reprinted.
                        else:
                            print("Your input was not understood.")
                            print()
                            print("Which phrase do you want to encrypt?: ")
                            print()
                            print(" 1. ", part2Phrase1)
                            print()
                            print(" 2. ", part2Phrase2)
                            print()
                            print(" 3. ", part2Phrase3)
                            print()
                            print(" 4. Back to menu.")
                            print()
                            userInput = input()
                            continue

                        #If a selection is chosen correctly, the user is then asked for their key to encrypt.
                        print()
                        print("What key would you like to use?")
                        print("  Rules:")
                        print("    1. The key must be 26 letters long")
                        print("    2. The key must consist of only alphabetic characters")
                        print("    3. The key must have no repeat characters")
                        print("          abcdefghijklmnopqrstuvwxyz")
                        userKey = input("Your key: ")
                        print()
                        print("Encrypting...")
                        print()
                        plainText = removeNonAlphChars(plainText)

                        #The function is called and the cipher is decrypted.
                        userCipher = substitutionEncrypt(plainText, userKey)

                        #After encryption, the menu is reprinted.
                        print("Your cipher is: ", userCipher)
                        print()
                        print("Using key: ", userKey)
                        print()
                        print("Which phrase do you want to encrypt?: ")
                        print()
                        print(" 1. ", part2Phrase1)
                        print()
                        print(" 2. ", part2Phrase2)
                        print()
                        print(" 3. ", part2Phrase3)
                        print()
                        print(" 4. Back to menu.")
                        print()
                        userInput = input()

                    #After a choice is completed, the menu is reprinted.
                    print()
                    print("Are you looking to:")
                    print(" 1. Encrypt a text")
                    print(" 2. Decrypt a given cipher")
                    print(" 3. Back to menu")
                    print()
                    userInput = input()

                #If the user selects choice 2, the user is asked what encrypted message to decrypt.
                elif (userInput == '2'):
                    print("What cipher would you like to decrypt?")
                    cipherText = input("Cipher: ")
                    print()

                    #The user is then asked what key to decrypt the cipherText with.
                    print("What key would you like to use?")
                    print("  Rules:")
                    print("    1. The key must be 26 letters long")
                    print("    2. The key must consist of only alphabetic characters")
                    print("    3. The key must have no repeat characters")
                    print("          abcdefghijklmnopqrstuvwxyz")
                    userKey = input("Your key: ")
                    print()
                    print("Decrypting...")
                    print()
                    cipherText = removeNonAlphChars(cipherText)

                    #The function is called and the cipher is decrypted.
                    userPlainText = substitutionDecypher(cipherText, userKey)

                    #After decryption, the menu is reprinted.
                    print("Using key: ", userKey)
                    print()
                    print("Your text is: ", userPlainText)
                    print()
                    print("Which phrase do you want to encrypt?: ")
                    print()
                    print("Are you looking to:")
                    print(" 1. Encrypt a text")
                    print(" 2. Decrypt a given cipher")
                    print(" 3. Back to menu")
                    print()
                    userInput = input()
                    
                #If the user selects none of the choices, the menu is reprinted.
                else:
                    print("Your input was not understood.")
                    print("Which phrase do you want to decrypt?: ")
                    print()
                    print("Are you looking to:")
                    print(" 1. Encrypt a text")
                    print(" 2. Decrypt a given cipher")
                    print(" 3. Back to menu")
                    print()
                    userInput = input()
                    continue
                

        #If the user selects none of the choices, the menu is reprinted.           
        else:
            print("Your input was not understood.")
            print()
            print("What would you like to do?")
            print(" 1. Decrypt one of the base ciphers")
            print(" 2. Encrypt a text with a given substitution key / Decrpyt a given text with a given subsitution key")
            print(" 3. Exit")
            print()
            userInput = input()

        #After a choice is completed, the menu is reprinted.
        print()
        print("What would you like to do?")
        print(" 1. Decrypt one of the base ciphers")
        print(" 2. Encrypt a text with a given substitution key / Decrpyt a given text with a given subsitution key")
        print(" 3. Exit")
        print()
        userInput = input()

    print()
    print("Thank you! Have a good day!")
    
    

#Removes all characters from the string that are not letters in the alphabet.
#Returns the modified string.
def removeNonAlphChars(cipherText):
    newText = ""
    for i in range(len(cipherText)):
        if (cipherText[i].isalpha()):
            newText += cipherText[i]
    return newText


#Encrypts a given string through substitution using a given key.
#Returns the encrypted string.
def substitutionEncrypt(plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = plainText.lower()
    cipherText = ""

    #Increments through the plain text, placing the new letters from the key into the cipher text.
    for i in range(len(plainText)):
        cipherText += key[alphabet.index(plainText[i])]
    
    return cipherText


#Decrypts a given string through substitution using a given key.
#Returns the decrypted string.
def substitutionDecypher(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipherText = cipherText.lower()
    plainText = ""

    #Increments through the cipher text, placing the new letters from the key into the plain text.
    for i in range(len(cipherText)):
        plainText += key[alphabet.index(cipherText[i])]
    
    return plainText


#Attempts to find the substitution key for a given ciphertext, using either bi, tri, or quadgram analysis.
#Has the option for a baseKey to be included, otherwise creates a new key based on letter frequency analysis.
#Returns the key with the highest fitness that it could calculate.
def findSubstitutionKey(cipherText, nGramDict, floorDict, baseKey):

    #If no baseKey is given, calculates a new key as a list through letter frequency analysis.
    if (baseKey == None):
        mostFrequentLetters = "etaoinshrdlcumwfgypbvkjxqz"
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        commonLetters = [0] * 26
        key = ['a'] * 26

        #Increments through the cipher text, adding one to the index where the letter's respective place in the alphabet would be.
        for i in range(len(cipherText)):
            commonLetters[alphabet.find(cipherText[i])] += 1

        #Increments through the given string of most frequent letters in the english language, adding it's letters to the new key in the index's of the most frequent letters in the cipher text.
        for i in range(len(mostFrequentLetters)):
            maxFound = -1
            index = 0
            for j in range(len(commonLetters)):
                if (commonLetters[j] > maxFound):
                    maxFound = commonLetters[j]
                    index = j
            key[index] = mostFrequentLetters[i]
            commonLetters[index] = -1

    #If a baseKey is given, uses that as the key.
    else:
        key = list(baseKey)
    
    #Converts the key into a string to be used in other functions.
    keyString = ""
    keyString = keyString.join(key)

    #Performs the first decrpytion using the key.
    plainText = substitutionDecypher(cipherText, keyString)

    #Sets the best values to the base values.
    bestKeyCount = 0 
    bestKey = key.copy()

    #Calculates the fitness of the first decryption using ngram analyis and sets it to the best fitness of this attempt.
    bestTextFitness = checkFitness(plainText, nGramDict, floorDict)

    #Sets the best fitness and the best key of this function call as the best fitness and key of this attempt.
    totalBestFitness = bestTextFitness
    totalBestKey = bestKey.copy()

    #Sets the base values.
    newKeyCount = 0
    firstRandLetterIndex = 0
    secondRandLetterIndex = 0
    temp = 'a'
    randDict = {}
    attempts = 0

    #Loops through this, and if there is no improvement in 10 attempts then it exits the loop.
    while(attempts < 10):

        #Loops until the dictionary of random combination of letters has filled and tried every single combination.
        while (len(randDict) != 26 * 25):

            #Sets the key of this iteration to the best key of this attempt.
            newKey = bestKey.copy()

            #Loops until it finds a combination of two random letters to switch that haven't been found yet.
            while ((len(randDict) < 26 * 25)):
                
                randPair = ""

                #Generates two random letter indexes.
                firstRandLetterIndex = random.randrange(0, 26, 1)
                secondRandLetterIndex = random.randrange(0, 26, 1)

                #If the indexes are the same, increments the second by one.
                if (firstRandLetterIndex == secondRandLetterIndex):
                    secondRandLetterIndex = (secondRandLetterIndex + 1) % 26

                #Creates the pair, and then checks if that pair has been attempted yet.
                randPair += str(firstRandLetterIndex)
                randPair += " "
                randPair += str(secondRandLetterIndex)
                if (not(randPair in randDict)):
                    randDict[randPair] = 0
                    break

            #Breaks out of the loop if the max combinations has been reached this attempt.
            if (len(randDict) == 26 * 25):
                break

            #Otherwise, switches the letters at the random indexes. and calculates the fitness of this new key.
            else:
                temp = newKey[firstRandLetterIndex]
                newKey[firstRandLetterIndex] = newKey[secondRandLetterIndex]
                newKey[secondRandLetterIndex] = temp
                newKeyString = ""
                newKeyString = newKeyString.join(newKey)
                newPlainText = substitutionDecypher(cipherText, newKeyString)

                #Calculates the fitness of the plain text with the new key.
                newTextFitness = checkFitness(newPlainText, nGramDict, floorDict)

                #If the new fitness is greater than the best fitness this attempt, sets the best fitness to this new fitness, sets the best key to this new key, and starts again with a clear random letter combination dictionary.
                if (newTextFitness > bestTextFitness):
                    bestTextFitness = newTextFitness
                    bestKey = newKey.copy()
                    randDict.clear()

        #When the dictionary has been filled of all possible combinations, the loop is left and that plaintext is as decrypted as it will get this attempt.

        #If this attempt's fitness is greater than the best fitness this function call, sets the total best fitness to this best fitness, sets the total best key to this attempt's best key, and resets the attempts to 0.
        if (bestTextFitness > totalBestFitness):
            totalBestFitness = bestTextFitness
            totalBestKey = bestKey.copy()
            attempts = 0

            #If there was no base key given, randomizes the best key.
            if (baseKey == None):
                random.shuffle(bestKey)

            #If a base key was given, resets the key to that value.
            else:
                bestKey = list(baseKey)

            #Sets the best fitness to an arbitrarily low value and clears the random letter combination dictionary.
            bestTextFitness = -100000
            randDict.clear()

        #Otherwise, increments the attempts.
        else:
            attempts += 1

            #If there was no base key given, randomizes the best key.
            if (baseKey == None):
                random.shuffle(bestKey)

            #If a base key was given, resets the key to that value.
            else:
                bestKey = list(baseKey)

            #Sets the best fitness to an arbitrarily low value and clears the random letter combination dictionary.
            bestTextFitness = -100000
            randDict.clear()

    #Returns the key with the highest key that it could calculate.
    return totalBestKey


#Decrypts a given string through translation using a given key.
#Returns the decrypted string.
def caesarDecypher(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = ""
    cipherText = removeNonAlphChars(cipherText)
    for i in range(len(cipherText)):
        plainText += alphabet[(alphabet.index(cipherText[i]) + key) % 26]

    return plainText

#Attempts to find the translation key for a given cipher text.
#Returns the key that it thinks decrypted the text, or no key at all.
def findCaesarKey(cipherText):
    bestKey = 0

    #Calculates the amount of english words in this cipher text.
    bestCount = decryptedCheck(cipherText)

    #Increments through all 25 keys that are possible using translation.
    for key in range(1, 26):

        #Decrypts the cipher text with the current key.
        plainText = caesarDecypher(cipherText, key)

        #Calculates the amount of english words in this cipher text.
        newCount = decryptedCheck(plainText)

        #If this count of words is higher than the best, sets this value to the highest and this key to the best.
        if (newCount > bestCount):
            bestKey = key
            bestCount = newCount

    #Determines that if the amount of words is greater than the length of the cipher text divided by 5, the cipher text is successfully decrypted.
    if (bestCount > (len(cipherText) / 5)):
        return bestKey

    #Otherwise, returns none.
    else:   
        return None

    
#Determines the fitness of the current cipher text, using the given ngram dictionary and floor values.
#Returns the fitness as an int.
def checkFitness(cipherText, nGramDict, floorDict):
    score = 0

    #Calculates the type of ngram being used: either bi, tri, or quad.
    lengthKey = len(list(nGramDict.keys())[0])

    #Increments through the range of the cipher text, calculating all bi, tri, or quadgrams and adding their respective score to the total.
    for i in range(len(cipherText) - (lengthKey - 1)):
        if (cipherText[i : i + lengthKey] in nGramDict):
            score += nGramDict[cipherText[i : i + lengthKey]]
        else :
            score += floorDict

    #Returns the fitness as an int.
    return score
    

#Calculates the number of english words in the given cipher text.
#Returns the number of words found in the cipher text as an int.
def decryptedCheck(cipherText):
    count = 0

    #Creates a value, currentText, that is the substring of letters being analyzed.
    #Only checks a maximum of 12 letters at a time in order to save time, assuming there will be no words in the text longer than 12 characters.
    longestWord = 12
    currentText = cipherText[0:longestWord]
    twoLetterWords = ["am", "an", "as", "at", "be", "by", "do", "go", "he", "if", "in", "is", "it", "me", "my", "of", "oh", "on", "or", "so", "to", "up", "us", "we"]
    lowerIndex = 0
    totalLettersChopped = 0;

    #The function keeps running while there is more of the current text to analyze.
    while (len(currentText) != 0):

        #Starts from the end of the current text
        length = len(currentText) - 1
        i = length

        #Increments downwards from the length of the current text.
        for i in range(length, -1, -1):

            #If the current text is larger than 2 characters and also a word, incremeents the count and moves the current text.
            if (len(currentText) > 2 and (currentText in words.words())):
                count += 1
                lowerIndex = i + totalLettersChopped + 1

                #Keeps track of the total amount of characters chopped in order to increment through the cipher text.
                totalLettersChopped += len(currentText)
                
                #Determines if there are more than 12 letters in the cipher text, only creating the current text from what's left over otherwise.
                if (lowerIndex + longestWord < len(cipherText)):
                    currentText = cipherText[lowerIndex: lowerIndex + longestWord]
                else:
                    currentText = cipherText[lowerIndex: len(cipherText)]
                break

            #If the current text is in the given list of two letter words, incremeents the count and moves the current text.
            elif (currentText in twoLetterWords):
                count += 1
                lowerIndex = i + totalLettersChopped + 1

                #Keeps track of the total amount of characters chopped in order to increment through the cipher text.
                totalLettersChopped += len(currentText)

                #Determines if there are more than 12 letters in the cipher text, only creating the current text from what's left over otherwise.
                if (lowerIndex + longestWord < len(cipherText)):
                    currentText = cipherText[lowerIndex: lowerIndex + longestWord]
                else:
                    currentText = cipherText[lowerIndex: len(cipherText)]
                break

#This block of code used to check if the last letter was either an a or an i, incrementing the count and moving the current text if it was.
#However, this proved to provide more false positives than successful identifications, and so it was removed.
            
#            elif (currentText == "a" or currentText == "i"):
#                count += 1
#                lowerIndex = i + totalLettersChopped + 1
#                totalLettersChopped += len(currentText)
#                if (lowerIndex + longestWord < len(cipherText)):
#                    currentText = cipherText[lowerIndex: lowerIndex + longestWord]
#                else:
#                    currentText = cipherText[lowerIndex: len(cipherText)]
#                break

            #If no words have been found, decrements the current text.
            else:
                currentText = currentText[0:i]

        lowerIndex = i + totalLettersChopped + 1

        #If there were no letters found in the current text, cops the leftmost letter from the current text and then increments it by 1 if there is space to in the cipher .
        if (i == 0 and (lowerIndex + longestWord < len(cipherText))):
            totalLettersChopped += 1
            currentText = cipherText[lowerIndex: lowerIndex + longestWord]

        #Otherwise, ff there were no letters found in the current text, increments the current text and creates it from what is left of the cipher text.
        elif (i == 0):
            totalLettersChopped += 1
            currentText = cipherText[lowerIndex: len(cipherText)]

    #Returns the number of words found in the cipher text as an int.
    return count


#Uses all known methods of decryption in order to decrypt the given cipher text.
def decrypt(cipherText, quadDict, floorQuad, triDict, floorTri, biDict, floorBi):
    print("Attempting decryption...")
    print()
    print("Before decryption: ", cipherText)
    print()
    cipherText = removeNonAlphChars(cipherText)

    print("Checking for encryption using translation...")

    #Attempts to calculate the key using translation, printing and returning from the function if successful.
    translationResult = findCaesarKey(cipherText)
    if (translationResult != None):
        print("Decryption successful using translation")
        print("Plain Text:")
        print(caesarDecypher(cipherText, translationResult))
        print("Final key:")
        print(translationResult)
        return

    #If not successful, the function continues with substitution decryption.
    else:
        print("Decryption using translation: Failed")

    print()
    print("Checking for encryption using substitution...")
    keyCount = 0
    plainText = ""
    finalGramKey = 0

    #Continues to decrypt the text until a key is found in which the amount of words are greater than the length of the cipher text divided by 5.
    while(keyCount < (len(cipherText) / 5)):

        #Uses a combination of function calls that I have found to be most effective.
        biGramKey = findSubstitutionKey(cipherText, biDict, floorBi, None)
        triGramKey = findSubstitutionKey(cipherText, triDict, floorTri, biGramKey)
        quadGramKey = findSubstitutionKey(cipherText, quadDict, floorQuad, triGramKey)
        quadGramKey1 = findSubstitutionKey(cipherText, quadDict, floorQuad, quadGramKey)
        quadGramKey2 = findSubstitutionKey(cipherText, quadDict, floorQuad, quadGramKey1)
        quadGramKey3 = findSubstitutionKey(cipherText, quadDict, floorQuad, quadGramKey2)
        finalGramKey = findSubstitutionKey(cipherText, quadDict, floorQuad, quadGramKey3)
        plainText = substitutionDecypher(cipherText, finalGramKey)
        keyCount = decryptedCheck(plainText)

    #Prints the decrypted text and returns from the function.
    print("Decryption successful using substitution")
    print("Plain Text:")
    print(substitutionDecypher(cipherText, finalGramKey))
    print("Final key:")
    print(finalGramKey)
    return
    

#Calls the main funciton.
main()

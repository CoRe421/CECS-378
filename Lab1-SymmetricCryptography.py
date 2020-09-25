import enchant
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
    print(decryptedCheck(caesarDecypher(problem1, 1)))

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
    return


def caesarDecypher(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = ""
    cipherText = removeSpaces(cipherText)
    for i in range(len(cipherText)):
        plainText += alphabet[(alphabet.index(cipherText[i]) + key) % 26]

    return plainText


def decryptedCheck(cipherText):
    count = 0
    currentText = ""
    
    for i in range(len(cipherText)):
        currentText += cipherText[i]
        print(currentText)
        if (currentText in words.words()):
            count += 1
            currentText = ""
            
    return count




main()

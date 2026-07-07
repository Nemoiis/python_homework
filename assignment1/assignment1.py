# Write your code here.
def sayHello():
    return "Hello"

def greeting(name):
    greeting = f"Hello {name}"
    return greeting

def calc(num1, num2, op="multiply"):

    try:
        match op:
            case "add":
                return num1 + num2
        
            case "subtract":
                return num1 - num2
        
            case "multiply":
                return num1 * num2

            case "divide":
                try:
                    return num1 / num2
                except ZeroDivisionError:
                    return "You can't divide by 0!"
        
            case "modulo":
                try:
                    return num1 % num2
                except ZeroDivisionError:
                    return "You can't divide by 0!"
                
            case "int_divide":
                try:
                    return num1 // num2
                except ZeroDivisionError:
                    return "You can't divide by 0!"
        
            case "power":
                return num1 ** num2
    except TypeError:
        return(f"You can't {op} Those Values")
    





def data_type_conversion(val, dataType):
    match dataType:
        case "float":
            try:
                return(float(val))
            except ValueError:
                return(f"You cant convert {val} into a {dataType}")

        case "str":
            return(str(val))

        case "int":
            try:
                return(int(val))
            except ValueError:
                return(f"You cant convert {val} into a {dataType}")


def grade(*args):
    try:
        avg = sum(args)/len(args)
    except TypeError:
        return "Invalid Data"
    match avg:
        case a if avg >= 90:
            return "A"
        
        case a if avg >= 80 and avg <= 89:
            return "B"
        
        case a if avg >= 70 and avg <= 79:
            return "C"
        
        case a if avg >= 60 and avg <= 69:
            return "D"
        
        case a if avg < 60:
            return "F"
        
def repeat(string, count):
    newString =""
    for i in range(count):
        newString += string

    return newString

def student_scores(pos,**kwargs):
    if pos == "best":
        topScore = 0
        topScorer = ""
        for key,value in kwargs.items():
            if value > topScore:
                topScore = value
                topScorer = str(key)   
        return topScorer
    
    elif pos == "mean":
        counter = 0
        total = 0
        
        for key,value in kwargs.items():
            total = total + value
            counter = counter + 1
        avg = total/counter
        return avg
    
def titleize(title):
    words = title.split()
    littleWords = ["a", "on", "an", "the", "of", "and", "is", "in"]

    for i, word in enumerate(words):
        if word in littleWords and i != 0 and i != len(words) - 1:
            continue
        else:
            words[i] = word.capitalize()

    title = " ".join(words)
    return title
    
def hangman(secret, guess):
    print ("_" * len(secret))
    results = ""


    for char in secret:
        if char in guess:
            results += char
        
        else:
            results += "_"
        
    return results

def pig_latin(string):
    vowels ="aeiou"
    consonants = "bcdfghjklmnprstuvwxyz"
    words = string.split()
    newPhrase = ""

    for word in words:
        if word[0] in vowels:
            newPhrase += word + "ay "

        elif word[0] not in vowels and word[0] not in consonants:
            word = word[2:]
            alteredword = word + "quay "
            newPhrase += alteredword

        elif word[0] not in vowels:
            ending =""
            newWord = ""
            for i,char in enumerate(word):
                if char not in vowels:
                    ending += char
                
                elif char in vowels:
                    word = word[i:]
                    newWord = word + ending + "ay "
                    newPhrase += newWord
                    break
    
            if ending == word:
                newPhrase += ending + "ay "

    return(newPhrase)










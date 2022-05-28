import string

def read_file_content(filename):
    fileContent = open(filename, "r")
    return fileContent

def count_words():
    text = read_file_content("./story.txt")
    dictionary = {}
    for line in text:
        line = line.strip()
        line = line.lower()
        
        line = line.translate(line.maketrans("," "", string.puntuation))
        words = line.split()
        
        for word in words:
            if word in dictionary:
                dictionary[word] +=1
            else:
                dictionary[word] = 1
        for key in list(dictionary.keys()):
            print(f"{{\"{key}\": {dictionary[key]}}}, ", end=" ")   
    
count_words

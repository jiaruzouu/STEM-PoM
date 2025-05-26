from bs4 import BeautifulSoup
import os 
import spacy

#load the model from spacy
nlp = spacy.load("en_core_web_sm")

def split_into_sentences(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract sentences and store them in a list
    sentences = [sent.text for sent in doc.sents]
    
    return sentences

def get_file_path(database_path):
    file_paths = []
    words = []
    attributes = []
    title = True 
    # key_content = []
    with open(database_path, 'r',encoding='utf-8') as file:
        for line in file:
            if not title:
                elements = line.split()
                if elements:
                    file_paths.append(elements[0])
                    words.append(elements[2])
                    attributes.append(elements[3] + " " + elements[4])
                    # index = line.rfind("     ") + 5
                    # combined_string = ''.join(line[index:])
                    # key_content.append(combined_string)
            title = False
    return file_paths, words, attributes

def get_sentence(input_file, target_word, length,single_sentence):
    infile = open(input_file, "r", encoding='utf-8')
    soup = BeautifulSoup(infile, 'html.parser')


    for data in soup(['annotation', 'script']):
        data.decompose()

    parsed_sentence = " ".join(soup.stripped_strings)
    if single_sentence:
        #option 1: split sentences using spacy model
        # sentences = split_into_sentences(parsed_sentence)
        #option 2: split sentences by '.'
        sentences = parsed_sentence.split('.')
        for sentence in sentences:
            idx = 0
            sentence = sentence.replace('\n', '')
            for word in sentence:
                idx += 1
                if target_word == word:
                    if (idx - length < 0 and idx + length > len(sentence)):
                        return sentence
                    elif (idx - length < 0):
                        return sentence[1: idx + length]
                    elif (idx - length > len(sentence)):
                        return sentence[idx - length: len(sentence)]
                    return sentence[idx - length: idx + length]
    else: 
        idx = 0
        parsed_sentence = parsed_sentence.replace('\n', '')
        for word in parsed_sentence:
            idx += 1
            if target_word == word:
                return parsed_sentence[idx - length: idx + length]
    return "Target variable not found in this file"

def modify_database(database_path,length,single_sentence):
    file_paths, words, attributes = get_file_path(database_path)
    # print(file_paths,words)
    with open(database_path, 'r',encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(len(file_paths)):
            new_sentence = get_sentence(file_paths[i],words[i],length,single_sentence)
            # print(new_sentence)
            index = lines[i+1].rfind("    ") + 5
            lines[i+1] = lines[i+1][:index] + new_sentence + '\n'
            # print("new lines is:", lines[i+1])
        with open(database_path, 'w',encoding='utf-8') as file:
            file.writelines(lines)



if __name__ == "__main__":
    database_path = 'test_database_demo.txt'
    length = 100
    single_sentence = False
    modify_database(database_path,length,single_sentence)

    # target_word = "𝑧"
    # input_file = "./0001/astro-ph0001008.html"
    # sentence = get_sentence(input_file,target_word,length)
    # print(sentence)

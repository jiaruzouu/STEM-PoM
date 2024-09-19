from bs4 import BeautifulSoup
import bs4
import os

# a helper function to remore all text in file
def clear_file(to_delete):
    open(to_delete, 'w').close()

# a helper function that return all filenames in given path
def get_filenames(input_address):
    file_list = []
    for filename in os.listdir(input_address):
        file_list.append(input_address + "/" + filename)
    return file_list


# the main function that extract all math tokens in a file
def extract(input_file, output_file):
    infile = open(input_file, "r", encoding='utf-8')
    soup = BeautifulSoup(infile, 'lxml')
    all_vars = soup.find_all("ci")
    for variables in all_vars:
        # open the file that we need to write to in append byte mode
        with open(output_file, "ab") as f:
            var_str = variables.string
            if var_str:
                f.write(var_str.encode('utf-8'))
                f.write("\n".encode('utf-8'))
    infile.close()


# the main function that extract all math tokens in a file
def extract_list(input_file):
    output_list = []
    infile = open(input_file, "r", encoding='utf-8')
    soup = BeautifulSoup(infile, 'lxml')
    all_vars = soup.find_all("ci")
    for variables in all_vars:
        # open the file that we need to write to in append byte mode
        var_str = variables.string
        if var_str not in output_list:
            output_list.append(var_str)
    infile.close()
    return output_list

# the function that output prettified file for visual
def prettify_files(input_file, output_file):
    infile = open(input_file, "r", encoding='utf-8')
    soup = BeautifulSoup(infile, 'lxml')
    with open(output_file, "wb") as f:
        f.write(soup.prettify().encode())
    infile.close()

# the function to remove all duplicated tokens in file
def clear_duplicate(input_file):
    clear_file(input_file)

def remove_duplicate(input_file):
    variable_list = []
    with open(input_file, "rb") as in_file:
        for line in in_file:
            if line in variable_list:
                continue
            else:
                variable_list.append(line)
    
    with open(input_file, "wb") as rewrite_file:
        rewrite_file.writelines(variable_list)


def first_word(input_file, target_word):
    infile = open(input_file, "r", encoding='utf-8')
    soup = BeautifulSoup(infile, 'html.parser')
    text = soup.get_text()
    
    # print(text.encode('utf-16'))
    # print(target_word.encode('utf-8'))
    #print(sentences)


    # problems I've met during this process
    # 1: unlike normal texts, mathmatical symbols cannot use for ... in ... to search
    # solution: instead search for the matching one word at a time until we find a match or reach the end
    # 2: the origional text is messed up with parser contents and annotations 
    # solution : we have to clean them up first, I used stripping to remove them
    # 3: sentence index out of bound
    # solution : some if conditions


    for data in soup(['annotation', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    parsed_sentence = " ".join(soup.stripped_strings)
    sentences = parsed_sentence.split('.')
    for sentence in sentences:
        idx = 0
        sentence = sentence.replace('\n', '')
        for word in sentence:
            idx += 1
            if target_word == word:
                if (idx - 50 < 0 and idx + 50 > len(sentence)):
                    return sentence
                elif (idx - 50 < 0):
                    return sentence[1: idx + 50]
                elif (idx - 50 > len(sentence)):
                    return sentence[idx - 50: len(sentence)]
                return sentence[idx - 50: idx + 50]
    return "Target variable not found in this file"


# individual test of each function
# open the folder that contains all the input files
input_address = "testFiles"
inputs = get_filenames(input_address)
"""
output_address = "variables"
outputs = get_filenames(output_address)
pretty_address = "prettify"
pretty = get_filenames(pretty_address)
"""
count = 0
while count < len(inputs):
    
    # call the extract function for all files
    # extract_list(inputs[count])
    # remove_duplicate(outputs[count])
    #out = first_word(inputs[count], "𝐴")
    #print(out)
    # save this line for clear outputs
    # clear_duplicate(outputs[count])
    # prettify_files(inputs[count], pretty_address[count])
    count += 1


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
# Importing the HTTP library
import requests as req
from tqdm import tqdm
#from extract import filename 
import os 
import sys

close_list = os.listdir('/Users/zourubin/Desktop/kani/parser/dataset')
data = pd.read_csv('/Users/zourubin/Desktop/kani/parser/example.csv')
var = data["var"]
txt = data["context"]
f = open("/Users/zourubin/Desktop/kani/parser/testresult.out", 'w')
print('The ouput of researching for dataset',file = f)
#print(close_list)
for secondlist in close_list:
    
    dir_list = os.listdir('/Users/zourubin/Desktop/kani/parser/dataset/'+secondlist+'/')
    #print (dir_list)
    print('---------------START WITH EXTRATING:',secondlist)
    for filename in tqdm(dir_list):
        #print(filename)
    #filename = 'dataset/astro-ph0001008.html'
        html = open('/Users/zourubin/Desktop/kani/parser/dataset/'+secondlist+'/'+filename,'r')
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)


        file_ = open('/Users/zourubin/Desktop/kani/parser/output/'+filename+"output.txt", "a")
        print(text, file=file_)
        file_.close()
    print('---------------FINISH EXTRATING:',secondlist)

    output_dir_list = os.listdir('/Users/zourubin/Desktop/kani/parser/output/')

    print("---------------START SEARCHING",secondlist)

    print('------------------------------------FILE REPO:',secondlist,'--------------------------------',file = f) 
    for output_filename in tqdm(output_dir_list):
        for string in txt:
        #print('Hi, Im seachnig file now:',output_filename)
            with open('/Users/zourubin/Desktop/kani/parser/output/'+output_filename, 'r') as fp:
                #print('the string for searching is:',string)
                # read all lines in a list
                lines = fp.readlines()
                common_linenumber = []
                for line in lines:
                    # check if string present on a current line
                    if line.find(string) != -1:
                        linenumber1 = lines.index(line)
                        print(string, ':string exists in file',file = f)
                        print('Line Number:', linenumber1,file = f)
                        print('Line:', line,file = f)
                        print(output_filename,file = f)
                        
    #compare the entries of each word and only leave the result that all strings share the same entry

    #delete the current file repo for sacing memory
    delete_list = os.listdir('/Users/zourubin/Desktop/kani/parser/output/')
    for delete_filename in delete_list:
        os.remove('/Users/zourubin/Desktop/kani/parser/output/'+delete_filename)
    
    print('---------------DONE WITH SEARCHING',secondlist)
                
f.close()


# # # word1 = 'On the other hand' 
# # # word2 = 'we have'

# # # with open(r'output.txt', 'r') as fp:
# # #     # read all lines in a list
# # #     lines = fp.readlines()
# # #     common_linenumber = []
# # #     for line in lines:
# # #         linenumber1 = -1
# # #         linenumber2 = -2
# # #         # check if string present on a current line
# # #         if line.find(word1) != -1:
# # #             linenumber1 = lines.index(line)
# # #             print(word1, 'string exists in file')
# # #             print('Line Number:', linenumber1)
# # #             print('Line:', line)
  
# # #         if line.find(word2) != -1:
# # #             linenumber2 = lines.index(line)
# # #             print(word2, 'string exists in file')
# # #             print('Line Number:', linenumber2)
# # #             print('Line:', line)

# # #         if linenumber1 == linenumber2: common_linenumber.append(linenumber1)

# # # print('common line number are:',common_linenumber)

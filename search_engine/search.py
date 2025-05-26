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

close_list = os.listdir('/projects/kani-lab/corpus/arXivML_np/')
data = pd.read_csv('/home/jiaruz2/extract/MDTE.csv')
var = data["var"]
txt = data["context"]
f = open("/home/jiaruz2/extract/test.out", 'w')
print('The ouput of researching for dataset',file = f)
#print(close_list)
for secondlist in close_list:
    
    dir_list = os.listdir('/projects/kani-lab/corpus/arXivML_np/'+secondlist+'/')
    #print (dir_list)
    print('---------------START WITH EXTRATING:',secondlist)
    for filename in dir_list:
        #print(filename)
    #filename = 'dataset/astro-ph0001008.html'
        html = open('/projects/kani-lab/corpus/arXivML_np/'+secondlist+'/'+filename,'r')
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


        file_ = open('/home/jiaruz2/extract/output/'+filename+"output.txt", "a")
        print(text, file=file_)
        file_.close()
    print('---------------FINISH EXTRATING:',secondlist)

    output_dir_list = os.listdir('/home/jiaruz2/extract/output/')

    print("---------------START SEARCHING",secondlist)

    print('------------------------------------FILE REPO:',secondlist,'--------------------------------',file = f)
    for output_filename in output_dir_list:
        for string in txt:
            #print('seachnig file now:',output_filename)
            with open('/home/jiaruz2/extract/output/'+output_filename, 'r') as fp:
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
                        #print('-------------------------------------------------------------------------',file = f)
    #compare the entries of each word and only leave the result that all strings share the same entry

    #delete the current file repo for sacing memory
    delete_list = os.listdir('/home/jiaruz2/extract/output/')
    for delete_filename in delete_list:
        os.remove('/home/jiaruz2/extract/output/'+delete_filename)
    
    print('---------------DONE WITH SEARCHING',secondlist)
                
f.close()

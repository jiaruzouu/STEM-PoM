import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
# Importing the HTTP library
import requests as req
import os 

close_list = os.listdir('/projects/kani-lab/corpus/arXivML_np/')
#print(close_list)

for secondlist in close_list:
    dir_list = os.listdir('/projects/kani-lab/corpus/arXivML_np/'+secondlist+'/')
    #print (dir_list)

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


        f = open('/home/jiaruz2/extract/output/'+filename+"output.txt", "a")
        print(text, file=f)
        f.close()




# filename = 'hep-th0001157.html'

# print(filename)
# #filename = 'dataset/astro-ph0001008.html'
# html = open(filename,'r')
# soup = BeautifulSoup(html, features="html.parser")

# # kill all script and style elements
# for script in soup(["script", "style"]):
#     script.extract()    # rip it out

# # get text
# text = soup.get_text()
# # break into lines and remove leading and trailing space on each
# lines = (line.strip() for line in text.splitlines())
# # break multi-headlines into a line each
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # drop blank lines
# text = '\n'.join(chunk for chunk in chunks if chunk)


# f = open('/home/jiaruz2/extract/output/'+filename+"output.txt", "a")
# print(text, file=f)
# f.close()
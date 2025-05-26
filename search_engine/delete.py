import os 
output_dir_list = os.listdir('/home/jiaruz2/extract/output/')

for filename in output_dir_list:
    #with open('/home/jiaruz2/extract/output/'+filename,'r+') as file:
        #print(file)
        #file.truncate(0)
    os.remove('/home/jiaruz2/extract/output/'+filename)
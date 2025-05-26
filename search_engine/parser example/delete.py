import os 
output_dir_list = os.listdir('output')

#print(output_dir_list)

for filename in output_dir_list:
    with open('output/'+filename,'r+') as file:
        #file.truncate(0)
        os.remove('output/'+filename)
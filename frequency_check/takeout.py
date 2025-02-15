file_path = 'test_database'

symbol_dict = {}

with open(file_path, 'r', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as output_file:
    for line in file:
        parts = line.split(' ')
        if len(parts) > 4:
            symbol = parts[2]
            description = ' '.join(parts[3:])
            symbol_dict[symbol] = []
            symbol_dict[symbol].append(description.strip())



import os
from bs4 import BeautifulSoup

symbols_set = set(symbol_dict.keys())

# Dictionary to hold symbols and the list of files they appear in
symbols_files_dict = {symbol: [] for symbol in symbols_set}

corpus_root_path = ''

# Function to search for symbols in an HTML file
def search_symbols_in_html(html_content, symbols_set):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    found_symbols = set()
    for symbol in symbols_set:
        if symbol in text:
            found_symbols.add(symbol)
    return found_symbols

# Walk through the corpus directory and process HTML files
for root, dirs, files in os.walk(corpus_root_path):
    
        #print(dir)

        
    for file_name in files:
        
            
        if file_name.endswith('.html'):  
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as html_file:
                html_content = html_file.read()
                found_symbols = search_symbols_in_html(html_content, symbols_set)
                    
                for symbol in found_symbols:
                    symbols_files_dict[symbol].append(file_path)  

# Write the output to a file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    for symbol, file_paths in symbols_files_dict.items():
        output_file.write(f"Symbol: {symbol}\n")
        output_file.write("Files:\n")
        for path in file_paths:
            output_file.write(f"\t{path}\n")
        output_file.write("\n")


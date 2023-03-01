#!/opt/conda/bin/python

from string import Template
import re
import argparse

def file_to_codeblock(file, lang, cap):
    #open text file in read mode
    text_file = open(file, "r")
    #read whole file to a string
    res = ''''''

    for line in text_file:
        new_line = '''\n\t"'''+line[:-1].replace('\\', '\\\\').replace('"', '\\"')+ '''\\n",'''
        res += new_line
    
    md_text = '''```{code-block} ''' + lang + '''\\n",
\t":caption: ''' + cap + '''\\n",
\t":linenos:''' + '''\\n",
\t"\\n",''' + res + '''
\t"```\\n",
\t"'''
    return md_text

def replace_nb(src, dest, files): 
    
    with open(src, 'r') as file:
        contents = file.read()

    template = Template(contents)
    
    file_vars_list = [ filename.split('.')[0].upper() for filename in files]
    langs = [ filename.split('.')[1] for filename in files]

    code_vars_dict = {}
    
    for i in range(len(files)):
        code_vars_dict[file_vars_list[i]] =  file_to_codeblock(files[i], langs[i], files[i])

    new_book = template.substitute(code_vars_dict)

    with open(dest, 'w') as file:
        file.write(new_book)
        
        
parser = argparse.ArgumentParser()
parser.add_argument('src', type=str)
parser.add_argument('dest', type=str)
parser.add_argument('files', type=str)

args = parser.parse_args()
source_nb = args.src
dest_nb = args.dest
replacing_files = [ filename for filename in args.files.split(',')]
print()
print("coverting " + source_nb + " to " + dest_nb)
print("injecting " + str(replacing_files) + "\n")

replace_nb(source_nb, dest_nb, replacing_files)
print("done")
#!/opt/conda/bin/python

from string import Template

def file_to_codeblock(file, lang, cap):
    #open text file in read mode
    text_file = open(file, "r")
    #read whole file to a string
    res = ''''''

    for line in text_file:
        new_line = '''\n\t"'''+line[:-1].replace('"', '\\"').replace('\\n', '\\\\n')+ '''\\n",'''
        res += new_line
    
    md_text = '''```{code-block} ''' + lang + '''\\n",
\t":caption: ''' + cap + '''\\n",
\t":linenos:''' + '''\\n",
\t"\\n",''' + res + '''
\t"```\\n",
\t"'''
    return md_text

def replace_nb(src, dest): 
    
    with open(src, 'r') as file:
        contents = file.read()

    template = Template(contents)

    my_vars = {
        'CODE1': file_to_codeblock("testfork.c", "c", "simple c code")
    }

    new_book = template.substitute(my_vars)

    with open(dest, 'w') as file:
        file.write(new_book)

        
code = file_to_codeblock("testfork.c", "c", "simple c code")
print('''    "'''+code)
replace_nb("ch1_src.ipynb", "ch1.ipynb")
print("done")
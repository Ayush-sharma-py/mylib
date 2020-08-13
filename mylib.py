import random
from math import *

def greater(num1 : int, num2 : int):
    if num1 > num2:
        return num1 
    elif num2 > num1:
        return num2
    else:
        return "equal"

def reverse_list(lis):
    new_lis = []
    for i in range(0,len(lis)):
        new_lis.append(lis[len(lis) -i -1])

    return new_lis


def reverse_string(strr : str):
    rev_str = ""
    for i in range(0,len(strr)):
        rev_str = rev_str + strr[len(strr) -1 -i]
    return rev_str

def lesser(num1 : int, num2 : int):
    if num1 < num2:
        return num1 
    elif num2 < num1:
        return num2
    else:
        return "equal"

def similarity(str1 : str, str2 : str):
    sim = 0
    a = lambda x, y : x if x < y else y
    for i in range(0,a(len(str1),len(str2))):
        if str1[i] == str2[i]:
            sim += 1
    return sim
    
def id(text):
    return type(text)

def new_text_file(name):
    f = open(f"{name}.txt","a+")
    f.close()

def create_html_file(names):
    basic_syntax = ["<html>","","  <head>",f"    <title>{names}</title>","  </head>",'',"  <body>","  </body>","","</html>" ]
    with open(f"C:\\Users\\Ayush Sharma\\Desktop\\temp computer project\\{names}.html","a+") as f:
        for i in basic_syntax:
            f.write(i)
            f.write("\n")
        f.close()

def graph(x : list,x_label : str,y : list,y_label : str,title : str):
    try:
        from matplotlib import pyplot as plt 
    except:
        raise Exception("Matplotlib not found")
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
 
def form_key(enc : str,enc_trace : str):
    try:
        key = {}
        for i in range(0,len(enc)):
            key[enc[i]] = enc_trace[i]
        return key
    except:
        if len(enc) != len(enc_trace):
            print("The length of both sting should be the same for a linear scan.")
        
def decrypt(enc : str,key : dict):
    possible = []
    if key:
        strr = ""
        for i in enc:
            try:
                strr += key[i]
            except:
                strr += i
        possible.append(strr)
    return possible

def translate(texts:str):
    from googletrans import Translator
    translator = Translator()
    texts = translator.translate(texts)
    return texts.text

def break_str(text:str):
    ret = []
    for i in text:
        ret.append(i)
    return ret

def unicoder(string):
    string = string.split("\\")
    new_str = ""
    for i in range(0,len(string)):
        if i != len(string) - 1:
            new_str += string[i] + "\\"
        else:
            new_str += string[i]
    return new_str

def get_random_item(lis : list):
    return lis[random.randint(0,len(lis)-1)]

def is_check_import_status(package : str):
    try:
        exec("import {}".format(package))
        print("done")
    except:
        print("Something Went wrong")


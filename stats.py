def get_num_words (text):
    words=text.split()
    cnt_words= len(words)
    return cnt_words

def get_num_chars (text):
    nocaps_text=text.lower()
    chars=list(nocaps_text) 
    dict={}
    for char in chars:
        if char not in dict:
            dict[char]=1
        else :
            dict[char]+=1
    return dict

def get_report (dictionary):
    unsorted_list=[]
    for char in dictionary:
        char_dict ={}
        char_dict["char"]=char
        char_dict["num"]=dictionary[char]
        unsorted_list.append(char_dict)
    sorted_list = sorted(unsorted_list, key=lambda k: (-k["num"],k["char"]))
    return sorted_list
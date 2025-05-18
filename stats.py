def get_num_words (text):
    words=text.split()
    cnt_words= len(words)
    return cnt_words

def get_num_chars (text):
    nocaps_text=text.lower()
    chars=list(nocaps_text) 
    dict={}
    cnt_char=int
    for char in chars:
        if char not in dict:
            cnt_char=1
            dict[f"{char}"]=cnt_char
        else :
            cnt_char=dict[f"{char}"]
            cnt_char+=1
            dict[f"{char}"]=cnt_char
    return dict

def get_report (dictionary):
    unsorted_list=[]
    for char in dictionary:
        char_dict ={}
        char_dict["char"]=char
        char_dict["num"]=dictionary[f"{char}"]
        unsorted_list.append(char_dict)
    unsorted_list.sort(reverse=True, key=lambda k : k["num"])
    sorted_list=unsorted_list
    return sorted_list
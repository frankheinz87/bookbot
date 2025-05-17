def get_num_words (text):
    words=text.split()
    cnt_words= len(words)
    return cnt_words

def get_num_chars (text):
    nocaps_text=text.lower()
    chars=list(nocaps_text) 
    result={}
    cnt_char=int
    for char in chars:
        if char not in result:
            cnt_char=1
            result[f"{char}"]=cnt_char
        else :
            cnt_char=result[f"{char}"]
            cnt_char+=1
            result[f"{char}"]=cnt_char
    return result
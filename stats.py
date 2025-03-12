def word_count(content):
    return len(content.split())

def char_count(content):
    result ={}
    spiltted_content = content.split()
    for single_word in spiltted_content:
        for char in single_word.lower():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    
    return result




def sorted_dict(result_dict):
    return sorted(result_dict.items(), key = lambda item:item[1], reverse = True)
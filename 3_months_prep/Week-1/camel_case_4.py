lines = []

while True:
    try:
        line = input().rstrip()
        data = line.split(';')
        final_text = ''
        
        if data[0] == 'C':
            splitted_text = data[2].split(' ')
            
            for i, txt in enumerate(splitted_text):
                if i == 0 and (data[1] == 'M' or data[1] == 'V'):
                    final_text += txt
                else:
                    final_text += txt.capitalize()
            
            if data[1] == 'M':
                final_text += "()"
        else:
            tmp_str = data[2]
            words = []
            
            for char in data[2]:
                if char.isupper():
                    cur_word = tmp_str.split(char)[0]
                    
                    if cur_word.strip() == '':
                        continue
                    
                    words.append(cur_word.lower())
                    tmp_str = tmp_str[len(cur_word):]
                    
            if data[1] == 'M':
                words.append(tmp_str.lower()[:-2])
            elif data[1] == 'V' or data[1] == 'C':
                words.append(tmp_str.lower())  
                    
            final_text = " ".join(words)
        
        print(final_text)
        
    except:
        break

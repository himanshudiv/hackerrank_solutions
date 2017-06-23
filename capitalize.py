def capitalize(strng):
    '''print the sting in capitalized form(First Character of Every New Word in Text)'''
    str_list=strng.split()
    i=0
    for item in str_list:
        str_list[i]=item.capitalize()
        i+=1
    return " ".join(str_list)

if __name__=='__main__':
	string= raw_input()
	capitalized_string=capitalize(string)
	print capitalized_string

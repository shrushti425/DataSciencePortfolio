def find_books(library,keyword):
    l2=[]
    for i in library:
        if keyword in i:
            l2.append(i)
    return l2
s=input('Enter Book names seperated by a comma(,)\n').upper()
library=s.split(',')
keyword=input('Enter the key to be searched') 
keyword.upper()
print(list(map(find_books,library,keyword)))

 

 
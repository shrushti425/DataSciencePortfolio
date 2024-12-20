class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    #for string representation of Book class
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print('The Book object is deleted')
b=Book('Python rocks','Shrushti',400)
print(b)
len(b)
del b
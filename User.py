# your improved User class goes here
import string


class Person:
    posts=[]
    def __init__(self,name,email_address,liscence_number):
        self.name=name
        self.email_address=email_address
        
        self.liscence_number=liscence_number
    
    def add_post(self):
        post=input('What\'s it you would like to say?   ')
        print(f"{self.name} just posted {post}")
        if self.name in Person.posts:
            Person.posts.insert(Person.posts.index(self.name) +1 , post )
        else:
            Person.post=Person.posts.append(self.name) 
            Person.post=Person.posts.append(post) 
        
    def __str__(self):
        return f"Hi, my name is {self.name}, my email and liscence number are {self.email_address}, {self.liscence_number}."
    #end of class
    
esmeralda=Person('Esmeralda', 'esm@gmail.org','7TFG321')
francisco=Person('francisco', 'fran@gmail.org','123qwe567')
dennis=Person('Dennis', 'den@gmail.org','1qgsd5767')

print(esmeralda.add_post())
print(esmeralda.add_post())
print(francisco.add_post())
print(esmeralda.add_post())
#print(dennis)
#print(Person.posts)

print(Person.posts)
class Person:
    researcher_lst = []
    poet_lst = []
    writer_lst = []
    def __init__(self, name, email, gender):
        self.name = name 
        self.email = email 
        self.gender = gender
    
    def __repr__(self):
        return f'Name : {self.name}; Email : {self.email}; Gender : {self.gender}'
        
    def __str__(self):
        return self.__repr__()
  
        
class Researcher(Person):
    def __init__(self, name, email, gender, field, university):    
        super().__init__(name, email, gender)
        super().researcher_lst
        self.field = field
        self.university = university 
    
    def add_researcher(self):
        self.researcher_lst.append(self.name)
        return self.researcher_lst  
    
    def __repr__(self):
        return f'Name : {self.name}, Email : {self.email}, Gender : {self.gender}, Field : {self.field}, University : {self.university}'

    def __str__(self):
        return self.__repr__()
         
    
class Poet(Person):
    def __init__(self, name, email, gender, method):
        super().__init__(name, email, gender)
        super().poet_lst
        self.method = method 
        
    def add_poet(self):
        self.poet_lst.append(self.name)
        return self.poet_lst
    
    def __repr__(self):
        return f'Name : {self.name}, Email : {self.email}, Gender : {self.gender}, Method : {self.method}'
    
    def __str__(self):
        return self.__repr__()


class Writer(Person):
    def __init__(self, name, email, gender, id, genre):
        super().__init__(name, email, gender)
        super().writer_lst
        self.id = id
        self.genre = genre
        
    def add_writer(self):
        self.writer_lst.append(self.name) 
        return self.writer_lst
     
    def __repr__(self):
        return f'Name : {self.name}, Email : {self.email}, Gender : {self.gender}, id : {self.id}, Genre : {self.genre}'
     
    def __str__(self):
        return self.__repr__()


class Opus(Person):
    def __init__(self, caption, owners):
        self.caption = caption
        self.owners = owners
        self.check = []
        super().researcher_lst
        super().poet_lst
        super().writer_lst
        
    def check_researcher(self):
        if type(self.owner) == list :
            for owner in self.owner :
                if owner in self.researcher_list :
                    self.chek.append(True)
                else :
                    self.chek.append(False)
            return f"check researcher : {all(self.check)}"
        elif type(self.owner) == str :
            if self.owner in self.researcher_list :
                return f"check researcher : {True}"
            else :
                return f"check researcher : {False}"
                
    def check_poet(self):
        if type(self.owner) == list :
            return "chek poet : poet cannot be more than one person"
        elif type(self.owner) == str :
            if self.owner in self.poet_list :
                return f"check poet : {True}"
            else :
                return f"check poet : {False}"

   
    def check_writer(self):
        if type(self.owner) == list :
            for owner in self.owner :
                if owner in self.writer_list :
                    self.check.append(True)
                else :
                    self.check.append(False)
            return f"check writer : {all(self.chek)}"
        elif type(self.owner) == str :
            if self.owner in self.writer_list :
                return f"check writer : {True}"
            else :
                return f"check writer : {False}"

    def __repr__(self):
        return f'Caption : {self.caption}, Owners : {self.owners}'
    
    def __str__(self):
        return self.__repr__()
        
        
                

class Book(Opus):
    def __init__(self, caption,owners, ISBN, publishers):
        super().__init__(caption, owners)
        self.ISBN = ISBN
        self.publishers = publishers
        
    def __repr__(self):
        return f'Caption : {self.caption}, Owners : {self.owners}, Publishrs : {self.publishers}, ISBN : {self.ISBN}'
    
    def __str__(self):
        return self.__repr__()
        
    
class Poetry(Opus):
    def __init__(self, caption, owners, template):
        super().__init__(caption, owners)
        self.template = template
    
    def __repr__(self):
        return f'Caption : {self.caption}, Owner : {self.owners}, Template : {self.template}'
    
    def __str__(self):
        return self.__repr__()
        

class Article(Opus):
    def __init__(self, caption, owners, magazine, publication):
        super().__init__(caption, owners)
        self.magazine = magazine
        self.publication = publication
        
    def __repr__(self):
        return f'Caption : {self.caption}, Owners : {self.owners}, Magazine : {self.magazine}, Publication : {self.publication}'
    
    def __str__(self):
        return self.__repr__()

        
    
    
    
    
    
    
    
    
    
    
    
    
            
        
    
        

class oYemi:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def personality(self):
        return f'{self.name} has a reserved personality'
    
    def relationship(self):
        return f'{self.name} is single'
    
    def job(self):
        return f'{self.name} is fortunate enough to be employed'
    
    def whip(self):
        return f'{self.name} drives a 2012 chevy cruze'
    
    def drip(self):
        return f'{self.name} needs more drip fr'
    
    def munyun(self):
        raise NotImplementedError('what you thought this was nerd')

oYemi = oYemi('Yemi', 24)

print(oYemi.personality())
print(oYemi.relationship())
print(oYemi.job())
print(oYemi.whip())
print(oYemi.drip())
print(oYemi.munyun())
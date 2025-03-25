class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return (self.name == other.name) and (self.score == other.score)
    
    def __ne__(self, other):
        return (self.name != other.name) or (self.score != other.score)
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score
    
    def __str__(self):
        return f"""imię: {self.name}
wynik z egzaminu: {self.score}"""
    

s1 = Student("Ola", 85)
s2 = Student("Marek", 90)

print(s1 < s2)
print(s1 > s2)
print(s1 == s2)
print(s2)
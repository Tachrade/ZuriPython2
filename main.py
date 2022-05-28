

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name,age,tracks,score):
     #Attributes
     self.name = str(name)
     self.age = int(age)
     self.tracks = list(tracks)
     self.score = float(score)

#Change students name, should accept a new name as an argument.
    def change_name(self, new_name):
     self.new_name = new_name
     print(f"The Stundent Old Name is: {self.name} , New Name is {new_name}")
     
#Change students' age, should accept a new age as an argument. Should ensure age remains an integer.
    def change_age(self, new_age):
     self.new_age = int(new_age)
     print(f"The Stundent Old Age is: {self.age} , New Agee is {new_age}")

#Add a new item to students tracks, should accept a new track as an argument
    def add_tracks(self, new_tracks):
      self.tracks.append(new_tracks)
      print(f"The Stundent Tracks are: {self.tracks} , New added track is {new_tracks}")

#get_score: Return student’s score
    def get_score(self):
     print(f"The Stundent Old Score still remains the same:",self.score )
    
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score()
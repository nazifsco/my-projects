class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

        print("Student details:  ")

    def change_name(self, name):
        self.name = name
        print("Name: ",self.name)

    def change_age(self, age):
        self.age = age
        print("Age: ",self.age)

    def add_track(self, tracks):
        self.tracks = tracks
        print("tracks",self.tracks)

    def get_score(self, score):
        self.score = score
        print("scores",self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(99.34)
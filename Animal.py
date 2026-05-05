class Animal:
    # Static class variable to keep track of the number of animals

    numOfAnimals = 0

    def __init__(self, species, name, animal_id, birth_date, color, gender, weight, originating_zoo, date_arrival):
        print(f"Animal created: {species}")  # Debug
        Animal.numOfAnimals += 1
        print(f"Total animals now: {Animal.numOfAnimals}")  # ← ADD THIS LINE
        self.species = species
        self.name = name
        self.animal_id = animal_id
        self.birth_date = birth_date
        self.color = color
        self.gender = gender
        self.weight = weight
        self.originating_zoo = originating_zoo
        self.date_arrival = date_arrival

        # Increment the static variable when a new object is created
        # this is the only place this field's value should be change

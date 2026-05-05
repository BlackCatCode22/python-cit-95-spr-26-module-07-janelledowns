# Main.py
# driver file for Zoo Keeper's Challenge
# last update 10/13/23 by dH
# last update 10/14/23
# last Update 4/1/24 by dH

from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Bear import Bear
from Tiger import Tiger

from datetime import date

print(f"Initial Animal.numOfAnimals: {Animal.numOfAnimals}")

# Create lists of the species
list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

# This is needed for the calc birthday stuff.
current_date = date.today()
current_year = current_date.year

def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"
    # if the birth season is unknown
    else:
        the_birth_day = str(year_of_birthday) + "-01-01"

    return the_birth_day


def process_one_line(one_line):
    # Create variables to help parse arrivingAnimals.txt
    groups_of_words = [part.strip() for part in one_line.strip().split(",")]
    print(one_line)
    print(groups_of_words)

    if len(groups_of_words) < 4:
            return

    single_words = groups_of_words[0].split()
    if len(single_words) <= 4:
            return

    age_in_years = single_words[0]
    a_gender = single_words[3]
    a_species = single_words[4]

    single_words = groups_of_words[1].split()
    season = single_words[2] if len(single_words) > 2 else ""

    color = groups_of_words[2] if len(groups_of_words) > 2 else ""
    weight = groups_of_words[3] if len(groups_of_words) > 3 else ""
    origin_01 = groups_of_words[4] if len(groups_of_words) > 4 else ""
    origin_02 = groups_of_words[5] if len(groups_of_words) > 5 else ""

    from_zoo = origin_01 + ", " + origin_02
    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:
            my_hyena = Hyena(name="aName", animal_id="anID", birth_date=birth_day, color=color, gender=a_gender, weight=weight, originating_zoo=from_zoo, date_arrival=current_date)
            my_hyena.name = Hyena.get_hyena_name(my_hyena)
            my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas).zfill(2)
            Animal.numOfAnimals += 1
            list_of_hyenas.append(my_hyena)

    if "lion" in a_species:
            my_lion = Lion(name="aName", animal_id="anID", birth_date=birth_day, color=color, gender=a_gender, weight=weight, originating_zoo=from_zoo, date_arrival=current_date)
            my_lion.name = Lion.get_lion_name(my_lion)
            my_lion.animal_id = "Li" + str(Lion.numOfLions).zfill(2)
            Animal.numOfAnimals += 1
            list_of_lions.append(my_lion)

    if "bear" in a_species:
            my_bear = Bear(name="aName", animal_id="anID", birth_date=birth_day, color=color, gender=a_gender, weight=weight, originating_zoo=from_zoo, date_arrival=current_date)
            my_bear.name = Bear.get_bear_name(my_bear)
            my_bear.animal_id = "Be" + str(Bear.numOfBears).zfill(2)
            Animal.numOfAnimals += 1
            list_of_bears.append(my_bear)

    if "tiger" in a_species:
            my_tiger = Tiger(name="aName", animal_id="anID", birth_date=birth_day, color=color, gender=a_gender, weight=weight, originating_zoo=from_zoo, date_arrival=current_date)
            my_tiger.name = Tiger.get_tiger_name(my_tiger)
            my_tiger.animal_id = "Ti" + str(Tiger.numOfTigers).zfill(2)
            Animal.numOfAnimals += 1
            list_of_tigers.append(my_tiger)

# Open arrivingAnimals.txt and read it one line at a time
# Open the file in read mode
file_path = r"C:\Users\Janelle\Documents\python-cit-95-programming-spr-26-janelledowns\Module 7\arrivingAnimals.txt"
with open(file_path, "r") as file:
    # Iterate through the file line by line
    for line in file:
        process_one_line(line)

# Access the static variable numOfAnimals
print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")

# Output the static variable numOfHyenas
print(f"\n\nNumber of hyenas created: {Hyena.numOfHyenas}")

# Output the static variable numOfLions
print(f"\n\nNumber of lions created: {Lion.numOfLions}")

print(f"\nNumber of bears created: {Bear.numOfBears}")

print(f"\nNumber of tigers created: {Tiger.numOfTigers}")

# output the animals
# this is zoo population
print()
print("Zookeeper's Challenge Zoo Population")
print()
print("Hyena Habitat:")
print()
for hyena in list_of_hyenas:
    print(hyena.animal_id + ", " + hyena.name + "; birthdate: " + str(hyena.birth_date) + "; " + hyena.color +
          "; " + hyena.gender + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived: " +
          str(hyena.date_arrival))
print()
print("Lion Habitat:")
print()
for lion in list_of_lions:
    print(lion.animal_id + ", " + lion.name + "; birthdate: " + str(lion.birth_date) + "; " + lion.color +
          "; " + lion.gender + "; " + lion.weight + "; " + lion.originating_zoo + "; arrived: " +
          str(lion.date_arrival))

print("Bear Habitat:")
for bear in list_of_bears:
        print(bear.animal_id + ", " + bear.name + "; birthdate: " + str(bear.birth_date) + "; " + bear.color +
              "; " + bear.gender + "; " + bear.weight + "; " + bear.originating_zoo + "; arrived: " +
              str(bear.date_arrival))

print("Tiger Habitat:")
for tiger in list_of_tigers:
        print(tiger.animal_id + ", " + tiger.name + "; birthdate: " + str(tiger.birth_date) + "; " + tiger.color +
              "; " + tiger.gender + "; " + tiger.weight + "; " + tiger.originating_zoo + "; arrived: " +
              str(tiger.date_arrival))
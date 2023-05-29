class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    #Syntax for accessing: Class.CLASS_CONSTANT

    all = []

    def __init__(self, name, pet_type="", owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
        
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception("Not a valid pet type.")
        self._pet_type = pet_type
        
    
class Owner:
    def __init__(self, name):
        self.name = name

    #Method that returns list of owner's pets
    def pets(self):
        # pet_list = [pet for pet in Pet.all if Pet.owner == self]
        return [pet for pet in Pet.all if pet.owner == self]
        
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input object is not of type Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

# chloe = Pet("Chloe", "dog", "Sarah")
# maggie = Pet("Maggie", "dog", "Sarah")
# balthazar = Pet("Balthazar", "reptile", "Sarah")

# sarah = Owner("Sarah")
# print(sarah)

# print(Pet.all) #returned objects

# print(sarah.pets)
#[]
# print(chloe.owner)
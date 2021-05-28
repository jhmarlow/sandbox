"""."""

def return_object(func):
    """ function"""
    def wrapper_object():
        """wrapper to return object to be called
        by decorator"""
        func()
    return self


@do_twice
def printer():
    """the function to be called into decorator."""
    print("test")
    
class CreateVsbObject:
    """."""

    def __init__(self, zip_file=None):
        """."""
        self.zip_file = zip_file

    def add_vsdb(self):
        """."""
        self.vsdb_path = self.zip_file + '.vsdb'

    def add_folder(self):
        """."""
        self.folder_path = self.zip_file + '_folder/'

    def create_object(self):
        """."""
        self.add_vsdb()
        self.add_folder()
        return self

# create object list
list_vsb_objects = []
for filepath in ['/user/path/zip1/', '/user/path/zip2/', '/user/path/zip3/']:
    list_vsb_objects.append(CreateVsbObject(filepath).create_object())


# print files
for file in list_vsb_objects:
    print(file.folder_path)

print("end")


# class Dog:

#     # Class Attribute
#     species = 'mammal'

#     # Initializer / Instance Attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # Instantiate the Dog object
# philo = Dog("Philo", 5)
# mikey = Dog("Mikey", 6)

# print(philo.name)


# # Access the instance attributes
# print("{} is {} and {} is {}.".format(
#     philo.name, philo.age, mikey.name, mikey.age))

# # Is Philo a mammal?
# if philo.species == "mammal":
#     print("{0} is a {1}!".format(philo.name, philo.species))
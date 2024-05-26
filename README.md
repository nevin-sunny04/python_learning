# python_learning
print() -> is used to print to the screen/console. it prints whatever is inside the "" as it is
print(f"Hello {} World") -> f string is used to print a dynamic value to the console. Something which can change and we are not sure of

input() -> is used to get the input from the user. this input can be stored into a variable and can be used later

and or not -> these are the relational operators

round() -> this is used to round up a number to the said decimal points. USAGE round(8/3 , 2) -> precision to 2 decimal places

random module -> used to play around with random numbers. randint(a, b) -> prints a random number between a and b including those numbers

lists -> is a data structure used to organise and store data in Python. Eg: fruits = ["Apple", "Banana", "Orange"]
        the items in the list can be accessed by list[index] . Eg: to get the Banana from the fruits list, fruits[1]
        to iterate through the list, we can use for loops, for items in list: print(item)

functions -> are block of codes which does something and be used multiple times.
              to define a function in Python, we use the def keyword and end with parenthesis. Eg: def my_functions():
                                                                              do_something
                                                          to call a function..... my_functions()

dictionary -> is a datastructure in python to store data in the form of a key, value pair.
              my_dict = {"key1": value1,
                          "key2": value2,
                          "key3": value3}
            to get a value from the dictionary, my_dict["key2"]

we can have nested lists and dictionaries.

Class -> a class is a blueprint of an object in an OO language. 
    class Users:
        def __init__(self): -> this is the constructor and is used to initialize an object of a class
    to create an object of the class -> class_obj = Users()

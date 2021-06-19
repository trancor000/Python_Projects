def parent():  # define function
    class Employee:  # instantiate parent class
        name = 'No Name Provided'  # list attributes
        position = ' '

    class Manager(Employee):  # instantiate child class
        department = 'Kitchen'  # list attributes
        directs = 6

    class Leader(Employee):  # instantiate second child class
        years = 4  # list attributes
        pay = 18.00


parent()

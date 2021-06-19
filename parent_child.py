def parent():
    class Employee:
        name = 'No Name Provided'
        position = ' '

    class Manager(Employee):
        department = 'Kitchen'
        directs = 6

    class Leader(Employee):
        years = 4
        pay = 18.00


parent()

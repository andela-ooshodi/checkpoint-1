'''
A room allocation system for Amity.
By Olufunmilade Oshodi.

Allocation Models for Amity
'''


class Room(object):

    def __init__(self, name):
        '''
        Initialize an instance
        Takes a string argument, name
        '''
        self.name = name
        self.members = []

    def is_occupied(self):
        return True if self.current_size() >= self.max_size else False

    def get_members(self):
        '''
        Returns a list of members allocated to a room
        '''
        members = [member.name for member in self.members]
        return members

    def current_size(self):
        '''
        Returns the current size of a room
        '''
        return len(self.members)

    def add_member(self, member):
        '''
        Adds a member to a room
        '''
        if member not in self.members:
            self.members.append(member)


class Office(Room):
    max_size = 6
    room_type = 'office'
    designation = 'unisex'


class Living(Room):
    max_size = 4
    room_type = 'living'

    def __init__(self, name, designation=None):
        '''
        Initialize an instance
        Takes two string arguments, name and designation = "male" or "female"
        '''
        self.designation = designation
        super(Living, self).__init__(name)


class Person(object):

    def __init__(self, name, gender):
        '''
        Initialize an instance
        Takes two string arguments, name and gender = "M" or "F"
        '''
        self.name = name
        self.gender = gender
        self.gender = self.gender.upper()
        self.office = None
        if self.gender != "M" and self.gender != "F":
            raise ValueError("Please specify the gender as either 'M' or 'F'")

    def __eq__(self, obj):
        if obj.name == self.name and obj.gender == self.gender and self.__class__ == obj.__class__:
            return True
        return False

    def assign_office(self, room):
        if isinstance(room, Office):
            self.office = room
            return True
        else:
            return False


class Staff(Person):
    pass


class Fellow(Person):

    def __init__(self, name, gender, choice=None):
        self.choice = choice
        self.livingspace = None
        super(Fellow, self).__init__(name, gender)

    def assign_living_space(self, room):
        if isinstance(room, Living):
            self.livingspace = room
            return True
        else:
            return False

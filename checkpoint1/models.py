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

    def get_members(self):
        '''
        Returns a list of members allocated to a room
        '''
        return self.members

    def current_size(self):
        '''
        Returns the current size of a room
        '''
        return len(self.members)

    def add_member(self, member):
        '''
        Adds a member to a room
        '''
        try:
            if " #".join([member.name, member.gender]) not in self.members:
                self.members.append(" #".join([member.name, member.gender]))
        except AttributeError:
            print "Can't determine if {} is".format(member),
            print "a 'fellow' or 'staff'"


class Office(Room):
    max_size = 6
    room_type = 'office'
    designation = 'unisex'


class Living(Room):
    max_size = 4
    room_type = 'living'

    def __init__(self, name, designation):
        '''
        Initialize an instance
        Takes two string arguments, name and designation = "male" or "female"
        '''
        self.designation = designation
        self.designation = self.designation.lower()
        if self.designation == "male" or self.designation == "female":
            super(Living, self).__init__(name)
        else:
            raise ValueError(
                "Please designate the room as either male or female")


class Person(object):

    def __init__(self, name, gender):
        '''
        Initialize an instance
        Takes two string arguments, name and gender = "M" or "F"
        '''
        self.name = name
        self.gender = gender
        self.gender = self.gender.upper()
        if self.gender != "M" and self.gender != "F":
            raise ValueError("Please specify the gender as either 'M' or 'F'")


class Staff(Person):
    pass


class Fellow(Person):
    choice = ''
    pass

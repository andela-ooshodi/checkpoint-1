'''
A room allocation system for Amity.
By Olufunmilade Oshodi.

Model file for allocation in Amity
'''


class Space(object):
    max_size = 0

    def __init__(self, name):
        self.name = name


class Office(Space):
    max_size = 6
    office_dic = {}

    def set_room(self):
        self.office_dic[self.name] = []

    def get_members(self):
        return self.office_dic[self.name]

    def current_size(self):
        return len(self.office_dic[self.name])


class Living(Space):
    max_size = 4
    living_dic = {}

    def set_room(self):
        self.living_dic[self.name] = []

    def get_members(self):
        return self.living_dic[self.name]

    def current_size(self):
        return len(self.living_dic[self.name])


class Person(object):

    def __init__(self, name):
        self.name = name


class Staff(Person):
    staff_list = []

    def set_staff(self):
        self.staff_list.append(self.name)


class Fellow(Person):
    male_list = []  # list for allocation to male rooms
    female_list = []  # list for allocation to female rooms
    mixed_list = []  # list for no allocation to living space

    def set_male(self):
        self.male_list.append(self.name)

    def set_female(self):
        self.female_list.append(self.name)

    def set_mixed(self):
        self.mixed_list.append(self.name)

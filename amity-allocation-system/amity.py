'''
A room allocation system for Amity.
By Olufunmilade Oshodi.

Allocation Logic for Amity
'''
import argparse

from models import Office, Living, Staff, Fellow


class Amity(object):

    '''
    Amity Class models the real life entity "Amity",
    defined by it's rooms and people data
    and it's methods(behaviors) that act on it's data
    '''
    rooms = {
        'office': [],
        'living': [],
    }
    unallocated = {
        'office': [],
        'living': [],
    }
    people = []
    office_pointer = 0
    living_pointer = 0

    def prepopulate(self):
        '''
        Prepopulate Amity with 10 offices and 10 living spaces
        '''
        office = ['Carat', 'Anvil', 'Crucible', 'Kiln', 'Forge',
                  'Foundry', 'Furnace', 'Boiler', 'Mint', 'Vulcan']
        living = ['Topaz', 'Silver', 'Gold', 'Onyx', 'Opal',
                  'Ruby', 'Platinium', 'Jade', 'Pearl', 'Diamond']

        for item in office:
            self.add_room(Office(item))
        for item in living:
            self.add_room(Living(item))

    def add_room(self, room):
        '''
        Adds a room to Amity
        '''
        try:
            if room.room_type not in self.rooms:
                self.rooms[room.room_type] = []
                self.rooms[room.room_type].append(room)
            else:
                if(room not in self.rooms[room.room_type]):
                    self.rooms[room.room_type].append(room)
        except AttributeError:
            print("Can't determine if {} is".format(room))
            print("an 'office' or a 'living space'")

    def add_person(self, person):
        '''
        Adds people to Amity
        '''
        if person not in self.people:
            self.people.append(person)

    def get_rooms(self):
        '''
        Returns all rooms in Amity
        '''
        amity_rooms = []
        for key in self.rooms:
            for values in self.rooms[key]:
                amity_rooms.append(
                    "{} ({})".format(values.name, values.room_type))
        return amity_rooms

    def get_next_office(self):
        '''
        Returns the next available office in Amity
        '''
        try:
            office = self.rooms['office'][self.office_pointer]
            if office.is_occupied():
                self.office_pointer += 1
                office = self.rooms['office'][self.office_pointer]
            return office
        except IndexError:
            return None

    def assign_office(self, person):
        '''
        Assigns a person to an Office
        '''
        office = self.get_next_office()
        if office is not None:
            office.add_member(person)
            person.assign_office(office)
            return True
        else:
            return False

    def get_next_living_space(self):
        '''
        Returns the next available livingspace in Amity
        '''
        self.default_pointer = self.living_pointer
        try:
            living = self.rooms['living'][self.living_pointer]
            if living.is_occupied():
                self.living_pointer += 1
                living = self.rooms['living'][self.living_pointer]
            return living
        except IndexError:
            return None

    def get_another_living_space(self):
        '''
        Returns the next available gender specific livingspace in Amity
        '''
        try:
            self.living_pointer += 1
            living = self.rooms['living'][self.living_pointer]
            if not living.is_occupied():
                self.living_pointer = self.default_pointer
                return living
            else:
                self.get_another_living_space()
        except IndexError:
            return None

    def assign_living_space(self, person):
        '''
        Assigns a person to a livingspace
        '''
        living = self.get_next_living_space()
        try:
            if living is not None:
                if living.designation is None:
                    living.designation = person.gender

                elif living.designation != person.gender:
                    living = self.get_another_living_space()
                    living.designation = person.gender

                living.add_member(person)
                person.assign_living_space(living)
                return True

            else:
                return False
        except AttributeError:
            return False

    def allocate(self):
        '''
        Allocates staffs and fellows
        '''
        for person in self.people:
            if person.office is None:
                if not self.assign_office(person):
                    self.unallocated['office'].append(person)
            if isinstance(person, Fellow) and person.choice.upper() == 'Y' and person.livingspace is None:
                if not self.assign_living_space(person):
                    self.unallocated['living'].append(person)

    def inputfile_reader(self):
        '''
        Reads the inputfile
        '''
        with open(self.inputfile, 'r') as f:
            for line in f:
                line = line.split()
                status = line[3].upper()
                if status == "FELLOW":
                    firstname, lastname, gender, status, choice = map(
                        str, line)
                    name = firstname + " " + lastname
                    person = Fellow(name, gender, choice)
                else:
                    firstname, lastname, gender, status = map(str, line)
                    name = firstname + " " + lastname
                    person = Staff(name, gender)

                self.add_person(person)

    def create_parser(self):
        '''
        Parser function for creating positional arguments
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "inputfile", help="Allocates base on input file passed")
        return parser

    def main(self):
        '''
        Allows for command line input and error checking if no file was passed
        '''
        parser = self.create_parser()
        args = parser.parse_args()
        self.inputfile = args.inputfile

    def print_result(self):
        '''
        Prints result of allocation
        '''
        print("Result:")
        print("\n")
        for key in self.rooms:
            for values in self.rooms[key]:
                print(values.name, "({0}, {1})".format(values.designation, values.room_type.upper()))
                print(values.get_members())
                print("\n")

    def print_unallocated(self):
        '''
        Prints a persons not allocated
        '''
        print("After Allocation, the following could not be allocated")
        for key in self.unallocated:
            print("{}:".format(key))
            person = [person.name for person in self.unallocated[key]]
            print(person)
            print

if __name__ == '__main__':
    amity = Amity()
    amity.main()
    amity.prepopulate()
    amity.inputfile_reader()
    amity.allocate()
    amity.print_result()
    amity.print_unallocated()

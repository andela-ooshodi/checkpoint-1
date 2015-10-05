'''
A room allocation system for Amity.
By Olufunmilade Oshodi.

Allocation Logic for Amity
'''
import random
import argparse

from models import Office, Living, Staff, Fellow


class Amity(object):
    rooms = {}

    def prepopulate(self):
        '''
        Prepopulate Amity with 10 offices and 10 living spaces
        '''
        office = ['Carat', 'Anvil', 'Crucible', 'Kiln', 'Forge',
                  'Foundry', 'Furnace', 'Boiler', 'Mint', 'Vulcan']
        living = ['Topaz', 'Silver', 'Gold', 'Onyx', 'Opal',
                  'Ruby', 'Platinium', 'Jade', 'Pearl', 'Diamond']
        self.rooms['office'] = []
        self.rooms['living'] = []
        for item in office:
            self.rooms['office'].append(Office(item))
        for item in living[:5]:
            self.rooms['living'].append(Living(item, 'male'))
        for item in living[5:]:
            self.rooms['living'].append(Living(item, 'female'))

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
            print "Can't determine if {} is".format(room),
            print "an 'office' or a 'living space'"

    def get_rooms(self):
        '''
        Returns all available rooms in Amity
        '''
        amity_rooms = []
        for key in self.rooms:
            for values in self.rooms[key]:
                amity_rooms.append(
                    values.name + "({})".format(values.room_type))
        return amity_rooms

    def allocate(self, person):
        '''
        Allocates staffs and fellows
        '''
        for key in self.rooms:
            random.shuffle(self.rooms[key])
            for room in self.rooms[key]:
                if isinstance(person, Fellow):
                    if person.choice == "Y" or person.choice == "y":
                        if room.room_type == 'living':
                            if room.current_size() < room.max_size:
                                if person.gender == 'M' and room.designation == 'male':
                                    room.add_member(person)
                                    break
                                elif person.gender == 'F' and room.designation == 'female':
                                    room.add_member(person)
                                    break
                if isinstance(person, Staff) or isinstance(person, Fellow):
                    if room.room_type == 'office':
                        if room.current_size() < room.max_size:
                            room.add_member(person)
                            break
                else:
                    raise ValueError(
                        "Can't allocate, undetermined if either a staff or fellow")

    def inputfile_reader(self):
        '''
        Reads the inputfile passed to Amity to allocate
        '''
        with open(self.inputfile, 'r') as f:
            for line in f:
                line = line.split()
                status = line[3]
                status = status.upper()
                if status == "FELLOW":
                    firstname, lastname, gender, status, choice = map(
                        str, line)
                    name = firstname + " " + lastname
                    individual = Fellow(name, gender)
                    individual.choice = choice
                    self.allocate(individual)
                else:
                    firstname, lastname, gender, status = map(str, line)
                    name = firstname + " " + lastname
                    individual = Staff(name, gender)
                    self.allocate(individual)

    def get_unallocated(self):
        '''
        Returns a list of unallocated individuals in Amity
        '''
        category = {}
        category['office'] = []
        category['living'] = []
        with open(self.inputfile, 'r') as f:
            for line in f:
                line = line.split()
                name = line[0] + " " + line[1]
                gender = line[2]
                category['office'].append(" #".join([name, gender]))
                status = line[3]
                status = status.upper()
                if status == "FELLOW":
                    choice = line[4]
                    choice = choice.upper()
                    if choice == "Y":
                        category['living'].append(" #".join([name, gender]))

        allocated = {}
        for key in self.rooms:
            allocated[key] = []
            for values in self.rooms[key]:
                allocated[key].extend(values.get_members())

        unallocated = {}
        for key in allocated:
            unallocated[key] = [
                item for item in category[key] if item not in allocated[key]]

        return unallocated

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

if __name__ == '__main__':
    amity = Amity()
    amity.main()
    amity.prepopulate()
    amity.inputfile_reader()

    for key in amity.rooms:
        for values in amity.rooms[key]:
            print values.name, "({0}, {1})".format(values.designation, values.room_type.upper())
            print values.get_members()
            print

    print "After Allocation, the following could not be allocated"
    print amity.get_unallocated()

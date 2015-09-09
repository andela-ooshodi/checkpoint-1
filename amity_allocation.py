'''
A room allocation system for Amity.

By Olufunmilade Oshodi.
'''
import random


class Rooms(object):
    # dictionary for available spaces in Amity

    def __init__(self):
        self.office_dic = {
            'Carat': [],
            'Anvil': [],
            'Crucible': [],
            'Kiln': [],
            'Forge': [],
            'Foundry': [],
            'Furnace': [],
            'Boiler': [],
            'Mint': [],
            'Vulcan': []
        }
        self.male_living_dic = {
            'Topaz': [],
            'Silver': [],
            'Gold': [],
            'Onyx': [],
            'Opal': []
        }
        self.female_living_dic = {
            'Ruby': [],
            'Platinium': [],
            'Jade': [],
            'Pearl': [],
            'Diamond': []
        }

    def allocate(self, firstname, lastname, n, space):
        if space == 'office':
            space = self.office_dic
        elif space == 'male':
            space = self.male_living_dic
        else:
            space = self.female_living_dic

        x = 0
        while x < 30:
            room = random.choice(space.values())
            if len(room) < n:
                room.append("%s %s" % (firstname, lastname))
                break
            x += 1


class Amity(object):

    def __init__(self):
        self.filename = 'input.txt'
        self.rooms = Rooms()

    def alloc(self):
        with open(self.filename, 'r') as f:
            count = sum(1 for line in f)
            # move the file pointer back to the beginning of the file
            f.seek(0)
            while count > 0:
                # get the current position of the file pointer
                current_fp = f.tell()
                line = f.readline()
                line = line.split()
                status = line[3]
                if status == "FELLOW":
                    # go back to last saved position of file pointer
                    f.seek(current_fp)
                    firstname, lastname, sex, status, choice = map(
                        str, f.readline().split())
                    if choice == "Y" and sex == "M":
                        # Allocate male living space
                        self.rooms.allocate(firstname, lastname, 4, 'male')
                        # Allocate office
                        self.rooms.allocate(firstname, lastname, 6, 'office')
                    elif choice == "Y" and sex == "F":
                        # Allocate female living space
                        self.rooms.allocate(firstname, lastname, 4, 'female')
                        # Allocate office
                        self.rooms.allocate(firstname, lastname, 6, 'office')
                    else:
                        # Allocate office
                        self.rooms.allocate(firstname, lastname, 6, 'office')
                else:
                    # go back to last saved position of file pointer
                    f.seek(current_fp)
                    firstname, lastname, sex, status = map(
                        str, f.readline().split())
                    # Allocate office
                    self.rooms.allocate(firstname, lastname, 6, 'office')

                count -= 1


class Sorting(object):

    def __init__(self):
        self.amity = Amity()

    def assort(self):
        self.amity.alloc()
        # lists hold unsorted fellows and staff before allocation
        self.unsorted_officelist = []
        self.unsorted_livinglist = []
        with open(self.amity.filename, 'r') as f:
            for line in f:
                line = line.split()
                firstname = line[0]
                lastname = line[1]
                status = line[3]
                self.unsorted_officelist.append(
                    "%s %s" % (firstname, lastname))
                if status == "FELLOW":
                    choice = line[4]
                    if choice == "Y":
                        self.unsorted_livinglist.append(
                            "%s %s" % (firstname, lastname))

        # list holds unallocated staff(s) or fellow(s) for office space after
        # allocation
        for key in self.amity.rooms.office_dic:
            self.unsorted_officelist = [
                x for x in self.unsorted_officelist if x not in self.amity.rooms.office_dic[key]
            ]

        # list holds unallocated fellow(s) for living space after allocation
        for key in self.amity.rooms.male_living_dic:
            self.unsorted_livinglist = [
                x for x in self.unsorted_livinglist if x not in self.amity.rooms.male_living_dic[key]
            ]

        for key in self.amity.rooms.female_living_dic:
            self.unsorted_livinglist = [
                x for x in self.unsorted_livinglist if x not in self.amity.rooms.female_living_dic[key]
            ]


class Result(object):

    def __init__(self):
        self.sorting = Sorting()

    def allocation_result(self):
        self.sorting.assort()

        for sort in sorted(self.sorting.amity.rooms.office_dic):
            print "%s office:" % sort
            print self.sorting.amity.rooms.office_dic[sort]
            print

        for sort in sorted(self.sorting.amity.rooms.male_living_dic):
            print "%s room:" % sort
            print self.sorting.amity.rooms.male_living_dic[sort]
            print

        for sort in sorted(self.sorting.amity.rooms.female_living_dic):
            print "%s room:" % sort
            print self.sorting.amity.rooms.female_living_dic[sort]
            print

        print "Staffs or fellows without office space:"
        print self.sorting.unsorted_officelist
        print
        print "Fellows without living space:"
        print self.sorting.unsorted_livinglist


if __name__ == "__main__":
    result = Result()
    result.allocation_result()

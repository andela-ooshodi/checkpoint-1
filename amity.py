'''
A room allocation system for Amity.
By Olufunmilade Oshodi.

Logic file for allocation in Amity
'''
from models import Office, Living, Staff, Fellow


class Amity(object):
    rooms = {
        'office': [],
        'living': []
    }

    def input_parser(self):
        # reads through a file to get the list of people to be allocated
        self.filename = 'input.txt'
        self.male_input_list = []
        self.female_input_list = []
        self.mixed_input_list = []
        self.staffs_input_list = []
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
                    firstname, lastname, gender, status, choice = map(
                        str, f.readline().split())
                    if choice == "Y" and gender == "M":
                        self.male_input_list.append(
                            "%s %s" % (firstname, lastname))
                    elif choice == "Y" and gender == "F":
                        self.female_input_list.append(
                            "%s %s" % (firstname, lastname))
                    else:
                        self.mixed_input_list.append(
                            "%s %s" % (firstname, lastname))
                else:
                    # go back to last saved position of file pointer
                    f.seek(current_fp)
                    firstname, lastname, gender, status = map(
                        str, f.readline().split())
                    self.staffs_input_list.append(
                        "%s %s" % (firstname, lastname))

                count -= 1

    def preload(self):
        # solely to build 10 offices and 10 living spaces for Amity
        office_list = ['Carat', 'Anvil', 'Crucible', 'Kiln', 'Forge',
                       'Foundry', 'Furnace', 'Boiler', 'Mint', 'Vulcan']
        living_list = ['Topaz', 'Silver', 'Gold', 'Onyx',
                       'Opal', 'Ruby', 'Platinium', 'Jade', 'Pearl', 'Diamond']
        for item in office_list:
            self.create_room(item, type='office')
        for item in living_list:
            self.create_room(item, type='living')

    def create_room(self, name, type):
        # create rooms to populate the rooms dictionary in amity
        self.rooms[type].append(
            Living(name).name if type == 'living' else Office(name).name)

    def add_room(self):
        # adds the created rooms to their respective dictionary and returns two
        # lists of available rooms in Amity
        for key in self.rooms:
            for values in self.rooms[key]:
                if key == 'office':
                    office = Office(values)
                    office.set_room()
                else:
                    living = Living(values)
                    living.set_room()

        return office.office_dic, living.living_dic

    def allocation(self):
        # function to allocate given input
        # allocate into offices
        self.master_list = self.staffs_input_list + self.male_input_list + \
            self.mixed_input_list + self.female_input_list
        for room in self.rooms['office']:
            office = Office(room)
            length = len(office.office_dic[room])
            while length < office.max_size:
                office.office_dic[room].append(self.master_list.pop(0))
                length += 1

        # allocate into male living
        for room in self.rooms['living'][:5]:
            living = Living(room)
            length = len(living.living_dic[room])
            while length < living.max_size:
                living.living_dic[room].append(self.male_input_list.pop(0))
                length += 1

        # allocate into female living
        for room in self.rooms['living'][5:]:
            living = Living(room)
            length = len(living.living_dic[room])
            while length < living.max_size:
                living.living_dic[room].append(self.female_input_list.pop(0))
                length += 1

    def get_staff(self):
        # staff list
        for staffs in self.staffs_input_list:
            staff = Staff(staffs)
            staff.set_staff()
        return staff.staff_list

    def get_fellows_not_living_in_amity(self):
        # fellows not living in amity
        for fellows in self.mixed_input_list:
            fellow = Fellow(fellows)
            fellow.set_mixed()
        return fellow.mixed_list

    def get_male_living_fellows(self):
        # fellows to be allocated male rooms
        for fellows in self.male_input_list:
            fellow = Fellow(fellows)
            fellow.set_male()
        return fellow.male_list

    def get_female_living_fellows(self):
        # fellows to be allocated female rooms
        for fellows in self.female_input_list:
            fellow = Fellow(fellows)
            fellow.set_female()
        return fellow.female_list

    def get_office_unallocated(self):
        # function to return those not allocated to an office
        return self.master_list

    def get_living_unallocated(self):
        # function to return those not allocated to a living space
        return self.male_input_list + self.female_input_list

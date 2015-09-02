import random


class SpaceAllocation(object):

    def __init__(self, filename):
        self.filename = filename
        # offices
        self.office1 = []
        self.office2 = []
        self.office3 = []
        self.office4 = []
        self.office5 = []
        self.office6 = []
        self.office7 = []
        self.office8 = []
        self.office9 = []
        self.office10 = []
        # living areas
        self.living1 = []
        self.living2 = []
        self.living3 = []
        self.living4 = []
        self.living5 = []
        self.living6 = []
        self.living7 = []
        self.living8 = []
        self.living9 = []
        self.living10 = []

    # males are allocated living space 1 - 5
    def male_living_allocation(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        n = 0
        while n < 30:
            living = random.choice(
                [self.living1, self.living2, self.living3, self.living4, self.living5]
            )
            if len(living) < 4:
                return living.append("%s %s" % (self.firstname, self.lastname))
                break
            n += 1

    # females are allocated living space 6 - 10
    def female_living_allocation(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        n = 0
        while n < 30:
            living = random.choice(
                [self.living6, self.living7, self.living8, self.living9, self.living10]
            )
            if len(living) < 4:
                return living.append("%s %s" % (self.firstname, self.lastname))
                break
            n += 1

    def office_allocation(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        n = 0
        while n < 30:
            office = random.choice(
                [self.office1, self.office2, self.office3, self.office4, self.office5,
                 self.office6, self.office7, self.office8, self.office9, self.office10]
            )
            if len(office) < 6:
                return office.append("%s %s" % (self.firstname, self.lastname))
                break
            n += 1

    def allocation(self):
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
                        self.male_living_allocation(firstname, lastname)

                        # Allocate office
                        self.office_allocation(firstname, lastname)

                    elif choice == "Y" and sex == "F":
                        # Allocate female living space
                        self.female_living_allocation(firstname, lastname)

                        # Allocate office
                        self.office_allocation(firstname, lastname)

                    else:
                        # Allocate office
                        self.office_allocation(firstname, lastname)

                else:
                    # go back to last saved position of file pointer
                    f.seek(current_fp)
                    firstname, lastname, sex, status = map(
                        str, f.readline().split())
                    # Allocate office
                    self.office_allocation(firstname, lastname)

                count -= 1

            # dictionary to contain allocated office space
            self.office_dic = {
                1: self.office1,
                2: self.office2,
                3: self.office3,
                4: self.office4,
                5: self.office5,
                6: self.office6,
                7: self.office7,
                8: self.office8,
                9: self.office9,
                10: self.office10
            }
            # dictionary to contain allocated living space
            self.living_dic = {
                1: self.living1,
                2: self.living2,
                3: self.living3,
                4: self.living4,
                5: self.living5,
                6: self.living6,
                7: self.living7,
                8: self.living8,
                9: self.living9,
                10: self.living10
            }

    def unallocated(self):
        self.allocation()

        # list to hold unsorted fellows and staff before allocation
        self.unsorted_officelist = []
        self.unsorted_livinglist = []
        with open(self.filename, 'r') as f:
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
        for key in self.office_dic:
            self.unsorted_officelist = [
                x for x in self.unsorted_officelist if x not in self.office_dic[key]
            ]

        # list holds unallocated fellow(s) for living space after allocation
        for key in self.living_dic:
            self.unsorted_livinglist = [
                x for x in self.unsorted_livinglist if x not in self.living_dic[key]
            ]

    def allocation_result(self):
        # call in the functions that handle allocation
        self.allocation()
        self.unallocated()

        for sort in sorted(self.office_dic):
            print "office %i :" % sort
            print self.office_dic[sort]
            print

        for sort in sorted(self.living_dic):
            print "living %i :" % sort
            print self.living_dic[sort]
            print

        print "Staffs or fellows without office space"
        print self.unsorted_officelist
        print
        print "Fellows without living space"
        print self.unsorted_livinglist

if __name__ == "__main__":
    allocate = SpaceAllocation('input.txt')
    allocate.allocation_result()

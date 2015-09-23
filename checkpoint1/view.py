'''
A room allocation system for Amity.
By Olufunmilade Oshodi.

Output file for allocation in Amity
'''

from amity import Amity
from models import Office, Living


class Engine(object):
    # This engine class runs the program and also for formatting the output

    def __init__(self):
        self.amity = Amity()

    def run(self):
        self.amity.preload()
        self.amity.add_room()
        self.amity.input_parser()
        self.amity.allocation()

        for room in self.amity.rooms['office']:
            office = Office(room)
            print "%s office:" % room
            print office.get_members()
            print

        for room in self.amity.rooms['living']:
            living = Living(room)
            print "%s room:" % room
            print living.get_members()
            print

        print "Staffs and Fellows without office space:"
        print self.amity.get_office_unallocated()
        print
        print "Fellows without living space:"
        print self.amity.get_living_unallocated()


allocation = Engine()
allocation.run()

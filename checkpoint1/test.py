import unittest
from amity import Amity
from models import Room, Office, Living, Staff, Fellow


class TestAmityModels(unittest.TestCase):

    def setUp(self):
        self.office = Office('Office')
        self.male_room = Living('MaleRoom', 'MALE')
        self.female_room = Living('FemaleRoom', 'FEMALE')
        self.chidi = Staff('Chidi', 'm')
        self.seyi = Staff('Seyi', 'M')
        self.lady_seyi = Staff('Seyi', 'f')
        self.lade = Fellow('Lade', 'M')
        self.fisayo = Fellow('Fisayo', 'M')
        self.kate = Fellow('Kate', 'F')
        self.sayo = Fellow('Sayo', 'F')

    def test_office_instance(self):
        self.assertIsInstance(
            self.office, Office,
            msg="office should be an instance of 'Office' class"
        )

    def test_office_object_type(self):
        self.assertTrue(
            (type(self.office) is Office),
            msg="The object should be a type of 'Office'"
        )

    def test_living_instance(self):
        self.assertIsInstance(
            self.male_room, Living,
            msg="living should be an instance of 'Living' class"
        )

    def test_living_object_type(self):
        self.assertTrue(
            (type(self.female_room) is Living),
            msg="The object should be a type of 'Living space'"
        )

    def test_staff_instance(self):
        self.assertIsInstance(
            self.chidi, Staff,
            msg="staff should be an instance of 'Staff' class"
        )

    def test_staff_object_type(self):
        self.assertTrue(
            (type(self.chidi) is Staff),
            msg="The object should be a type of 'Staff'"
        )

    def test_fellow_instance(self):
        self.assertIsInstance(
            self.lade, Fellow,
            msg="fellow should be an instance of 'Fellow' class"
        )

    def test_fellow_object_type(self):
        self.assertTrue(
            (type(self.lade) is Fellow),
            msg="The object should be a type of 'Fellow'"
        )

    def test_can_return_members_of_office(self):
        self.office.add_member(self.chidi)
        self.office.add_member(self.seyi)
        self.office.add_member(self.lady_seyi)
        members = ['Chidi #M', 'Seyi #M', 'Seyi #F']
        self.assertEquals(self.office.get_members(
        ), members, msg="The function should return the members in that office")

    def test_can_return_current_size_of_office(self):
        self.office.add_member(self.chidi)
        self.office.add_member(self.seyi)
        self.office.add_member(self.lady_seyi)
        self.assertEquals(self.office.current_size(
        ), 3, msg="The function should return the current number of members in that office")

    def test_can_return_members_of_living(self):
        self.male_room.add_member(self.lade)
        self.male_room.add_member(self.fisayo)
        self.female_room.add_member(self.sayo)
        self.female_room.add_member(self.kate)
        male_members = ['Lade #M', 'Fisayo #M']
        female_members = ['Sayo #F', 'Kate #F']
        self.assertEquals(self.male_room.get_members(
        ), male_members, msg="The function should return the members in that living space")
        self.assertEquals(self.female_room.get_members(
        ), female_members, msg="The function should return the members in that living space")

    def test_can_return_current_size_of_living(self):
        self.male_room.add_member(self.lade)
        self.male_room.add_member(self.fisayo)
        self.female_room.add_member(self.sayo)
        self.female_room.add_member(self.kate)
        self.assertEquals(self.male_room.current_size(
        ), 2, msg="The function should return the current number of members in that living space")
        self.assertEquals(self.female_room.current_size(
        ), 2, msg="The function should return the current number of members in that living space")\


    def test_room_class_exceptions(self):
        self.assertRaises(
            AttributeError, Office('TestOffice').add_member('testmember'))

    def test_living_class_exceptions(self):
        with self.assertRaises(ValueError):
            Living('TestLiving', 'testdesignation')

    def test_person_class_exceptions(self):
        with self.assertRaises(ValueError):
            Staff('TestStaff', 'testgender')


class TestPreloadedAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        self.amity.prepopulate()
        self.parser = self.amity.create_parser()
        args = self.parser.parse_args(["input.txt"])
        self.amity.inputfile = args.inputfile
        self.amity.inputfile_reader()

    def test_script_with_empty_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_initial_rooms_in_amity(self):
        self.assertEqual(len(self.amity.rooms[
                         'living']), 10, msg="Amity should be preloaded with 10 living spaces")
        self.assertEqual(len(
            self.amity.rooms['office']), 10, msg="Amity should be preloaded with 10 offices")

    def test_allocation_from_inputfile(self):
        self.assertLessEqual(self.amity.rooms['office'][0].current_size(), 6)
        self.assertLessEqual(self.amity.rooms['living'][9].current_size(), 4)

    def test_unallocated(self):
        self.assertGreaterEqual(len(self.amity.get_unallocated()['living']), 0)
        self.assertGreaterEqual(len(self.amity.get_unallocated()['office']), 0)


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

        # create and allocate Staffs and Fellows
        self.chidi = Staff('Chidi', 'M')
        self.lady_chi = Staff('Chidimma', 'f')
        self.laide = Fellow('Laide', 'f')
        self.laide.choice = 'Y'
        self.rukky = Fellow('Rukkie', 'f')
        self.olaide = Fellow('Olaide', 'm')
        self.olaide.choice = 'y'

    def test_total_number_of_people_allocated_to_offices(self):
        self.amity.allocate(self.chidi)
        self.amity.allocate(self.lady_chi)
        self.amity.allocate(self.laide)
        self.amity.allocate(self.rukky)
        self.amity.allocate(self.olaide)
        members = []
        for x in range(len(self.amity.rooms['office'])):
            members.extend(self.amity.rooms['office'][x].get_members())
        self.assertEquals(len(
            members), 5, msg="Only the total number of persons allocated should be returned")

    def test_total_number_of_residents(self):
        self.amity.allocate(self.chidi)
        self.amity.allocate(self.lady_chi)
        self.amity.allocate(self.laide)
        self.amity.allocate(self.rukky)
        self.amity.allocate(self.olaide)
        members = []
        for x in range(len(self.amity.rooms['living'])):
            members.extend(self.amity.rooms['living'][x].get_members())
        self.assertEquals(len(
            members), 2, msg="Only fellows who opted for living spaces should be residents")

    def test_add_room(self):
        # create Offices and Rooms
        gold = Office('Gold')
        helium = Office('Helium')
        mars = Living('Mars', 'male')
        venus = Living('Venus', 'female')
        self.amity.add_room(gold)
        self.amity.add_room(helium)
        self.amity.add_room(mars)
        self.amity.add_room(venus)

        self.assertEqual(len(self.amity.rooms[
                         'living']), 2, msg="Only rooms added to Amity should be returned")
        self.assertEqual(len(self.amity.rooms[
                         'office']), 2, msg="Only rooms added to Amity should be returned")
        self.assertRaises(
            AttributeError, self.amity.add_room('TestRoom'))

    def test_get_rooms(self):
        self.assertEquals(len(self.amity.get_rooms()), 4,
                          msg="Amity should contain rooms that have been added in it")

    def test_add_new_type_of_room(self):
        training = Room('Training')
        training.room_type = 'training'
        self.amity.add_room(training)
        self.assertTrue(self.amity.rooms['training'])
        del self.amity.rooms['training']

    def test_allocation_exceptions(self):
        with self.assertRaises(ValueError):
            self.amity.allocate('TestPerson')


if __name__ == '__main__':
    unittest.main()

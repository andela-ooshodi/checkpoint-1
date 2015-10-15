import unittest
from amity import Amity
from models import Office, Living, Staff, Fellow
from StringIO import StringIO
from mock import patch


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

        self.office.add_member(self.chidi)
        self.office.add_member(self.seyi)
        self.office.add_member(self.lady_seyi)
        self.male_room.add_member(self.lade)
        self.male_room.add_member(self.fisayo)
        self.female_room.add_member(self.sayo)
        self.female_room.add_member(self.kate)

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

    def test_can_return_current_size_of_office(self):
        self.assertEquals(self.office.current_size(
        ), 3, msg="The function should return the current number of members in that office")

    def test_can_return_current_size_of_living(self):
        self.assertEquals(self.male_room.current_size(
        ), 2, msg="The function should return the current number of members in that living space")
        self.assertEquals(self.female_room.current_size(
        ), 2, msg="The function should return the current number of members in that living space")


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        self.amity.prepopulate()
        self.parser = self.amity.create_parser()
        args = self.parser.parse_args(["input.txt"])
        self.amity.inputfile = args.inputfile
        self.amity.inputfile_reader()
        self.amity.allocate()

    def tearDown(self):
        del self.amity.rooms['office']
        del self.amity.rooms['living']
        self.amity.people = []

    def test_script_with_empty_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_initial_rooms_in_amity(self):
        self.assertEqual(len(self.amity.rooms[
                         'living']), 10, msg="Amity should be preloaded with 10 living spaces")
        self.assertEqual(len(
            self.amity.rooms['office']), 10, msg="Amity should be preloaded with 10 offices")

    def test_number_of_persons_from_input(self):
        self.assertEquals(len(self.amity.people), 64)

    def test_members_of_room(self):
        self.assertLessEqual(
            len(self.amity.rooms['office'][0].get_members()), 6)
        self.assertLessEqual(
            len(self.amity.rooms['living'][0].get_members()), 4)

    def test_current_size_of_room(self):
        self.assertLessEqual(self.amity.rooms['office'][0].current_size(), 6)
        self.assertLessEqual(self.amity.rooms['living'][9].current_size(), 4)

    def test_unallocated(self):
        self.assertGreaterEqual(len(self.amity.unallocated['living']), 0)
        self.assertGreaterEqual(len(self.amity.unallocated['office']), 0)

    def test_total_number_of_romms_in_Amity(self):
        self.assertEquals(len(self.amity.get_rooms()), 20)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result(self, mock_out):
        result_str = "Result:"
        self.amity.print_result()
        self.assertIn(result_str, mock_out.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_unallocated(self, mock_out):
        result_str = "After Allocation, the following could not be allocated"
        self.amity.print_unallocated()
        self.assertIn(result_str, mock_out.getvalue())

if __name__ == '__main__':
    unittest.main()

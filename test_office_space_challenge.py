import unittest
from office_space_challenge import Amity, Office, Living, Staff, Fellow


class TestSpaceAndPersonClass(unittest.TestCase):

    def setUp(self):
        self.office = Office('office')
        self.living = Living('living')
        self.staff = Staff('staff')
        self.fellow = Fellow('fellow')

        self.office.set_room()
        self.office.office_dic['office'].extend(
            ['Adam', 'James', 'John', 'Zack', 'Cody', 'Will'])

        self.living.set_room()
        self.living.living_dic['living'].extend(
            ['Jamie', 'George', 'Alex', 'Mike'])

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
            self.living, Living,
            msg="living should be an instance of 'Living' class"
        )

    def test_living_object_type(self):
        self.assertTrue(
            (type(self.living) is Living),
            msg="The object should be a type of 'Living'"
        )

    def test_staff_instance(self):
        self.assertIsInstance(
            self.staff, Staff,
            msg="staff should be an instance of 'Staff' class"
        )

    def test_staff_object_type(self):
        self.assertTrue(
            (type(self.staff) is Staff),
            msg="The object should be a type of 'Staff'"
        )

    def test_fellow_instance(self):
        self.assertIsInstance(
            self.fellow, Fellow,
            msg="fellow should be an instance of 'Fellow' class"
        )

    def test_fellow_object_type(self):
        self.assertTrue(
            (type(self.fellow) is Fellow),
            msg="The object should be a type of 'Fellow'"
        )

    def test_can_return_members_of_office(self):
        members = ['Adam', 'James', 'John', 'Zack', 'Cody', 'Will']
        self.assertEquals(self.office.get_members(
        ), members, msg="The function should return the members in that office")

    def test_can_return_current_size_of_office(self):
        self.assertEquals(self.office.current_size(
        ), 6, msg="The function should return the current number of members in that office")

    def test_can_return_members_of_living(self):
        members = ['Jamie', 'George', 'Alex', 'Mike']
        self.assertEquals(self.living.get_members(
        ), members, msg="The function should return the members in that living space")

    def test_can_return_current_size_of_living(self):
        self.assertEquals(self.living.current_size(
        ), 4, msg="The function should return the current number of members in that living space")


class TestAmityAllocation(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        self.amity.preload()
        self.amity.add_room()
        self.amity.input_parser()
        self.amity.allocation()

        self.office = Office('Carat')
        self.living = Living('Onyx')

    def test_number_of_people_allocated_to_offices(self):
        self.assertLessEqual(
            len(self.office.office_dic['Carat']),
            6, msg="Not more than 6 people can be allocated to carat"
        )

    def test_number_of_people_allocated_to_living(self):
        self.assertLessEqual(
            len(self.living.living_dic['Onyx']),
            4, msg="Not more than 4 people can be allocated to Onyx"
        )

    def test_staff_is_not_allocated_to_living(self):
        with open('input.txt', 'r') as f:
            for line in f:
                line = line.split()
                status = line[3]
                if status == "STAFF":
                    name = line[0] + " " + line[1]
                    self.assertNotIn(
                        name,
                        self.living.living_dic['Onyx'],
                        msg="Staff member cannot be allocated to living space"
                    )

    def test_fellow_with_choice_N_is_not_allocated_to_living(self):
        with open('input.txt', 'r') as f:
            for line in f:
                line = line.split()
                name = line[0] + " " + line[1]
                status = line[3]
                if status == "FELLOW":
                    choice = line[4]
                    if choice == "N":
                        self.assertNotIn(
                            name,
                            self.living.living_dic['Onyx'],
                            msg="%s shouldn't be allocated to living space" % (
                                name)
                        )

    def test_female_is_not_given_male_room(self):
        with open('input.txt', 'r') as f:
            for line in f:
                line = line.split()
                name = line[0] + " " + line[1]
                sex = line[2]
                status = line[3]
                if status == "FELLOW":
                    choice = line[4]
                    if choice == "Y" and sex == "F":
                        self.assertNotIn(
                            name, self.living.living_dic[
                                'Onyx'],
                            msg="%s shouldn't be allocated Onyx" % (name)
                        )

    def test_can_return_staff_list(self):
        self.assertEquals(self.amity.get_staff(), self.amity.staffs_input_list,
                          msg="The function should return an updated list of instances of 'Staff' class")

    def test_can_return_fellow_list(self):
        self.assertEquals(self.amity.get_male_living_fellows(), self.amity.male_input_list,
                          msg="The function should return an updated list of instances of 'Fellow' class")
        self.assertEquals(self.amity.get_fellows_not_living_in_amity(), self.amity.mixed_input_list,
                          msg="The function should return an updated list of instances of 'Fellow' class")



if __name__ == '__main__':
    unittest.main()

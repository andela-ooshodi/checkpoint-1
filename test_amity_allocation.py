import unittest
from amity_allocation import Sorting, Result


class TestOfficeSpaceAllocation(unittest.TestCase):

    def setUp(self):
        self.sorting = Sorting()
        self.sorting.assort()
        self.result = Result()

    def test_number_of_people_allocated_to_offices(self):
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Carat']),
            6, msg="Not more than 6 people can be allocated to Carat"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Anvil']),
            6, msg="Not more than 6 people can be allocated to Anvil"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Crucible']),
            6, msg="Not more than 6 people can be allocated to Crucible"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Kiln']),
            6, msg="Not more than 6 people can be allocated to Kiln"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Forge']),
            6, msg="Not more than 6 people can be allocated to Forge"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Foundry']),
            6, msg="Not more than 6 people can be allocated to Foundry"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Furnace']),
            6, msg="Not more than 6 people can be allocated to Furnace"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Boiler']),
            6, msg="Not more than 6 people can be allocated to Boiler"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Mint']),
            6, msg="Not more than 6 people can be allocated to Mint"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.office_dic['Vulcan']),
            6, msg="Not more than 6 people can be allocated to Vulcan"
        )

    def test_number_of_people_allocated_to_living(self):
        self.assertLessEqual(
            len(self.sorting.amity.rooms.male_living_dic['Topaz']),
            4, msg="Not more than 4 people can be allocated to Topaz"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.male_living_dic['Silver']),
            4, msg="Not more than 4 people can be allocated to Silver"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.male_living_dic['Gold']),
            4, msg="Not more than 4 people can be allocated to Gold"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.male_living_dic['Onyx']),
            4, msg="Not more than 4 people can be allocated to Onyx"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.male_living_dic['Opal']),
            4, msg="Not more than 4 people can be allocated to Opal"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.female_living_dic['Ruby']),
            4, msg="Not more than 4 people can be allocated to Ruby"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.female_living_dic['Platinium']),
            4, msg="Not more than 4 people can be allocated to Platinium"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.female_living_dic['Jade']),
            4, msg="Not more than 4 people can be allocated to Jade"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.female_living_dic['Pearl']),
            4, msg="Not more than 4 people can be allocated to Pearl"
        )
        self.assertLessEqual(
            len(self.sorting.amity.rooms.female_living_dic['Diamond']),
            4, msg="Not more than 4 people can be allocated to Diamond"
        )

    def test_staff_is_not_allocated_to_living(self):
        with open(self.sorting.amity.filename, 'r') as f:
            for line in f:
                line = line.split()
                status = line[3]
                if status == "STAFF":
                    name = line[0] + " " + line[1]
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.male_living_dic['Topaz'],
                        msg="Staff member cannot be allocated to Topaz"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.male_living_dic['Silver'],
                        msg="Staff member cannot be allocated to Silver"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.male_living_dic['Gold'],
                        msg="Staff member cannot be allocated to Gold"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.male_living_dic['Onyx'],
                        msg="Staff member cannot be allocated to Onyx"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.male_living_dic['Opal'],
                        msg="Staff member cannot be allocated to Opal"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.female_living_dic['Ruby'],
                        msg="Staff member cannot be allocated to Ruby"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.female_living_dic[
                            'Platinium'],
                        msg="Staff member cannot be allocated to Platinium"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.female_living_dic['Jade'],
                        msg="Staff member cannot be allocated to Jade"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.female_living_dic['Pearl'],
                        msg="Staff member cannot be allocated to Pearl"
                    )
                    self.assertNotIn(
                        name,
                        self.sorting.amity.rooms.female_living_dic['Diamond'],
                        msg="Staff member cannot be allocated to Diamond"
                    )

    def test_fellow_with_choice_N_is_not_allocated_to_living(self):
        with open(self.sorting.amity.filename, 'r') as f:
            for line in f:
                line = line.split()
                name = line[0] + " " + line[1]
                status = line[3]
                if status == "FELLOW":
                    choice = line[4]
                    if choice == "N":
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.male_living_dic['Topaz'],
                            msg="%s shouldn't be allocated Topaz" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.male_living_dic['Silver'],
                            msg="%s shouldn't be allocated Silver" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.male_living_dic['Gold'],
                            msg="%s shouldn't be allocated Gold" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.male_living_dic['Onyx'],
                            msg="%s shouldn't be allocated Onyx" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.male_living_dic['Opal'],
                            msg="%s shouldn't be allocated Opal" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic['Ruby'],
                            msg="%s shouldn't be allocated Ruby" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic[
                                'Platinium'],
                            msg="%s shouldn't be allocated Platinium" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic['Jade'],
                            msg="%s shouldn't be allocated Jade" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic[
                                'Pearl'],
                            msg="%s shouldn't be allocated Pearl" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic[
                                'Diamond'],
                            msg="%s shouldn't be allocated Diamond" % (name)
                        )

    def test_male_is_not_given_female_room(self):
        with open(self.sorting.amity.filename, 'r') as f:
            for line in f:
                line = line.split()
                name = line[0] + " " + line[1]
                sex = line[2]
                status = line[3]
                if status == "FELLOW":
                    choice = line[4]
                    if choice == "Y" and sex == "M":
                        self.assertNotIn(
                            name, self.sorting.amity.rooms.female_living_dic[
                                'Ruby'],
                            msg="%s shouldn't be allocated Ruby" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic[
                                'Platinium'],
                            msg="%s shouldn't be allocated Platinium" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic['Jade'],
                            msg="%s shouldn't be allocated Jade" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic[
                                'Pearl'],
                            msg="%s shouldn't be allocated Pearl" % (name)
                        )
                        self.assertNotIn(
                            name,
                            self.sorting.amity.rooms.female_living_dic[
                                'Diamond'],
                            msg="%s shouldn't be allocated Diamond" % (name)
                        )


if __name__ == '__main__':
    unittest.main()

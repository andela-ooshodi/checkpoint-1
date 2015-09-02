import unittest
from office_space_allocation import SpaceAllocation 


class TestOfficeSpaceAllocation(unittest.TestCase):

    def setUp(self):
        self.allocate = SpaceAllocation('input.txt')
        self.allocate.allocation()
        self.allocate.unallocated()

    def test_number_of_people_allocated_to_office(self):
        self.assertLessEqual(len(self.allocate.office1), 6,msg="Not more than 6 people can be allocated to office 1")
        self.assertLessEqual(len(self.allocate.office2), 6,msg="Not more than 6 people can be allocated to office 2")
        self.assertLessEqual(len(self.allocate.office3), 6,msg="Not more than 6 people can be allocated to office 3")
        self.assertLessEqual(len(self.allocate.office4), 6,msg="Not more than 6 people can be allocated to office 4")
        self.assertLessEqual(len(self.allocate.office5), 6,msg="Not more than 6 people can be allocated to office 5")
        self.assertLessEqual(len(self.allocate.office6), 6,msg="Not more than 6 people can be allocated to office 6")
        self.assertLessEqual(len(self.allocate.office7), 6,msg="Not more than 6 people can be allocated to office 7")
        self.assertLessEqual(len(self.allocate.office8), 6,msg="Not more than 6 people can be allocated to office 8")
        self.assertLessEqual(len(self.allocate.office9), 6,msg="Not more than 6 people can be allocated to office 9")
        self.assertLessEqual(len(self.allocate.office10), 6,msg="Not more than 6 people can be allocated to office 10")
        
    def test_number_of_people_allocated_to_living(self):
        self.assertLessEqual(len(self.allocate.living1), 4,msg="Not more than 4 people can be allocated to living 1 living space")
        self.assertLessEqual(len(self.allocate.living2), 4,msg="Not more than 4 people can be allocated to living 2 living space")
        self.assertLessEqual(len(self.allocate.living3), 4,msg="Not more than 4 people can be allocated to living 3 living space")
        self.assertLessEqual(len(self.allocate.living4), 4,msg="Not more than 4 people can be allocated to living 4 living space")
        self.assertLessEqual(len(self.allocate.living5), 4,msg="Not more than 4 people can be allocated to living 5 living space")
        self.assertLessEqual(len(self.allocate.living6), 4,msg="Not more than 4 people can be allocated to living 6 living space")
        self.assertLessEqual(len(self.allocate.living7), 4,msg="Not more than 4 people can be allocated to living 7 living space")
        self.assertLessEqual(len(self.allocate.living8), 4,msg="Not more than 4 people can be allocated to living 8 living space")
        self.assertLessEqual(len(self.allocate.living9), 4,msg="Not more than 4 people can be allocated to living 9 living space")
        self.assertLessEqual(len(self.allocate.living10), 4,msg="Not more than 4 people can be allocated to living 10 living space")

    
    def test_staff_is_not_allocated_to_living(self):
        with open(self.allocate.filename, 'r') as f:
            for line in f:
                line = line.split()
                name = line[0] + " " + line[1]
                status = line[3]
                if status == "STAFF":
                    self.assertNotIn(name, self.allocate.living1, msg="Staff member cannot be allocated living 1 living space")
                    self.assertNotIn(name, self.allocate.living2, msg="Staff member cannot be allocated living 2 living space") 
                    self.assertNotIn(name, self.allocate.living3, msg="Staff member cannot be allocated living 3 living space") 
                    self.assertNotIn(name, self.allocate.living4, msg="Staff member cannot be allocated living 4 living space") 
                    self.assertNotIn(name, self.allocate.living5, msg="Staff member cannot be allocated living 5 living space") 
                    self.assertNotIn(name, self.allocate.living6, msg="Staff member cannot be allocated living 6 living space") 
                    self.assertNotIn(name, self.allocate.living7, msg="Staff member cannot be allocated living 7 living space") 
                    self.assertNotIn(name, self.allocate.living8, msg="Staff member cannot be allocated living 8 living space") 
                    self.assertNotIn(name, self.allocate.living9, msg="Staff member cannot be allocated living 9 living space") 
                    self.assertNotIn(name, self.allocate.living10, msg="Staff member cannot be allocated living 10 living space") 

    def test_fellow_with_choice_N_is_not_allocated_to_living(self):
        with open(self.allocate.filename, 'r') as f:
            for line in f:
                line = line.split()
                name = line[0] + " " + line[1]
                status = line[3]
                if status == "FELLOW":
                    choice = line[4]
                    if choice == "N":
                        self.assertNotIn(name, self.allocate.living1, msg="%s shouldn't be allocated living 1 living space" % (name))
                        self.assertNotIn(name, self.allocate.living2, msg="%s shouldn't be allocated living 2 living space" % (name)) 
                        self.assertNotIn(name, self.allocate.living3, msg="%s shouldn't be allocated living 3 living space" % (name))
                        self.assertNotIn(name, self.allocate.living4, msg="%s shouldn't be allocated living 4 living space" % (name)) 
                        self.assertNotIn(name, self.allocate.living5, msg="%s shouldn't be allocated living 5 living space" % (name))
                        self.assertNotIn(name, self.allocate.living6, msg="%s shouldn't be allocated living 6 living space" % (name))
                        self.assertNotIn(name, self.allocate.living7, msg="%s shouldn't be allocated living 7 living space" % (name))
                        self.assertNotIn(name, self.allocate.living8, msg="%s shouldn't be allocated living 8 living space" % (name))
                        self.assertNotIn(name, self.allocate.living9, msg="%s shouldn't be allocated living 9 living space" % (name))
                        self.assertNotIn(name, self.allocate.living10, msg="%s shouldn't be allocated living 10 living space" % (name))

    def test_male_is_not_given_female_room(self):
        with open(self.allocate.filename, 'r') as f:
            for line in f:
                line = line.split()
                name = line[0] + " " + line[1]
                sex = line[2]
                status = line[3]
                if status == "FELLOW":
                    choice = line[4]
                    if choice == "Y" and sex == "M":
                        self.assertNotIn(name, self.allocate.living6, msg="%s shouldn't be allocated living 6 living space" % (name))
                        self.assertNotIn(name, self.allocate.living7, msg="%s shouldn't be allocated living 7 living space" % (name))
                        self.assertNotIn(name, self.allocate.living8, msg="%s shouldn't be allocated living 8 living space" % (name))
                        self.assertNotIn(name, self.allocate.living9, msg="%s shouldn't be allocated living 9 living space" % (name))
                        self.assertNotIn(name, self.allocate.living10, msg="%s shouldn't be allocated living 10 living space" % (name))
        


if __name__ == '__main__':
    unittest.main()

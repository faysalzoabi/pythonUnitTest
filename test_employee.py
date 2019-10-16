import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setup')
        self.emp_1 = Employee('corey', 'faysal', 50000)
        self.emp_2 = Employee('john', 'doe', 60000)

    def tearDown(self):
        print('teardown')

    def test_email(self):
        # emp_1 = Employee('corey', 'faysal', 50000)
        # emp_2 = Employee('john', 'doe', 60000)

        self.assertEqual(self.emp_1.email, 'corey.faysal@email.com')
        self.assertEqual(self.emp_2.email, 'john.doe@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.faysal@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.doe@email.com')

    def test_fullname(self):
        # emp_1 = Employee('corey', 'faysal', 50000)
        # emp_2 = Employee('john', 'doe', 60000)

        self.assertEqual(self.emp_1.fullname, 'corey faysal')
        self.assertEqual(self.emp_2.fullname, 'john doe')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John faysal')
        self.assertEqual(self.emp_2.fullname, 'Jane doe')

    def test_apply_raise(self):
        # emp_1 = Employee('corey', 'faysal', 50000)
        # emp_2 = Employee('john', 'doe', 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/faysal/May')
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()


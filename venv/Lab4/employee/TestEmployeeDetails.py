import unittest
from Lab4.employee.EmployeeDetails import EmployeeDetails
from Lab4.employee.EmpBusinessLogic import EmpBusinessLogic


class TestEmployeeDetails(unittest.TestCase):
    employee = None
    empBusinessLogic = EmpBusinessLogic()
    def setUp(self):
        print("setup!!")
        self.employee = EmployeeDetails()
        self.employee.name = "Rajeev"
        self.employee.age = 25
        self.employee.monthlySalary = 8000

    def tearDown(self):
        print("tear down!!")
        self.employee = None

    def testCalculateYearlySalary(self):
        print("testCalculateYearlySalary")
        salary = self.empBusinessLogic.calculateYearSalary(self.employee)
        self.assertEqual(96000, salary)
    def testCalculateAppraisal(self):
        print("testCalculateAppraisal")
        appraisal = self.empBusinessLogic.calculateAppraisal(self.employee)
        self.assertEqual(500, appraisal)

if __name__ == '__main__':
    unittest.main()

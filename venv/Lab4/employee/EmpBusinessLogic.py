class EmpBusinessLogic:
    def calculateYearSalary(self, employeeDetails):
        yearlySalary = employeeDetails.monthlySalary*12
        return yearlySalary

    def calculateAppraisal(self, employeeDetails):
        appraisal = 0
        if (employeeDetails.monthlySalary < 10000):
            appraisal = 500
        else:
            appraisal = 1000
        return appraisal
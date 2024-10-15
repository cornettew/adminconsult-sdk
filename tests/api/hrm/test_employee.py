import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.hrm import EmployeeList, Employee

def test_get_employees(client_credentials: ClientCredentials):

    admin_employees = EmployeeList(client_credentials)
    admin_employees.get()

    if admin_employees.count > 0:
        employee_id = admin_employees[0].employee_id

        admin_employee = Employee(client_credentials)
        admin_employee.get(employee_id)
        assert admin_employee.employee_id == employee_id
    else:
        # No customers found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0
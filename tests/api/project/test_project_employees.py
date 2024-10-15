import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.project import ProjectEmployeeList, ProjectEmployee, Project, ProjectList
from adminconsult.api.customer import Customer

def test_get_project_contacts(client_credentials: ClientCredentials):

    admin_project_employees = ProjectEmployeeList(client_credentials)
    admin_project_employees.get(max_results=100)

    if admin_project_employees.count > 0:
        project_employee_pk = admin_project_employees[0].project_employee_pk

        admin_project_employee = ProjectEmployee(client_credentials)
        admin_project_employee.get(project_employee_pk)
        assert admin_project_employees[0] == admin_project_employee
    else:
        # No customers found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

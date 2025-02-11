import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.project import ProjectList, Project

def test_get_projects(client_credentials: ClientCredentials):

    admin_projects = ProjectList(client_credentials)
    admin_projects.get(max_results=750)

    if admin_projects.count > 0:
        project_id = admin_projects[0].project_id

        admin_project = Project(client_credentials)
        admin_project.get(project_id)
        assert admin_projects[0] == admin_project
    else:
        # No customers found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0
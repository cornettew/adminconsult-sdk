import json

from tests.api import client_credentials

from adminconsult.api.taskflow import TaskFlowData


def test_get_taskflow_data(client_credentials):
    
    taskflow_data = TaskFlowData(client_credentials, task_id=244)
    taskflow_data.get(11)

    assert taskflow_data.taskdata_id == 11
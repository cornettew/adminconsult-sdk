from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

from adminconsult.api.hrm import EmployeeList

import regex as re
from datetime import datetime
from dateutil import parser

class SubtaskData(Entity):
    '''
    Capture the data of one subtask in a taskflow.

    Every subtask is identified with its subtask_id which is mentioned after the subtask label - "subtask_label (subtask_id)".

    A subtask is composed of 

    * a value
        This can be a string value or a bool value represented by int 0 or 1.
        {
            "name (subtask_id)": "value"
            OR
            "name (subtask_id)": 0 or 1
        }
    * date, optional
        A string value which representent the date on which the task is checked.
        {
            "name (subtask_id) date": 0 or 1
        }
    * who, optional
        A string value returning the username of the Admin Consult user which marked the task.
        {
            "name (subtask_id) who": "      # Admin Username
        }
    '''

    _property_mapping = dict({
        'task_id': {
            'GET': None,
            'POST': None,
            'PUT': 'TaskId'
        },
        'subtask_id': {
            'GET': None,
            'POST': None,
            'PUT': 'SubtaskId'
        },
        'subtask_label': {
            'GET': None,
            'POST': None,
            'PUT': None
        },
        'taskdata_id': {
            'GET': None,
            'POST': None,
            'PUT': 'RecordId'
        },
        'value': {
            'GET': None,
            'POST': None,
            'PUT': 'Value'
        },
        'date': {
            'GET': None,
            'POST': None,
            'PUT': None
        },
        'who': {
            'GET': None,
            'POST': None,
            'PUT': 'UserName'
        }
    })

    def __init__(self, client_credentials, task_id, subtask_id, subtask_label, taskdata_id, subtask_data: dict) -> None:

        # Metadata
        self.task_id = int(task_id)
        self.subtask_id = int(subtask_id)     
        self.subtask_label = subtask_label
        self.taskdata_id = int(taskdata_id)

        # Data
        self.value = None
        self.date = None
        self.who = None
        self._who_enabled = False
        
        super().__init__(client_credentials=client_credentials, 
                         endpoint='taskflow/tasks/{}'.format(self.task_id), 
                         primary_property='record_id-subtask_id', 
                         payload=subtask_data
                         )
    
    def set_attributes(self, payload: dict):
        '''
        Set entity properties based on received payload and property mapping.

        
        '''

        # Interpret values
        self.value = payload['{}({})'.format(self.subtask_label, self.subtask_id)]
        
        if '{}({}) date'.format(self.subtask_label, self.subtask_id) in payload.keys():
            if payload['{}({}) date'.format(self.subtask_label, self.subtask_id)] is not None and not isinstance(payload['{}({}) date'.format(self.subtask_label, self.subtask_id)], datetime):
                self.date = parser.isoparse(payload['{}({}) date'.format(self.subtask_label, self.subtask_id)])
            else:
                self.date = None

        if '{}({}) who'.format(self.subtask_label, self.subtask_id) in payload.keys():
            self.who = payload['{}({}) who'.format(self.subtask_label, self.subtask_id)]
            self._who_enabled = True

    def to_json(self):

        data_json = dict({
            '{}({})'.format(self.subtask_label, self.subtask_id): self.value
            })
        
        if self._who_enabled:
            data_json['{}({}) date'.format(self.subtask_label, self.subtask_id)] = self.date
            data_json['{}({}) who'.format(self.subtask_label, self.subtask_id)] = self.who

        return data_json
    
    def get(self):

        raise AttributeError('Cannot execute GET request on \'{}\' endpoint. '.format(self._endpoint))
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def _update_entity(self):
        
        _ = self._execute_request(method='post', endpoint='{}/update'.format(self._endpoint), payload=self._create_put_payload())

    def update(self, value, employee_id: int=None):

        # Parse bool values
        # Validate username

        if isinstance(value, bool):
            self.value = int(value)
        if isinstance(value, datetime):
            self.value = value.strftime('%Y%m%d')
        else:
            self.value = value

        if self._who_enabled:

            # Validate/set user_name
            if employee_id is None:
                raise Exception('Must pass \'employee_id\' to update subtask.')
            admin_employees = EmployeeList(self._client_credentials, refresh=True)
            admin_employees.get(eq__employee_id=employee_id, eq__employee_active=True)
            self.who = admin_employees[0].login_name

            # Set date to today. Admin Consult will do the same automatically. Setting this avoids refresh after update
            self.date = datetime.now().date().strftime('%Y-%m-%d %H:%M:%S')

        self._update_entity()
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))
    

class TaskFlowData(Entity):
    '''
    Subclass this Class to represent specific/custom taskflows.
    * Set task_id
    * override '.update_subtask(subtask_id=int, value, user_name)' with more meaningful methodnames and valiation of value.
    '''
    
    _task_id: int = None

    taskplanning_id: int = None
    taskdata_id: int = None
    deadline: datetime = None
    project_id: int = None
    customer_id: int = None
    company_id: int = None

    # Add autocompletion 'Subtask' definition ?
    _subtasks: list[SubtaskData] = []

    _property_mapping = dict({
        'taskplanning_id': {
            'GET': 'TaskPlanningId',
            'POST': None,
            'PUT': None
        },
        'taskdata_id': {
            'GET': 'Id',
            'POST': None,
            'PUT': None
        },
        'deadline': {
            'GET': 'Deadline',
            'POST': None,
            'PUT': None
        },
        'project_id': {
            'GET': 'ProjectId',
            'POST': None,
            'PUT': None
        },
        'customer_id': {
            'GET': 'CustomerId',
            'POST': None,
            'PUT': None
        },
        'company_id': {
            'GET': 'company_id',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, task_id, payload=None):

        self._task_id = task_id
        self._subtasks = []

        super().__init__(client_credentials=client_credentials, 
                         endpoint='taskflow/tasks/{}/data'.format(self._task_id), 
                         primary_property='taskdata_id', 
                         payload=payload,
                         datetime_properties=['deadline'])


    # Overriding _get_entity() because of the requirement to pass datefrom and dateuntil
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?datefrom=1900-01-01&dateto=2999-12-31&recordid={}'.format(self._endpoint, id))

        return object[0]

    def get(self, taskdata_id: int):
        return super().get(id=taskdata_id)
    
    def set_attributes(self, payload: dict):

        super().set_attributes(payload=payload)

        for key in [k for k in payload.keys()]:
            # Drop keys which are already mapped. Retaining the keys which represent tasks
            if key in [v['GET'] for v in self._property_mapping.values()]:
                del payload[key]
            elif key in self._property_mapping.keys():
                del payload[key]

        for k in payload.keys():
            self._set_subtask_details(k, payload)

    def _set_subtask_details(self, label, payload):

        # Discard *who and *date labels. These are extra metadata to another task
        if re.match(r'.*(( who)|( date)){1}$', label):
            return

        # Extract subtask id
        subtask_id_matches = re.findall(r'(?<=\({1})[0-9]+(?=\){1})', label)
        if len(subtask_id_matches) != 1:
            raise Exception('Regex search found {} subtask ids in subtask label instead of one. Label = \'{}\''.format(len(subtask_id_matches), list(payload.keys())[0]))

        # Extract subtask label
        subtask_label_matches = re.findall(r'.*(?=\([0-9]+\){1})', label)

        self._subtasks += [SubtaskData(self._client_credentials, self._task_id, subtask_id_matches[0], subtask_label_matches[0], self.taskdata_id, payload)]
    
    def refresh(self):

        self._subtasks = []
        return super().refresh()

    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))
    
    def get_subtask(self, subtask_id: int) -> SubtaskData:
        '''
        Override this method in taskflow specific subclasses to identify subtasks more easily.
        '''

        filtered_sub_tasks = [st for st in self._subtasks if st.subtask_id == subtask_id]

        if len(filtered_sub_tasks) == 1:
            return filtered_sub_tasks[0]
        else:
            raise Exception('{} subtasks founds with \'subtask_id\' = \'{}\''.format(len(filtered_sub_tasks), subtask_id))

    def get_subtask_column_name(self, subtask_id: int) -> str:
        
        st = self.get_subtask(subtask_id)

        return '{}({})'.format(st.subtask_label, st.subtask_id)

    def update_subtask(self, subtask_id: int, value, employee_id: str):
        '''
        Make sure to not write str values to int fields and vice versa ! This will break the taskflow table.
        Override this method in taskflow specific subclasses to enforce data validation.
        '''

        filtered_sub_tasks = [st for st in self._subtasks if st.subtask_id == subtask_id]

        if len(filtered_sub_tasks) == 1:
            subtask = filtered_sub_tasks[0]
            subtask.update(value=value, employee_id=employee_id)
            self.refresh()
        else:
            raise Exception('{} subtasks founds with \'subtask_id\' = \'{}\''.format(len(filtered_sub_tasks), subtask_id))

    # Override to_json to include subtask data.
    def to_json(self):
        ent_json = super().to_json()

        for subtask in self._subtasks:
            ent_json.update(subtask.to_json())
        
        return ent_json


class TaskFlowDataList(EntityCollection):

    _collection: list[TaskFlowData]

    def __init__(self, client_credentials: ClientCredentials, task_id, on_max='ignore', payload=None):

        self._collection = []

        self._task_id = task_id

        super().__init__(client_credentials=client_credentials, endpoint='taskflow/tasks/{}/data'.format(self._task_id), on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[TaskFlowData]:
        return super().__iter__()
    
    def __getitem__(self, item) -> TaskFlowData:
        return super().__getitem__(item=item)

    def _generate_url_filter(self, **value_filters):
        # Override because there is no 'Filter=TaskId eq 15' structure used but '&TaskId=15'

        # Apply filters on GET method
        filters = []

        # Interpret and verify filters
        for k, value in value_filters.items():
            try:
                operator = str(k).split('__')[0]
                attribute = str(k).split('__')[1]
                # Format filter_key
                if operator not in ['eq']:
                    raise Exception('Filter operater must be \'eq\'. Got \'{}\''.format(operator))
                # Format filter_value
                if isinstance(value, str):
                    value = '\'{}\''.format(value)
                elif isinstance(value, datetime):
                    value = value.strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(value, bool) and value:
                    value = 'true'
                elif isinstance(value, bool) and not value:
                    value = 'false'

                filters += ['{}={}'.format(self._search_parameters[attribute], value)]
            except IndexError:
                raise IndexError('Make sure the value_filters follow the structure \'operator__attribute_name\'. Got filter keyword \'{}\''.format(k))
            except KeyError:
                raise AttributeError('{} has no attribute \'{}\'. Therefore the url filter \'{}\' cannot work.'.format(self.__class__.__name__, attribute, k))

        if any(filters):
            return '{}'.format('&'.join(filters))
        else:
            return None
        
    def get(self, date_from: datetime, date_until: datetime, max_results=20000, erase_former=True, **value_filters):
        '''
        'date_from' and 'date_until' are required filters.
        Optional filters such as 'eq__project_id', 'eq__company_id', 'eq__taskdata_id' can be passed as kwargs.
        '''

        super().get(max_results=max_results, eq__date_from=date_from, eq__date_until=date_until, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [TaskFlowData(self._client_credentials, task_id=self._task_id, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = {'date_from': 'datefrom', 
                                   'date_until': 'dateto', 
                                   'project_id': 'projectid',
                                   'company_id': 'companyid',
                                   'taskdata_id': 'recordid',
                                   'language': 'language'}

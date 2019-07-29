import os
from todoist.api import TodoistAPI


class TodoistApiCall:
    def __init__(self):
        self.api_key = os.environ.get("API_KEY")
        self.api_call = TodoistAPI(self.api_key)
        self.api_call.sync()

    def list_projects_names(self):
        for project in range(len(self.api_call.state['projects'])):
            print(self.api_call.state['projects'][project].data['name'])

    def find_project_id(self, project_name):
        api_call = TodoistAPI(self.api_key)
        api_call.sync()
        for project in range(len(api_call.state['projects'])):
            if api_call.state['projects'][project].data['name'].lower() == project_name.lower():
                return api_call.state['projects'][project].data['id']

    def list_project_tasks(self, project_id):
        api_call = TodoistAPI(self.api_key)
        api_call.sync()
        for item in range(len(api_call.state['items'])):
            if api_call.state['items'][item].data['project_id'] == project_id:
                print(api_call.state['items'][item].data['content'])

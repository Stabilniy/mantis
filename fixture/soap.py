from suds.client import Client
class SoapHelper:

    def __init__(self, app, base_url):
        self.app = app
        self.base_url = base_url

    def get_project_list(self, username, password):
        base_url = self.base_url
        client = Client(base_url + "/api/soap/mantisconnect.php?wsdl")
        return client.service.mc_projects_get_user_accessible(username, password)

    def login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        return client.service.mc_login(username, password)




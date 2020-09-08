from Modules.Project import Project

class ProjectHelper:
    def __init__(self, app, base_url):
        self.app = app
        self.base_url = base_url

    def new_project_creation(self, project):
        wd = self.app.wd
        self.project_manage_page()
        wd.find_element_by_xpath("//td[@class='form-title']//input[@class='button-small']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").send_keys(project.project_name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@class='button']").click()

    def project_manage_page(self):
        wd = self.app.wd
        base_url = self.base_url
        wd.get(base_url + "/manage_proj_page.php")

    def project_count(self):
        wd = self.app.wd
        return (len(wd.find_elements_by_xpath("//table[@class='width100']//tr")))


    def get_project_list(self):
        wd = self.app.wd
        self.project_manage_page()
        project_list = []
        list_tr = wd.find_elements_by_xpath("//table[@class='width100']//tr")
        for row in list_tr[3:]:
            cell = row.find_elements_by_tag_name("td")
            project_name= cell[0].text
            id_str = str(cell[0].find_element_by_tag_name("a").get_attribute("href"))
            long = len(id_str)
            point = id_str.index("=")
            dif = long - point
            id = id_str[-dif+1:]
            description = cell[4].text
            project_list.append(Project(id=id, project_name=project_name, description=description))
        return project_list

    def get_project_list_soap(self):
        project_list_soap = []
        l = self.app.soap.get_project_list("administrator", "root")
        for i in l:
            project_list_soap.append(Project(id=i.id, project_name=i.name, description=i.description))
        return project_list_soap

    def delete_project_by_id(self, id):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_edit_page.php?project_id=%s"%id)
        wd.find_element_by_xpath("//div[@class='border center']//input[@class='button']").click()
        wd.find_element_by_xpath("//input[@class='button']").click()












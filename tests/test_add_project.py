from Modules.Project import Project
import random
import string

def test_add_new_project(app):
    symbols = string.ascii_letters + string.digits
    project_name = '_'.join([random.choice(symbols) for i in range(random.randrange(10))])
    description = '_'.join([random.choice(symbols) for i in range(random.randrange(10))])
    #project_list_soap = []
    #base_url = app.base_url
    #l = app.soap.get_project_list(base_url, "administrator", "root")
    #for i in l:
    #    project_list_soap.append(Project(id=i.id, project_name=i.name, description=i.description))
        #return project_list_soap

    old_project_list = app.project.get_project_list_soap()
    #old_project_list = project_list_soap
    project = Project(project_name = project_name, description=description)
    app.project.new_project_creation(project)
    old_project_list.append(project)
    new_project_list = app.project.get_project_list_soap()
    assert sorted(old_project_list, key =Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)




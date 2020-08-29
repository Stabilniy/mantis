from Modules.Project import Project
import random
import string

def test_delet_project(app):
    if app.project.project_count() < 3:
        symbols = string.ascii_letters + string.digits
        project_name = '_'.join([random.choice(symbols) for i in range(random.randrange(10))])
        description = '_'.join([random.choice(symbols) for i in range(random.randrange(10))])
        project = Project(project_name = project_name, description=description)
        app.project.new_project_creation(project)
    old_project_list = app.project.get_project_list_soap()
    project = random.choice(old_project_list)
    app.project.delete_project_by_id(project.id)
    new_project_list = app.project.get_project_list_soap()
    old_project_list.remove(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)

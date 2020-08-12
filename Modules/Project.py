from sys import maxsize

class Project:
    def __init__(self, id = None, project_name = None, description = None):
        self.id = id
        self.project_name = project_name
        self.description = description


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.project_name, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize



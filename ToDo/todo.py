class Task:
    pass

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return "{}".format(self.description)


task1 = Task("Lalala", "now?")
task2 = Task("Babababba", "nowie?")
task3 = Task("Gaggaga", "noooooow?")
print(task1)


class TodoList:
    pass

    # tasks = []

    def __init__(self, tasks=[]):
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)
        return "task added?"


list1 = TodoList()
print(list1.add_task(task1))
print(list1.tasks)

from django.db import models


ROLE = (
    ('m', 'Manager'),
    ('d', 'Deputy'),
    ('n', None),
)

class Project(models.Model):
    msu = models.CharField(max_length=10)
    code = models.CharField(max_length=10)

    def __str__(self):
        return "code: {}, msu: {}".format(self.code, self.msu)

class Group(models.Model):
    msu = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

    def __str__(self):
        return "msu: {}, name: {}".format(self.name, self.msu)

class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=ROLE)
    group = models.ForeignKey(Group)

    def __str__(self):
        return "name: {}, surname: {}".format(self.name, self.surname)

class Allocation(models.Model):
    project = models.ForeignKey(Project)
    person = models.ForeignKey(Person)

    def __str__(self):
        return "project: {}, person: {}".format(self.project.code, self.person.name)

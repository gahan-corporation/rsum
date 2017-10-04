#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test class for the entry item test case."""
from __future__ import unicode_literals

from django.test import TestCase
from django.apps import apps

from home.models.cv import CV 
from home.models.section import Section
from home.models.subsection import SubSection
from home.models.project import Project
from home.models.projectitem import ProjectItem
from home.models.entry import Entry
from home.models.entryitem import EntryItem
from rsum.settings.rsum import values

import socket
import yaml


class EntryItemTestCase(TestCase):
    """EntryItemTestCase class."""
    def setUp(self):
        """Setup the EntryItemTestCase."""
        s = values.get(socket.gethostname())
        f = open('/srv/rsum/cvs/{0}/{1}.yml'.format(s.get('dir'), s.get('name')))
        abridged = yaml.load(f.read())
        f.close()

        cv = CV()
        cv.name = 'abridged'
        cv.save()

        for name, section in sorted(
            abridged.items(),
            key=lambda t: t[1].get('id')
        ): 
            if isinstance(section, str):
                pass
            else:
                s = Section()
                s.cv = cv
                s.name = name
                s.content = type(section)
                s.save()
                ss = SubSection()
                ss.name = 'ptest'
                ss.section = s
                ss.save()
                p = Project()
                p.name = "pitest"
                p.content = type(dict())
                p.sub_section = ss
                p.save()
                pi = ProjectItem()
                pi.content = type(dict())
                pi.project = p
                pi.save()
                e = Entry()
                e.content = type(list()) 
                e.projectitem = pi
                e.save()
                self.e = e

    def test_save_entry_item(self):
        """Test saving an EnryItem."""
        e = self.e
        entry_item_string = str("this is a string")
        entry_item_list = [
            'this',
            'is',
            'a',
            'list',
            'of',
            'strings'
        ]

        ei = EntryItem()
        ei.entry = e
        ei.value = 'this is a different string'
        ei.save()

        ei = EntryItem()
        ei_result = ei.save_list_item(entry_item_string, e)
        self.assertEqual(
            list(ei_result),
            list(EntryItem.objects.values())
        )

        ei_result = ei.save_list_item(entry_item_list, e)
        self.assertEqual(
            list(ei_result),
            list(EntryItem.objects.values())
        )


class GetEntryItemTestCase(TestCase):
    """Test class for EntryItem get methods."""
    def setUp(self):
        """Setup testing for EntryItem get methods."""
        cv_instance = CV()
        cv_id = cv_instance.check_sections(name_of_owner='alex', name_of_cv='abridged', template='acecv')
        sections = Section.objects.filter(cv=cv_instance)
        subsections = [list(SubSection.objects.filter(section=section)) for section in sections]
        projects = []
        for subsection in subsections:
            for subsection_object in subsection:
                project = list(Project.objects.filter(
                    sub_section=subsection_object
                ))
                projects.append(project)
        projectitems = []
        for project in projects:
            for project_object in project:
                projectitem = list(ProjectItem.objects.filter(
                    project=project_object
                )) 
                projectitems.append(projectitem)
        entries = []
        for projectitem in projectitems:
            for projectitem_object in projectitem:
                entry = list(Entry.objects.filter(
                    projectitem=projectitem_object
                ))
                entries.append(entry)
        entryitems = []
        for index,entry in enumerate(entries):
            entryitem = list(EntryItem.objects.filter(
                entry=index
            ))
            entryitems.append(entryitem)
        self.entryitems = entryitems
        self.entries = entries

    def test_get_entry_item(self):
        """Test getting an EntryItem. """
        entries = self.entries
        entryitems = []
        for index, entry in enumerate(entries):
            entryitem = list(EntryItem.objects.filter(
                entry=index
            ))
            entryitems.append(entryitem)
        self.assertEqual(
            self.entryitems,
            entryitems
        )
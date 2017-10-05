#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for class that defines SubSection objects."""
from collections import OrderedDict

from django.db import models
from django.contrib.postgres.fields import JSONField

from sub_section_item import SubItem 

import json


class SubSection(models.Model):
    """Class to define SubSection objects.

    .. attribute:: section

       Related :obj:`home.models.section.Section` object.

    .. attribute:: name

       Name of SubSection.

    .. attribute:: content

       Content for SubSection.
    """
    section = models.ForeignKey(
        'home.Section', 
        on_delete=models.CASCADE,
        related_name='section'
    )
    name = models.CharField(max_length=200)
    content = JSONField()

    @classmethod
    def create(cls, name='default', *args, **kwargs):
        """Class method to handle creation of SubSection objects for testing.
        
        :param cls: The SubSection class.
        :type cls: :obj:`home.models.subsection.SubSection`
        :param str name: Name of the sub section.
        :param str content: Content for the sub section.
        :return: Reference to the created SubSection.
        :rtype: :obj:`home.models.subsection.SubSection`
        """
        sub_items = {}
        content = kwargs.get('content')
        section = kwargs.get('section')
        sub_section = cls(name=name, content=content, section=section)
        sub_section.save()

        if (isinstance(content, str) or
            isinstance(content, int)):
            SubItem.create(name=name, content=content, sub_section=sub_section)
            return sub_section 

        if (isinstance(content, list)):
            for index,item in enumerate(content):
                SubItem.create(
                    name=index,
                    content=item,
                    sub_section=sub_section)
            return sub_section

        try:
            temp_list = [sub_item for name, sub_item in content.items()]
            print(temp_list)
            sub_items = OrderedDict(
                sorted(temp_list, key=lambda k: k.get('id'))
            )
            print(sub_items)
        except:
            sub_items = content.items()

        for name, sub_item in content.items():
            SubItem.create(
                name=name,
                content=sub_item,
                sub_section=sub_section)        

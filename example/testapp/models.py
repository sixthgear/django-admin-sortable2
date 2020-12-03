# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Author(models.Model):
    name = models.CharField('Name', null=True, blank=True, max_length=255)
    notes = GenericRelation('testapp.Notes')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SortableBook(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    notes = GenericRelation('testapp.Notes')

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    book = models.ForeignKey(SortableBook, null=True, on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return 'Chapter: {0}'.format(self.title)

    def __unicode__(self):
        return 'Chapter: {0}'.format(self.title)


class Notes(models.Model):
    note = models.CharField('Note', null=True, blank=True, max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    my_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['my_order']
        verbose_name = 'note'
        verbose_name_plural = 'notes'

    def __str__(self):
        return 'Note: {0}'.format(self.note)

    def __unicode__(self):
        return 'Note: {0}'.format(self.note)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from . import models


class ChapterInline(SortableInlineAdminMixin, admin.StackedInline):
    model = models.Chapter
    extra = 1


class NotesInline(SortableInlineAdminMixin, GenericTabularInline):
    model = models.Notes
    extra = 1


@admin.register(models.SortableBook)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_per_page = 12
    list_display = ['author', 'title', 'my_order']
    list_display_links = ['title']
    inlines = [ChapterInline, NotesInline]


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [NotesInline]

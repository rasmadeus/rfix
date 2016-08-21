from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as tr


class Page(models.Model):
    lang = models.CharField(max_length=2)
    desc = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    @staticmethod
    def guest_default():
        page = Page()
        page.lang = tr('en')
        page.title = tr('RFIX is a lightweight bug tracker')
        page.desc = tr('RFIX is a lightweight bug tracker')
        page.keywords = tr('RFIX, bugtracker')
        page.author = tr('K. Kulikov')
        return page

    def head(self):
        meta = '<meta name="{name}" content="{content}">'
        tags = [meta.format(name=name, content=content)
            for name, content in (
                ('description', self.desc),
                ('keywords', self.keywords),
                ('author', self.author),
            )
        ]
        tags.append('<title>{title}</title>'.format(title=self.title))
        return '\n'.join(tags)

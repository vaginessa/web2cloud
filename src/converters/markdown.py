#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base_converter import BaseConverter


class Markdown(BaseConverter):
    def title(self, text):
        return '# %s\n' % text

    def text(self, text):
        return '%s\n' % text

    def image(self, src):
        return '![Alt text](%s)\n' % src

    def list_item(self, text):
        return '- %s\n' % text
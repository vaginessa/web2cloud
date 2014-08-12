#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import datetime

import models


class FeedParser(object):
    def parse(self, url, adapter):
        parsed = self._parse(url)
        entries = self._create_entries(parsed, adapter)
        return entries

    @staticmethod
    def _parse(url):
        return feedparser.parse(url).entries

    def _create_entries(self, parsed, adapter):
        entries = list()
        for x in parsed:
            entry = self._new_entry(x)
            entry.sections = adapter.adapt(entry.content)
            entries.append(entry)
        return entries

    @staticmethod
    def _new_entry(parsed):
        return models.Entry(
            content      = parsed.content[0].value,
            id           = parsed.id,
            title        = parsed.title,
            summary      = parsed.summary,
            tags         = [x.term for x in parsed.tags],
            # 9-valued tuple: ( year, month, day, hour, minute, second, day of week, day of year, dst-flag )
            # (Ref: http://stackoverflow.com/questions/686717/python-convert-9-tuple-utc-date-to-mysql-datetime-format)
            published_at = datetime.datetime(*(parsed.published_parsed[:6]))
        )
#  Copyright 2008-2011 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from robot import utils


class TestSuite(object):

    def __init__(self, parent=None, source='', name='', doc='', metadata=None,
                 status='PASS'):
        self.parent = parent
        self.source = source
        self.name = name
        self.doc = doc
        self.metadata = metadata
        self.status = status
        self.message = ''
        self.keywords = []
        self.suites = []
        self.tests = []
        self.starttime = ''
        self.endtime = ''
        self.elapsedtime = ''

    def _get_metadata(self):
        return self._metadata
    def _set_metadata(self, metadata):
        self._metadata = utils.NormalizedDict(hmetadata, ignore=['_'])
    metadata = property(_get_metadata, _set_metadata)


class TestCase(object):

    def __init__(self, parent=None, name='', doc='', tags=None, status='PASS'):
        self.parent = parent
        self.name = name
        self.doc = doc
        self.tags = tags
        self.status = status
        self.message = ''
        self.timeout = ''
        self.critical = True
        self.keywords = []
        self.starttime = ''
        self.endtime = ''
        self.elapsedtime = ''

    tags = property(lambda self: self._tags,
                    lambda self, tags: setattr(self, '_tags', Tags(tags)))


class Tags(object):

    def __init__(self, tags=None):
        if isinstance(tags, basestring):
            tags = [tags]
        self._tags = utils.normalize_tags(tags or [])

    def add(self, tags):
        self._tags = utils.normalize_tags(list(self) + list(Tags(tags)))

    def remove(self, tags):
        tags = Tags(tags)
        self._tags = [t for t in self if t not in tags]

    def __contains__(self, tag):
        return utils.eq_any(tag, list(self), ignore=['_'])

    def __len__(self):
        return len(self._tags)

    def __iter__(self):
        return iter(self._tags)

    def __unicode__(self):
        return u'[%s]' % ', '.join(self)

    def __str__(self):
        return unicode(self).encode('UTF-8')


class Keyword(object):

    def __init__(self, name='', doc='', status='PASS', type='kw'):
        self.name = name
        self.doc = doc
        self.status = status
        self.type = type
        self.args = []
        self.messages = []
        self.keywords = []
        self.children = []
        self.starttime = ''
        self.endtime = ''
        self.elapsedtime = ''
        self.timeout = ''
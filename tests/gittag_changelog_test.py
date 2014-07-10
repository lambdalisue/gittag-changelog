#!/usr/bin/env nosetests
# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import os
import imp
try:
    import mock
except ImportError:
    from unittest import mock

gittag_changelog_file = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'src/gittag_changelog.py'
)
gittag_changelog = imp.load_source('gittag_changelog', gittag_changelog_file)


def test_doctest():
    import doctest
    doctest.testmod(gittag_changelog, verbose=True, raise_on_error=True)


def test_gittag_changelog():
    def side_effect(popenargs, **kwargs):
        if popenargs[:2] == ['git', 'config']:
            return (
                "git@github.com:lambdalisue/vim-gista.git\n"
            )
        elif popenargs[:2] == ['git', 'tag']:
            return (
                "v0.1.0\n"
                "v0.1.10\n"
                "v0.1.2\n"
                "v0.1.3\n"
            )
        elif popenargs[:2] == ['git', 'show']:
            return (
                "tag {}\n"
                "Tagger: Alisue <lambdalisue@hashnote.net>\n"
                "Date:   Tue Jul 1 17:26:48 2014 +0900\n"
                "\n"
                "Commit comment\n"
            ).format(popenargs[2])
        elif popenargs[:2] == ['git', 'log']:
            return (
                "- Fixed #29 (Mon Jul 7 18:32:12 2014 +0900) "
                "[0dfa117](https://github.com/lambdalisue/vim-gista/"
                "commit/0dfa11777ea235df695bb7e1674eec296f5cb8be)\n"
                "- Fixed #30 (Mon Jul 7 18:41:08 2014 +0900) "
                "[ed96f7f](https://github.com/lambdalisue/vim-gista/"
                "commit/ed96f7faa0e1079a78c8bb60f74111d1e547d2f2)\n"
                "- Merge branch 'issue30' (Mon Jul 7 18:41:26 2014 +0900) "
                "[f8dad73](https://github.com/lambdalisue/vim-gista/"
                "commit/f8dad7386e11d0f440cf0bdf75ea77f538ee6773)\n"
                "- Bump version (Mon Jul 7 18:41:50 2014 +0900) "
                "[7418491](https://github.com/lambdalisue/vim-gista/"
                "commit/741849115d0d51c3e476b30f7d2e694bf7e82ebc)\n"
            )
    with mock.patch('subprocess.check_output', side_effect=side_effect):
        changelogs = list(gittag_changelog.iterate_changelogs(
            'repository directory'))
        # if no exception raised, it mean success.


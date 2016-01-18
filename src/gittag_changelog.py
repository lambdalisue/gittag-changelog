#!/usr/bin/env python
# coding=utf-8
"""
A simple script to create a changelog from git tags.

License: MIT license
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
__version__ = '0.1.0'
import os
import re
import subprocess

VERSION = __version__.split('.')


def natsorted(l):
    """
    Naturally sort a specified iterable

    >>> example = ('v0.1.0', 'v0.1.10', 'v0.1.2')
    >>> natsorted(example)
    ['v0.1.0', 'v0.1.2', 'v0.1.10']
    """
    pattern = re.compile(r'[^\d]+')
    extract_digits = lambda x: list(
        map(int, [s for s in pattern.split(x) if s])
    )
    return sorted(l, key=extract_digits)


def parse_info_output(output):
    """
    Parse `git info` and return github username and repository name

    >>> example = "git@github.com:lambdalisue/vim-gista.git"
    >>> parse_info_output(example)
    ('lambdalisue', 'vim-gista')
    """
    patterns = (
        r'git@github.com:([^/]+)/([^\s]+)',
        r'ssh://git@github.com/([^/]+)/([^\s]+)',
    )
    for pattern in patterns:
        m = re.search(pattern, output)
        if m:
            # Note: repository_name should not include '.git'
            return m.group(1), os.path.splitext(m.group(2))[0]
    # Non github repository
    return None, None


def parse_show_output(output):
    """
    Parse `git show <name>` and return the date.

    >>> example = '''
    ... tag v0.1.0
    ... Tagger: Alisue <lambdalisue@hashnote.net>
    ... Date:   Tue Jul 1 17:26:48 2014 +0900
    ...
    ... The followings are commit comments but quite similar to the meta
    ... informations above. These should not be influence the return value.
    ... Tagger: Invalid
    ... Date:   Invalid
    ... '''
    >>> parse_show_output(example)
    'Tue Jul 1 17:26:48 2014 +0900'
    """
    date = re.search(r'Date:\s+(.*)', output).group(1)
    return date


def iterate_changelogs(repository):
    # shortcut lambda function
    call = lambda popenargs: subprocess.check_output(
        popenargs, stderr=subprocess.STDOUT, cwd=repository
    ).decode('utf8')

    # get repository information
    username, repository_name = parse_info_output(
        call(['git', 'config', '--get', 'remote.origin.url'])
    )
    if username and repository_name:
        # URL of the commit on GitHub
        url = "https://github.com/{}/{}/commit/%H".format(
            username, repository_name
        )
        # pretty:format
        commitfmt = "- %s (%ad) [%h]({})".format(url)
    else:
        # Non github repository
        # pretty:format
        commitfmt = "- %s (%ad) %h"

    # get tagged versions
    versions = call(['git', 'tag']).splitlines()
    versions = natsorted(versions)
    versions.append('HEAD')

    previous = versions[0]
    for version in versions[1:]:
        version_date = parse_show_output(call(['git', 'show', version]))
        # get commits from previous version to this version
        commits = call([
            'git', 'log', '{}...{}'.format(previous, version),
            '--pretty=format:{}'.format(commitfmt),
            '--reverse'
        ])
        yield "### {} ({})\n\n{}\n".format(version, version_date, commits)
        previous = version


def unittest():
    import doctest
    doctest.testmod()


def console_main(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository',
                        default=os.path.curdir,
                        help=("A target git repository path"))
    parser.add_argument('--order',
                        choices=('asc', 'desc'),
                        default='desc',
                        help=("The changelog appearance order"))

    args = parser.parse_args(args)
    changelogs = list(iterate_changelogs(args.repository))
    if args.order == 'desc':
        changelogs = reversed(changelogs)

    for changelog in changelogs:
        print(changelog)


if __name__ == '__main__':
    console_main()

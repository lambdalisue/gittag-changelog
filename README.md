gittag-changelog
===============================================================================
[![Travis CI](https://secure.travis-ci.org/lambdalisue/gittag-changelog.png?branch=master)](http://travis-ci.org/lambdalisue/gittag-changelog)
[![Coveralls](https://coveralls.io/repos/lambdalisue/gittag-changelog/badge.png?branch=master)](https://coveralls.io/r/lambdalisue/gittag-changelog/)

Author
    Alisue <lambdalisue@hashnote.net>
Supported python versions
    Python 2.6, 2.7, 3.2, 3.3

gittag-changelog is a small script to create a markdown formatted changelog from git tags.
A generated changelog looks like:

```
### v0.1.15 (Mon Jul 7 20:33:49 2014 +0900)

- Add a way to reopen a gist without using cache (Mon Jul 7 20:32:56 2014 +0900) [85be809](https://github.com/lambdalisue/vim-gista/commit/85be809bbd954dae4ba99ad607ad045d1d1e527a)
- Bump version (Mon Jul 7 20:33:28 2014 +0900) [02ddd7e](https://github.com/lambdalisue/vim-gista/commit/02ddd7e12e913bf7b3dec8546547805fe8a4525c)

### v0.1.14 (Mon Jul 7 18:42:04 2014 +0900)

- Fixed #29 (Mon Jul 7 18:32:12 2014 +0900) [0dfa117](https://github.com/lambdalisue/vim-gista/commit/0dfa11777ea235df695bb7e1674eec296f5cb8be)
- Fixed #30 (Mon Jul 7 18:41:08 2014 +0900) [ed96f7f](https://github.com/lambdalisue/vim-gista/commit/ed96f7faa0e1079a78c8bb60f74111d1e547d2f2)
- Merge branch 'issue30' (Mon Jul 7 18:41:26 2014 +0900) [f8dad73](https://github.com/lambdalisue/vim-gista/commit/f8dad7386e11d0f440cf0bdf75ea77f538ee6773)
- Bump version (Mon Jul 7 18:41:50 2014 +0900) [7418491](https://github.com/lambdalisue/vim-gista/commit/741849115d0d51c3e476b30f7d2e694bf7e82ebc)

### v0.1.13 (Mon Jul 7 18:09:56 2014 +0900)

- Add 'disable_python_client' option (Mon Jul 7 17:36:07 2014 +0900) [023cd8c](https://github.com/lambdalisue/vim-gista/commit/023cd8c3a8687197e44239d7d280fd651ca38877)
- Bump version (Mon Jul 7 18:09:42 2014 +0900) [5d5c521](https://github.com/lambdalisue/vim-gista/commit/5d5c521a77d5708b0d172305559369b798d31084)

...

### v0.1.2 (Wed Jul 2 03:57:26 2014 +0900)

- Fixed #14 (Wed Jul 2 03:48:58 2014 +0900) [69abfd2](https://github.com/lambdalisue/vim-gista/commit/69abfd264b0a85c4c54cd04d2a99e943248a8513)
- Fixed #15 (Wed Jul 2 03:55:20 2014 +0900) [7e26881](https://github.com/lambdalisue/vim-gista/commit/7e26881f8071973924fbf762db86faf81f3fc697)
- Fixed #13 (Wed Jul 2 03:56:33 2014 +0900) [139ffe1](https://github.com/lambdalisue/vim-gista/commit/139ffe1b97ba96f415125c7c887b67d723dfc225)
- Bump version (Wed Jul 2 03:57:12 2014 +0900) [1166a7d](https://github.com/lambdalisue/vim-gista/commit/1166a7d9a619549c4f3aa0f30419cc2c001102f1)

### v0.1.1 (Wed Jul 2 03:05:18 2014 +0900)

- Change unite strategy (Wed Jul 2 00:19:42 2014 +0900) [bc3422c](https://github.com/lambdalisue/vim-gista/commit/bc3422c8908cd1d75ce5a324241db296ae5a1458)
- Improve documentations for new implementations (Wed Jul 2 03:03:09 2014 +0900) [9532413](https://github.com/lambdalisue/vim-gista/commit/95324138acd6182af7a3e9f8c371ff9a5dd8372c)
- Bump version (Wed Jul 2 03:04:57 2014 +0900) [1c176a9](https://github.com/lambdalisue/vim-gista/commit/1c176a9bbc02519f14aa85f44182e913996822e6)
```


Install
===============================================================================

With wget (Ubuntu, Debian, ...etc)
-------------------------------------------------------------------------------
Run the following command.

```sh
$ wget http://goo.gl/vVh6PN -O - | sh
```

With cURL (Mac OS X, Cent OS, ...etc)
-------------------------------------------------------------------------------
Run the following command.

```sh
$ curl http://goo.gl/vVh6PN | sh
```

Without using one liner installer (Windows)
-------------------------------------------------------------------------------
1.  Clone this repository to `~/.gista-changelog`:

    ```sh
    $ git clone https://github.com/lambdalisue/gittag-changelog ~/.gittag-changelog
    ```

2.  Add `changelog` alias to git:

    ```sh
    $ git config --global --add alias.changelog "!python $HOME/.gittag-changelog/src/gittag_changelog.py"
    ```

Usage
===============================================================================
1.  Make sure that you are in git repository and the repository have several tags like below:

    ```sh
    $ git tag
    v0.1.0
    v0.1.10
    v0.1.2
    v0.1.3
    v0.1.4
    v0.1.5
    v0.1.6
    v0.1.7
    v0.1.8
    v0.1.9
    ```

    If you don't have any tags, create it with `git tag -a 'v0.1.0' -m "Version 0.1.0"` or so on.
    gittag-changelog requires at least two tags.

2.  Run `changelog` alias as:

    ```sh
    $ git changelog
    ```

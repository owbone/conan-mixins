'''ConanFile mixins for Git functionality.'''


class GitMixin(object):
    '''ConanFile mixin to simplify cloning source code from a Git repository.

    The derived class must define:
        - GIT_REPO as the Git repository url
        - GIT_TAG as the tag/branch/sha1 to checkout

    The repository will be cloned alongside the existing files in the current
    directory.
    '''
    def source(self):
        self.__clone(self.GIT_REPO, self.GIT_TAG)

    def __git(self, *args):
        self.run('git {}'.format(' '.join(args)))

    def __clone(self, repo, tag):
        self.__git('init .')
        self.__git('remote add -t \* -f origin', '{}'.format(repo))
        self.__git('checkout {}'.format(tag))
        self.__git('submodule update --recursive')

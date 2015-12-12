'''ConanFile mixins for CMake functionality.'''

from conans import CMake


class CMakeMixin(object):
    '''ConanFile mixin to simplify building and packaging CMake projects.

    The derived class may define:
        - CMAKE_CONFIGURE_ARGS: a tuple of extra arguments to pass to cmake
          during configuration (default: ()).
        - CMAKE_BUILD_ARGS: a tuple of extra arguments to pass to cmake
          during building (default: ()).
        - CMAKE_RUN_TESTS: a boolean to enable or disable automatically running
          ctest (default: False).

    The derived class may override the package() function to override the
    default "install and copy" step.
    '''
    INSTALL_PREFIX = '/'
    INSTALL_DIR = 'root'

    def build(self):
        self.__configure(
            CMake(self.settings),
            '-DCMAKE_INSTALL_PREFIX:PATH={}'.format(self.INSTALL_PREFIX),
            *getattr(self, 'CMAKE_CONFIGURE_ARGS', ())
        )
        self.__build(
            CMake(self.settings),
            *getattr(self, 'CMAKE_BUILD_ARGS', ())
        )

        if getattr(self, 'CMAKE_RUN_TESTS', False):
            self.run('ctest')

    def package(self):
        self.__cmake(
            '--build . --target install',
            '-- DESTDIR={}'.format(self.INSTALL_DIR)
        )
        self.copy(pattern='*', dst='', src=self.INSTALL_DIR)

    def __cmake(self, *args):
        self.run('cmake {}'.format(' '.join(args)))

    def __configure(self, cmake, *args):
        self.__cmake('.', cmake.command_line, *args)

    def __build(self, cmake, *args):
        self.__cmake('--build .', cmake.build_config, *args)

# conan-mixins

Python mixins to simplify creation of [Conan](https://conan.io/) packages.

## Mixins

 * **GitMixin** for automatically cloning source code from a Git repository.
 * **CMakeMixin** for automatically building, testing and installing a CMake project.

## Example

This example uses the above mixins to produce a Conan package for [cppformat](https://github.com/cppformat/cppformat.git) 2.0.0. The `source` step is taken care of by `GitMixin` and the `build` and `package` steps are taken care of by the `CMakeMixin`.

```python
from conans import ConanFile
from mixins import CMakeMixin, GitMixin

class CppFormat(GitMixin, CMakeMixin, ConanFile):
    name = 'cppformat'
    version = '2.0.0'
    settings = 'os', 'compiler', 'build_type', 'arch'

    # Configure GitMixin
    GIT_REPO = 'https://github.com/cppformat/cppformat.git'
    GIT_TAG = 'tags/{}'.format(version)

    # Configure CMakeMixin
    CMAKE_RUN_TESTS = True
```

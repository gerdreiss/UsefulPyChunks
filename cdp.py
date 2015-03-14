#!/usr/local/bin/python
# add this to .bashrc and then use as follows:
# > cdp os
cdp () {
    cd '$(python -c "import os.path as _, ${1}; print(_.dirname(_.realpath(${1}.__file__[:-1])))")'
}
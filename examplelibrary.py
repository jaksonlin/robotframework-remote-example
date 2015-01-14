#!/usr/bin/env python

import os


class ExampleRemoteLibrary(object):

    def count_items_in_directory(self, path):
        """Returns the number of items in the directory specified by `path`."""
        return len([i for i in os.listdir(path) if not i.startswith('.')])

    def strings_should_be_equal(self, str1, str2):
        print "Comparing '%s' to '%s'." % (str1, str2)
        if not (isinstance(str1, basestring) and isinstance(str2, basestring)):
            raise AssertionError("Given strings are not strings.")
        if str1 != str2:
            raise AssertionError("Given strings are not equal.")


if __name__ == '__main__':
    import sys
    from robotremoteserver import RobotRemoteServer

    RobotRemoteServer(ExampleRemoteLibrary(), *sys.argv[1:])
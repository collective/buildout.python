def test(options, buildout):
    from subprocess import Popen, PIPE
    import os
    import sys

    python = options['python']
    if not os.path.exists(python):
        raise IOError("There is no file at %s" % python)
    if sys.platform == 'darwin':
        output = Popen([python, "-c", "import platform; print (platform.mac_ver())"], stdout=PIPE).communicate()[0]
        if not output.startswith("('10."):
            raise IOError("Your python at %s doesn't return proper data for platform.mac_ver(), got: %s" % (python, output))
    elif sys.platform == 'linux2' and (2, 4) <= sys.version_info < (2, 5):
        output = Popen([python, "-c", "import socket; print (hasattr(socket, 'ssl'))"], stdout=PIPE).communicate()[0]
        if not output.startswith("True"):
            raise IOError("Your python at %s doesn't have ssl support, got: %s" % (python, output))

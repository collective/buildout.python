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

    p = Popen([python, "-c", "getattr(__builtins__, 'unichr', chr)(120144)"])
    p.communicate()
    if p.returncode != 0:
        raise IOError("Your Python isn't compiled with wide character support")

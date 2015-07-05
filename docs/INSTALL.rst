Mac OS X
--------

Install XCode from the App Store.


GNU/Linux
---------

Install the GNU C (gcc) and C++ (g++) compilers, development libraries for
libssl, python and curl.

On Debian and Ubuntu GNU/Linux, install the following packages::

  $ sudo apt-get install build-essential libssl-dev python curl

On CentOS / RHEL, install the following::

  $ sudo yum groupinstall "Development tools"
  $ sudo yum install openssl-devel python curl


All Platforms
-------------

Bootstrap the buildout with the standard system Python like this::

  $ /usr/bin/python bootstrap.py

Run buildout like this afterwards::

  $ ./bin/buildout

Now you can use the Python executables in ``python-2.7/bin/python2.7``, etc.

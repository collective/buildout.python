Mac OS X
--------

Install XCode from the App Store.

Install openssl@1.1 with homebrew.

For Python versions 2.4, 2.5 and 3.2, only OpenSSL versions up to 1.0.x are
supported, but homebrew has removed the 1.0 formula. You can install the last
OpenSSL 1.0 release as an @1.0 release with::

    $ brew install mjpieters/tap/openssl@1.0

GNU/Linux
---------

Install the GNU C (gcc) and C++ (g++) compilers, development libraries for
libssl, python and curl.

On Debian and Ubuntu GNU/Linux, install the following packages::

  $ sudo apt-get install build-essential libssl-dev python curl libbz2-dev
  libsqlite3-dev libtinfo-dev

For sqlite support on Python 2.4 install the following package::

  $ sudo apt-get install libsqlite-dev

For lzma compression support on Python 3.x install the following package::

  $ sudo apt-get install liblzma-dev

On CentOS / RHEL, install the following::

  $ sudo yum groupinstall "Development tools"
  $ sudo yum install openssl-devel python curl bzip2-devel sqlite-devel

All Platforms
-------------

Bootstrap the buildout with the standard system Python like this::

  $ /usr/bin/python bootstrap.py

Run buildout like this afterwards::

  $ ./bin/buildout

Now you can use the Python executables in ``python-2.7/bin/python2.7``, etc.

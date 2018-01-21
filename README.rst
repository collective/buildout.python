Introduction
------------

This buildout is a collection of configurations to make it easy to compile
various Python versions with or without the necessary dependencies.

The default ``buildout.cfg`` configuration is for Mac OS X Leopard, because that's
what this buildout was initially created for.

The default configuration is optimized for production builds, trading in
an increase in build time for a faster Python executable. See the
compilation options sections below on how to change this.

Installation
------------

See ``docs/INSTALL.rst``

Upgrade
-------

See ``docs/UPGRADE.rst``

Advanced Usage
--------------

The buildout is split up to make it easy to mix and match the parts you need.

If the ``links.cfg`` is used, then a script ``install-links`` is created in the
``bin`` directory. That script makes it easy to create symbolic links to all
the binaries and scripts in this buildout. You should set the destination for
those links by creating a ``local.cfg`` with the following content and run it
with ``bin/buildout -c local.cfg`` after modifying the ``prefix`` setting to your
needs::

    [buildout]
    extends = buildout.cfg

    [install-links]
    prefix = /path/for/the/links

The buildout is built in a way that you can easily extend it with your own
configuration.

Just get a Git clone::

    git clone git://github.com/collective/buildout.python.git python

And use a custom ``buildout.cfg`` like this::

    [buildout]
    extends = python/src/base.cfg python/src/python27.cfg
    python-buildout-root = ${buildout:directory}/python/src

If you want just one python version but all dependencies, then use something
like this::

    [buildout]
    extends =
      src/base.cfg
      src/readline.cfg
      src/zlib.cfg
      src/python25.cfg
      src/links.cfg

    python-buildout-root = ${buildout:directory}/src

    parts =
        ${buildout:base-parts}
        ${buildout:readline-parts}
        ${buildout:zlib-parts}
        ${buildout:python25-parts}
        ${buildout:links-parts}

The ``python-buildout-root`` setting is important, otherwise the whole buildout
doesn't work.

Compilation Options
-------------------

If you want to adjust the configuration or compilation options for
a Python variant, you can do so via your `local.cfg`.

If you are installing Python 3.6, you could for example turn off compile
time optimizations via the ``extra_options -=``. Or if you are on a newer
version of Mac OS, you could link against an OpenSSL library installed
via Homebrew, via the ``environment`` section::

    [python-3.6-build:default]
    extra_options -=
        --enable-optimizations
    environment =
        LDFLAGS=-L/usr/local/opt/openssl/lib
        CPPFLAGS=-I/usr/local/opt/openssl/include

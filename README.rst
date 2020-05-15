.. image:: https://github.com/collective/buildout.python/workflows/build/badge.svg
   :target: https://github.com/collective/buildout.python/actions?query=workflow%3Abuild+branch%3Amaster

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

Create a `local.cfg` file to customise what is built or alter configuration.
You can use this limit what versions are built, or to configure where to find
libraries and header files.

Start the file with::

    [buildout]
    extends = buildout.cfg

and you can then run buildout with::

    $ ./bin/buildout -c local.cfg

to use this adjusted configuration.

To limit what Python versions are built, re-define the `buildout.parts`
variable, found in `buildout.cfg`::

    # build Python versions 3.7, 3.8 and 3.9
    parts =
        ${buildout:base-parts}
        ${buildout:readline-parts}
        ${buildout:zlib-parts}
        ${buildout:python37-parts}
        ${buildout:python38-parts}
        ${buildout:python39-parts}
        ${buildout:links-parts}

You can set additional environment variables or `configure` switches for all 
Python builds by extending the `python-build:default.extra_options` and 
`python-build:default.environment` options. Setting the `optimizations` option 
to an empty value disables the Profile-Guided optimization compilation option
for modern Python versions::

    [python-build:default]
    optimizations =
    environment +=
        SOMEVARIABLE=somevalue
    extra_opts +=
        --some-supported-option

If you are installing Python 3.6, and if you are on a newer
version of Mac OS, you could link against a SQLite library installed
via Homebrew, and enable the `loadable-sqlite-extensions` option, via
the ``[python-build:darwin]`` section::

    [python-build:darwin]
    shellvars +=
        sqlite = brew --prefix sqlite
    extra_opts +=
        --with-loadable-sqlite-extensions
    environment =
        LDFLAGS=-L${:openssl}/lib -L${:sqlite}/lib
        CPPFLAGS=-I${:openssl}/include -I${:sqlite/include}

Refer to the `buildout.cfg` and `src/*.cfg` files for further definitions you
may want to override.

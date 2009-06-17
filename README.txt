This buildout is a collection of configurations to make it easy to compile
various Python versions with or without the necessary dependencies.

The default buildout.cfg configuration is for Mac OS X, because that's what
this buildout was initially created for.

The buildout is split up to make it easy to mix and match the parts you need.

If the links.cfg is used, then a script 'install-links' is created in the
'bin' directory. That script makes it easy to create symbolic links to all
the binaries and scripts in this buildout. You should set the destination for
those links by creating a 'local.cfg' with the following content and run it
with 'bin/buildout -c local.cfg' after modifying the 'prefix' setting to your
needs:

  [buildout]
  extends = buildout.cfg
  
  [install-links]
  prefix = /path/for/the/links

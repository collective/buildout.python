import os
from zc.recipe.cmmi import Recipe as Base
from zc.recipe.cmmi import system
import logging


# we need to patch the environment variable handling, see comment below


class Recipe(Base):
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        directory = buildout['buildout']['directory']
        download_cache = buildout['buildout'].get('download-cache')

        location = options.get(
            'location', buildout['buildout']['parts-directory'])
        options['location'] = os.path.join(location, name)

        self.url = self.options['url']
        extra_options = self.options.get('extra_options', '')
        # get rid of any newlines that may be in the options so they
        # do not get passed through to the commandline
        self.extra_options = ' '.join(extra_options.split())

        self.autogen = self.options.get('autogen', '')

        self.patch = self.options.get('patch', '')
        self.patch_options = self.options.get('patch_options', '-p0')

        # this is the only part patched, it's needed for environment
        # variables with spaces
        self.environ = self.options.get('environment', '').split('\n')
        if self.environ:
            self.environ = dict([x.split('=', 1) for x in self.environ if x])
        else:
            self.environ = {}

        self.source_directory_contains = self.options.get(
            'source-directory-contains', 'configure')
        self.configure_cmd = self.options.get(
            'configure-command', './configure')
        self.configure_options = self.options.get('configure-options', None)
        if self.configure_options:
            self.configure_options = ' '.join(self.configure_options.split())

        self.shared = options.get('shared', None)
        if self.shared:
            if os.path.isdir(self.shared):
                # to prevent nasty surprises, don't use the directory directly
                # since we remove it in case of build errors
                self.shared = os.path.join(self.shared, 'cmmi')
            else:
                if not download_cache:
                    raise ValueError(
                        "Set the 'shared' option of zc.recipe.cmmi to an existing"
                        " directory, or set ${buildout:download-cache}")

                self.shared = os.path.join(
                    directory, download_cache, 'cmmi', 'build')
                self.shared = os.path.join(self.shared, self._state_hash())

            options['location'] = self.shared

    def cmmi(self, dest):
        """Do the 'configure; make; make install' command sequence.

        When this is called, the current working directory is the
        source directory.  The 'dest' parameter specifies the
        installation prefix.

        This can be overridden by subclasses to support packages whose
        command sequence is different.
        """
        options = self.configure_options
        if options is None:
            options = '--prefix=%s' % dest
        if self.extra_options:
            options += ' %s' % self.extra_options
        # add logging here
        logger = logging.getLogger(self.name)
        logger.debug("%s %s" % (self.configure_cmd, options))
        system("%s %s" % (self.configure_cmd, options))
        system("make")
        system("make install")

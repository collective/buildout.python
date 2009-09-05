import os
from zc.recipe.cmmi import Recipe as Base


# we need to patch the environment variable handling, see comment below


class Recipe(Base):
    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        directory = buildout['buildout']['directory']
        self.download_cache = buildout['buildout'].get('download-cache')
        self.install_from_cache = buildout['buildout'].get('install-from-cache')

        if self.download_cache:
            # cache keys are hashes of url, to ensure repeatability if the
            # downloads do not have a version number in the filename
            # cache key is a directory which contains the downloaded file
            # download details stored with each key as cache.ini
            self.download_cache = os.path.join(
                directory, self.download_cache, 'cmmi')
            if not os.path.isdir(self.download_cache):
                os.mkdir(self.download_cache)

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

        self.shared = options.get('shared', None)
        if self.shared:
            if os.path.isdir(self.shared):
                # to prevent nasty surprises, don't use the directory directly
                # since we remove it in case of build errors
                self.shared = os.path.join(self.shared, 'cmmi')
            else:
                if not self.download_cache:
                    raise ValueError(
                        "Set the 'shared' option of zc.recipe.cmmi to an existing"
                        " directory, or set ${buildout:download-cache}")

                self.shared = os.path.join(
                    directory, self.download_cache, 'build')
                if not os.path.isdir(self.shared):
                    os.mkdir(self.shared)
                self.shared = os.path.join(self.shared, self._state_hash())

            options['location'] = self.shared

from zc.recipe.cmmi import Recipe as Base
from zc.recipe.cmmi import system
import logging


class Recipe(Base):

    def cmmi(self, dest):
        """Do the 'configure; make; make install' command sequence.

        When this is called, the current working directory is the
        source directory.  The 'dest' parameter specifies the
        installation prefix.

        This can be overridden by subclasses to support packages whose
        command sequence is different.
        """
        options = self.configure_options
        # Patch check for duplicate --prefix in extra_options
        if options is None and '--prefix' not in self.extra_options:
            options = '--prefix=%s' % dest
        else:
            options = ''
        if self.extra_options:
            options += ' %s' % self.extra_options
        # add logging here
        logger = logging.getLogger(self.name)
        logger.debug("%s %s" % (self.configure_cmd, options))
        system("%s %s" % (self.configure_cmd, options))
        # add support for different make_options
        self.make_options = self.options.get('make-options', None)
        if self.make_options:
            make_options = ' '.join(self.make_options.split())
        else:
            make_options = ''
        system("make %s" % make_options)
        system("make install")

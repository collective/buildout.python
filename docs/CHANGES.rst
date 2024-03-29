Changes
=======

2021-06-01
----------

- Python 3.8.10, 3.9.5, 3.10.0b1
  [mj]

2021-04-07
----------

- Python 3.10.0a7
  [mj]

2021-04-05
----------

- Python 3.9.4 ABI fix.
  [mj]

- Make bootstrap.py work in GitHub actions with Ubuntu's `python-setup` package installed.

2021-04-04
----------

- Python 3.8.9 and 3.9.3 security releases
  [mj]

2021-03-15
----------

- Python 3.5.10
  [mj]

2021-03-10
----------

- Python 3.6.13, 3.7.10, 3.8.8, 3.9.2 and 3.10a6
  [mj]

- PyPy 2.7-3.7.3, 3.7-3.7.3
  [mj]

2020-10-29
----------

- PyPy 2.7, 3.7.2
  [mj]

- Python 3.10.0a1
  [mj]

2020-10-19
----------

- PyPy 3.7, 7.3.2
  [mj]

2020-10-12
----------

- Python 3.8.6, Python 3.9.0.
  [mj]

2020-09-01
----------

- Update fest: Python 3.6.12, 3.7.9, 3.8.5 and 3.9.0rc1.
  [mj]

- Update PyPy and PyPy 3 to 7.3.1
  [mj]

2020-06-10
----------

- Update to Python 3.9.0b3.
  [mj]

2020-05-16
----------

- Include OpenSSL 1.0.1 to build Python 2.4, 2.5 and 3.2 on Linux.
  [mj]

- Install local setuptools egg when setuptools used by Python is too new (39.x
  or higher); zc.buildout relies on behaviour that was removed (issue #85).
  [mj]

2020-05-15
----------

- Backported build fixes for OS X 10.14 SDK location changes from Python 2.7 / 
  3.7 to older Python releases.
  [mj]

- Refactored and cleaned up the project layout.
  [mj]

2020-05-13
----------

- Pin docutils for Python 2.4 and Python 2.5
  [mj]

- Update to Python 2.7.18 3.8.3rc1 and 3.9.0a6
  [mj]

- Rework per-version build environment and configure switches to facilitate
  customisation better
  [mj]

- Update macOS homebrew openssl setup for OpenSSL 1.0.x, as that version is no
  longer available from homebrew-core. Clean up unnecessary patches for Setup.
  [mj]

2020-03-16
----------

- Update to Python 3.7.7 final
  [mj]

2020-03-08
----------

- Update to Python 3.8.2 final and 3.9.0a4
  [mj]

2020-02-22
----------

- Update to Python 3.8.2rc2 and 3.9.0a3
  [mj]

2020-01-22
----------

- Update to Python 3.6.10, 3.7.6, and 3.8.1
  [mj]

- Update to Python 3.9.0a2
  [mj]

2019-12-15
----------

- Update to Python 3.6.10rc1, 3.7.6rc1, and 3.8.1rc1
  [mj]

2019-11-26
----------

- Added Python 3.9.0a1
  [mj]

2019-11-02
----------

- Update to Python 3.5.9.
  [mj]

2019-10-30
----------

- Update to Python 3.5.8.
  [mj]

2019-10-21
----------

- Update to Python 3.8.0 final, 3.7.5, 3.5.8rc2, 2.7.17.
  [mj]

2019-08-19
----------

- Update to Python 3.8.0b3
  [mj]

2019-07-09
----------

- Update to Python 3.7.4
  [mj]

2019-07-05
----------

- Update to Python 3.6.9, 3.8.0b2
  [mj]

2019-06-30
----------

- Add preliminary macOS Catalina (10.15) support.
  [hannosch]

- Update PyPy to 7.1.1.
  [hannosch]

2019-06-09
----------

- Update to Python 3.8.0b1
  [mj]

2019-03-29
----------

- Update PyPy to 7.1.0.
  [hannosch]

- Update to Python 3.4.10, 3.5.7, 3.7.3, 3.8.0a3.
  [hannosch]

2019-03-08
----------

- Update to 2.7.16.
  [hannosch]

2019-02-26
----------

- Update to Python 3.8.0a2.
  [hannosch]

2019-02-16
----------

- Update PyPy and PyPy3 to 7.0.0.
  [hannosch]

2019-02-09
----------

- Add Python 3.8.0a1.
  [hannosch]

2018-12-25
----------

- Update to 3.6.8 and 3.7.2.
  [hannosch]

2018-12-02
----------

- Update PyPy and PyPy3 to 6.0.0.
  PyPy3 6.0 on macOS requires at least High Sierra (10.13).
  [hannosch]

2018-10-21
----------

- Update to 3.6.7 and 3.7.1.
  [hannosch]

2018-10-15
----------

- For Python 3.4 and newer, use ensurepip rather than easy_install to bootstrap.
  [mj]

2018-09-27
----------

- Update to 3.4.9 and 3.5.6.
  [hannosch]

2018-07-04
----------

- Update to 3.6.6 and 3.7.0.
  [hannosch]

2018-06-29
----------

- Add macOS Mojave (10.14) support.
  [hannosch]

2018-05-07
----------

- Update to 2.7.15 and 3.7.0b4
  [mj]

2018-04-01
----------

- Pin pip to <10dev for Python 2.6.
  [fschulze]


2018-03-30
----------

- Update to 3.6.5 and 3.7.0b3
  [hannosch]


2018-03-16
----------

- Update virtualenv to 15.1.0
  [mj]


2018-03-14
----------

- Update to 3.6.5rc1
  [fschulze]


2018-03-07
----------

- Update to 3.7.0b2
  [mj]

- Updated the install-links script to work on either Python 2 or 3
  [mj]


2018-02-18
----------

- Adjust bootstrap.py to only use https URLs for PyPI
  [mj]


2018-02-05
----------

- Update to 3.4.8 and 3.5.5
  [mj]


2018-02-04
----------

- Update to 3.7.0b1
  [mj]


2018-01-30
----------

- Update to Python 3.4.8rc1 and 3.5.5rc1.
  [fschulze]


2018-01-26
----------

- Add zlib to the build, so Python 2.4 compiles on Linux
  [fschulze]

- Add Travis-CI testing.
  [fschulze]


2018-01-10
----------

- Correct PyPy buildout rule for Darwin
  [mj]

- Adjust pip install command on 2.5 to work around lack of SSL validation.
  [mj]

- Reinstate buildout version 1.4.4 to retain compatibility with Python < 2.7
  [mj]

- Update to 3.7.0a4
  [mj]


2017-12-26
----------

- Update PyPy and PyPy3 to 5.10.0.
  [fschulze]


2017-12-20
----------

- Update to 3.6.4.
  [fschulze]


2017-12-06
----------

- Update to 3.6.4rc1 and 3.7.0a3.
  [fschulze]


2017-10-30
----------

- Fix Python 2.4 and 2.5 installations, now that PyPI has disabled HTTP
  redirects (https://mail.python.org/pipermail/distutils-sig/2017-October/031712.html)
  [fschulze]


2017-10-18
----------

- Use OpenSSL 1.1 for 2.7 and 3.5 and up with homebrew.
  [fschulze]

- Remove Pillow. For macOS use homebrew for libjpeg. Install Pillow in
  virtualenv.
  [fschulze]

- Update to 3.7.0a2.
  [fschulze]


2017-10-06
----------

- Update PyPy to 5.9.0.
  [fschulze]


2017-10-04
----------

- Update Python 3.6 to 3.6.3
  [mj]


2017-09-20
----------

- Add Python 3.7.0a1.
  [hannosch]

- Update to 3.3.7 and 3.6.3rc1.
  [hannosch]


2017-09-17
----------

- Update to 2.7.14.
  [hannosch]

- Add macOS High Sierra (10.13) support.
  [hannosch]


2017-08-13
----------

- Update python 3.4 to 3.4.7
- Update python 3.5 to 3.5.4
  [mj]


2017-07-28
----------

- Pin setuptools to <36.1. Upgrading further causes Pillow to fail to install.
  This may be caused by the inability of setuptools to install/upgrade itself
  anymore.
  [fschulze]


2017-07-18
----------

- Update to 3.6.2.
  [mj]


2017-06-09
----------

- Update pypy to 5.8.0.
  [hannosch]


2017-05-30
----------

- Update pypy to 5.7.1.
  [hannosch]


2017-03-23
----------

- Update pypy to 5.7.0.
  [fschulze]

- Update to 3.6.1.
  [hannosch]


2017-03-11
----------

- Update to 3.6.1rc1.
  [fschulze]


2017-03-01
----------

- Downgrade readline from 6.3 to 6.2.
  [Joerg Baach]


2017-02-21
----------

- Update ez_setup-latest.py from 18.4 to 33.1.1 and use it for Python 2.7.
  [hannosch]


2017-01-17
----------

- Update to 3.4.6 and 3.5.3.
  [fschulze]


2017-01-05
----------

- Update to 3.4.6rc1 and 3.5.3rc1.
  [fschulze]

- Pin Pillow to <4 for Python 2.6.
  [fschulze]


2016-12-23
----------

- Update to 3.6.0 final
  [mj]

- Disable `--enable-optimizations` flag for Python 2.7.13 until builds work on
  OS X.
  [mj]


2016-12-22
----------

- Update to 2.7.13. Had to remove the `--enable-optimizations` flag for
  El Capitan (OS X 10.11), as C extension modules like _struct failed to build.
  Didn't test on Sierra (macOS 10.12) or older, where it is still enabled.
  [fschulze]

- Update to 3.6.0rc2.
  [fschulze]


2016-12-07
----------

- Update to 3.6.0rc1.
  [fschulze]


2016-11-27
----------

- Add `--enable-optimizations` configure flag.
  [hannosch]


2016-11-22
----------

- Update to 3.6.0b4.
  [fschulze]


2016-11-02
----------

- Update to 3.6.0b3.
  [mj]


2016-10-18
----------

- Update to 3.6.0b2.
  [fschulze]

- Update to PyPy3 5.5.0-alpha.
  [fschulze]


2016-08-16
----------

- Update to 3.6.0b1.
  [mj]


2016-07-24
----------

- Add macOS Sierra (10.12) support.
  [aclark4life]


2016-06-28
----------

- Update to Python 2.7.12, 3.5.2 and 3.4.5.
  [fschulze]


2016-06-09
----------

- Update to jpegsrc v9b.
  [fschulze]

- Updated readline to 6.3.
  [fschulze]

- Update to PyPy3 5.2.0-alpha1.
  [fschulze]

- Update virtualenv to 15.0.2.
  [fschulze]

- Add virtualenv version pin for Python 3.2.
  [fschulze]

- Move pinned virtualenv settings to respective python*.cfg.
  [fschulze]

- The virtualenv*.in templates were all the same, use only one.
  [fschulze]

- Update to PyPy 5.3.0.
  [fschulze]


2016-05-18
----------

- Add Python 3.6.0a1.
  [fschulze]

- Update to PyPy 5.1.1.
  [fschulze]


2016-04-21
----------

- Update to PyPy 5.1.0.
  [fschulze]


2016-01-16
----------

- Update to PyPy on Linux to 4.0.1.
  [fschulze]

- Update to Python 3.4.4.
  [fschulze]


2015-12-09
----------

- Make pypy and pypy3 work automatically for newer OS X releases.
  [fschulze]

- Move Linux specific download URLs for pypy and pypy3 from default to
  linux2 section.
  [fschulze]

- Update to Python 2.7.11, 3.5.1 and 3.4.4rc1.
  [fschulze]

- Add missing md5sum for older releases.
  [fschulze]


2015-11-22
----------

- Update to Python 2.7.11rc1.
  [hannosch]


2015-11-20
----------

- Upgraded to pypy 4.0.1.
  [fschulze]


2015-11-10
----------

- Upgraded to pypy 4.0.0.
  [fschulze]


2015-11-02
----------

- Added a Python 3.5 virtualenv command
  [mj]

2015-10-01
----------

- Use latest setuptools for Python 3.3, 3.4 and 3.5.  The old ez_setup
  and/or setuptools is giving errors.
  This fixes #51 and refs #40.
  [maurits]

- Added missing default urls for pypy and pypy3.
  [maurits]

- Fixed Python2.4 ssl bindings on El Capitan.
  [jladage]

- Introduce a new `darwin-elcapitan` platform and adjust various parts to
  use the same settings as under `darwin-yosemite`.
  [hannosch]

2015-09-13
----------

- Upgraded Python 3.5 to 3.5.0
  [mj]

2015-07-05
----------

- Upgraded pypy to 2.6.0.
  [hannosch]

- Upgraded Python 3.5 to 3.5.0b2.
  [hannosch]

- Upgraded Python 3 to 3.2.5, 3.3.6 and 3.4.3.
  [hannosch]

- Changed Python 2.4, 2.5 and 2.6 downloads to use https.
  [hannosch]

2015-05-24
----------

- Upgraded Python 2.7 to 2.7.10
  [mj]

- Upgraded Python 3.5 to 3.5.0a4
  [mj]

2015-03-12
----------

- Virtualenv: do not call with --distribute option.
  [maurits]

- Python2.4: make platform.mac_ver() return '10.10' on Yosemite.
  [RichardBarrell]

2015-02-09
----------

- Added Python 3.5.0a1
  [mj]

2015-02-07
----------

- Updated pypy to 2.5.0 and pypy3 to 2.4.0.
  [fschulze]

2014-12-12
----------

- Update to Python 2.7.9.
  [hannosch]

2014-12-01
----------

- Update to Python 2.7.9rc1.
  [fschulze]

2014-11-18
----------

- Fix install-links script for changed name of pip script. It lost the dash
  between pip and the version number.
  [fschulze]

2014-10-16
----------

- Update to Python 3.4.2.
  [hannosch]

2014-09-24
----------

- Introduce a new `darwin-yosemite` platform and adjust various parts to
  use the same settings as under `darwin-mavericks`.
  [mj]

2014-09-21
----------

- Update to PyPy 2.4.0.
  [hannosch]

2014-09-16
----------

- Use virtualenv for Python 3.4.

- Upgrade virtualenv to 1.11.6
  [fschulze]

2014-07-20
----------

- Expand ~ to user's home in prefix of install-links script.
  [lgraf]

2014-07-03
----------

- Update to Python 2.7.8 and 3.4.1.
  [hannosch]

2014-03-20
----------

- Clarify naming of ez_setup.py for 1.x / 2.x versions.
  [hannosch]

2014-03-17
----------

- Update to Python 3.4.0
  [mj]

2014-03-14
----------

- Use ez_setup.py from setuptools 2.2 for all Python versions >= 2.6.
  [hannosch]

- Update to PyPy 2.2.1.
  [hannosch]

- Update bundled ez_setup.py to version 1.4.2, last to support Python < 2.6.
  [hannosch]

2014-03-13
----------

- Update to Python 3.3.5 and Python 3.4.0rc3.
  [fschulze]


2014-02-14
----------

- Update to Python 3.3.4 and Python 3.4.0rc1.
  [fschulze]


2013-11-26
----------

- Fix missing ssl support in Python 2.4 on Debian, Ubuntu and possibly other
  Linux distributions.
  [nueces, fschulze]

- Update to Python 3.4.0b1.
  [fschulze]

- Fix Python 2.5 for Mavericks.
  [fschulze]


2013-11-22
----------

- Only add the PyPy parts on OS X.
  [fschulze]

- Update to Python 3.3.3 and PyPy 2.2.
  [fschulze]


2013-11-14
----------

- Fix Python 2.4 for Mavericks.


2013-11-13
----------

- Update to Python 2.7.6.
  [fschulze]


2013-11-09
----------

- Update to Python 2.6.9.
  [fschulze]


2013-10-23
----------

- Introduce a new `darwin-mavericks` platform and adjust various parts to
  use the same settings as under `darwin-mountainlion`.
  [hannosch]


2013-10-11
----------

- Replace install-links shell script with a more sophisticated Python one which
  also properly handles pypy.
  [fschulze, mauritsvanrees]


2013-10-10
----------

- Added Python 3.4 to default buildout.cfg.
  [fschulze]

- Use pyvenv for Python 3.4.
  [fschulze]


2013-10-05
----------

- Update to Python 2.6.9rc1.
  [fschulze]

- Added `python34.cfg` for Python 3.4.0a3. Only the build part is active,
  virtualenv 1.10.1 doesn't work with Python 3.4 yet.
  [fschulze]


2013-10-02
----------

- Use collective.recipe.cmmi which allows multiple patches.
  [fschulze]


2013-10-01
----------

- Install PIL in the built python instead of the virtualenv, so any new
  virtualenv created with --system-site-packages has access to it.
  [fschulze]


2013-08-31
----------

- Update to PyPy 2.1.
  [fschulze]

- Added pypy3.cfg.
  [fschulze]


2013-08-26
----------

- For Python 2.7, set LD_RUN_PATH and C_INCLUDE_PATH prior to
  easy_install of Pillow in virtualenv; recent Pillow build may obey
  this to link against local zlib and libjpeg on some platforms
  (notably, Linux ld.so), using "rpath" hard-coded in built _imaging.so.
  [seanupton]
- Include --always-unzip flag for easy_install of Pillow to avoid
  installation in ~/.python-eggs directory.
  [seanupton]


2013-08-14
----------

- Update Virtualenv to 1.10.1 for Python > 2.5 and Virtualenv to 1.9.1 for
  Python 2.5 (last compatible version).
  [davidjb]
- Fix issue compiling Python 2.5 on x86_64 systems.
  [davidjb]
- Fix issue compiling Python 2.5 for Subversion >= 1.7.
  [davidjb]
- Fix issue compiling Python 2.5 if sqlite can't be found.
  [davidjb]

2013-07-16
----------

- Update to PyPy 2.0.2.
  [hannosch]

2013-05-16
----------

- Update to PyPy 2.0.
  [hannosch]

- Update to Python 2.7.5, 3.2.5 and 3.3.2.
  [hannosch]

2013-04-11
----------

- Update to Python 2.7.4, 3.2.4 and 3.3.1.
  [hannosch]

2013-04-08
----------

- Update to PyPy 2.0-beta2.
  [fschulze]

2013-03-29
----------

- Update virtualenv to 1.9.1.
  [fschulze]

2013-03-26
----------

- Update to Python 2.7.4rc1, 3.2.4rc1 and 3.3.1rc1.
  [hannosch]

2013-03-16
----------

- Pin down Pillow to 1.x for python 2.4 and 2.5.
  Pillow 2.x supports only python >= 2.6
  [jone]

2013-02-26
----------

- Use collective.recipe.cmmi which is a proper release of monkeycmmi.
  [fschulze]

- Pin zc.buildout to 1.4.4 to prevent parts/buildout/site.py issues.
  [fschulze]

2013-01-08
----------

- Update to PyPy 2.0-beta1.
  [hannosch]

2012-10-01
----------

- Add more detailed platform detection for linux.
  [fschulze]

- Use virtualenv 1.8.2 except for Python 2.4, which needs virtualenv 1.7.2.
  [fschulze, sgillies]

- When installing Python 2.4 we need to use zc.recipe.egg 1.2.2.
  [fschulze]

- Added patch for python 2.5 to search for libs in /usr/lib/i386-linux-gnu/.
  Fixes bug occurring in Linux Mint 12.
  [silviot, fschulze]

2012-09-30
----------

- Update to Python 3.3.0 final.
  [hannosch]

2012-09-24
----------

- Update to Python 3.3.0rc3.
  [hannosch]

2012-09-10
----------

- Update to Python 3.3.0rc2.
  [hannosch]

2012-08-25
----------

- Update to Python 3.3.0rc1.
  [hannosch]

2012-07-19
----------

- Update to PyPy 1.9.
  [hannosch]

- Use Pillow by default, the problems caused by the original are too big by now.
  You can change the install arg with
  ``pil-install-args = -f http://dist.repoze.org/ -U PIL==1.1.6`` in the
  ``[buildout]`` section.
  [fschulze]

- Update to virtualenv 1.7.2.
  [hannosch]

- Update to Python 3.3.0b1.
  [hannosch]

2012-04-04
----------

- Update to Python 3.3.0a2.
  [hannosch]

2012-03-21
----------

- Added `python33.cfg` for Python 3.3.0a1.
  [hannosch]

- Update to Python 2.6.8rc2, Python 2.7.3rc2 and Python 3.2.3rc2.
  [hannosch]

2012-02-25
----------

- Update to virtualenv 1.7.1.2, PyPy 1.8, Python 2.6.8rc1, Python 2.7.3rc1
  and Python 3.2.3rc1.
  [hannosch]

2012-01-29
----------

- Fixed link to zlib 1.2.5 source that broke after release of zlib 1.2.6.
  [lukebrannon]

2011-12-22
----------

- Update to PyPy 1.7.
  [hannosch]

2011-11-30
----------

- Python 2.6: added patch for missing sslv2 support on newer Linuxes and to
  support Ubuntu/Debian multiarch library paths.
  [joka]

2011-08-20
----------

- Updated `monkeycmmi` to 0.2 and avoid patch for environment / spaces handling.

2011-07-30
----------

- Update to jpegsrc v8c and set `-arch x86_64` for Lion.
  [hannosch]

- Update to virtualenv 1.6.4.
  [hannosch]

- Updated readline to 6.2.
  [hannosch]

- Changed `MACOSX_DEPLOYMENT_TARGET` to `10.7` for Python 2.4 on Lion.
  [hannosch]

2011-07-25
----------

- Add OSX Lion support to the buildout.
  [dsa]

2011-06-15
----------

- Updated pypy to 1.5 (only 64 bit version, there is no release for 32 bit).
  [fschulze]

- Added pdbtextmate support for Python 3.2.
  [fschulze]

- Removed Python 3.1.x it doesn't work properly anymore and isn't used much
  and not supported anymore.
  [fschulze]

- Update to Python 2.7.2.
  [fschulze]

- Update to Python 2.6.7 final.
  [fschulze]

2011-05-28
----------

- Update to Python 2.5.6 final.
  [hannosch]

2011-05-23
----------

- Update to Python 2.6.7rc2 to include more security fixes.
  [hannosch]

2011-05-18
----------

- New PyPy version 1.4.1.
  [fschulze]

2011-05-08
----------

- Update to Python 2.5.6c1 and 2.6.7rc1 to include security fixes.
  [hannosch]

2011-04-07
----------

* Add patch to fix recursion error crash on python2.6 OS X from
  http://bugs.python.org/issue9670 (edited to apply with patch -p0).
  [elro]

2009-11-26
----------

* Renamed part for readline patches, so the old ones from 5.2 don't interfere.
  [fschulze]

2009-11-25
----------

* Added ugly hack which hopefully solves the build order issues causing
  Python 2.4 to be build before readline was built.
  [fschulze]

* Ugraded to readline 6.0, 5.2 had compile issues on OS X.
  [fschulze]

2009-11-05
----------

* Use virtualenv 1.4rc1 with the --distribute option.
  [fschulze]

* Autodetect 32/64 bit in Snow Leopard.
  [fschulze]

2009-11-03
----------

* Upgraded virtualenv-distribute to latest version to get distribute 0.6.6.
  [reinout]


2009-10-28
----------

* Added configuration to build Python with debug symbols for C level
  debugging. Activate by including src/debug.cfg in your custom configuration.
  [witsch]


2009-10-27
----------

* Updated to Python 2.6.4.
  [fschulze]


2009-10-12
----------

* Updated to Python 2.6.4rc1.
  [hannosch]


2009-10-07
----------

* Fixed Python 2.5.
  [fschulze]

* Added some sanity checks to make sure the installed Python virtualenvs
  actually work.
  [fschulze]

* Auto-detection of the platfrom. No need for separate configs for
  Snow Leopard etc.
  [fschulze]

* Use virtualenv-distribute.
  [fschulze]

* Use distribute instead of setuptools.
  [fschulze]


2009-10-02
----------

* Updated to Python 2.6.3.
  [fschulze]


2009-09-05
----------

* Made MacPorts compatible on Snow Leopard by compiling as 64-bit.
  [fschulze]

* Added Python 2.6 back on Snow Leopard.
  [fschulze]


2009-08-31
----------

* Running on Snow Leopard with 32-bit. Conflicts with MacPorts.
  [fschulze]

* Removed zc.buildout scripts again, because the installation fails for some
  weird reason.
  [fschulze]


2009-08-29
----------

* Make it possible to extend both distribute.cfg and pdbtextmate.cfg. See
  pdbtextmate.cfg for notes though!
  [fschulze]

* Reorganized documentation.
  [fschulze]

* By depending on zc.buildout >= 1.4.0 the amount of repition in the python
  parts was vastly reduced and makes the configuration more easily readable.
  [fschulze]

* Fixed path to patch for Python 2.5 on Snow Leopard.
  [fschulze]

* Added buildout-2.x scripts back without causing version conflicts by
  wrapping them with zc.recipe.eggs instead of installing with easy_install.
  [fschulze]

* Minimized changes for Snow Leopard.
  [fschulze]


2009-08-27
----------

* Removed zc.buildout installation. It just causes version conflicts in
  buildouts with a version pin on zc.buildout and similar issues.
  [fschulze]

from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='monkeycmmi',
      version=version,
      description="",
      long_description="",
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'zc.recipe.cmmi==1.2.1',
      ],
      entry_points = {'zc.buildout':
                      ['default = monkeycmmi:Recipe']},
      )

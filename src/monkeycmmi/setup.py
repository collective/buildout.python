from setuptools import setup, find_packages

version = '0.2'

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
        'zc.recipe.cmmi==1.3.5',
      ],
      entry_points = {'zc.buildout':
                      ['default = monkeycmmi:Recipe']},
      )

from setuptools import setup, find_packages
import os

version = '1.4'

setup(name='cioppino.twothumbs',
      version=version,
      description="Rating widget based on thumbs up and down.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='rating, content, thumbs',
      author='eleddy',
      author_email='elizabeth.leddy@gmail.com',
      url='https://github.com/eleddy/cioppino.twothumbs',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cioppino'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],

      )

from setuptools import setup, find_packages
import os

version = '1.8'
description = open("README.rst").read() + "\n"
description += open(os.path.join("docs", "HISTORY.rst")).read()

setup(
    name='cioppino.twothumbs',
    version=version,
    description="Rating widget based on thumbs up and down.",
    long_description=description,
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
        'Plone',
        'plone.behavior',
        'setuptools',
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    setup_requires=[],
)

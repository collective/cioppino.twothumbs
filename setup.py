from setuptools import find_packages
from setuptools import setup


version = "3.0.0"
with open("README.rst") as myfile:
    description = myfile.read() + "\n"
with open("CHANGES.rst") as myfile:
    description += myfile.read()

setup(
    name="cioppino.twothumbs",
    version=version,
    description="Rating widget based on thumbs up and down.",
    long_description=description,
    # Get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="rating, content, thumbs",
    author="eleddy",
    author_email="elizabeth.leddy@gmail.com",
    url="https://github.com/collective/cioppino.twothumbs",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["cioppino"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Plone",
        "plone.behavior",
        "setuptools",
    ],
    extras_require={"test": ["plone.app.testing"]},
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    setup_requires=[],
)

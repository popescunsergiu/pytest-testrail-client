import setuptools
from setuptools import setup

setup(
    name="pytest-testrail-client",
    version="1.0.5",
    use_scm_version=False,
    description="pytest plugin for Testrail",
    long_description=open("README.rst").read(),
    author="Sergiu Popescu",
    author_email="popescunsergiu@gmail.com",
    url="https://github.com/popescunsergiu/pytest-testrail-client",
    download_url="https://github.com/popescunsergiu/pytest-testrail-client/archive/v1.0.5.tar.gz",
    packages=setuptools.find_packages(exclude=('tests', 'dev_tools')),
    install_requires=[
        "cucumber-tag-expressions>=2.0.0",
        "gherkin-official>=4.1.0",
        "pytest>=4.2",
        "pytest-bdd>=3.3.0",
        "requests",
    ],
    entry_points={
        "pytest11": [
            "pytest-testrail-client = pytest_testrail_client.pytest_testrail_client",
        ]
    },
    setup_requires=["setuptools_scm"],
    license="Mozilla Public License 2.0 (MPL 2.0)",
    keywords="py.test pytest qa ",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)

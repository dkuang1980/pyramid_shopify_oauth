import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')
CHANGES = read('CHANGES.md')

version = '0.0.1'

setup(
    name="pyramid_shopify_oauth",
    version=version,
    author="Da Kuang",
    author_email="dkuang1980@gmail.com",
    description="create pyramid app without worrying about Shopify OAuth",
    keywords="pyramid python shopify oauth",
    url="https://github.com/dakuang/pyramid_shopify_oauth",
    long_description='%s\n\n%s' % (README, CHANGES),
    install_requires=[
        "ShopifyAPI"
    ],
    packages=find_packages(),
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)

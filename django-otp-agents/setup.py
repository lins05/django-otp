#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-otp-agents',
    version='0.1.1',
    description="Integration of django-otp and django-agent-trust.",
    long_description=open('README').read(),
    author='Peter Sagerson',
    author_email='psagersDjwublJf@ignorare.net',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    url='https://bitbucket.org/psagers/django-otp',
    license='BSD',
    install_requires=[
        'django-otp',
        'django-agent-trust',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
) 

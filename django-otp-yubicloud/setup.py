#!/usr/bin/env python

from distutils.core import setup


setup(
    name='django-otp-yubicloud',
    version='0.1.0',
    description='A django-otp plugin that verifies tokens with a YubiCloud service.',
    long_description=open('README').read(),
    author='Peter Sagerson',
    author_email='psagersDjwublJf@ignorare.net',
    packages=[
    ],
    url='https://bitbucket.org/psagers/django-otp',
    license='BSD',
    install_requires=[
        'django-otp'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
) 

#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-otp-agents',
    version='0.2.0',
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
        'django-otp >= 0.2.0',
        'django-agent-trust >= 0.1.8',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],
)

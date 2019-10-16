#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='cielo',
    version='0.1.5',
    description='SDK API-3.0 Python 3 Cielo',
    author='Cosmo André',
    author_email='cosmo_moraes@hotmail.com',
    url='https://github.com/cosmo9able/cielo',
    keywords='fork api3.0 cielo python sdk ecommerce',
    packages=find_packages(),
    install_requires=['requests', 'future'],
    license='MIT',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        #'Programming Language :: Python :: 2.6',
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    )
)


setup(**settings)




# # -*- coding: utf-8 -*-
# from setuptools import setup

# setup(
#     name='cielo',
#     version='0.1.1',
#     url='',
#     license='MIT License',
#     author='Cosmo André',
#     author_email='cosmo_moraes@hotmail.com',
#     keywords='fork api3.0 cielo python sdk ecommerce',
#     description=u'',
#     packages=['cielo.api30'],
#     install_requires=['requests'],
# )

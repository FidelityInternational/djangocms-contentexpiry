from setuptools import find_packages, setup

import djangocms_contentexpiry


INSTALL_REQUIREMENTS = [
    'Django>=1.11,<2.0',
    'django-cms>=3.5.0'
    ]


setup(
    name='djangocms-contentexpiry',
    packages=find_packages(),
    include_package_data=True,
    version=djangocms_contentexpiry.__version__,
    description=djangocms_contentexpiry.__doc__,
    long_description=open('README.md').read(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    install_requires=INSTALL_REQUIREMENTS,
    author='Fidelity International',
    url='https://github.com/fidelityInternational/djangocms-contentexpiry',
    license='BSD',
    test_suite='tests.settings.run',
)

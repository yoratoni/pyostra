try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


NAME = 'pyostra'
VERSION = '0.1.3'
DESCRIPTION = 'THe internal Python package used for the Ostra projects such as the advanced NFTs generator.'
LONG_DESCRIPTION = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read()


setup(
    name=NAME,
    version=VERSION,
    author='Yoratoni',
    author_email='twingearas@gmail.com',
    url='https://github.com/yoratoni/pyostra',
    license='BSD',
    
    description=DESCRIPTION,
    long_description_content_type = 'text/markdown',
    long_description=LONG_DESCRIPTION,
    keywords='ostra internal color colour terminal windows crossplatform',

    packages=[NAME],
    install_requires=['colorama'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Terminals'
    ]
)

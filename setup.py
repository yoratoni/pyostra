try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


NAME = 'pyostra'
VERSION = '0.1.2'
DESCRIPTION = 'THe internal Python package used for the Ostra projects such as the advanced NFTs generator.'
LONG_DESCRIPTION = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read()


setup(
    name=NAME,
    version=VERSION,
    author='Yoratoni',
    author_email='twingearas@gmail.com',
    url='https://github.com/yoratoni/pyostra',
    license='MIT',
    
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,

    packages=[NAME],
    install_requires=['colorama', 'time', 'typing', 'inspect'],
    
    keywords='ostra',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Terminals'
    ]
)

from setuptools import setup, find_packages


__description__ = 'THe internal Python package used for the Ostra projects such as the advanced NFTs generator.'
__long_description__ = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read()
__classifiers__ = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'Topic :: Utilities'
]


setup(
    name='pyostra',
    version='0.1.1',
    author='Yoratoni',
    author_email='twingearas@gmail.com',
    license='MIT',
    
    description=__description__,
    long_description_content_type='text/markdown',
    long_description=__long_description__,

    packages=find_packages(),
    install_requires=['colorama'],
    
    keywords='ostra',
    classifiers=__classifiers__
)

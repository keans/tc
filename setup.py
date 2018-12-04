from setuptools import setup, find_packages
import codecs
import os

# get current directory
here = os.path.abspath(os.path.dirname(__file__))


def get_long_description():
    """
    get long description from README.rst file
    """
    with codecs.open(os.path.join(here, "README.rst"), "r", "utf-8") as f:
        return f.read()


setup(
    name='tc',
    version='0.0.1',
    description='A simple console-based time tracker.',
    long_description=get_long_description(),
    url='https://github.com/keans/tc',
    author='Ansgar Kellner',
    author_email='keans@gmx.de',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='python packaging',
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests']
    ),
    install_requires=["Click", "python-dateutil"],
    py_modules=["tc"],
    entry_points="""
       [console_scripts]
       tc=tc.cli:cli
    """
)

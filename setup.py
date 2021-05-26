from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Intended Audience :: Financial and Insurance Industry',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT Lisence',
    'Programming Language :: Python :: 3'
]

setup(
    name='compoundinterest',
    version='0.0.1',
    description='Module of compound interest factors which includes single payment, uniform payment series, and arithmetic gradient calculations',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url=''
    author='Zaafirrahman',
    author_email='zaafir123rahman@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['compoundinterest', 'engineeringeconomics'],
    packages=find_packages(),
    install_requires=['']
)
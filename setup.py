from setuptools import setup

long_description = open('README.rst').read()

setup(
    name='awsmc',
    version='0.0.10',
    description='Simple and cheap minecraft hosting on AWS',
    long_description=long_description,
    install_requires=[
        'paramiko',
        'requests',
        'screenutils',
        'boto3',
        'python-crontab'
    ],
    url='https://github.com/brenns10/awsmc',
    author='Stephen Brennan',
    author_email='stephen@brennan.io',
    license='Revised BSD',
    packages=['awsmc'],
    entry_points={
        'console_scripts': [
            'awsmc = awsmc.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
    ],
    keywords='AWS minecraft',
)

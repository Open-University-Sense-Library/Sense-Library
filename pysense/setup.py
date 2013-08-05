from distutils.core import setup

setup(
    name='pySense',
    version='1.0.0',
    author='T. Sharma & T. Webster'
    author_email='@'
    packages=['pysense', 'pysense.test'],
    scripts=['Traffic Lights'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Gives control of SenseBoard through python',
    long_description=open('README.txt').read()
    install_requires=[
        "pyserial >=2.6"
    ],
)

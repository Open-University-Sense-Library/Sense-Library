from distutils.core import setup

setup(
    name='pySense',
    version='1.0.0',
    author='T. Sharma & T. Webster',
    author_email='toran@toransharma.com',
    packages=['pysense'],
    url='http://toransharma.com/pysense',
    license='GPL.txt',
    description='Gives control of SenseBoards through python',
    long_description=open('README.txt').read(),
    requires=['pySerial'],
)

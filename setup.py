from distutils.core import setup

setup(name='jbloshuo',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Hire Tom',
      url='http://small.dada.pink/jbloshuo',
      install_requires = ['bottle'],
      packages=['jbloshuo'],
      entry_points={'console_scripts': ['jbloshuo = jbloshuo:run']},
      version='0.0.1',
      license='AGPL',
)

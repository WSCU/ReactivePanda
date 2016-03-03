from distutils.core import setup
import os


def find_dir(q):  # Find a directory q
    for root, dirs, files in os.walk('/'):
        for d in dirs:
            if d == q:
                return os.path.join(root, d)


dist_dir = find_dir('ReactivePanda')
setup(name='Reactive Panda Engine',
      description='Reactive Panda game engine for programming',
      version='1.0',
      packages=['PandaFRP', 'PandaSRC', 'lib']
      )

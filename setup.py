from distutils.core import setup

setup(name='cpe_manager',
      version='0.0.2',
      description='Tools for CPE management (mostly VSOL/Chinese ONUs)',
      author='Rafael Carvallo',
      author_email='rafael.carvalloh@gmail.com',
      url='',
      packages=['cpe_manager', 'cpe_manager.models'],
      install_requires=[
       'requests',
       'beautifulsoup4',
       'selenium',
      ]
     )

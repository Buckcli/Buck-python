from setuptools import setup, find_packages


setup (
  name = 'buck',
  version = '2.4.0',
  description = ' Get started with your projects faster .',
  url = 'https://github.com/Pleasant-tech/Buck/',
  keywords='productivity, setuptools, bucket, cli, buck, getbuck',
  long_description = "Run multiple commands all in one.",
  #package_dir={'': 'src'},
  packages = find_packages(),
  include_package_data = True,
  install_requires=[
    'firebase-admin',],

   
 
  license="MIT",
  classifiers =[
    "License :: OSI Approved :: MIT License",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3 :: Only',
  ],
  entry_points = '''
    [console_scripts]
    buck = src.main:main
  ''',
  zip_safe=False,
  author = 'Pleasant Tech',
  author_email = 'pleasanttech21@gmail.com'

  
)
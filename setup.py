from setuptools import setup
import pathlib



def readme():
    this_directory = pathlib.Path(__file__).parent.resolve()
    long_description = (this_directory / 'README.md').read_text(encoding='utf-8')
    
    return long_description


setup(name='csv_pull',
      version='1.0.0',
      description='Data Extract',
      long_description=readme(),
      long_description_content_type = 'text/markdown',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Topic :: CSV Extraction :: File Manipulation',
      ],
      url='https://github.com/Ebenezer319/csv_pull',
      author='CSV Extractors',
      packages=['csv_pull', 'csv_pull.tests'],
      install_requires=[
          'numpy',
          'pandas',
          'setuptools',
          'pathlib',
          'unittest'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['pull-csv=csv_pull.csv_pull:main'],
      },
      include_package_data=True,
      zip_safe=False)

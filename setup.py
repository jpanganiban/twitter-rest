from setuptools import setup


setup(name='twitterrest',
      description="A very simple client for Twitter's REST API",
      version='1.0',
      author='Jesse Panganiban',
      author_email='me@jpanganiban.com',
      py_modules=['twitterrest'],
      install_requires=[
          'requests'
        ],
    )

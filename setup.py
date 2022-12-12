from setuptools import setup, find_packages

setup(
    name='saas_co',
    version='6.9',
    license='MIT',
    author="David Schwartz",
    author_email='david.schwartz@devfactory.com',
    packages=['saas_co'],
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='cost optimization cur',
    install_requires=[
          'boto3',
          'asyncio',
          'botocore',
          'pandas',
          'awswrangler',
          'jsonpath-ng'
      ],
)

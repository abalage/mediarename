from setuptools import setup

setup(
    author='Balázs NÉMETH',
    author_email='balagetech@protonmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPLv3',
        'Operating System :: OS Independent',
    ],
    description='A package to mass rename media files based on their metadata.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    name='mediarename',
    python_requires='>=3.11',
    url='https://github.com/abalage/mediarename',
)

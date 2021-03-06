# coding=utf-8
"""Install config."""
from setuptools import setup, find_packages
import os

long_description = '''A wrapper around Espeak and Mbrola, to do simple Text-To-Speech (TTS),
    with the possibility to tweak the phonemic form.'''
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name='voxpopuli',
    version='0.1.3',
    description='A wrapper around Espeak and Mbrola, to do simple Text-To-Speech (TTS),'
                ' with the possibility to tweak the phonemic form.',
    url='https://github.com/hadware/voxpopuli',
    author='Hadware',
    author_email='hadwarez@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='tts speech phonems audio',
    packages=find_packages(),
    install_requires=['pyaudio'],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'])

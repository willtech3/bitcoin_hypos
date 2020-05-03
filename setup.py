from setuptools import setup, find_packages
import subprocess

#version = subprocess.check_output("git describe --abbrev=0", shell=True).decode("utf-8").strip()[1:]

setup(
  name='cash_displayer',
  #version=version,
  packages=find_packages(),
  package_data={'cash_displayer.config': ['*.ini']},
  include_package_data=True,
  install_requires=[
     'termcolor',
  ],
  entry_points='''
      [console_scripts]
      hypo=cash_displayer.scripts.hypo:run
      real=cash_displayer.scripts.real:run
      ''',
)

from setuptools import setup, find_packages, find_namespace_packages
import subprocess

#version = subprocess.check_output("git describe --abbrev=0", shell=True).decode("utf-8").strip()[1:]

setup(
  name='bitcoin_hypos',
  #version=version,
  package_data={'bitcoin_hypos.config': ['*.ini']},
  include_package_data=True,
  packages=find_namespace_packages(),
  install_requires=[
     'coinbase'
  ],
  entry_points='''
      [console_scripts]
      hypo=bitcoin_hypos.scripts.hypo:run
      real=bitcoin_hypos.scripts.real:run
      ''',
)

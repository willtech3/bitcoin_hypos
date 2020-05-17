from setuptools import setup, find_packages
import subprocess

#version = subprocess.check_output("git describe --abbrev=0", shell=True).decode("utf-8").strip()[1:]

setup(
  name='bitcoin_hypos',
  #version=version,
  packages=find_packages(),
  package_data={'bitcoin_hypos.config': ['*.ini']},
  include_package_data=True,
  install_requires = find_packages(["*.tests", "*.tests.*", "tests.*", "tests"]),
  entry_points='''
      [console_scripts]
      hypo=bitcoin_hypos.scripts.hypo:run
      real=bitcoin_hypos.scripts.real:run
      ''',
)

#!/usr/bin/env python3

import subprocess
import os
import sys

build_dir = 'build'
h2a_url = 'https://github.com/alexcoplan/heap2asm.git'
h2a_dir = os.path.join(build_dir, 'h2a')
h2a_script = os.path.join(h2a_dir, 'bootstrap.py')

def run(cmd):
  print(" ".join(cmd))
  subprocess.check_call(cmd)

if not (os.path.exists(h2a_dir) and os.path.exists(h2a_script)):
  cmd = ['git', 'clone', h2a_url, h2a_dir]
  run(cmd)

sys.path.insert(0, os.getcwd())
import build.h2a.bootstrap as bstrap
os.chdir(h2a_dir)
bstrap.main()

# Minimal smlnj + ninja build system

![ci status](https://github.com/alexcoplan/hello-build-sml/workflows/CI/badge.svg)

This project is an example of a minimal build system for Standard ML using smlnj
as the compiler and ninja to orchestrate the build. Notable features are:

 - Generates native executables by bootstrapping a heap2asm build (not included
   with the standard smlnj distribution).
 - Uses CM to generate depfiles which ninja is then aware of (not supported by
   the standard tooling).
 - This project comes with a working github CI setup (with a Linux runner), and
   should also build just fine on macOS.

To build, ensure `SMLNJ_HOME` is set appropriately, and then:
```
./configure.py
ninja
```

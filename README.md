# Minimal smlnj + ninja build system

This project is an example of a minimal build system for Standard ML using smlnj
as the compiler and ninja to orchestrate the build. Notable features are:

 - Generates native executables by bootstrapping a heap2asm build (not included
   with the standard smlnj distribution).
 - Uses CM to generate depfiles which ninja is then aware of (not supported by
   the standard tooling).

Probably any real project wants to use a script to generate the ninja, but this
is a good starting point.

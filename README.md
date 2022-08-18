# Constrained form-finding of tension compression structures

Papel pre-print: https://arxiv.org/abs/2111.02607

This repository contains data and code that supports the experiments presented in the paper "Constrained form-finding of tension-compression structures", submitted to the journal of Computer-Aided Design in 2022.

The code used to model the structures described therein is organized in three folders that match the three experimental sections of the paper:

1. Section 3: Two-segment compression strut, described in``extensions/README.md``
2. Section 4: Recurrent network experiments described in ``numerical_validation/README.md``
3. Section 5: Spiraling staircase in ``case_study/README.md``

The code in this repository runs in three different environments.
The Python script in the folder ``case_study`` sections 3 can be executed from a command line interface.
The jupyter notebooks in the folder ``numerical_validation`` can be executed locally or remotely using Google Colab.
The file in ``case_study`` can be run only in grasshopper for Rhino3D. 

Regardless of the file or the environment, all the files require a valid installation of ``compas_cem`` to be executed.
Follow the instructions listed in this website to install ``compas_cem`` according to your operating system.

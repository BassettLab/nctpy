nctpy: Network Control Theory for Python
=====================================================================================

Overview
--------
.. image:: https://zenodo.org/badge/370716682.svg
   :target: https://zenodo.org/badge/latestdoi/370716682
.. image:: https://readthedocs.org/projects/nctpy/badge/?version=latest
    :target: https://nctpy.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://img.shields.io/pypi/l/ansicolortags.svg
   :target: https://pypi.python.org/pypi/ansicolortags/

Network Control Theory (NCT) is a branch of physical and engineering sciences that treats a network as a dynamical
system. Generally, the system is controlled through `control signals` that originate at a control node (or control nodes) and
move through the network. In the brain, NCT models each region’s activity as a time-dependent internal state that is
predicted from a combination of three factors: (i) its previous state, (ii) whole-brain structural connectivity,
and (iii) external inputs. NCT enables asking a broad range of questions of a networked system that are highly relevant
to network neuroscientists, such as: which regions are positioned such that they can efficiently distribute activity
throughout the brain to drive changes in brain states? Do different brain regions control system dynamics in different
ways? Given a set of control nodes, how can the system be driven to a specific target state, or switch between a pair of
states, by means of internal or external control input?

``nctpy`` is a Python toolbox that provides researchers with a set of tools to conduct some of the
common NCT analyses reported in the literature. Below, we list select publications that serve as a primer for
these tools and their use cases:

1. Parkes, L., Kim, J. Z., et al. A network control theory pipeline for studying the dynamics of the structural connectome. 
In press at Nature Protocols (2024). https://www.biorxiv.org/content/10.1101/2023.08.23.554519v1

2. Karrer, T. M., Kim, J. Z., Stiso, J. et al. A practical guide to methodological considerations in the
controllability of structural brain networks.
Journal of Neural Engineering (2020). https://doi.org/10.1088/1741-2552/ab6e8b

3. Kim, J. Z., & Bassett, D. S. Linear dynamics & control of brain networks.
arXiv (2019). https://arxiv.org/abs/1902.03309

.. _readme_requirements:

Requirements
------------

Currently, ``nctpy`` works with Python 3.9 and requires the following core dependencies:

    - numpy (tested on 1.23.4)
    - scipy (tested on 1.9.3)
    - tqdm (tested on 4.64.1)

The ``utils`` module also requires:

    - statsmodels (tested on 0.13.2)

The ``plotting`` module also requires:

    - seaborn (tested on 0.12.0)
    - nibabel (tested on 4.0.2)
    - nilearn (tested on 0.9.2)

There are some additional (optional) dependencies you can install (note, these are only used for i/o and plotting in the
Python notebooks located in the `scripts` directory):

    - pandas (tested on 1.5.1)
    - matplotlib (tested on 3.5.3)
    - jupyterlab (tested on 3.4.4)
    - sklearn (tested on 0.0.post1)

If you want to install the environment that was used to run the analyses presented in the manuscript, use the
environment.yml file.

Basic installation
------------------

Assuming you have Python 3.9 installed, you can install ``nctpy`` by opening a terminal and running
the following:

.. code-block:: bash

    pip install nctpy

Questions
---------

If you have any questions, please contact Linden Parkes and Jason Kim: info@parkeslab.com.

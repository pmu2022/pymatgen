Compatibility
=============

Pymatgen is a tool used for academic research and is actively developed by
a large community of people. As such, releases are frequent, and new features
and capabilities are constantly being added.

However, pymatgen is also used as a library by other tools, and as such breaking
changes such as the removal or renaming of existing functionality, or substantive
changes in the output of existing code, are tried to be kept to a minimum. This is
especially true of all classes contained in the pymatgen.core module.

Despite this, it is sometimes necessary to make breaking changes to enable future
development, or because other libraries we depend upon might change
their own requirements. When this happens this page will be updated with guidance.

Minimum Python Version
----------------------

As a rule of thumb, pymatgen will support whatever versions of Python the latest
version of numpy supports (at the time of writing, this is Python 3.7+). You can
also check what versions of Python are being tested automatically as part of our
continuous integration testing on GitHub. We currently test pymatgen on Mac,
Windows and Linux.

Guidance If An API Changes
--------------------------

You can pin your own script or library to an older version of pymatgen, or
install an older version of pymatgen, for example `pip install pymatgen==2021.3.3`.

If a breaking change is causing significant issues, please post on the GitHub
Issues page to see if it can be resolved.

Recent Breaking Changes
-----------------------

v2022.0.0
~~~~~~~~~

Pymatgen root imports have been removed from v2022.0.0 in preparation for a change to a more modular, extensible
architecture that will allow more developers to contribute.

Specifically, the following "convenience imports" have been removed in favor of
their canonical import::

    from pymatgen import Composition  # now "from pymatgen.core.composition import Composition"
    from pymatgen import Lattice  # now "from pymatgen.core.lattice import Lattice"
    from pymatgen import SymmOp  # now "from pymatgen.core.operations import SymmOp"
    from pymatgen import DummySpecie, DummySpecies, Element, Specie, Species  # now "from pymatgen.core.periodic_table ..."
    from pymatgen import PeriodicSite, Site  # now "from pymatgen.core.sites ..."
    from pymatgen import IMolecule, IStructure, Molecule, Structure  # now "from pymatgen.core.structure ..."
    from pymatgen import ArrayWithUnit, FloatWithUnit, Unit  # now "from pymatgen.core.units ..."
    from pymatgen import Orbital, Spin  # now "from pymatgen.electronic_structure.core ..."
    from pymatgen import MPRester  # now "from pymatgen.ext.matproj ..."
	
If your existing code uses `from pymatgen import <something>`, you will need to make
modifications.

The easiest way is to use an IDE to run a Search and Replace. 
First, replace any `from pymatgen import MPRester` with
`from pymatgen.ext.matproj import MPRester`. Then, replace
`from pymatgen import` with `from pymatgen.core import`. Alternatively, if you
are using a Mac command line, you can try::

    find . -name '*.py' | xargs sed -i "" 's/from pymatgen import MPRester/from pymatgen.ext.matproj import MPRester/g'
    find . -name '*.py' | xargs sed -i "" 's/from pymatgen import/from pymatgen.core import/g'

From a Linux command line, you can try::

    find . -name '*.py' | xargs sed -i 's/from pymatgen import MPRester/from pymatgen.ext.matproj import MPRester/g'
    find . -name '*.py' | xargs sed -i 's/from pymatgen import/from pymatgen.core import/g'

This should resolve most import errors and only a few more modifications may
need to be done by hand.

v2021.3.3
~~~~~~~~~

The variable `pymatgen.SETTINGS` has been moved to `pymatgen.settings.SETTINGS`. Since this is
mostly used internally within pymatgen, it is not expected to lead to significant external issues.

v2021.2.8.1
~~~~~~~~~~~

The minimum version of Python was increased from 3.6 to 3.7 following the lead of numpy. However,
at this point there are no exclusively Python 3.7+ features used in pymatgen so pymatgen may still
be able to be installed manually on Python 3.6 systems, although this usage is not supported.

Support for `aconvasp` has been removed since the corresponding tests were failing and this module
was not being maintained.

v2020.10.20
~~~~~~~~~~~

The band structure plotting functionality, `BSPlotter`, has been overhauled to allow plotting of
multiple band structures. This might cause issues for tools relying on the internal structure
of BSPlotter's plot data.

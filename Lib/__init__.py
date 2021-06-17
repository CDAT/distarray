"""
Distributed array
"""
__all__ = ["mvMultiArrayIter"]
from .mvMultiArrayIter import MultiArrayIter

import os

mpi_disabled = os.environ.get("CDMS_NO_MPI", "False").lower() == 'true'

# is mpi4py available?
hasMpi4py = True
try:
    # skip trying to load mpi4py module
    if mpi_disabled:
        raise Exception()
    from mpi4py import MPI
except:
    hasMpi4py = False

if hasMpi4py:
    from .mvDistArray import DistArray, daZeros, daOnes, daArray
    from .mvGhostedDistArray import GhostedDistArray, ghZeros, ghOnes, ghArray
    __all__ += ["mvDistArray", "mvGhostedDistArray"]

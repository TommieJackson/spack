##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack.compiler import *


class Cce(Compiler):
    """Cray compiler environment compiler."""
    # Subclasses use possible names of C compiler
    cc_names = ['cc']

    # Subclasses use possible names of C++ compiler
    cxx_names = ['CC']

    # Subclasses use possible names of Fortran 77 compiler
    f77_names = ['ftn']

    # Subclasses use possible names of Fortran 90 compiler
    fc_names = ['ftn']

    # MacPorts builds gcc versions with prefixes and -mp-X.Y suffixes.
    suffixes = [r'-mp-\d\.\d']

    PrgEnv = 'PrgEnv-cray'
    PrgEnv_compiler = 'cce'

    link_paths = {'cc': 'cc',
                  'cxx': 'c++',
                  'f77': 'f77',
                  'fc': 'fc'}

    @classmethod
    def default_version(cls, comp):
        return get_compiler_version(comp, '-V', r'[Vv]ersion.*(\d+(\.\d+)+)')

    @property
    def openmp_flag(self):
        return "-h omp"

    @property
    def cxx11_flag(self):
        return "-h std=c++11"

    @property
    def pic_flag(self):
        return "-h PIC"

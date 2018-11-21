#python .\setup.py build_exe
#python .\setup.py bdist_msi

import sys, os
from cx_Freeze import setup, Executable

import tkinter
root = tkinter.Tk()
os.environ['TCL_LIBRARY'] = root.tk.exprstring('$tcl_library')
os.environ['TK_LIBRARY'] = root.tk.exprstring('$tk_library')

build_exe_options = {'include_msvcr': True, 'optimize': True}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = 'cliphist',
    description='Clip History Simple Tool App',
    version='1.0.0',
    options = {'build_exe': build_exe_options},
    executables = [Executable('clip_hist.pyw', base=base)]
)



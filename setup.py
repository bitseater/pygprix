import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

version = "0.1"

include_files = ["data/style.css",
                 "data/pygprix.ico"]

zip_include_packages = ["PyQt6",
                        "PySide6"]

options = {
    "build_exe": {
        "build_exe": "build/pygprix-" + version,
        "zip_include_packages": zip_include_packages,
        "include_files": include_files,
    },
}

executables = [Executable("src/app.py",
                          target_name="PyGPrix",
                          base=base, 
                          copyright="Copyright (C) 2024 Carlos Suárez", 
                          icon='data/pygprix.ico')]

setup(
    name="PyGPrix",
    version=version,
    description="Ergast API with Python & QT",
    author="Carlos Suárez",
    author_email="bitseater@gmail.com",
    url="https://github.com/bitseater/pygprix",
    options=options,
    executables=executables
)
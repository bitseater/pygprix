import sys
from cx_Freeze import setup, Executable

options = {
    "build_exe": {
        "zip_include_packages": ["PyQt6", "PySide6"],
        "include_files": ["data/style.css","data/pygprix.ico"],
    },
}

base = "Win32GUI" if sys.platform == "win32" else None

executables = [Executable("pygprix/app.py",
                          target_name="PyGPrix",
                          base=base, 
                          copyright="Copyright (C) 2024 Carlos Suárez", 
                          icon='data/pygprix.ico',)]

setup(
    name="PyGPrix",
    version="0.1",
    description="Ergast API with Python & QT",
    author="Carlos Suárez",
    author_email="bitseater@gmail.com",
    url="https://github.com/bitseater/pygprix",
    options=options,
    executables=executables
)
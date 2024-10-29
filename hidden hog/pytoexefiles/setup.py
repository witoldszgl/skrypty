from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("sus_terminal.pyw", base=base)
]

build_exe_options = {
    "packages": ["os", "sys", "tkinter", "PIL", "playsound", "time", "random", "ctypes"],
    "include_files": ["toggle.wav", "daemon.png"]
}

setup(
    name="Hidden Hog",
    version="1.0",
    description="An intriguing hidden desktop experience",
    options={"build_exe": build_exe_options},
    executables=executables
)

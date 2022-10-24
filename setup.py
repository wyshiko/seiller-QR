from cx_Freeze import setup, Executable
base = None
executables = [Executable("QR-Generator.py", base=base)]
packages = ["idna", "tkinter", "qrcode"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "QR",
    options = options,
    version = "1.0",
    description = 'Generateur de QR code',
    executables = executables
)
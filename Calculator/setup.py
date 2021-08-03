import cx_freez
includefiles = ['cal.ico']

base = None
if sys.platform == 'win32':
    base = "WIN32GUI"

if sys.platform =='win64':
    base = "WIN64GUI"

shortcut_table = [
    ("DesktopShortcut", #shortcut
    "DestopFolder", # Directory
    "My Claculator", # Name
    "TARGETDIR", # Component
    "[TARGETDIR]\Calculator.exe" ,# Target
    None,   # Argument
    None,   # Description
    None,   # Hotkey
    None,   # Icon
    None,   # IconIndex
    None,   # shotcut
    "TARGETDIR",    # wkdir
    )
]
msi_data = {'Shortcut': shortcut_table}

#Change some default MSI options and specify the use of the above defined tables

bdist_msi_options = {'data':msi_data}
setup(
    version="0.1",
    description=" My Calculator",
    author="Roshan Mishra",
    name="Calculator",
    options={"build_exe":{"include_files":includefiles}, "bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="cal_fun.py",
            base=base,
            icon='cal.ico',
        )
    ]
)
#pip install cx_freeze
import cx_Freeze
executables =[
    cx_Freeze.Executable(script="index.py", icon="meteoro.ico")
]
cx_Freeze.setup(
    name = "Foguetadas do Zanin",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["imagemdefundo.jpg",
                            "foguetecerto.png",
                            "meteoro.png",
                            "meteoro.mp3",
                            "trilha.mp3"
                            ]
        }
    }, executables = executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi
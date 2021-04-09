# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import glob
import shutil

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "moveFile":

    try:
        #source = GetParams("source").replace("\\", os.sep)
        source = GetParams("source")
        dest = GetParams("dest")
        ext_ = GetParams("ext_")
        opt_ = GetParams("opt_")
        #source = os.path.normpath(source)
        print('PATH', source)

        if not source.endswith("/"):
            source = source + "/"
        if not ext_:
            ext_ = "*.*"

        source = source + ext_

        if opt_:
            if opt_ == "move_":
                try:
                    print(source, dest)
                    for f in glob.glob(source):
                        shutil.move(f, dest)

                except Exception as e:
                    PrintException()
                    raise (e)

            if opt_ == "copy_":
                print('copy')
                try:

                    for f in glob.glob(source):
                        print('sdasdsa',f)
                        shutil.copy(f, dest)

                except Exception as e:
                    PrintException()
                    raise (e)
    except:
        PrintException()


if module == "moveFolder":

    source = GetParams("source")
    dest = GetParams("dest")
    opt_ = GetParams("opt_")
    files = os.listdir(source)

    if opt_:
        if opt_ == "move_":
            try:
                for f in files:
                    path_ = source + '/' + f
                    if os.path.isdir(path_):
                        shutil.move(path_, dest)

            except Exception as e:
                PrintException()
                raise (e)

        if opt_ == "copy_":
            try:
                for f in files:
                    path_ = os.path.join(source, f)
                    if os.path.isdir(path_):
                        print(path_)
                        for item in os.listdir(path_):
                            s = os.path.normpath(os.path.join(path_, item))
                            d = os.path.normpath(os.path.join(dest, os.path.basename(path_), item))
                            if os.path.isdir(s):
                                shutil.copytree(s, d, False, None)
                            else:
                                shutil.copy2(s,d)
                        # shutil.copytree(path_, dest,)

            except Exception as e:
                PrintException()
                raise (e)






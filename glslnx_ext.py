"""
----------------------------------------------------------------------------------------------------------
---------------------------------------- GLSL_LNX_Ext - *.glslnx -----------------------------------------
----------------------------------------------------------------------------------------------------------
-> Description:
GLSLNX is a description language to build large shaders. It is a prototype for a bigger idea.
The idea is to create multiple files shader files that are going to be merged together into a single file. 
This concept can be extended when adding conditionnal behavior and other basic operators. 
It could help build very large shaders w/ adaptative features based on the build configuration 
for the application that is being made.
----------------------------------------------------------------------------------------------------------
-> Current supported features:
    - merging multiple GLSL files into one big shader
    - that's it.
----------------------------------------------------------------------------------------------------------
-> Instructions:
    1. create a *.glslnx file (you can edit the code so the format has the name you want)
        1.1 always declare files in the order you want them to be merge into
        1.2 always have a "main.glsl" file (or whatever the name) that contains 
            the entrypoint of the shader
        1.3 the default output file name is "output.glsl"
    2. use the command "python glslnx_ext.py [glslnx file path]" and wait
----------------------------------------------------------------------------------------------------------
-> Disclaimer:
This code was written at 2:30am after a night of partying. So it's probably gross and slow. 
It was just to see how practical some kind of "build system" for shaders would be. 
Don't expect much maintenance for it. :)
----------------------------------------------------------------------------------------------------------
-> Semantic:
#f "file path"
#m "main file path"
#o "output name"
----------------------------------------------------------------------------------------------------------
-> License:
Do what you want with this code.
Copy, modify, distribute.
----------------------------------------------------------------------------------------------------------
"""

import sys
import re
import os.path

print("[GLSLNX] version: 1.0, last edit: 05/07/2017")
##load makefile
path = sys.argv[1]
fileObj = open(path, 'r')
fileObjHead, fileObjTail = os.path.split(path)
fileTypeCheck = re.match("^.*\.(glslnx|GLSLNX)$", path)
if fileTypeCheck:
    print("[GLSLNX]     Building from: " + path)
    ##parse makefile
    outputFilePath = "output.glsl"
    filesToIncludePaths = []
    entryPointFilePath = "NONE"
    makeFileLines = fileObj.readlines()
    for l in makeFileLines:
        ##identify files to include
        if l[:2] == "#f":
            s = l[3:].rstrip()
            filesToIncludePaths.append(s)
            print("[GLSLNX]     ----Include file: " + s)

        ##identify entrypoint
        elif l[:2] == "#m":
            s = l[3:].rstrip()
            entryPointFilePath = s
            print("[GLSLNX]     ----Entrypoint file: " + s)
        ##parse outputfile name
        elif l[:2] == "#o":
            outputFilePath = l[3:].rstrip()
        else:
            print("WARNING: invalid lined detected!")

    if entryPointFilePath != "NONE":
        ##loading main files
        entryPointFileObj = open(fileObjHead + "/" + entryPointFilePath, 'r')
        entryPointFileCompleteString = entryPointFileObj.readlines()
        entryPointFileObj.close()
        ##building new shader code
        outputString = ""
        #check if gl version statement is here
        appendVersionStatement = False
        firstLine = entryPointFileCompleteString[0]
        if firstLine[:8] == "#version":
            outputString += firstLine + "\n"
            appendVersionStatement = True

        #compiling files together
        for f in filesToIncludePaths:
            tmpFileObj = open(fileObjHead + "/" + f, 'r')
            outputString += tmpFileObj.read() + "\n" + "//-------------------------//" + "\n"
            tmpFileObj.close()
        
        if appendVersionStatement:
            for i in range(1, len(entryPointFileCompleteString)):
                outputString += entryPointFileCompleteString[i]
        else:
            for l in entryPointFileCompleteString:
                outputString += l
        
        ##output to file
        outputFileObj = open(fileObjHead + "/" + outputFilePath, 'w')
        outputFileObj.write(outputString)
        outputFileObj.close()
    else:
        print("[GLSLNX] ERROR: no entry point file!")
else:
    print("[GLSLNX] ERROR: filetype is invalid!")

fileObj.close
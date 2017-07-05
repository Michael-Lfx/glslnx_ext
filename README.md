# GLSLNX_EXT

## Description
GLSLNX is a description language to build large shaders. It is a prototype for a bigger idea.
The idea is to create multiple files shader files that are going to be merged together into a single file. 
This concept can be extended when adding conditionnal behavior and other basic operators. 
It could help build very large shaders w/ adaptative features based on the build configuration 
for the application that is being made.

## Current supported features
* merging multiple GLSL files into one big shader
* that's it.

## Instructions
1. create a *.glslnx file (you can edit the code so the format has the name you want)
    * always declare files in the order you want them to be merge into
    * always have a "main.glsl" file (or whatever the name) that contains 
    the entrypoint of the shader
    * the default output file name is "output.glsl"
2. use the command "python glslnx_ext.py [glslnx file path]" and wait

## Disclaimer
This code was written at 2:30am after a night of partying. So it's probably gross and slow. 
It was just to see how practical some kind of "build system" for shaders would be. 
Don't expect much maintenance for it. :)

## Semantic
``#f "file path"``
``#m "main file path"``
``#o "output name"``

## License
Do what you want with this code.
Copy, modify, distribute.
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
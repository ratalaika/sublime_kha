# -*- coding: utf-8 -*-

import sys
#sys.path.append("/usr/lib/python2.6/")
#sys.path.append("/usr/lib/python2.6/lib-dynload")

import sublime, sublime_plugin
import subprocess, time
import tempfile
import os, signal
#import xml.parsers.expat
import re
import codecs
import glob
import hashlib
import shutil
import functools

# Information about where the plugin is running from
plugin_file = __file__
plugin_filepath = os.path.realpath(plugin_file)
plugin_path = os.path.dirname(plugin_filepath)


try: # Python 3
 
    # Import the features module, including the haxelib and key commands etc
    from .features import *

    # Import the helper functions and regex helpers
    from .HaxeHelper import runcmd, show_quick_panel
    from .HaxeHelper import spaceChars, wordChars, importLine, packageLine, compilerOutput
    from .HaxeHelper import compactFunc, compactProp, libLine, classpathLine, typeDecl 
    from .HaxeHelper import libFlag, skippable, inAnonymous, extractTag
    from .HaxeHelper import variables, functions, functionParams, paramDefault
    from .HaxeHelper import isType, comments, haxeVersion, haxeFileRegex, controlStruct

except (ValueError): # Python 2
    
    # Import the features module, including the haxelib and key commands etc
    from features import *
    
    # Import the helper functions and regex helpers
    from HaxeHelper import runcmd, show_quick_panel
    from HaxeHelper import spaceChars, wordChars, importLine, packageLine, compilerOutput
    from HaxeHelper import compactFunc, compactProp, libLine, classpathLine, typeDecl 
    from HaxeHelper import libFlag, skippable, inAnonymous, extractTag
    from HaxeHelper import variables, functions, functionParams, paramDefault
    from HaxeHelper import isType, comments, haxeVersion, haxeFileRegex, controlStruct

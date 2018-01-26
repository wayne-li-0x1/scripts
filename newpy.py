#!/usr/bin/env python3
#-*-coding: utf-8 -*-
#pylint: disable=no-value-for-parameter,trailing-whitespace

"""
newpy.py

click command:
    newpy()

"""

import click

SCRIPT_TEMPL = \
"""#!/usr/bin/env python3
#-*-coding: utf-8 -*-
#pylint: disable=no-value-for-parameter

\"\"\"
%s.py

click command:
    %s()

\"\"\"

import click

@click.command()
def %s():
    \"\"\"
    <command description>
    \"\"\"
    return

if __name__ == "__main__":
    %s()
"""

@click.command()
@click.option('--script', default=True, type=bool, help="Script or non-script(module)")
@click.argument('name', required=True)
def newpy(name, script):
    """
    Create a new python3 script or a python3 module.
    And the created python file is gurranteed to pass pylint3(10.0/10.0)
    """
    if not script:
        print("NYI: Module py creation")
        return

    out_fn = name
    if name[-3:] != ".py":
        out_fn = name + ".py"
    else:
        out_fn = name
        name = ".".join((name.split("."))[:-1])

    print("Creating python %s: %s ..."%("script" if script else "module", out_fn))
    out_fp = open(out_fn, 'w')
    out_fp.write(SCRIPT_TEMPL%(name, name, name, name))
    out_fp.close()

    #now add execution permission
    import os
    import stat

    out_st = os.stat(out_fn)
    out_mode = out_st.st_mode
    out_mode |= (out_mode &0o444)>>2
    os.chmod(out_fn, out_mode)

    return

if __name__ == "__main__":
    newpy()



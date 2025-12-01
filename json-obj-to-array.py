"""Transform a json log into a json array

Transforms a Suricata JSON log 'stats.json' into an array, for ease
of parsing by JupyterLite notebook.
"""
with open("stats.json", "r") as i:
    with open("stats-parsable-stats.json", "w") as o:
        o.write("[")
        first_line = True
        for line in i:
            if first_line:
                first_line = False
            else:
                o.write(",")
            o.write(line)
        o.write("]")

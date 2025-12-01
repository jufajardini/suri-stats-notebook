# Suricata Stats Notebook

A simple Jupyter notebook to parse and visualize Suricata statistics logs.

## Motivation

This notebook was created as part of a SuriCon 2025 Montreal talk on the Suricata
statistics (aka Suricata stats) log files, in particular the EVE json logs.

The idea was to offer a simple demo with stats visualizations, to showcase what
Suricata stats have to offer. There are lots of great tools for proper data
manipulation and visualization, this script just helps with... Not having to
set-up complex things to play with whichever stats you want to see.

As such, this repo exists as complement to the presentation slides, mostly (as
of now).

## Preparation

The notebook was created on the JupyterLite lab (https://jupyter.org/try-jupyter/lab/).
As such, it required a minimal preparation of the raw Suricata stats.eve log to
be made into an array -- otherwise the file wouldn't be loaded.

For such, any tooling could be used. In the presentation I used the scrip
`json-obj-to-array.py` that is also in this repo. It is very crude for now, and
file names must be changed in the code itself :P

## Repo Contents

- demo-ids.ipynb -- the jupyter notebook
- `json-obj-to-array.py` -- python script to transform a suricata stats.json log

## Notebook Contents / Usage

Its goal was to have something simple that would allow one to load a log file
and extract simple data such as:
- JSON object structure
- log timestamp as its own array, to aid graph creation (as the field is not part of the stats object)
- Stats as a table
- Number of stats counters (as each final node is called for the Suricata stats)

After that, 4 functions for graph build and visualization are provided:
- `diff_values` -- for internal usage - called by other functions if counter is incremental
- `plot_incremental_counter_over_time` -- plot a counter over time
- `plot_correlate_counters` -- correlate two counters
- `plot_correlate_2_y_counters` -- correlate two counters over time




#!/usr/bin/env python
'''
Created on 2015/11/26

@author: rsaito
'''

import os
from glob import glob

IMMWEB_TOPDIR   = "/Users/rsaito/Sites/ucsd-imm.github.io/Ver0p7"
REPLACE_STR     = "<!-- main_area content -->"
TEMPLATE_FILE   = os.path.join(IMMWEB_TOPDIR, "TEMPLATES", "ucsd_imm1_2.html")
INPUT_HTML_DIR  = os.path.join(IMMWEB_TOPDIR, "HTMLi")
OUTPUT_HTML_DIR = os.path.join(IMMWEB_TOPDIR, "HTMLo")

template_html_str = "".join(open(TEMPLATE_FILE).readlines())


for ifile in glob(os.path.join(INPUT_HTML_DIR, "*.[Hh]tm*")):
    html_istr = "".join(open(ifile).readlines())
    ofile = os.path.join(OUTPUT_HTML_DIR, os.path.basename(ifile))
    html_ostr = template_html_str.replace(REPLACE_STR, html_istr)

    open(ofile, "w").write(html_ostr)        
    print(ifile, "was converted to", ofile)

    

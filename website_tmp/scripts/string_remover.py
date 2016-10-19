# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 13:53:00 2016

@author: god
"""

import glob
import numpy as np

#die filenames in string array einlesen
filenames = sorted(glob.glob('*.html'))
#index_fr=[line for line in open('index_fr.html').readlines()]
index_en=[line for line in open('index_en.html').readlines()]


for k in xrange(np.size(filenames)):
    #fur jede file, das prozedere laufen lassen
    infile = open(filenames[k])
    outfile = open('out/'+filenames[k], 'w')
    print k
    
#    if '_fr' in filenames[i]:
#        replacements=replacements_fr  
#    elif '_en' in filenames[i]:
#        replacements=replacements_en  
#    else:
#        break
#        print 'files dont contain either _fr nor _en'

    #menu_fr=index_fr[50:119]
    #footer_fr=index_fr[268:308]
    menu_en=index_en[49:118]
    footer_en=index_en[267:307]
    lines = [line for line in infile.readlines()]
    
    for i, line in enumerate(lines):
#in the following, it is easier to work just with lines[i], there fore 2 conditions in the if
#        if (c in lines[i] and b in lines[i+1]):
#            print 'working'
#            lines.remove(lines[i])
#            lines.remove(lines[i])
#            lines.remove(lines[i])
#            lines.remove(lines[i])
#            lines[i]='            <div class="col-xs-12">\r\n'
        if '<li><i class="icon-phone"></i>' in lines[i]:
            print 'found phone'
            lines.remove(lines[i])
#        if '<!--=== End Header ===-->' in lines[i]:
#            print 'found end top'
#            indexm_f=i
#        if '<!--=== Footer ===-->' in lines[i]:
#            print 'found footer'
#            indexf_i=i
#        if '<!--=== End Footer ===-->' in lines[i]:
#            print 'found end_footer'
#            indexf_f=i   
#    lines[indexm_i:indexm_f]=menu_en
#    lines[indexf_i:indexf_f]=footer_en
    for i, line in enumerate(lines): 
        outfile.write(lines[i])
infile.close()
outfile.close()
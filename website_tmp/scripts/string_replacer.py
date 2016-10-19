# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 20:33:06 2014

@author: god
Script for replacing strings in the files. More concretely, it runs through all html files and differentiates those with _en and _fr in the filenames.
"""
#import glob
#import numpy as np
#
##die filenames in string array einlesen
#filenames = sorted(glob.glob('*.html'))
#
#
##replacements_fr = {'index.html':'index_fr.html', 'tv.html':'tv_fr.html', 'beamer.html':'beamer_fr.html','ls.html':'ls_fr.html','kontakt.html':'kontakt_fr.html','laptops.html':'laptops_fr.html','eco.html':'eco_fr.html','about.html':'about_fr.html','soon.html':'soon_fr.html'}
##replacements_en = {'index.html':'index_en.html', 'tv.html':'tv_en.html', 'beamer.html':'beamer_en.html','ls.html':'ls_en.html','kontakt.html':'kontakt_en.html','laptops.html':'laptops_en.html','eco.html':'eco_en.html','about.html':'about_en.html','soon.html':'soon_en.html'}
##replacements= {'<li><a href="soon.html">Beamer</a></li>':'<li><a href="http://www.ricardo.ch/online-shop/smart-reparaturen/?CategoryNr=42221&SortingType=1&SellerNickName=smart-reparaturen" target="_blank">Beamer</a></li>','<a href="shop.html" class="btn-m btn-lg btn-m-blue">Boutique</a>':'<a href="http://www.fr.ricardo.ch/online-shop/smart-reparaturen/?CategoryNr=42221&SortingType=1&SellerNickName=smart-reparaturen" target="_blank" class="btn-m btn-lg btn-m-blue">Boutique</a>','<li><a href="soon_fr.html">Vidéoprojecteurs</a></li>':'<li><a href="http://www.fr.ricardo.ch/online-shop/smart-reparaturen/?CategoryNr=42221&SortingType=1&SellerNickName=smart-reparaturen" target="_blank">Vidéoprojecteurs</a></li>','<a href="shop.html" class="btn-m btn-lg btn-m-blue">Shop</a>':'<a href="http://www.ricardo.ch/online-shop/smart-reparaturen/?CategoryNr=42221&SortingType=1&SellerNickName=smart-reparaturen" target="_blank" class="btn-m btn-lg btn-m-blue">Shop</a>','<li><a href="soon_en.html">Projectors</a></li>':'<li><a href="http://www.ricardo.ch/online-shop/smart-reparaturen/?CategoryNr=42221&SortingType=1&SellerNickName=smart-reparaturen" target="_blank">Projectors</a></li>','<a href="shop.html" class="btn-m btn-lg btn-m-blue">Shop</a>':'<a href="http://www.ricardo.ch/online-shop/smart-reparaturen/?CategoryNr=42221&SortingType=1&SellerNickName=smart-reparaturen" target="_blank" class="btn-m btn-lg btn-m-blue">Shop</a>'}
#replacements
#
#
#
#for i in xrange(np.size(filenames)):
#    #fur jede file, das prozedere laufen lassen
#    infile = open(filenames[i])
#    outfile = open('out/'+filenames[i], 'w')
#    print i
#    
##    if '_fr' in filenames[i]:
##        replacements=replacements_fr  
##    elif '_en' in filenames[i]:
##        replacements=replacements_en  
##    else:
##        replacements=replacements_de  
#    for line in infile:
#        for src, target in replacements.iteritems():
#            line = line.replace(src, target)
#        outfile.write(line)
#infile.close()
#outfile.close()
#
#"""the later part of the script links the list of languages when clicked on each page to the corresponding translated page"""




#import glob
#import numpy as np
#
##die filenames in string array einlesen
#filenames = sorted(glob.glob('*.html'))
#
#purenames = [w.replace('_en','') for w in filenames]
#purenames = [purenames.replace('_fr','') for purenames in purenames]
#purenames = [purenames.replace('.html','') for purenames in purenames]
#
#
#
#
##replacements_fr = {'index.html':'index_fr.html', 'tv.html':'tv_fr.html', 'beamer.html':'beamer_fr.html','ls.html':'ls_fr.html','kontakt.html':'kontakt_fr.html','laptops.html':'laptops_fr.html','eco.html':'eco_fr.html','about.html':'about_fr.html','soon.html':'soon_fr.html'}
##replacements_en = {'index.html':'index_en.html', 'tv.html':'tv_en.html', 'beamer.html':'beamer_en.html','ls.html':'ls_en.html','kontakt.html':'kontakt_en.html','laptops.html':'laptops_en.html','eco.html':'eco_en.html','about.html':'about_en.html','soon.html':'soon_en.html'}
#
#a="""<li class="active"><a href="soon.html">English</a></li>
#                            <li><a href="#">Deutsch</a></li>"""
#
#for i in xrange(np.size(filenames)):
#    #fur jede file, das prozedere laufen lassen
#    infile = open(filenames[i])
#    outfile = open('out/'+filenames[i], 'w')
#    print i
#    
##    if '_fr' in filenames[i]:
##        purenames=filenames[i].replace(")
##    elif '_en' in filenames[i]:
##        replacements=replacements_en  
##    else:
##        break
##        print 'files dont contain either _fr nor _en'
#
#    replacements={'<li class="active"><a href="soon.html">English</a></li>':'<li ><a href="'+purenames[i]+'_en.html'+'">English</a></li>','<li><a href="#">Deutsch</a></li>':'<li><a href="'+purenames[i]+'.html'+'">Deutsch</a></li><li><a href="'+purenames[i]+'_fr.html'+'">Français</a></li>','<li class="active"><a href="soon_en.html">English</a></li>':'<li ><a href="'+purenames[i]+'_en.html'+'">English</a></li>','<li class="active"><a href="soon_fr.html">English</a></li>':'<li ><a href="'+purenames[i]+'_en.html'+'">English</a></li>'}
#    
#
#    for line in infile:
#        for src, target in replacements.iteritems():
#            line = line.replace(src, target)
#        outfile.write(line)
#infile.close()
#outfile.close()


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
        if '!--=== Header ===-->' in lines[i]:
            print 'found top'
            indexm_i=i
        if '<!--=== End Header ===-->' in lines[i]:
            print 'found end top'
            indexm_f=i
        if '<!--=== Footer ===-->' in lines[i]:
            print 'found footer'
            indexf_i=i
        if '<!--=== End Footer ===-->' in lines[i]:
            print 'found end_footer'
            indexf_f=i   
    lines[indexm_i:indexm_f]=menu_en
    lines[indexf_i:indexf_f]=footer_en
    for i, line in enumerate(lines): 
        outfile.write(lines[i])
infile.close()
outfile.close()
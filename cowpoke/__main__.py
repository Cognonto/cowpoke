# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:19:01 2020

@author: Michael K. Bergman
"""

from cowpoke.config import * 
from owlready2 import *
import csv

world = World()

kb_src = master_deck.get('kb_src')                         # we get the build setting from config.py

if kb_src is None:
    kb_src = 'standard'
elif kb_src is 'extract':
    kbpedia = 'C:/1-ActivePython/kbpedia/v300/build/ontologies/kbpedia_reference_concepts.owl'
    kko_file = 'C:/1-ActivePython/kbpedia/v300/build/stubs/kko.owl'
elif kb_src is 'full':
    kb_src = 'start'    
elif kb_src == 'working':
    kbpedia = 'C:/1-ActivePython/kbpedia/working/kbpedia_reference_concepts.owl'
    kko_file = 'C:/1-ActivePython/kbpedia/working/kko.owl'
elif kb_src == 'standard':
    kbpedia = 'C:/1-ActivePython/kbpedia/v300/working/kbpedia_reference_concepts.owl'
    kko_file = 'C:/1-ActivePython/kbpedia/v300/build/stubs/kko.owl'
elif kb_src == 'start':
    kbpedia = 'C:/1-ActivePython/kbpedia/v300/build/stubs/kbpedia_rc_stub.owl'
    kko_file = 'C:/1-ActivePython/kbpedia/v300/build/stubs/kko.owl'
else:
    print('You have entered an inaccurate source parameter for the build.')
skos_file = 'http://www.w3.org/2004/02/skos/core'


kb = world.get_ontology(kbpedia).load()
rc = kb.get_namespace('http://kbpedia.org/kko/rc/')               

skos = world.get_ontology(skos_file).load()
kb.imported_ontologies.append(skos)
core = world.get_namespace('http://www.w3.org/2004/02/skos/core#')

kko = world.get_ontology(kko_file).load()
kb.imported_ontologies.append(kko)
kko = kb.get_namespace('http://kbpedia.org/ontologies/kko#')


def render_using_iri(entity):
    return entity.iri

def render_using_label(entity):
    return entity.label.first() or entity.name    

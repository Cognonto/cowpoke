# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:49:55 2020

@author: Michael K. Bergman
"""

                                                      
from cowpoke.__main__ import *
from cowpoke.config import *
                              
""" we get the run specification dictionary from config.py """

def mapping_builder(**build_deck):
    print('Beginning KBpedia mappings build . . .')
    loop_list = build_deck.get('loop_list')
    base = build_deck.get('base')
    ext = build_deck.get('ext')
    out_file = build_deck.get('out_file')
    for loopval in loop_list:                                               
        print('   . . . processing', loopval)                             
        in_file = (base + loopval + ext)
        print(in_file)
        with open(in_file, 'r', encoding='utf8') as input:
            is_first_row = True
            reader = csv.DictReader(input, delimiter=',', fieldnames=['s', 'p', 'o'])
            for row in reader:                                              
                if is_first_row:
                    is_first_row = False                
                    continue
                r_s = row['s']                                              
                if 'kko/rc' in r_s:                                         
                    r_s = r_s.replace('http://kbpedia.org/kko/rc/', '')
                    r_s = getattr(rc, r_s)
                else:
                    r_s = r_s.replace('http://kbpedia.org/ontologies/kko#', '')
                    r_s = getattr(kko, r_s)                                         
                r_p = row['p']                                              
                r_o = row['o']
                if loopval == 'dbpedia':                                                       
                    kb_frag = 'dbpedia_id'
                    kb_prop = getattr(rc, kb_frag)
                    r_s.dbpedia_id.append(r_o)                             
                elif loopval == 'dbpedia-ontology':
                    kb_frag = 'dbpedia_ontology_id'
                    kb_prop = getattr(rc, kb_frag)
                    r_s.dbpedia_ontology_id.append(r_o)
                elif loopval == 'geonames':
                    kb_frag = 'geo_names_id'
                    kb_prop = getattr(rc, kb_frag)
                    r_s.geo_names_id.append(r_o)
                elif loopval == 'schema.org':
                    kb_frag = 'schema_org_id'
                    kb_prop = getattr(rc, kb_frag)
                    r_s.schema_org_id.append(r_o)
                elif loopval == 'wikidata':
                    kb_frag = 'wikidata_q_id'
                    kb_prop = getattr(rc, kb_frag)
                    r_s.wikidata_q_id.append(r_o)
                elif loopval == 'wikipedia':
                    kb_frag = 'wikipedia_id'
                    kb_prop = getattr(rc, kb_frag)
                    r_s.wikipedia_id.append(r_o)
                elif loopval == 'wikipedia-categories':
                    kb_frag = 'wikipedia_category_id'
                    kb_prop = getattr(rc, kb_frag)
                    r_s.wikipedia_category_id.append(r_o)
                else:
                    print(loopval, 'is not on list.')
                kko.mappingAsObject[r_s, kb_prop, r_o] = [r_p]                    
                print(r_s)
    print('External mapping uploads are complete.')
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:49:55 2020

@author: Michael K. Bergman
"""

"""
Most of the visualization specifications and functions are provided in the accompanying
CWPK interactive notebooks (#55 and #56). See those for specific routines.
"""                            
                                                      
from cowpoke.__main__ import *
from cowpoke.config import *

def graph_extractor(**extract_deck):
    print('Beginning graph structure extraction . . .')
    loop_list = extract_deck.get('loop_list')
    loop = extract_deck.get('loop')
    class_loop = extract_deck.get('class_loop')
    base = extract_deck.get('base')
    ext = extract_deck.get('ext')
    parent_set = ['kko.SocialSystems','kko.Products','kko.Methodeutic','kko.Eukaryotes',
              'kko.ConceptualSystems','kko.AVInfo','kko.Systems','kko.Places',
              'kko.OrganicChemistry','kko.MediativeRelations','kko.LivingThings',
              'kko.Information','kko.CopulativeRelations','kko.Artifacts','kko.Agents',
              'kko.TimeTypes','kko.Symbolic','kko.SpaceTypes','kko.RepresentationTypes',
              'kko.RelationTypes','kko.OrganicMatter','kko.NaturalMatter',
              'kko.AttributeTypes','kko.Predications','kko.Manifestations',
              'kko.Constituents']

    if loop is not 'class_loop':
        print("Needs to be a 'class_loop'; returning program.")
        return
    header = ['target', 'source', 'weight', 'SuperType']
    out_file = extract_deck.get('out_file')
    cur_list = []
    with open(out_file, mode='w', encoding='utf8', newline='') as output:                                           
        csv_out = csv.writer(output)
        csv_out.writerow(header)    
        for value in loop_list:
            print('   . . . processing', value)
            s_set = []
            root = eval(value)
            s_set = root.descendants()
            frag = value.replace('kko.','')
            for s_item in s_set:
                child_set = list(s_item.subclasses())
                count = len(list(child_set))
                if value not in parent_set:
                    for child_item in child_set:
                        s_rc = str(s_item)
                        child = str(child_item)
                        new_pair = s_rc + child
                        new_pair = str(new_pair)
                        cur_list.append(new_pair)
                        s_rc = s_rc.replace('rc.','')
                        child = child.replace('rc.','')
                        row_out = (s_rc,child,count,frag)
                        csv_out.writerow(row_out)
                elif value in parent_set:
                    for child_item in child_set:
                        s_rc = str(s_item)
                        child = str(child_item)
                        new_pair = s_rc + child
                        new_pair = str(new_pair)
                        if new_pair not in cur_list:
                            cur_list.append(new_pair)
                            s_rc = s_rc.replace('rc.','')
                            child = child.replace('rc.','')
                            row_out = (s_rc,child,count,frag)
                            csv_out.writerow(row_out)
                        elif new_pair in cur_list:
                            continue
        output.close()         
        print('Processing is complete . . .')
graph_extractor(**extract_deck)
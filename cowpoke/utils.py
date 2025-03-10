# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:35:44 2020

@author: Michael K. Bergman
"""

                                                      
from cowpoke.__main__ import *
from cowpoke.config import *
                              
""" we get the run specification dictionary from config.py """


def dup_remover(**build_deck):
    print('Beginning duplicate remover routine . . .')
    loop_list = build_deck.get('loop_list')
    loop = build_deck.get('loop')
    base = build_deck.get('base')
    base_out = build_deck.get('base_out')
    ext = build_deck.get('ext')
    for loopval in loop_list:
        print('   . . . removing dups in', loopval)
        frag = loopval.replace('kko.','')
        in_file = (base + frag + ext)
        newrows = []                                           
        with open(in_file, 'r', encoding='utf8') as input:
            is_first_row = True
            reader = csv.DictReader(input, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])
            for row in reader:
                if row not in newrows:                         
                    newrows.append(row)                        
        out_file = (base_out + frag + ext)    
        with open(out_file, 'w', encoding='utf8', newline='') as output:
            is_first_row = True
            writer = csv.DictWriter(output, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])                 
            writer.writerows(newrows)
    print('File dup removals now complete.')  
    

def set_union(**build_deck):
    print('Beginning set union routine . . .')                         
    loop_list = build_deck.get('loop_list')
    loop = build_deck.get('loop')
    base = build_deck.get('base')
    short_base = build_deck.get('short_base')
    base_out = build_deck.get('base_out')
    ext = build_deck.get('ext')
    f_union = (short_base + 'union' + ext)
    filetemp = open(f_union, 'w+', encoding='utf8')               
    filetemp.truncate(0)
    filetemp.close()
    input_rows = []
    union_rows = []
    first_pass = 0                                               
    for loopval in loop_list:
        print('   . . . evaluating', loopval, 'using set union operations . . .')
        frag = loopval.replace('kko.','')
        f_input = (base + frag + ext)
        with open(f_input, 'r', encoding='utf8') as input_f:    
            is_first_row = True
            reader = csv.DictReader(input_f, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])
            for row in reader:
                if row not in input_rows:                          
                    input_rows.append(row)
            if first_pass == 0:                                  
                union_rows = input_rows
        with open(f_union, 'r', encoding='utf8', newline='') as union_f: 
            is_first_row = True
            reader = csv.DictReader(union_f, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])
            for row in reader:
                if row not in union_rows:
                    if row not in input_rows:
                        union_rows.append(row)
                    union_rows = input_rows + union_rows              
        with open(f_union, 'w', encoding='utf8', newline='') as union_f:
            is_first_row = True
            u_writer = csv.DictWriter(union_f, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])                 
            u_writer.writerows(union_rows)                                     
        first_pass = 1        
    print('Set union operation now complete.') 


def set_difference(**build_deck):
    print('Beginning set difference routine . . .')                         
    loop_list = build_deck.get('loop_list')
    loop = build_deck.get('loop')
    base = build_deck.get('base')
    short_base = build_deck.get('short_base')
    base_out = build_deck.get('base_out')
    ext = build_deck.get('ext')
    f_union = (short_base + 'union' + ext)
    filetemp = open(f_union, 'w+', encoding='utf8')               
    filetemp.truncate(0)
    filetemp.close()
    input_rows = []
    union_rows = []
    first_pass = 0                                               
    for loopval in loop_list:
        print('   . . . evaluating', loopval, 'using set difference operations . . .')
        frag = loopval.replace('kko.','')
        f_input = (base + frag + ext)
        with open(f_input, 'r', encoding='utf8') as input_f:    
            is_first_row = True
            reader = csv.DictReader(input_f, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])
            for row in reader:
                if row not in input_rows:                          
                    input_rows.append(row)
            if first_pass == 0:                                  
                union_rows = input_rows
        with open(f_union, 'r', encoding='utf8', newline='') as union_f: 
            is_first_row = True
            reader = csv.DictReader(union_f, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])
            for row in reader:
                if row not in union_rows:
                    if row not in input_rows:
                        union_rows.append(row)
                    union_rows = union_rows - input_rows              
        with open(f_union, 'w', encoding='utf8', newline='') as union_f:
            is_first_row = True
            u_writer = csv.DictWriter(union_f, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])                 
            u_writer.writerows(union_rows)                                     
        first_pass = 1        
    print('Set difference operation now complete.')


def set_intersection(**build_deck):
    print('Beginning set intersection routine . . .')                     
    loop_list = build_deck.get('loop_list')
    loop = build_deck.get('loop')
    base = build_deck.get('base')
    short_base = build_deck.get('short_base')
    base_out = build_deck.get('base_out')
    ext = build_deck.get('ext')
    f_intersection = (short_base + 'intersection' + ext)                 
    filetemp = open(f_intersection, 'w+', encoding='utf8')                       
    filetemp.truncate(0)
    filetemp.close()
    first_pass = 0                                                        
    for loopval in loop_list:
        print('   . . . evaluating', loopval, 'using set intersection operations . . .')
        frag = loopval.replace('kko.','')
        f_input = (base + frag + ext)
        input_rows = set()                                              
        intersection_rows = set()
        with open(f_input, 'r', encoding='utf8') as input_f:              
            input_rows = input_f.readlines()[1:]                         
        with open(f_intersection, 'r', encoding='utf8', newline='') as intersection_f:
            if first_pass == 0:                                           
                intersection_rows = input_rows
            else:
                intersection_rows = intersection_f.readlines()[1:]
            intersection = list(set(intersection_rows) & set(input_rows))
        with open(f_intersection, 'w', encoding='utf8', newline='') as intersection_f:
            intersection_f.write('id,subClassOf,parent\n')
            for row in intersection:
                intersection_f.write('%s' % row)                                                             
        first_pass = 1        
    print('Set intersection operation now complete.')
    

def typol_intersects(**build_deck):
    kko_list = typol_dict.values()
    count = build_deck.get('count')
    out_file = build_deck.get('out_file')
    with open(out_file, 'w', encoding='utf8') as output:
        print('count,kko_1,kko_2,intersect RCs', file=output)
        for i in combinations(kko_list,2):                              
            kko_1 = i[0]                                              
            kko_2 = i[1]                                              
            kko_1_frag = kko_1.replace('kko.', '')
            kko_1 = getattr(kko, kko_1_frag)                         
            kko_2_frag = kko_2.replace('kko.', '')
            kko_2 = getattr(kko, kko_2_frag)     
            descent_1 = kko_1.descendants(include_self = False)       
            descent_1 = set(descent_1)
            descent_2 = kko_2.descendants(include_self = False)
            descent_2 = set(descent_2)
            intersect = descent_1.intersection(descent_2)              
            num = len(intersect)
            if num <= count:                                           
                print(num, kko_1, kko_2, intersect, sep=',', file=output)
            else: 
                print(num, kko_1, kko_2, sep=',', file=output)
    print('KKO typology intersection analysis is done.')
    

def disjoint_status():
    output = list(world.disjoint_classes())
    disjoint_file = open('C:/1-PythonProjects/kbpedia/v300/build_ins/working/kbpedia_disjoint.csv', 'w', encoding='utf8')
    disjoint_file.write('id,disjoints\n')
    for element in output:
        element = str(element)
        element = element.replace('AllDisjoint([', '')
        element = element.replace('C:\\1-PythonProjects\\kbpedia\\sandbox\\', '')
        element = element.replace(' | ', ',')
        element = element.replace(' ', '')
        element = element.replace('])', '')
        element = element.replace(',ontology=get_ontology("http://kbpedia.org/ontologies/kko#"))', '')
        element = element.replace(']', '')
        disjoint_file.write(element)
        disjoint_file.write('\n')
    disjoint_file.close() 
    
    
def branch_orphan_check(**build_deck):
    print('Beginning branch and orphan checks . . .')                     
#    loop_list = build_deck.get('loop_list')                               
    loop_list = kko.Generals.descendants()                                
    loop_list = set(loop_list)
    kko_list = list(typol_dict.values())
    item_list = []
    for i, item in enumerate(kko_list):                                                                     
        item_frag = item.replace('kko.','')
        kko_item = getattr(kko, item_frag)
        kko_list[i] = kko_item
    print('After:', kko_list)
    out_file = 'C:/1-PythonProjects/kbpedia/v300/targets/stats/branches_orphans.csv'
    with open(out_file, 'w', encoding='utf8') as output:
        print('rc', file=output)
        kko_list = set(kko_list)
        for loopval in loop_list:
            val = loopval
            print('   . . . evaluating', loopval, 'checking for branches and orphans . . .')  
            val_list = val.ancestors(include_self = False)
            val_list = set(val_list)
            intersect = val_list.intersection(kko_list)
            num = len(intersect)
            print(num)
            if num == 0:
                print('Unconnected RC:', val, file=output)    
    print('Branch and orphan analysis now complete.')


def dups_parental_chain(**build_deck):
    print('Beginning duplicate RC placement analysis . . .')                     
    loop_list = kko.AudioInfo.descendants()                                
    out_file = 'C:/1-PythonProjects/kbpedia/v300/targets/stats/parental_dups.csv'    
    with open(out_file, 'w', encoding='utf8') as output:
        print('count,rc,dups', file=output)
        for item in loop_list:                                           
            rc = item
            rc_list = rc.ancestors(include_self = False)
            dup_keep = []
            for par_item in rc_list:
                parent = par_item
                par_list = parent.subclasses()
                for dup_item in par_list:
                    dup = dup_item
                    if rc == dup:
#                        dup_check = dup.ancestors(include_self = False)
#                        if(all(x in rc_list for x in dup_check)):
#                            print(rc, ',', parent, file=output)   
                        dup_keep.append(parent)                
            count = len(dup_keep)
            if count > 1:
                print(count, ',', rc, ',', dup_keep, file=output)
    print('Duplicate RC checking and analysis is complete.')     
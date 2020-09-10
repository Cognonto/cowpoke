# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:35:44 2020

@author: Michael K. Bergman
"""

                                                      
from cowpoke.__main__ import *
from cowpoke.config import *
                              
""" we get the run specification dictionary from config.py """


def row_clean(value, iss=''):
    if iss == 'i_id':
        value = value.replace('http://kbpedia.org/kko/rc/', 'rc.')
        value = value.replace('http://kbpedia.org/ontologies/kko#', 'kko.')
        return value
    if iss == 'i_id_frag':
        value = value.replace('http://kbpedia.org/kko/rc/', '')
        value = value.replace('http://kbpedia.org/ontologies/kko#', '')
        return value
    if iss == 'i_parent':
        value = value.replace('http://kbpedia.org/kko/rc/', 'rc.')           
        value = value.replace('http://kbpedia.org/ontologies/kko#', 'kko.')
        value = value.replace('owl:', 'owl.')
        return value
    if iss == 'i_parent_frag':
        value = value.replace('http://kbpedia.org/kko/rc/', '')           
        value = value.replace('http://kbpedia.org/ontologies/kko#', '')
        value = value.replace('owl:', '')
        return value
    

def class_struct_builder(**build_deck):                                  
    print('Beginning KBpedia class structure build . . .')               
    kko_list = typol_dict.values()                                      
    loop_list = build_deck.get('loop_list')
    loop = build_deck.get('loop')
    base = build_deck.get('base')
    ext = build_deck.get('ext')
    out_file = build_deck.get('out_file')
    if loop is not 'class_loop':
        print("Needs to be a 'class_loop'; returning program.")
        return
    for loopval in loop_list:
        print('   . . . processing', loopval)                           
        frag = loopval.replace('kko.','')
        in_file = (base + frag + ext)
        with open(in_file, 'r', encoding='utf8') as input:
            is_first_row = True
            reader = csv.DictReader(input, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])                 
            for row in reader:
                r_id = row['id'] 
                r_parent = row['parent']
                id = row_clean(r_id, iss='i_id')                         
                id_frag = row_clean(r_id, iss='i_id_frag')
                parent = row_clean(r_parent, iss='i_parent')
                parent_frag = row_clean(r_parent, iss='i_parent_frag')
                if is_first_row:                                       
                    is_first_row = False
                    continue      
                with rc:                                                
                    kko_id = None
                    kko_frag = None
                    if parent_frag == 'Thing':                                                        
                        if id in kko_list:                                
                            kko_id = id
                            kko_frag = id_frag
                        else:    
                            id = types.new_class(id_frag, (Thing,))       
                if kko_id != None:                                         
                    with kko:                                                
                        kko_id = types.new_class(kko_frag, (Thing,))  
        with open(in_file, 'r', encoding='utf8') as input:
            is_first_row = True
            reader = csv.DictReader(input, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])
            for row in reader:                                                
                r_id = row['id'] 
                r_parent = row['parent']
                id = row_clean(r_id, iss='i_id')
                id_frag = row_clean(r_id, iss='i_id_frag')
                parent = row_clean(r_parent, iss='i_parent')
                parent_frag = row_clean(r_parent, iss='i_parent_frag')
                if is_first_row:
                    is_first_row = False
                    continue          
                with rc:
                    kko_id = None                                   
                    kko_frag = None
                    kko_parent = None
                    kko_parent_frag = None
                    if parent_frag is not 'Thing':
                        if id in kko_list:
                            continue
                        elif parent in kko_list:
                            kko_id = id
                            kko_frag = id_frag
                            kko_parent = parent
                            kko_parent_frag = parent_frag
                        else:   
                            var1 = getattr(rc, id_frag)               
                            var2 = getattr(rc, parent_frag)
                            if var2 == None:                            
                                continue
                            else:                                
                                var1.is_a.append(var2)
                if kko_parent != None:                                         
                    with kko:                
                        if kko_id in kko_list:                               
                            continue
                        else:
                            var1 = getattr(rc, kko_frag)
                            var2 = getattr(kko, kko_parent_frag)                     
                            var1.is_a.append(var2)
        with open(in_file, 'r', encoding='utf8') as input:                
            is_first_row = True
            reader = csv.DictReader(input, delimiter=',', fieldnames=['id', 'subClassOf', 'parent'])
            for row in reader:                                              
                r_id = row['id'] 
                r_parent = row['parent']
                id = row_clean(r_id, iss='i_id')
                id_frag = row_clean(r_id, iss='i_id_frag')
                parent = row_clean(r_parent, iss='i_parent')
                parent_frag = row_clean(r_parent, iss='i_parent_frag')
                if is_first_row:
                    is_first_row = False
                    continue
                if parent_frag == 'Thing':               
                    var1 = getattr(rc, id_frag)
                    var2 = getattr(owl, parent_frag)
                    try:
                        var1.is_a.remove(var2)
                    except Exception:
                        continue
    with open(out_file, 'w', encoding='utf8') as f:
        print('KBpedia class structure build is complete.')
        f.close()   
    

def property_struct_builder(**build_deck):
    print('Beginning KBpedia property structure build . . .')
    kko_list = typol_dict.values()
    loop_list = build_deck.get('loop_list')
    loop = build_deck.get('loop')
    base = build_deck.get('base')
    ext = build_deck.get('ext')
    out_file = build_deck.get('out_file')
    if loop is not 'property_loop':
        print("Needs to be a 'property_loop'; returning program.")
        return
    for loopval in loop_list:
        print('   . . . processing', loopval)
        frag = 'struct_properties'                                    
        in_file = (base + frag + ext)
        with open(in_file, 'r', encoding='utf8') as input:
            is_first_row = True
            reader = csv.DictReader(input, delimiter=',', fieldnames=['id', 'subPropertyOf', 'parent'])
            for row in reader:
                if is_first_row:
                    is_first_row = False                
                    continue
                r_id = row['id'] 
                r_parent = row['parent']
                value = r_parent.find('owl.')
                if value == 0:                                        
                    continue
                value = r_id.find('rc.')
                if value == 0:
                    id_frag = r_id.replace('rc.', '')
                    parent_frag = r_parent.replace('kko.', '')
                    var2 = getattr(kko, parent_frag)                 
                    with rc:                        
                        r_id = types.new_class(id_frag, (var2,))
    with open(out_file, 'w', encoding='utf8') as f:
        print('KBpedia property structure build is complete.')   
        f.close() 


def class_annot_build(**build_deck):
    print('Beginning KBpedia class annotation build . . .')
    loop_list = build_deck.get('loop_list')
    loop = build_deck.get('loop')
    class_loop = build_deck.get('class_loop')
    out_file = build_deck.get('out_file')
    if loop is not 'class_loop':
        print("Needs to be a 'class_loop'; returning program.")
        return
    for loopval in loop_list:
        print('   . . . processing', loopval) 
        in_file = loopval
        with open(in_file, 'r', encoding='utf8') as input:
            is_first_row = True
            reader = csv.DictReader(input, delimiter=',', fieldnames=['id', 'prefLabel', 'subClassOf', 
                                   'altLabel', 'definition', 'editorialNote', 'isDefinedBy', 'superClassOf'])                 
            for row in reader:
                r_id = row['id']
                id = getattr(rc, r_id)
                if id == None:
                    print(r_id)
                    continue
                r_pref = row['prefLabel']
                r_alt = row['altLabel']
                r_def = row['definition']
                r_note = row['editorialNote']
                r_isby = row['isDefinedBy']
                r_super = row['superClassOf']
                if is_first_row:                                       
                    is_first_row = False
                    continue      
                id.prefLabel.append(r_pref)
                i_alt = r_alt.split('||')
                if i_alt != ['']: 
                    for item in i_alt:
                        id.altLabel.append(item)
                id.definition.append(r_def)        
                i_note = r_note.split('||')
                if i_note != ['']:   
                    for item in i_note:
                        id.editorialNote.append(item)
                id.isDefinedBy.append(r_isby)
                i_super = r_super.split('||')
                if i_super != ['']:   
                    for item in i_super:
                        item = 'http://kbpedia.org/kko/rc/' + item
#                        Code block to be used if objectProperty; 5.5 hr load
#                        item = getattr(rc, item)
#                        if item == None:
#                            print('Failed assignment:', r_id, item)
#                            continue
#                        else:                                
                        id.superClassOf.append(item)
    kb.save(out_file, format="rdfxml") 
    print('KBpedia class annotation build is complete.')


def prop_annot_build(**build_deck):
    print('Beginning KBpedia property annotation build . . .')
    loop_list = build_deck.get('loop_list')
    loop = build_deck.get('loop')
    out_file = build_deck.get('out_file')
    if loop is not 'property_loop':
        print("Needs to be a 'property_loop'; returning program.")
        return
    for loopval in loop_list:
        print('   . . . processing', loopval) 
        in_file = loopval
        with open(in_file, 'r', encoding='utf8') as input:
            is_first_row = True
            reader = csv.DictReader(input, delimiter=',', fieldnames=['id', 'prefLabel', 'subPropertyOf', 'domain',  
                                   'range', 'functional', 'altLabel', 'definition', 'editorialNote'])                 
            for row in reader:
                r_id = row['id']                
                r_pref = row['prefLabel']
                r_dom = row['domain']
                r_rng = row['range']
                r_alt = row['altLabel']
                r_def = row['definition']
                r_note = row['editorialNote']
                r_id = r_id.replace('rc.', '')
                id = getattr(rc, r_id)
                if id == None:
                    print(r_id)
                    continue
                if is_first_row:                                       
                    is_first_row = False
                    continue
                id.prefLabel.append(r_pref)
                i_dom = r_dom.split('||')
                if i_dom != ['']: 
                    for item in i_dom:
                        id.domain.append(item)
                if 'owl.' in r_rng:
                    r_rng = r_rng.replace('owl.', '')
                    r_rng = getattr(owl, r_rng)
                    id.range.append(r_rng)
                elif r_rng == ['']:
                    continue
                else: 
                    continue 
#                    id.range.append(r_rng)
                i_alt = r_alt.split('||')    
                if i_alt != ['']: 
                    for item in i_alt:
                        id.altLabel.append(item)
                id.definition.append(r_def)        
                i_note = r_note.split('||')
                if i_note != ['']:   
                    for item in i_note:
                        id.editorialNote.append(item)
    kb.save(out_file, format="rdfxml") 
    print('KBpedia property annotation build is complete.')         
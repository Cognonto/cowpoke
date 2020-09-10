# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:35:44 2020

@author: Michael K. Bergman
"""

                                                      
from cowpoke.__main__ import *
from cowpoke.config import *
                              
""" we get the run specification dictionary from config.py """

def annot_extractor(**extract_deck):
    print('Beginning annotation extraction . . .') 
    r_default = ''
    r_label = ''
    r_iri = ''
    render = extract_deck.get('render')
    if render == 'r_default':
        set_render_func(default_render_func)
    elif render == 'r_label':
        set_render_func(render_using_label)
    elif render == 'r_iri':
        set_render_func(render_using_iri)
    else:
        print('You have assigned an incorrect render method--execution stopping.')
        return    
    loop_list = extract_deck.get('loop_list')
    loop = extract_deck.get('loop')
    out_file = extract_deck.get('out_file')
    class_loop = extract_deck.get('class_loop')
    property_loop = extract_deck.get('property_loop')
    descent_type = extract_deck.get('descent_type')
    """ These are internal counters used in this module's methods """
    p_set = []
    a_ser = []
    x = 1
    cur_list = []
    with open(out_file, mode='w', encoding='utf8', newline='') as output:
        csv_out = csv.writer(output)                                       
        if loop == 'class_loop':                                             
            header = ['id', 'prefLabel', 'subClassOf', 'altLabel', 
                      'definition', 'editorialNote', 'isDefinedBy', 'superClassOf']
        else:
            header = ['id', 'prefLabel', 'subPropertyOf', 'domain', 'range', 
                      'functional', 'altLabel', 'definition', 'editorialNote']
        csv_out.writerow(header)    
        for value in loop_list:                                            
            print('   . . . processing', value)                                           
            root = eval(value) 
            if descent_type == 'descent':
                p_set = root.descendants()
            elif descent_type == 'single':
                a_set = root
                p_set.append(a_set)
            else:
                print('You have assigned an incorrect descent method--execution stopping.')
                return    
            for p_item in p_set:
                if p_item not in cur_list:                                 
                    a_pref = p_item.prefLabel
                    a_pref = str(a_pref)[1:-1].strip('"\'')                
                    a_sub = p_item.is_a
                    for a_id, a in enumerate(a_sub):                        
                        a_item = str(a)
                        if a_id > 0:
                            a_item = a_sub + '||' + str(a)
                        a_sub  = a_item
                    if loop == 'property_loop':   
                        a_item = ''
                        a_dom = p_item.domain
                        for a_id, a in enumerate(a_dom):
                            a_item = str(a)
                            if a_id > 0:
                                a_item = a_dom + '||' + str(a)
                            a_dom  = a_item    
                        a_dom = a_item
                        a_rng = p_item.range
                        a_rng = str(a_rng)[1:-1]
                        a_func = ''
                    a_item = ''
                    a_alt = p_item.altLabel
                    for a_id, a in enumerate(a_alt):
                        a_item = str(a)
                        if a_id > 0:
                            a_item = a_alt + '||' + str(a)
                        a_alt  = a_item    
                    a_alt = a_item
                    a_def = p_item.definition
                    a_def = str(a_def)[2:-2]
                    a_note = p_item.editorialNote
                    a_note = str(a_note)[1:-1]
                    if loop == 'class_loop':                                  
                        a_isby = p_item.isDefinedBy
                        a_isby = str(a_isby)[2:-2]
                        a_isby = a_isby + '/'
                        a_item = ''
                        a_super = p_item.superClassOf
                        for a_id, a in enumerate(a_super):
                            a_item = str(a)
                            if a_id > 0:
                                a_item = a_super + '||' + str(a)
                            a_super = a_item    
                        a_super  = a_item
                    if loop == 'class_loop':                                  
                        row_out = (p_item,a_pref,a_sub,a_alt,a_def,a_note,a_isby,a_super)
                    else:
                        row_out = (p_item,a_pref,a_sub,a_dom,a_rng,a_func,
                                   a_alt,a_def,a_note)
                    csv_out.writerow(row_out)                               
                    cur_list.append(p_item)
                    x = x + 1
    print('Total unique IDs written to file:', x)  
    print('The annotation extraction for the', loop, 'is completed.') 


def struct_extractor(**extract_deck):    
    print('Beginning structure extraction . . .')
# 1 - render method goes here    
    r_default = ''
    r_label = ''
    r_iri = ''
    render = extract_deck.get('render')
    if render == 'r_default':
        set_render_func(default_render_func)
    elif render == 'r_label':
        set_render_func(render_using_label)
    elif render == 'r_iri':
        set_render_func(render_using_iri)
    else:
        print('You have assigned an incorrect render method--execution stopping.')
        return
# 2 - note about custom extractions
    loop_list = extract_deck.get('loop_list')
    loop = extract_deck.get('loop')
    out_file = extract_deck.get('out_file')
    class_loop = extract_deck.get('class_loop')
    property_loop = extract_deck.get('property_loop')
    descent_type = extract_deck.get('descent_type')
    x = 1
    cur_list = []
    a_set = []
    s_set = []
    new_class = 'owl:Thing'
# 5 - what gets passed to 'output'
    with open(out_file, mode='w', encoding='utf8', newline='') as output:
        csv_out = csv.writer(output)
        if loop == 'class_loop':                                             
            header = ['id', 'subClassOf', 'parent']
            p_item = 'rdfs:subClassOf'
        else:
            header = ['id', 'subPropertyOf', 'parent']
            p_item = 'rdfs:subPropertyOf'
        csv_out.writerow(header)       
# 3 - what gets passed to 'loop_list' 
        for value in loop_list:
            print('   . . . processing', value)                                           
            root = eval(value)
# 4 - descendant or single here
            if descent_type == 'descent':
                a_set = root.descendants()
                a_set = set(a_set)
                s_set = a_set.union(s_set)
            elif descent_type == 'single':
                a_set = root
                s_set.append(a_set)
            else:
                print('You have assigned an incorrect descent method--execution stopping.')
                return                         
        print('   . . . processing consolidated set.')
        for s_item in s_set:
            o_set = s_item.is_a
            for o_item in o_set:
                row_out = (s_item,p_item,o_item)
                csv_out.writerow(row_out)
                if loop == 'class_loop':
                    if s_item not in cur_list:                
                        row_out = (s_item,p_item,new_class)
                        csv_out.writerow(row_out)
                cur_list.append(s_item)
                x = x + 1
    print('Total unique IDs written to file:', x) 
    

def typol_extractor(**extract_deck):
    print('Beginning structure extraction . . .')
    r_default = ''
    r_label = ''
    r_iri = ''
    render = run_deck.get('render')
    if render == 'r_default':
        set_render_func(default_render_func)
    elif render == 'r_label':
        set_render_func(render_using_label)
    elif render == 'r_iri':
        set_render_func(render_using_iri)
    else:
        print('You have assigned an incorrect render method--execution stopping.')
        return
    loop_list = extract_deck.get('loop_list')
    loop = extract_deck.get('loop')
    class_loop = extract_deck.get('class_loop')
    base = extract_deck.get('base')
    ext = extract_deck.get('ext')
    new_class = 'owl:Thing'

    if loop is not 'class_loop':
        print("Needs to be a 'class_loop'; returning program.")
        return
    header = ['id', 'subClassOf', 'parent']
    p_item = 'rdfs:subClassOf'
    for value in loop_list:
        print('   . . . processing', value)
        x = 1
        s_set = []
        cur_list = []
        root = eval(value)
        s_set = root.descendants()
        frag = value.replace('kko.','')
        out_file = (base + frag + ext)
        with open(out_file, mode='w', encoding='utf8', newline='') as output:                                           
            csv_out = csv.writer(output)
            csv_out.writerow(header)       
            for s_item in s_set:
                o_set = s_item.is_a
                for o_item in o_set:
                    row_out = (s_item,p_item,o_item)
                    csv_out.writerow(row_out)
                    if s_item not in cur_list:                
                        row_out = (s_item,p_item,new_class)
                        csv_out.writerow(row_out)
                cur_list.append(s_item)
                x = x + 1
        output.close()         
        print('Total unique IDs written to file:', x) 
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:49:55 2020

@author: Michael K. Bergman
"""

                                                      
from cowpoke.__main__ import *
from cowpoke.config import *
                              
""" we get the run specification dictionary from config.py """

from itertools import combinations                                       

def typol_stats(**build_deck):
    kko_list = typol_dict.values()
    count = build_deck.get('count')
    out_file = build_deck.get('out_file')
    with open(out_file, 'w', encoding='utf8') as output:
        print('count,size_1,kko_1,size_2,kko_2,intersect RCs', file=output)
        for i in combinations(kko_list,2):                              
            kko_1 = i[0]                                              
            kko_2 = i[1]                                              
            kko_1_frag = kko_1.replace('kko.', '')
            kko_1 = getattr(kko, kko_1_frag)
            print(kko_1_frag)
            kko_2_frag = kko_2.replace('kko.', '')
            kko_2 = getattr(kko, kko_2_frag)     
            descent_1 = kko_1.descendants(include_self = False)       
            descent_1 = set(descent_1)
            size_1 = len(descent_1)
            descent_2 = kko_2.descendants(include_self = False)
            descent_2 = set(descent_2)
            size_2 = len(descent_2)
            intersect = descent_1.intersection(descent_2)              
            num = len(intersect)
            if num <= count:                                           
                print(num, size_1, kko_1, size_2, kko_2, intersect, sep=',', file=output)
            else: 
                print(num, size_1, kko_1, size_2, kko_2, sep=',', file=output)
    print('KKO typology intersection analysis is done.')
    
import collections

from rdflib import URIRef, Graph, Literal
from rdflib.namespace import VOID, RDF

graph = world.as_rdflib_graph()
g = graph

def generate2VoID(g, dataset=None, res=None, distinctForPartitions=True):
    """
    Returns a VoID description of the passed dataset

    For more info on Vocabulary of Interlinked Datasets (VoID), see:
    http://vocab.deri.ie/void

    This only makes two passes through the triples (once to detect the types
    of things)

    The tradeoff is that lots of temporary structures are built up in memory
    meaning lots of memory may be consumed :)
    
    distinctSubjects/objects are tracked for each class/propertyPartition
    this requires more memory again

    """

    typeMap = collections.defaultdict(set)
    classes = collections.defaultdict(set)
    for e, c in g.subject_objects(RDF.type):
        classes[c].add(e)
        typeMap[e].add(c)

    triples = 0
    subjects = set()
    objects = set()
    properties = set()
    classCount = collections.defaultdict(int)
    propCount = collections.defaultdict(int)

    classProps = collections.defaultdict(set)
    classObjects = collections.defaultdict(set)
    propSubjects = collections.defaultdict(set)
    propObjects = collections.defaultdict(set)
    num_classObjects = 0
    num_propSubjects = 0
    num_propObjects = 0
    
    for s, p, o in g:

        triples += 1
        subjects.add(s)
        properties.add(p)
        objects.add(o)

        # class partitions
        if s in typeMap:
            for c in typeMap[s]:
                classCount[c] += 1
                if distinctForPartitions:
                    classObjects[c].add(o)
                    classProps[c].add(p)

        # property partitions
        propCount[p] += 1
        if distinctForPartitions:
            propObjects[p].add(o)
            propSubjects[p].add(s)

    if not dataset:
        dataset = URIRef('http://kbpedia.org/kko/rc/')

    if not res:
        res = Graph()

    res.add((dataset, RDF.type, VOID.Dataset))

    # basic stats
    res.add((dataset, VOID.triples, Literal(triples)))
    res.add((dataset, VOID.classes, Literal(len(classes))))

    res.add((dataset, VOID.distinctObjects, Literal(len(objects))))
    res.add((dataset, VOID.distinctSubjects, Literal(len(subjects))))
    res.add((dataset, VOID.properties, Literal(len(properties))))

    for i, c in enumerate(classes):
        part = URIRef(dataset + "_class%d" % i)
        res.add((dataset, VOID.classPartition, part))
        res.add((part, RDF.type, VOID.Dataset))

        res.add((part, VOID.triples, Literal(classCount[c])))
        res.add((part, VOID.classes, Literal(1)))

        res.add((part, VOID["class"], c))

        res.add((part, VOID.entities, Literal(len(classes[c]))))
        res.add((part, VOID.distinctSubjects, Literal(len(classes[c]))))

        if distinctForPartitions:
            res.add(
                (part, VOID.properties, Literal(len(classProps[c]))))
            res.add((part, VOID.distinctObjects,
                     Literal(len(classObjects[c]))))
            num_classObjects = num_classObjects + len(classObjects[c])           
            

    for i, p in enumerate(properties):
        part = URIRef(dataset + "_property%d" % i)
        res.add((dataset, VOID.propertyPartition, part))
        res.add((part, RDF.type, VOID.Dataset))

        res.add((part, VOID.triples, Literal(propCount[p])))
        res.add((part, VOID.properties, Literal(1)))

        res.add((part, VOID.property, p))

        if distinctForPartitions:

            entities = 0
            propClasses = set()
            for s in propSubjects[p]:
                if s in typeMap:
                    entities += 1
                for c in typeMap[s]:
                    propClasses.add(c)

            res.add((part, VOID.entities, Literal(entities)))
            res.add((part, VOID.classes, Literal(len(propClasses))))

            res.add((part, VOID.distinctSubjects,
                     Literal(len(propSubjects[p]))))
            res.add((part, VOID.distinctObjects,
                     Literal(len(propObjects[p]))))
            num_propSubjects = num_propSubjects + len(propSubjects[p])
            num_propObjects = num_propObjects + len(propObjects[p]) 
    print('triples:', triples)
    print('subjects:', len(subjects))
    print('objects:', len(objects))
    print('classObjects:', num_classObjects)
    print('propObjects:', num_propObjects)      
    print('propSubjects:', num_propSubjects)
     

    return res, dataset    
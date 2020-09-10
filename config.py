# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:26:08 2020

@author: Michael K. Bergman
"""

from cowpoke.__main__ import *

""" This is the placeholder for a custom dictionary that may be assiged to 
    a 'loop_list'. Cut-and-paste 1 to n key:value pairs below that represent
    your desired set of 'roots'. Make sure you also set 'loop' to either class or 
    property based.
"""


master_deck = {              
              'kb_src'        : 'standard',
              }    



file_dict = {              
              'wikipedia-categories' : 'wikipedia-categories',
              }    


custom_dict = {
              'Associatives'          : 'kko.Associatives',
              'AtomsElements'         : 'kko.AtomsElements',
              'AttributeTypes'        : 'kko.AttributeTypes',
              }


typol_alpha_dict = {
             """This is the dictionary for KBpedia typologies.
             """
             'ActionTypes'           : 'kko.ActionTypes',
             'AdjunctualAttributes'  : 'kko.AdjunctualAttributes',
             'Agents'                : 'kko.Agents',
             'Animals'               : 'kko.Animals',
             'AreaRegion'            : 'kko.AreaRegion',
             'Artifacts'             : 'kko.Artifacts',
             'Associatives'          : 'kko.Associatives',
             'AtomsElements'         : 'kko.AtomsElements',
             'AttributeTypes'        : 'kko.AttributeTypes',
             'AudioInfo'             : 'kko.AudioInfo',
             'AVInfo'                : 'kko.AVInfo',
             'BiologicalProcesses'   : 'kko.BiologicalProcesses',
             'Chemistry'             : 'kko.Chemistry',
             'Concepts'              : 'kko.Concepts',
             'ConceptualSystems'     : 'kko.ConceptualSystems',
             'Constituents'          : 'kko.Constituents',
             'ContextualAttributes'  : 'kko.ContextualAttributes',
             'CopulativeRelations'   : 'kko.CopulativeRelations',
             'Denotatives'           : 'kko.Denotatives',
             'DirectRelations'       : 'kko.DirectRelations',
             'Diseases'              : 'kko.Diseases',
             'Drugs'                 : 'kko.Drugs',
             'EconomicSystems'       : 'kko.EconomicSystems',
             'EmergentKnowledge'     : 'kko.EmergentKnowledge',
             'Eukaryotes'            : 'kko.Eukaryotes',
             'EventTypes'            : 'kko.EventTypes',
             'Facilities'            : 'kko.Facilities',
             'FoodDrink'             : 'kko.FoodDrink',
             'Forms'                 : 'kko.Forms',
#             'Generals'              : 'kko.Generals',
             'Geopolitical'          : 'kko.Geopolitical',
             'Indexes'               : 'kko.Indexes',
             'Information'           : 'kko.Information',
             'InquiryMethods'        : 'kko.InquiryMethods',
             'IntrinsicAttributes'   : 'kko.IntrinsicAttributes',
             'KnowledgeDomains'      : 'kko.KnowledgeDomains',
             'LearningProcesses'     : 'kko.LearningProcesses',
             'LivingThings'          : 'kko.LivingThings',
             'LocationPlace'         : 'kko.LocationPlace',
             'Manifestations'        : 'kko.Manifestations',
             'MediativeRelations'    : 'kko.MediativeRelations',
             'Methodeutic'           : 'kko.Methodeutic',
             'NaturalMatter'         : 'kko.NaturalMatter',
             'NaturalPhenomena'      : 'kko.NaturalPhenomena',
             'NaturalSubstances'     : 'kko.NaturalSubstances',
             'OrganicChemistry'      : 'kko.OrganicChemistry',
             'OrganicMatter'         : 'kko.OrganicMatter',
             'Organizations'         : 'kko.Organizations',
             'Persons'               : 'kko.Persons',
             'Places'                : 'kko.Places',
             'Plants'                : 'kko.Plants',
             'Predications'          : 'kko.Predications',
             'PrimarySectorProduct'  : 'kko.PrimarySectorProduct',
             'Products'              : 'kko.Products',
             'Prokaryotes'           : 'kko.Prokaryotes',
             'ProtistsFungus'        : 'kko.ProtistsFungus',
             'RelationTypes'         : 'kko.RelationTypes',
             'RepresentationTypes'   : 'kko.RepresentationTypes',
             'SecondarySectorProduct': 'kko.SecondarySectorProduct',
             'Shapes'                : 'kko.Shapes',
             'SituationTypes'        : 'kko.SituationTypes',
             'SocialSystems'         : 'kko.SocialSystems',
             'Society'               : 'kko.Society',
             'SpaceTypes'            : 'kko.SpaceTypes',
             'StructuredInfo'        : 'kko.StructuredInfo',
             'Symbolic'              : 'kko.Symbolic',
             'Systems'               : 'kko.Systems',
             'TertiarySectorService' : 'kko.TertiarySectorService',
             'Times'                 : 'kko.Times',
             'TimeTypes'             : 'kko.TimeTypes',
             'TopicsCategories'      : 'kko.TopicsCategories',
             'VisualInfo'            : 'kko.VisualInfo',  
             'WrittenInfo'           : 'kko.WrittenInfo'
             }


typol_dict = {
             """This is the dictionary for KBpedia typologies.
             """
#             'Generals'              : 'kko.Generals',
             'Manifestations'        : 'kko.Manifestations',
             'Symbolic'              : 'kko.Symbolic',
             'Systems'               : 'kko.Systems',
             'ConceptualSystems'     : 'kko.ConceptualSystems',
             'Concepts'              : 'kko.Concepts',
             'Constituents'          : 'kko.Constituents',
             'SpaceTypes'            : 'kko.SpaceTypes',
             'Predications'          : 'kko.Predications',
             'Artifacts'             : 'kko.Artifacts',
             'Products'              : 'kko.Products',
             'RelationTypes'         : 'kko.RelationTypes',
             'SecondarySectorProduct': 'kko.SecondarySectorProduct',
             'OrganicMatter'         : 'kko.OrganicMatter',
             'CopulativeRelations'   : 'kko.CopulativeRelations',
             'Shapes'                : 'kko.Shapes',
             'Methodeutic'           : 'kko.Methodeutic',
             'KnowledgeDomains'      : 'kko.KnowledgeDomains',
             'AttributeTypes'        : 'kko.AttributeTypes', 
             'ActionTypes'           : 'kko.ActionTypes',
             'Forms'                 : 'kko.Forms',
             'LivingThings'          : 'kko.LivingThings',
             'TimeTypes'             : 'kko.TimeTypes',
             'EventTypes'            : 'kko.EventTypes',
             'MediativeRelations'    : 'kko.MediativeRelations',
             'AdjunctualAttributes'  : 'kko.AdjunctualAttributes',             
             'Agents'                : 'kko.Agents',
             'Eukaryotes'            : 'kko.Eukaryotes',
             'Places'                : 'kko.Places',
             'SituationTypes'        : 'kko.SituationTypes',
             'Information'           : 'kko.Information',
             'Animals'               : 'kko.Animals',
             'SocialSystems'         : 'kko.SocialSystems',
             'Organizations'         : 'kko.Organizations',
             'Society'               : 'kko.Society',
             'IntrinsicAttributes'   : 'kko.IntrinsicAttributes',
             'LocationPlace'         : 'kko.LocationPlace',
             'ContextualAttributes'  : 'kko.ContextualAttributes',
             'PrimarySectorProduct'  : 'kko.PrimarySectorProduct',
             'TertiarySectorService' : 'kko.TertiarySectorService',
             'Persons'               : 'kko.Persons',
             'NaturalMatter'         : 'kko.NaturalMatter',
             'DirectRelations'       : 'kko.DirectRelations',
             'Facilities'            : 'kko.Facilities',
             'StructuredInfo'        : 'kko.StructuredInfo',
             'LearningProcesses'     : 'kko.LearningProcesses',
             'FoodDrink'             : 'kko.FoodDrink',
             'WrittenInfo'           : 'kko.WrittenInfo',
             'Plants'                : 'kko.Plants',             
             'AreaRegion'            : 'kko.AreaRegion',
             'AVInfo'                : 'kko.AVInfo',
             'Drugs'                 : 'kko.Drugs',
             'RepresentationTypes'   : 'kko.RepresentationTypes',
             'Geopolitical'          : 'kko.Geopolitical',
             'NaturalSubstances'     : 'kko.NaturalSubstances',
             'TopicsCategories'      : 'kko.TopicsCategories',
             'EconomicSystems'       : 'kko.EconomicSystems',
             'Chemistry'             : 'kko.Chemistry',
             'VisualInfo'            : 'kko.VisualInfo',
             'Associatives'          : 'kko.Associatives',
             'NaturalPhenomena'      : 'kko.NaturalPhenomena',
             'Denotatives'           : 'kko.Denotatives',
             'OrganicChemistry'      : 'kko.OrganicChemistry',
             'Diseases'              : 'kko.Diseases',
             'Indexes'               : 'kko.Indexes',
             'InquiryMethods'        : 'kko.InquiryMethods',
             'AtomsElements'         : 'kko.AtomsElements',
             'Times'                 : 'kko.Times',
             'AudioInfo'             : 'kko.AudioInfo',
             'BiologicalProcesses'   : 'kko.BiologicalProcesses',
             'Prokaryotes'           : 'kko.Prokaryotes',
             'EmergentKnowledge'     : 'kko.EmergentKnowledge',
             'ProtistsFungus'        : 'kko.ProtistsFungus',          
             }


prop_dict = {
            """This is the dictionary for added KBpedia properties in the 
            categories shown.
            """
            'objectProperties' : 'kko.predicateProperties',
            'dataProperties'   : 'kko.predicateDataProperties',
            'representations'  : 'kko.representations',
            }


mapping_dict = {
            """This is the dictionary for relating external mapping keys to their
            respective files on disk (directory name handled separately).
            """
            'dbpedia'              : 'dbpedia',
            'dbpedia-ontology'     : 'dbpedia-ontology',
            'geonames'             : 'geonames',
            'schema.org'           : 'schema.org',
            'wikidata'             : 'wikidata',
            'wikipedia'            : 'wikipedia',
            'wikipedia-categories' : 'wikipedia-categories',
            }


mapping_long_dict = {
            """This is the dictionary for relating external mapping keys to their
            respective files on disk (directory name handled separately) --
            long version.
            """
            'dbpedia'              : 'dbpedia',
            'dbpedia-ontology'     : 'dbpedia-ontology',
            'geonames'             : 'geonames',
            'schema.org'           : 'schema.org',
            'wikidata'             : 'wikidata',
            'wikipedia'            : 'wikipedia',
            'wikipedia-categories' : 'wikipedia-categories',
            'bibo'                 : '/secondary/bibo',
            'cc'                   : '/secondary/cc',
            'dc'                   : '/secondary/dc',
            'doap'                 : '/secondary/doap',
            'event'                : '/secondary/event',
            'foaf'                 : '/secondary/foaf',
            'frbr'                 : '/secondary/frbr',
            'geo'                  : '/secondary/geo',
            'mo'                   : '/secondary/mo',
            'oo'                   : '/secondary/oo',
            'org'                  : '/secondary/org',
            'po'                   : '/secondary/po',
            'rss'                  : '/secondary/rss',
            'sioc'                 : '/secondary/sioc',
            'time'                 : '/secondary/time',
            'transit'              : '/secondary/transit',
            }



extract_deck = {
           """This is the dictionary for the specifications of each
           extraction run. Here are specific instructions:
           1. The 'render' assignment must be either 'r_default', 'r_label' 
              or 'r_iri'
           2. The 'loop' assignment must be either 'class_loop' or 
              'property_loop'
           3. The 'descent_type' assignment must be either 'descent' or 'single'
           4. The 'loop_list' assignment must be a dictionary.values() one
           """
           'r_default'     : '',
           'r_label'       : '',
           'r_iri'         : '',            
           'property_loop' : '',
           'class_loop'    : '',
           'descent'       : '',
           'single'        : '',
           'descent_type'  : 'descent',
           'loop'          : 'property_loop',
           'loop_list'     : prop_dict.values(),
           'out_file'      : 'C:/1-PythonProjects/kbpedia/v300/extractions/properties/prop_struct_out.csv',
           'render'        : 'r_default',
           'base'          : 'C:/1-PythonProjects/kbpedia/v300/build_ins/properties/',
           'ext'           : '.csv',
           }
    

build_deck = {              
              'loop_list'     : typol_dict.values(),
              'loop'          : 'property_loop',
              'base'          : 'C:/1-PythonProjects/kbpedia/v300/build_ins/mappings/',
              'ext'           : '.csv',              
              'out_file'      : 'C:/1-PythonProjects/kbpedia/v300/targets/stats/kko_typol_stats.csv',
              'short_base'    : 'C:/1-PythonProjects/kbpedia/v300/build_ins/typologies/dups_removed/',
              'base_out'      : 'C:/1-PythonProjects/kbpedia/v300/build_ins/typologies/dups_removed/typol_',
              'count'         : 14,
              }  
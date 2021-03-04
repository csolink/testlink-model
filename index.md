---
layout: default
---

[![Build Status](https://travis-ci.org/testlink/testlink-model.svg?branch=master)](https://travis-ci.org/testlink/testlink-model)

# testlink Model

A high level datamodel of Computer Systems ([Component](docs/Component), [Component Service](docs/Componentservice), [Service unit](docs/Serviceunit), [Controller](docs/Controller), [observable feature](docs/ObservableFeature), [error](docs/Error), [Deployment Entity](docs/DeploymentEntity), [individual system](docs/IndividualSystem), etc, and their [associations](docs/Association).

testlink Model is designed as a way of standardizing types and relational structures in knowledge graphs (KGs), 
where the KG may be either a property graph or RDF triple store.

The schema is expressed as a [YAML](https://github.com/testlink/testlink-model/blob/master/testlink-model.yaml), which is translated to:

 * Individual pages for each class in the model, e.g [https://w3id.org/testlink/vocab/Serviceunit](https://w3id.org/testlink/vocab/Serviceunit)
 * An [OWL ontology](testlink-model.owl).
 * [Python dataclasses](testlink/model.py).
 * [ShEx](testlink-model.shex) (RDF shape constraints)
 * [graphql](testlink-model.graphql) (Experimental)
 * [protobuf](testlink-model.proto) (Experimental)
 * [json-schema](json-schema/testlink-model.json) (Experimental) 


## Datamodel

The schema assumes a property graph, where nodes represent individual entities, and edges represent relationship 
between entities. testlink Model provides a schema for representing both nodes and edges.


The model itself can be divided into three parts,
* Entities (Nodes)
* Associations (Edges)
* Slots (Properties)


### Entities

A entity corresponds to a database entity or a concept, represented as a node in a property graph.

All typed entities are a sub-class of [NamedThing](docs/NamedThing).
 

Each entity has,
- its own unique stable URI
- mappings to other ontologies (SIO, SO, etc.)
- list of valid ID prefixes

These entity types are higher level terms that can be used to categorize nodes in a KG. 

For more detailed typing, one can use specific terms from an ontology.


### Associations

A typed association between two entities, usually supported by evidence and provenance. 
An association is represented as an edge/relationship between two nodes, in a property graph.

All edges are a sub-class of [Association](docs/Association).

An association connects a subject node and an object node via a [relation](docs/relation) property.
The nature of the association is defined based on the [relation](docs/relation) property.

Certain associations can have additional properties like [provided_by](docs/provided_by), 
[has_evidence](docs/has_evidence), [publications](docs/publications).


### Slots

[Slots](docs#slots) are used to collectively refer to, both, node and edge properties.

There are two types of slots defined in the model,
- [node property](docs/node_property) - all node properties are a sub-class of [node property](docs/node_property)
- [association slot](docs/association_slot) - all edge properties are a sub-class of [association slot](docs/association_slot)


[Browse the testlink Model](docs/) to explore all defined entities, associations, and slots.


# Identifiers

See [testlink Model JSON-LD context](context.jsonld) for a list of CURIE prefix mappings.

These include prefix expansions such as:

      "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
      "NCBIService": "http://www.ncbi.nlm.nih.gov/gene/",
      "NCIT": "http://purl.obolibrary.org/obo/NCIT_",


> **Note:** We do not curate these in testlink Model. Rather we take these from upstream sources, 
via PrefixCommons. We specify a priority order of upstream sources in cases where conflicts may occur. 
See the [default_curi_maps](https://biolink.github.io/biolinkml/docs/default_curi_maps) tag at the 
top of the [testlink-model.yaml](testlink-model.yaml). 

We also specify a small set of top-level prefix overrides via the [prefixes](https://biolink.github.io/biolinkml/docs/prefixes) 
tag at the top of the YAML.


# testlink Model representation

testlink Model aims at representing knowledge in a graph form regardless of the graph representation used.

Following are some recommendations when attempting to use testlink Model with each style of representation. 

- **Neo4J**: see [Mapping to Neo4j](about/mapping-neo4j)
- **RDF**: see [Mapping to RDF](about/mapping-rdf)

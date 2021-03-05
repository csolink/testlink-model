[![Python 3.7](https://upload.wikimedia.org/wikipedia/commons/f/fc/Blue_Python_3.7_Shield_Badge.svg)](https://www.python.org/downloads/release/python-370/)
[![Build Status](https://travis-ci.com/testlink/testlink-model.svg?branch=main)](https://travis-ci.com/testlink/testlink-model)
![Regenerate testlink Model Artifacts](https://github.com/csolink/testlink-model/workflows/Regenerate%20testlink%20Model%20Artifacts/badge.svg)
![Deploy Documentation](https://github.com/csolink/testlink-model/workflows/Deploy%20Documentation/badge.svg)

<img src="images/testlink-logo.png" width="20%">

# testlink Model (Experimental)

Quickstart docs:

- Browse the model: [https://csolink.github.io/testlink-model](https://csolink.github.io/testlink-model)
  - [named thing](https://csolink.github.io/testlink-model/docs/NamedThing.html)
  - [association](https://csolink.github.io/testlink-model/docs/Association.html)
  - [predicate](https://csolink.github.io/testlink-model/docs/predicates.html)

See also [testlink Model Guidelines](./guidelines/index.md) for understanding, curating, and working with the model.


## Introduction

The purpose of the testlink Model is to provide a high-level datamodel of Cyber system entities
(component, component services, observability, Service unit, errors, networks, instances, control actor, etc),
their properties, relationships, and enumerate ways in which they can be associated.

The representation is independent of storage technology or metamodel (Solr documents, neo4j/property graphs,
RDF/OWL, JSON, CSVs, etc). Different mappings to each of these are provided.

The specification of the testlink Model is a [single YAML file](testlink-model.yaml) built using [biolinkml](https://github.com/biolink/biolinkml).
The basic elements of the YAML are:

 - Class Definitions: definitions of upper level *classes* representing both 'named thing' and 'association'
 - Slot Definitions: definitions of *slots* (aka properties) that can be used to relate members of these classes to other classes or data types. Slots collectively refer to predicates, node properties, and edge properties

The model itself is being used in the following projects:


## Organization

The main source of truth is [testlink-model.yaml](testlink-model.yaml). This is a YAML file that is intended to
be relatively simple to view and edit in its native form.

The yaml definition is currently used to derive:

  - [JSON Schema](json-schema)
  - [Python dataclasses](testlink/model.py)
  - [Java code gen](java)
  - [ProtoBuf definitions](testlink-model.proto)
  - [GraphQL](testlink-model.graphql)
  - [RDF](testlink-model.ttl)
  - [OWL](testlink-model.owl.ttl)
  - [RDF Shape Expressions](testlink-model.shex)
  - [JSON-LD context](context.jsonld)
  - [Graphviz](graphviz)
  - [GOlr YAML schemas](golr-views)
    - these can be compiled down to Solr XML schemas
    - these are also intermediate targets used within the BBOP/AmiGO framework
  - [Markdown documentation](docs)


## Make and build instructions

Prerequisites: Python 3.7+, make, graphiz, python3-pip, and pipenv

To install pipenv,

```sh
sudo pip3 install pipenv
```

To set your python version:

```sh
vi Pipfile    # i.e. requires=3.8
pipenv --python /usr/bin/python3
```

To install the project,
```sh
make install
```

If you make changes to [testlink-model.yaml](testlink-model.yaml) then be sure to run the Makefile to generate
up-to-date artifacts and documentation.

```sh
make
```


**Note:** the Makefile requires the following dependencies to be installed:

### jsonschema

[jsonschema](https://json-schema.org/)

Generally install using 

```sh
pip3 install jsonschema
```

### jsonschema2pojo

[jsonschema2pojo](https://github.com/joelittlejohn/jsonschema2pojo)

If you are on a Mac, it can be installed using `brew`:
```sh
brew install jsonschema2pojo
```
For other OS environments, download the latest release then extract it into your execution path.

### GraphViz

See [GraphViz site](https://graphviz.org/) for installation in your operating system.



## How do I use testlink Model YAML programatically?

For operations such as CURIE lookup, finding class by synonyms, get parents, get ancestors, etc. please make use of [biolink-model-toolkit](https://github.com/biolink/biolink-model-toolkit/). It provides a convenience methods for traversing biolink Model.


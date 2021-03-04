---
title: "Curating the testlink Model"
parent: "testlink Model Guidelines"
layout: default
nav_order: 2
---

# Curating the testlink Model

Before curating the testlink Model, we recommend that you familiarize yourself with the basics of [LinkML](https://github.com/biolink/biolinkml).

In testlink Model all the curation should happen in one place: [testlink-model.yaml](../testlink-model.yaml)
This is the one source of truth for the model.

This section explores how to go about adding new classes and slots to the model.

### Adding an Entity class

An entity class represents entities like Componentservices, Errors, Control Actors, etc.

Instances of these Entity classes are represented as nodes in a graph.

testlink Model has several entity classes like `componentservice`, `error`, `observable feature`, `control actor`.

All these classes are arranged in a hierarchy with the root of all entities being the `named thing` class.


To add an entity class to testlink Model you need to determine the following,
  - What is an appropriate name for this entity?
    - The name for an entity should be clear and concise. It should describe instances of this class
  - Where in the [`named thing` hierarchy](https://csolink.github.io/testlink-model/docs/NamedThing) does the new class fit?
    - Determine what the immediate parent for this class is going to be
  - What are the slots that this class can have (in addition to its inherited slots)?
    - Determine what additional properties that this class ought to have
  - Do certain slots have to be constrained to certain values?
    - Determine whether there are properties (new or inherited) whose value have to be constrained to a certain value space
  - What are the valid namespace prefixes for identifiers of instances of this class?
    - For representing an instance of this entity class determine the identifier namespace and valid prefix(es)
  - What are the mapping(s) for this class?
    - Mappings are a way of rooting this new entity classs in the context of other ontologies, thesauri, controlled vocabularies and taxonomies
    - Determine the level of granularity for your mappings where they can be divided into 5 types: `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`


As an example, let's consider the definition of the entity class `componentservice`:

```yaml
  componentservice:
    is_a: componentservice or servicetype
    aliases: ['locus', 'cs']
    slots:
      - id
      - name
      - symbol
      - description
      - synonym
      - xref
    broad_mappings:
      - csrc:Resource_Type
      - OSO:hasComponentType
      - schema:serviceType
    exact_mappings: []
    id_prefixes: []  # todo
```

In the above YAML snippet, `is_a`, `aliases`, `slots`, `exact_mappings`, and `id_prefixes` are slots from LinkML where each slot has a specific meaning and they add semantics to the class definition.

In addition to the aforementioned slots, LinkML provides ways to leverage mixin classes to reuse certain slots across different classes.

Say you want to use the mixin class `thing with taxon` that defines an `in taxon` slot.

You can achieve that as follows:

```yaml
  componentservice:
    is_a: componentservice or servicetype
    mixins:
      - thing with taxon
    aliases: ['locus', 'cs']
    ...
```

In the above YAML snippet, we are explicitly defining the entity class `componentservice` to have `in taxon` as a slot in addition to all its slots, its parent slots, and all of its ancestor slots.

There are [other LinkML slots](https://biolink.github.io/biolinkml/docs/ClassDefinition#Attributes) that can be used to define your class and further capture the semantics of your class.

For more information on what each slot means and how to use them in testlink Model, refer to [Using the Modeling Language](using-the-modeling-language.md).


### Adding an Association class

An association represents an assertion (statement) which connects a subject to an object via a predicate.

Instances of the Association class are represented as edges in a graph.

testlink Model has several Association classes like `componentservice to componentservice association`, `componentservice to error association`, `error to observable feature association`.

All these classes are arranged in a hierarchy with the root of all associations being the `association` class.



To add an Association class to testlink Model you need to determine the following,
  - What is an appropriate name for this association
    - The name for an association should be clear and concise. It should capture the type of assertion that it is trying to represent
  - What type of nodes does this association link?
    - Determine what the subject and the object classes are in this assertion
  - Where in the hierarchy does the new class fit?
    - Determine where in the [`association slot` hierarchy]() does this new assocation class fit
  - What are the slots that this association class can have (in addition to inherited slots)?
    - Determine what additional properties that this class ought to have
  - Do certain slots have to be constrained on what values it ought to have?
    - Determine whethere there are properties (new or inherited)  whose value have to be constrained to a certain value space
  - What are the mapping(s) for this class?
    - Mappings are a way of rooting this new association in the context of other ontologies, thesauri, controlled vocabularies and taxonomies
    - Determine the level of granularity for your mappings where they can be divided into 5 types: `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`



As an example, let's consider the definition of class  `variant to error association`:

```yaml
  variant to error association:
    is_a: association
    defining_slots:
      - subject
      - object
    mixins:
      - variant to thing association
      - entity to error association
    slot_usage:
      subject:
        description: >-
          a sequence variant in which the variantcomponentserice state is associated in some way with the error state
        examples: []   # todo
      relation:
        description: >-
          E.g. is pathogenic for
        subproperty_of: related condition
      object:
        description: >-
          a error that is associated with that variant
        examples: []   # todo
```

In the above YAML snippet, `is_a`, `defining_slots`, `mixins`, and `slot_usage` are slots from LinkML where each slot has a specific meaning and they add semantics to the class definition.

There are [other LinkML slots](https://biolink.github.io/biolinkml/docs/ClassDefinition#Attributes) that can be used to define your class and represent the semantics of your class.

For more information on what each slot means and how to use them in testlink Model, refer to [Using the Modeling Language](using-the-modeling-language.md).


### Adding a predicate/relation

A predicate is a slot that links two instances of a class. 

To add a predicate to testlink Model you need to determine the following,
  - What is an appropriate name for this predicate?
    - A human readable name for this predicate. It should capture the nature of the relationship
  - Where in the hierarchy does the new slot fit?
    - Determine where in the [`related to` hierarchy](https://csolink.github.io/testlink-model/docs/related_to) does this new predicate slot fit
  - What are the domain and range constraints (if any)?
    - Determine which type of entity classes can this predicate link
  - What are the mapping(s) for this slot?
    - Mappings are a way of rooting this new association in the context of other ontologies, thesauri, controlled vocabularies and taxonomies
    - Determine the level of granularity for your mappings where they can be divided into 5 types: `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`


As an example, let's consider the definition of slot `interacts with`:

```yaml
  interacts with:
    domain: named thing
    range: named thing
    description: >-
      holds between any two entities that directly or indirectly interact with each other
    is_a: related to
    in_subset:
      - translator_minimal
    symmetric: true
    close_mappings:
      - schema:InteractAction    # act of
    exact_mappings:
      - RO:0002434    # interacts with
    narrow_mappings:
      - AML:contains
      - CTRL:isConnectedTo
      - CTRL:isSupervisedBy
      - csrc:system
      - NCIT:has_target
      - SAN:actsOn
      - SAN:isPropertyOf
      - sosa:actsOnProperty
      - gr:offers
      - gr:owns
      - gr:predecessorOf
      - gr:seeks
```

In the above YAML snippet, `domain`, `range`, `description`, `is_a`, `in_subset`, `symmetric`, `exact_mappings` and `narrow_mappings` are slots from LinkML where each slot has a specific meaning and they add semantics to the slot definition.

For more information on what each slot means and how to use them in testlink Model, refer to [Using the Modeling Language](using-the-modeling-language.md).


### Adding properties

You can add slots that represent node properties or edge properties.


To add a node/edge property to testlink Model you need to determine the following,
  - What is an appropriate name for this slot?
    - A human readable name for this property
  - Is it a node property or an edge property (association slot)?
    - Determine whether the property is a node or an edge property
  - Where in the hierarchy does the new property fit?
    - Determine where in the property hierarchy does this new property fit
    - If you want to add a node property then it should be added as part of the [`node property` hierarchy](https://csolink.github.io/testlink-model/docs/node_property)
    - If you want to add an edge property then it should be added as part of the [`association slot` hierarchy](https://csolink.github.io/testlink-model/docs/association_slot)
  - Is this a required property?
    - Determine whether all instances of a class must have a value for this property
  - What are the domain and range constraints (if any)?
    - Determine which type of classes can have this property and what the value space for this property should be
  - What are the mapping(s) for this slot?
    - Mappings are a way of rooting this new property in the context of other ontologies, thesauri, controlled vocabularies and taxonomies
    - Determine the level of granularity for your mappings where they can be divided into 5 types: `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`


As an example, let's consider the slot `name` which is a node property:

```yaml
  name:
    is_a: node property
    aliases: ['label', 'display name']
    domain: named thing
    range: label type
    description: >-
      A human-readable name for a thing
    in_subset:
      - translator_minimal
    required: true
    slot_uri: rdfs:label
    broad_mappings:
      - CSO:named_entity
    exact_mappings:
      - CSO:named_entity
      # DB_Object_Name
      - gr:name
      - OM:name
      - REPR:name
      - schema:name
      - SIO:000116   # name
      - sumo:Name
      - WIKIDATA_PROPERTY:P2561   # name
    close_mappings:
      - IAO:0000111    # editor preferred term
      - IAO:0000118    # alternative term
      - skos:altLabel
      - sumo:originalTitle
    narrow_mappings:
      - AML:hasAttributeName
      - dct:title
```


As another example, let's consider the slot `relation` which is an edge property:

```yaml
  relation:
    is_a: association slot
    description: >-
      The relation which describes an association between a subject and an object in a more granular manner.
      Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    domain: association
    range: uriorcurie
    required: true
```

In the above YAML snippets, `is_a`, `aliases`, `domain`, `range`, `description`, `in_subset`, `required`, `slot_uri`, `exact_mappings` are slots from LinkML where each slot has a specific meaning and they add semantics to the slot definition.

There are [other LinkML slots](https://biolink.github.io/biolinkml/docs/ClassDefinition#Attributes) that can be used to define your class and represent the semantics of your class.

For more information on what each slot means and how to use them in testlink Model, refer to [Using the Modeling Language](using-the-modeling-language.md).


### Managing mappings

In the previous sections there were references to mappings and differentiating these mappings based on their granularity, which can be a bit of a nuanced exercise.

What does it mean for a external concept (or predicate or property) to be one of `related_mappings`, `broad_mappings`, `narrow_mappings` `close_mappings`, `exact_mappings`?

Here is a rule of thumb on how to determine the granularity of mapping:
- An external concept can be considered as an exact mapping to a testlink Model class or slot if the former can be used interchangeably with the latter. That is, the semantics are identical and any transitive property that the external concept might bring into the model should not violate the internal consistency of the model
- If it is difficult to determine if an external concept can be considered an exact mapping then it is much safer to treat it as a close mapping
- If an external concept can be treated a sub-class of the testlink Model class or slot then it can be treated as a narrow mapping
- If an external concept can be treated as a super-class of the testlink Model class or slot then it can be treated as a broad mapping
- If an external concept is distantly related to a testlink Model class or slot then it can be treated as a related mapping


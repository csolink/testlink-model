---
parent: Associations
title: testlink:BuildConfigurationToBuildAssociation
grand_parent: Classes
layout: default
---

# Class: BuildConfigurationToBuildAssociation


Any association between a build configuration and a build. There is no assumption of cardinality

URI: [testlink:BuildConfigurationToBuildAssociation](https://w3id.org/testlink/vocab/BuildConfigurationToBuildAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OntologyClass],[Build]%3Cobject%201..1-%20[BuildConfigurationToBuildAssociation%7Cpredicate:predicate_type;negated(i):boolean%20%3F;relation(i):uriorcurie;type(i):string%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[BuildConfiguration]%3Csubject%201..1-%20[BuildConfigurationToBuildAssociation],[Association]%5E-[BuildConfigurationToBuildAssociation],[BuildConfiguration],[Build],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [build configuration to build association➞object](build_configuration_to_build_association_object.md)  <sub>REQ</sub>
    * Description: build configuration implicated in build
    * range: [Build](Build.md)
 * [build configuration to build association➞predicate](build_configuration_to_build_association_predicate.md)  <sub>REQ</sub>
    * Description: the relationship type used to connect build configuration to build
    * range: [PredicateType](types/PredicateType.md)
 * [build configuration to build association➞subject](build_configuration_to_build_association_subject.md)  <sub>REQ</sub>
    * Description: parent build configuration
    * range: [BuildConfiguration](BuildConfiguration.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of testlink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>1..*</sub>
    * range: [Association](Association.md)

### Inherited from email:

 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for an attribute or entity.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (samples)
 * [enabled](enabled.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)

### Inherited from entity:

 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (samples)

### Inherited from environment:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (samples)
 * [note](note.md)  <sub>OPT</sub>
    * range: [NarrativeText](types/NarrativeText.md)
 * [archived](archived.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)

### Domain for slot:

 * [build configuration to build association➞object](build_configuration_to_build_association_object.md)  <sub>REQ</sub>
    * Description: build configuration implicated in build
    * range: [Build](Build.md)
 * [build configuration to build association➞predicate](build_configuration_to_build_association_predicate.md)  <sub>REQ</sub>
    * Description: the relationship type used to connect build configuration to build
    * range: [PredicateType](types/PredicateType.md)
 * [build configuration to build association➞subject](build_configuration_to_build_association_subject.md)  <sub>REQ</sub>
    * Description: parent build configuration
    * range: [BuildConfiguration](BuildConfiguration.md)
---
parent: Associations
title: testlink:ServerHubToServerAssociation
grand_parent: Classes
layout: default
---

# Class: ServerHubToServerAssociation


Any association between a server hub and a server. There is no assumption of cardinality

URI: [testlink:ServerHubToServerAssociation](https://w3id.org/testlink/vocab/ServerHubToServerAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Server]%3Cobject%201..1-%20[ServerHubToServerAssociation%7Cpredicate:predicate_type;negated(i):boolean%20%3F;relation(i):uriorcurie;type(i):string%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[ServerHub]%3Csubject%201..1-%20[ServerHubToServerAssociation],[Association]%5E-[ServerHubToServerAssociation],[ServerHub],[Server],[Publication],[OntologyClass],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [server hub to server association➞object](server_hub_to_server_association_object.md)  <sub>REQ</sub>
    * Description: server hub implicated in server
    * range: [Server](Server.md)
 * [server hub to server association➞predicate](server_hub_to_server_association_predicate.md)  <sub>REQ</sub>
    * Description: the relationship type used to connect server hub to server
    * range: [PredicateType](types/PredicateType.md)
 * [server hub to server association➞subject](server_hub_to_server_association_subject.md)  <sub>REQ</sub>
    * Description: parent server hub
    * range: [ServerHub](ServerHub.md)

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

 * [server hub to server association➞object](server_hub_to_server_association_object.md)  <sub>REQ</sub>
    * Description: server hub implicated in server
    * range: [Server](Server.md)
 * [server hub to server association➞predicate](server_hub_to_server_association_predicate.md)  <sub>REQ</sub>
    * Description: the relationship type used to connect server hub to server
    * range: [PredicateType](types/PredicateType.md)
 * [server hub to server association➞subject](server_hub_to_server_association_subject.md)  <sub>REQ</sub>
    * Description: parent server hub
    * range: [ServerHub](ServerHub.md)

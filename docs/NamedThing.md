---
parent: Entities
title: testlink:NamedThing
grand_parent: Classes
layout: default
---

# Class: NamedThing


a databased entity or concept/class

URI: [testlink:NamedThing](https://w3id.org/testlink/vocab/NamedThing)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Server],[OntologyClass],[Occurrent],[NamedThing]%3Ccategory%201..%2A-%20[NamedThing%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[ComputationalProcessOrActivity]-%20has%20input%200..%2A%3E[NamedThing],[ComputationalProcessOrActivity]-%20has%20output%200..%2A%3E[NamedThing],[Configuration]-%20has%20part%200..%2A%3E[NamedThing],[Attribute]-%20has%20qualitative%20value%200..1%3E[NamedThing],[Association]-%20object%201..1%3E[NamedThing],[Association]-%20subject%201..1%3E[NamedThing],[NamedThing]%5E-[Server],[NamedThing]%5E-[OntologyClass],[NamedThing]%5E-[InformationContentEntity],[NamedThing]%5E-[Environment],[NamedThing]%5E-[CyberEntity],[NamedThing]%5E-[ComputationalEntity],[NamedThing]%5E-[AdministrativeEntity],[NamedThing]%5E-[Activity],[Entity]%5E-[NamedThing],[InformationContentEntity],[Environment],[Entity],[CyberEntity],[Configuration],[ComputationalProcessOrActivity],[ComputationalEntity],[Attribute],[Association],[AdministrativeEntity],[Activity])

---


## Parents

 *  is_a: [Entity](Entity.md) - Root testlink Model class for all things and informational relationships, real or imagined.

## Children

 * [Activity](Activity.md) - An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
 * [AdministrativeEntity](AdministrativeEntity.md)
 * [ComputationalEntity](ComputationalEntity.md)
 * [CyberEntity](CyberEntity.md) - An entity that has digital reality (a.k.a. cyber essence).
 * [Environment](Environment.md) - An environment
 * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.
 * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
 * [Server](Server.md) - A piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called "clients"

## Referenced by class

 *  **[Occurrent](Occurrent.md)** *[has input](has_input.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has output](has_output.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has part](has_part.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has participant](has_participant.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Attribute](Attribute.md)** *[has qualitative value](has_qualitative_value.md)*  <sub>OPT</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[interacts with](interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[named thing➞category](named_thing_category.md)*  <sub>1..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Association](Association.md)** *[object](object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[overlaps](overlaps.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[part of](part_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[produced by](produced_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[produces](produces.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[related to](related_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Association](Association.md)** *[subject](subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

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

 * [archived](archived.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [enabled](enabled.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)
 * [note](note.md)  <sub>OPT</sub>
    * range: [NarrativeText](types/NarrativeText.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | BFO:0000001 |
|  | | WIKIDATA:Q35120 |


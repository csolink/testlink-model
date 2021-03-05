---
parent: Entities
title: testlink:OntologyClass
grand_parent: Classes
layout: default
---

# Class: OntologyClass


a concept or class in an ontology, vocabulary or thesaurus

URI: [testlink:OntologyClass](https://w3id.org/testlink/vocab/OntologyClass)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TaxonomicRank],[SystemTaxon],[RelationshipType],[Attribute]-%20has%20attribute%20type%201..1%3E[OntologyClass%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[Association]-%20qualifiers%200..%2A%3E[OntologyClass],[OntologyClass]%5E-[TaxonomicRank],[OntologyClass]%5E-[SystemTaxon],[OntologyClass]%5E-[RelationshipType],[NamedThing]%5E-[OntologyClass],[NamedThing],[AttributeType],[Attribute],[Association])

---


## Identifier prefixes

 * LCSH

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
 * [SystemTaxon](SystemTaxon.md) - A classification of a set of systems.
 * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)

## Referenced by class

 *  **[Association](Association.md)** *[association type](association_type.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[AttributeType](AttributeType.md)** *[has attribute type](has_attribute_type.md)*  <sub>REQ</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[qualifiers](qualifiers.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


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

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

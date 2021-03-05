---
parent: Entities
title: testlink:SystemTaxon
grand_parent: Classes
layout: default
---

# Class: SystemTaxon


A classification of a set of systems.

URI: [testlink:SystemTaxon](https://w3id.org/testlink/vocab/SystemTaxon)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[TaxonomicRank],[SystemTaxon]%3Csubclass%20of%200..1-%20[SystemTaxon%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[TaxonomicRank]%3Chas%20taxonomic%20rank%200..1-%20[SystemTaxon],[ThingWithTaxon]-%20in%20taxon%200..%2A%3E[SystemTaxon],[OntologyClass]%5E-[SystemTaxon],[OntologyClass],[NamedThing])

---


## Identifier prefixes

 * NCBITaxon
 * LCSH

## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Referenced by class

 *  **[ThingWithTaxon](ThingWithTaxon.md)** *[in taxon](in_taxon.md)*  <sub>0..*</sub>  **[SystemTaxon](SystemTaxon.md)**
 *  **None** *[subclass of](subclass_of.md)*  <sub>OPT</sub>  **[SystemTaxon](SystemTaxon.md)**
 *  **[SystemTaxon](SystemTaxon.md)** *[system taxon➞subclass of](system_taxon_subclass_of.md)*  <sub>OPT</sub>  **[SystemTaxon](SystemTaxon.md)**

## Attributes


### Own

 * [system taxon➞has taxonomic rank](system_taxon_has_taxonomic_rank.md)  <sub>OPT</sub>
    * range: [TaxonomicRank](TaxonomicRank.md)
 * [system taxon➞subclass of](system_taxon_subclass_of.md)  <sub>OPT</sub>
    * Description: subclass of holds between two taxa, e.g. subclass of superclass
    * range: [SystemTaxon](SystemTaxon.md)

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

### Domain for slot:

 * [system taxon➞has taxonomic rank](system_taxon_has_taxonomic_rank.md)  <sub>OPT</sub>
    * range: [TaxonomicRank](TaxonomicRank.md)
 * [system taxon➞subclass of](system_taxon_subclass_of.md)  <sub>OPT</sub>
    * Description: subclass of holds between two taxa, e.g. subclass of superclass
    * range: [SystemTaxon](SystemTaxon.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | taxon |
|  | | taxonomic classification |
| **In Subsets:** | | my_system_model |
| **Exact Mappings:** | | csrc:Taxonomy |
|  | | sumo:Taxonomy |
|  | | WIKIDATA:Q16521 |


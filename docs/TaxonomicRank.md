---
parent: Entities
title: testlink:TaxonomicRank
grand_parent: Classes
layout: default
---

# Class: TaxonomicRank


A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)

URI: [testlink:TaxonomicRank](https://w3id.org/testlink/vocab/TaxonomicRank)

WIKIDATA:Q427626
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon]-%20has%20taxonomic%20rank%200..1%3E[TaxonomicRank%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[OntologyClass]%5E-[TaxonomicRank],[SystemTaxon],[OntologyClass],[NamedThing])

---


## Identifier prefixes

 * TAXRANK

## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Referenced by class

 *  **None** *[has taxonomic rank](has_taxonomic_rank.md)*  <sub>OPT</sub>  **[TaxonomicRank](TaxonomicRank.md)**
 *  **[SystemTaxon](SystemTaxon.md)** *[system taxon➞has taxonomic rank](system_taxon_has_taxonomic_rank.md)*  <sub>OPT</sub>  **[TaxonomicRank](TaxonomicRank.md)**

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | WIKIDATA:Q427626 |


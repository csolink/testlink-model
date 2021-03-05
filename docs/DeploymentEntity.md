---
parent: Entities
title: testlink:DeploymentEntity
grand_parent: Classes
layout: default
---

# Class: DeploymentEntity


A process location, serviceunit type or gross deployment part

URI: [testlink:DeploymentEntity](https://w3id.org/testlink/vocab/DeploymentEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[SystemicEntity],[SystemTaxon],[NamedThing],[DeploymentEntity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]uses%20-.-%3E[ThingWithTaxon],[DeploymentEntity]uses%20-.-%3E[CyberEssence],[DeploymentEntity]%5E-[Deployment],[DeploymentEntity]%5E-[Component],[SystemicEntity]%5E-[DeploymentEntity],[Deployment],[CyberEssence],[Component],[Attribute])

---


## Identifier prefixes

 * LCSH

## Parents

 *  is_a: [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes
 *  mixin: [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.

## Children

 * [Component](Component.md) - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
 * [Deployment](Deployment.md)

## Referenced by class


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

### Inherited from systemic entity:

 * [systemic entity➞has attribute](systemic_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may often be an system attribute
    * range: [Attribute](Attribute.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | samples |
| **Close Mappings:** | | WIKIDATA:Q4936952 |
| **Narrow Mappings:** | | csrc:Platform |
|  | | MAID:9390403 |
|  | | MAID:105339364 |
|  | | csrc:Public_cloud |
|  | | csrc:cloud_computing |
|  | | csrc:Private_cloud |
|  | | csrc:Hybrid_cloud |
|  | | csrc:Java_Platform_Enterprise_Edition |
|  | | csrc:Platform_as_a_Service |
| **Broad Mappings:** | | MAID:96711827 |
|  | | WIKIDATA:Q3055454 |


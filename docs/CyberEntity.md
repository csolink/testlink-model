---
parent: Entities
title: testlink:CyberEntity
grand_parent: Classes
layout: default
---

# Class: CyberEntity


An entity that has digital reality (a.k.a. cyber essence).

URI: [testlink:CyberEntity](https://w3id.org/testlink/vocab/CyberEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[CyberEssence],[ComputationalProcessOrActivity]-%20enabled%20by%200..%2A%3E[CyberEntity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[CyberEntity]uses%20-.-%3E[CyberEssence],[NamedThing]%5E-[CyberEntity],[ComputationalProcessOrActivity])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Uses Mixins

 *  mixin: [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.

## Referenced by class

 *  **[ComputationalProcessOrActivity](ComputationalProcessOrActivity.md)** *[enabled by](enabled_by.md)*  <sub>0..*</sub>  **[CyberEntity](CyberEntity.md)**

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
| **Narrow Mappings:** | | csrc:Authenticable_Entity |
|  | | csrc:cyber_resource |
|  | | csrc:non_person_entity |
|  | | MAID:179768478 |


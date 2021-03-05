---
parent: Entities
title: testlink:ComputationalEntity
grand_parent: Classes
layout: default
---

# Class: ComputationalEntity




URI: [testlink:ComputationalEntity](https://w3id.org/testlink/vocab/ComputationalEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemicEntity],[OperationalEntity],[NamedThing],[ComputationalProcessOrActivity],[ComputationalEntity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]%5E-[SystemicEntity],[ComputationalEntity]%5E-[OperationalEntity],[ComputationalEntity]%5E-[ComputationalProcessOrActivity],[NamedThing]%5E-[ComputationalEntity])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ComputationalProcessOrActivity](ComputationalProcessOrActivity.md) - Either an individual operational activity, or a collection of causally connected operational activities
 * [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
 * [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000602 |
|  | | SIO:000097 |
|  | | sumo:ComputationalSystem |
| **Narrow Mappings:** | | CSO:computational_grid |
|  | | CSO:computational_resource |
|  | | CSO:computational_power |
|  | | REPR:ComputationalTool |
|  | | schema:SoftwareApplication |
| **Broad Mappings:** | | NCIT:C18141 |
|  | | ssn:FeatureOfInterest |
|  | | ssn:System |


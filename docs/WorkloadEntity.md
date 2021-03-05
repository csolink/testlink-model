---
parent: Entities
title: testlink:WorkloadEntity
grand_parent: Classes
layout: default
---

# Class: WorkloadEntity


An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)

URI: [testlink:WorkloadEntity](https://w3id.org/testlink/vocab/WorkloadEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkloadEntity%7Chas_computational_sequence:computational_sequence%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]%5E-[Workload],[WorkloadEntity]%5E-[ServerGroup],[WorkloadEntity]%5E-[ApplicationInstance],[OperationalEntity]%5E-[WorkloadEntity],[Workload],[SystemTaxon],[ServerGroup],[OperationalEntity],[NamedThing],[ApplicationInstance])

---


## Parents

 *  is_a: [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

## Children

 * [ApplicationInstance](ApplicationInstance.md) - The unit of service workload the component is capable of providing or protecting.
 * [ServerGroup](ServerGroup.md) - An group of servers
 * [Workload](Workload.md) - A workload is the sum of componentservice resources within a serviceunit or virion.

## Referenced by class


## Attributes


### Own

 * [has computational sequence](has_computational_sequence.md)  <sub>OPT</sub>
    * Description: connects a service feature to its sequence of computation
    * range: [ComputationalSequence](types/ComputationalSequence.md)

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sequence feature |
| **Exact Mappings:** | | MAID:2993258540 |
| **Narrow Mappings:** | | MAID:115235246 |


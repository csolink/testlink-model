---
parent: Entities
title: testlink:ConsumedResource
grand_parent: Classes
layout: default
---

# Class: ConsumedResource


A control actor (often a cluster) consumed for information, engineering or technical use.

URI: [testlink:ConsumedResource](https://w3id.org/testlink/vocab/ConsumedResource)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[NamedThing],[ControlActor],[ConsumedResource%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]uses%20-.-%3E[Cluster],[ConsumedResource]uses%20-.-%3E[Application],[ControlActor]%5E-[ConsumedResource],[Cluster],[Application])

---


## Parents

 *  is_a: [ControlActor](ControlActor.md) - May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part

## Uses Mixins

 *  mixin: [Cluster](Cluster.md) - The cyber combination of two or more operational entities in which the identities are retained and are mixed in the form of solutions,
 *  mixin: [Application](Application.md) - The cyper combination of one or more components, serviceunits (pod), in which the identities are retained and mixed in the form of solutions,

## Attributes


### Inherited from application:

 * [has control actor](has_control_actor.md)  <sub>0..*</sub>
    * Description: one or more control actors within a cluster
    * range: [ControlActor](ControlActor.md)

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
| **Narrow Mappings:** | | CSO:power_consumed |
|  | | csrc:cyber_resource |
|  | | csrc:Filesystem |
|  | | csrc:network |
|  | | csrc:Operating_System |
|  | | csrc:Random_Access_Memory |
|  | | csrc:Read_Only_Memory |
|  | | csrc:Resource_pooling |
|  | | csrc:Storage |
|  | | MAID:70437156 |
|  | | NCIT:C19012 |
| **Related Mappings:** | | dwc:resourceID |
|  | | SAN:isConsumedBy |


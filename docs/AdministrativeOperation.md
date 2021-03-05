---
parent: Entities
title: testlink:AdministrativeOperation
grand_parent: Classes
layout: default
---

# Class: AdministrativeOperation


A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error

URI: [testlink:AdministrativeOperation](https://w3id.org/testlink/vocab/AdministrativeOperation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[OperationalEntity],[NamedThing],[ControlActor],[Cluster],[Application],[AdministrativeOperation%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]uses%20-.-%3E[Cluster],[AdministrativeOperation]uses%20-.-%3E[Application],[OperationalEntity]%5E-[AdministrativeOperation])

---


## Parents

 *  is_a: [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

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
| **Comments:** | | The ID represents a role rather than a substance |
| **Exact Mappings:** | | SAN:ActuationValue |
|  | | SAN:ActuatingRange |
|  | | schema:ControlAction |
|  | | sumo:administrator |
|  | | sumo:OperationOrder |
| **Narrow Mappings:** | | csrc:create_read_update_delete |
|  | | csrc:Installation |
|  | | csrc:Secure_Erase_Command |
| **Broad Mappings:** | | CSO:administrative_data_processing |
|  | | CSO:control_and_automation |
|  | | CSO:network_operations |
|  | | csrc:control |
|  | | EDAM-OPERATION:0004 |
|  | | MAID:21547014 |
|  | | NCIT:C62617 |
|  | | sumo:AdministrationAndManagement |
|  | | sumo:Directing |
| **Related Mappings:** | | schema:AdministrativeArea |


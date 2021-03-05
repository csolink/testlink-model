---
parent: Entities
title: testlink:OperationalEntity
grand_parent: Classes
layout: default
---

# Class: OperationalEntity


A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

URI: [testlink:OperationalEntity](https://w3id.org/testlink/vocab/OperationalEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkloadEntity],[ThingWithTaxon],[SystemTaxon],[OperationalEntity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]uses%20-.-%3E[ThingWithTaxon],[OperationalEntity]uses%20-.-%3E[CyberEssence],[OperationalEntity]%5E-[WorkloadEntity],[OperationalEntity]%5E-[Notification],[OperationalEntity]%5E-[ControlActor],[OperationalEntity]%5E-[AdministrativeOperation],[ComputationalEntity]%5E-[OperationalEntity],[Notification],[NamedThing],[CyberEssence],[ControlActor],[ComputationalEntity],[AdministrativeOperation])

---


## Parents

 *  is_a: [ComputationalEntity](ComputationalEntity.md)

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes
 *  mixin: [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.

## Children

 * [AdministrativeOperation](AdministrativeOperation.md) - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
 * [ControlActor](ControlActor.md) - May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part
 * [Notification](Notification.md) - A event consumed by a healthy system as a source of information
 * [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Narrow Mappings:** | | csrc:operational_technology |
|  | | NCIT:C47908 |
|  | | schema:operatingSystem |
|  | | ssn:Deployment |
|  | | sumo:Computer |
|  | | sumo:ComputerProgram |
|  | | sumo:ComputerProcess |
|  | | sumo:ComputerResource |
|  | | sumo:computerRunning |
|  | | sumo:OperationalAmplifier |
|  | | sumo:Server |
| **Broad Mappings:** | | sumo:ComputerComponent |
| **Related Mappings:** | | CSO:operational_profile |
|  | | geolink:hasOperationArea |
|  | | geolink:hasOperator |
|  | | geolink:isOperatorOf |


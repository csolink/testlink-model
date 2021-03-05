---
parent: Entities
title: testlink:ControlActor
grand_parent: Classes
layout: default
---

# Class: ControlActor


May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part

URI: [testlink:ControlActor](https://w3id.org/testlink/vocab/ControlActor)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[OrchestrationExposure],[OperationalEntity],[OperationalActivity],[NotificationComponent],[NamedThing],[Cluster]-%20has%20control%20actor%200..%2A%3E[ControlActor%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[Application]-%20has%20control%20actor%200..%2A%3E[ControlActor],[OperationalActivity]-%20has%20input%200..%2A%3E[ControlActor],[OperationalActivity]-%20has%20output%200..%2A%3E[ControlActor],[ControlActor]%5E-[OrchestrationExposure],[ControlActor]%5E-[NotificationComponent],[ControlActor]%5E-[ConsumedResource],[OperationalEntity]%5E-[ControlActor],[ConsumedResource],[Cluster],[Application])

---


## Parents

 *  is_a: [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

## Children

 * [ConsumedResource](ConsumedResource.md) - A control actor (often a cluster) consumed for information, engineering or technical use.
 * [NotificationComponent](NotificationComponent.md)
 * [OrchestrationExposure](OrchestrationExposure.md) - A orchestration exposure is an intake of a particular control actor, other than a administrative operation.

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[has control actor](has_control_actor.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[OperationalActivity](OperationalActivity.md)** *[operational activity➞has input](operational_activity_has_input.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[OperationalActivity](OperationalActivity.md)** *[operational activity➞has output](operational_activity_has_output.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**

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
| **Exact Mappings:** | | CTRL:ControlActor |
| **Narrow Mappings:** | | CSO:data_planes |
|  | | csrc:controlled |
|  | | csrc:controlled_access_area |
|  | | csrc:controlled_area |
|  | | csrc:controlled_interface |
|  | | csrc:controlled_space |
|  | | csrc:Control_Group |
|  | | csrc:Orchestrator |
|  | | csrc:Orchestration |
|  | | csrc:threat_actor |
|  | | csrc:Transmission_Power_Control |
|  | | CTRL:isSupervisedBy |
|  | | CTRL:supervises |
|  | | EFO:0009743 |
|  | | MAID:10597312 |
|  | | NCIT:C72011 |
|  | | NCIT:C134832 |
|  | | NCIT:C49887 |
| **Related Mappings:** | | CSO:control_system |
|  | | MAID:48209547 |
|  | | schema:ControlAction |
|  | | WIKIDATA:Q1331104 |


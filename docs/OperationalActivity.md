---
parent: Entities
title: testlink:OperationalActivity
grand_parent: Classes
layout: default
---

# Class: OperationalActivity


An execution of a operational function carried out by a servicetype or macrooperational complex.

URI: [testlink:OperationalActivity](https://w3id.org/testlink/vocab/OperationalActivity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MacrooperationalMachineMixin]%3Cenabled%20by%200..%2A-++[OperationalActivity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[ControlActor]%3Chas%20output%200..%2A-%20[OperationalActivity],[ControlActor]%3Chas%20input%200..%2A-%20[OperationalActivity],[OperationalActivity]uses%20-.-%3E[Occurrent],[ComputationalProcessOrActivity]%5E-[OperationalActivity],[Occurrent],[NamedThing],[MacrooperationalMachineMixin],[ControlActor],[ComputationalProcessOrActivity])

---


## Identifier prefixes

 * CSO
 * CTRL
 * csrc
 * CVE
 * MAID
 * NCIT
 * REPR
 * RO
 * SIO
 * SAN

## Parents

 *  is_a: [ComputationalProcessOrActivity](ComputationalProcessOrActivity.md) - Either an individual operational activity, or a collection of causally connected operational activities

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity.

## Referenced by class


## Attributes


### Own

 * [operational activity➞enabled by](operational_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The servicetype, componentservice, or complex that catalyzes the reaction
    * range: [MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)
 * [operational activity➞has input](operational_activity_has_input.md)  <sub>0..*</sub>
    * Description: A orchestration entity that is the input for the reaction
    * range: [ControlActor](ControlActor.md)
 * [operational activity➞has output](operational_activity_has_output.md)  <sub>0..*</sub>
    * Description: A orchestration entity that is the output for the reaction
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

### Domain for slot:

 * [operational activity➞enabled by](operational_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The servicetype, componentservice, or complex that catalyzes the reaction
    * range: [MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)
 * [operational activity➞has input](operational_activity_has_input.md)  <sub>0..*</sub>
    * Description: A orchestration entity that is the input for the reaction
    * range: [ControlActor](ControlActor.md)
 * [operational activity➞has output](operational_activity_has_output.md)  <sub>0..*</sub>
    * Description: A orchestration entity that is the output for the reaction
    * range: [ControlActor](ControlActor.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | operation function |
|  | | operation event |
|  | | reaction |
| **Broad Mappings:** | | csrc:activity |
| **Related Mappings:** | | geolink:hasOperator |
|  | | sumo:LogicalOperator |


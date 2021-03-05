---
parent: Entities
title: testlink:Activity
grand_parent: Classes
layout: default
---

# Class: Activity


An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.

URI: [testlink:Activity](https://w3id.org/testlink/vocab/Activity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[ActivityAndBehavior],[Activity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]uses%20-.-%3E[ActivityAndBehavior],[NamedThing]%5E-[Activity])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Uses Mixins

 *  mixin: [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral healthy, organization or mechanical actor in the world

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
| **Exact Mappings:** | | AML:activity |
|  | | csrc:Activity |
|  | | OM:Activity |
|  | | prov:Activity |
|  | | NCIT:C45329 |
|  | | NCIT:C43431 |
|  | | SAN:Acting |
| **Narrow Mappings:** | | csrc:intelligence_activities |
|  | | csrc:COMSEC_Incident_Monitoring_Activity |
|  | | csrc:Government_Contracting_Activity |
|  | | csrc:Intelligence_Advanced_Research_Projects_Activity |
|  | | csrc:malicious_cyber_activity |
|  | | csrc:user_activity_monitoring |
|  | | CSO:activity_recognition |
|  | | CSO:voice_activity_detection |
|  | | CSO:architecture_activity |
|  | | CSO:learning_activity |
|  | | CSO:malicious_activities |
|  | | CSO:design_activity |
|  | | CSO:maintenance_activity |
|  | | CSO:complex_activity |
|  | | CSO:user_activity |
|  | | sosa:Actuation |
|  | | WIKIDATA:Q1914636 |
| **Broad Mappings:** | | csrc:Activities |
|  | | sumo:activityCapability |


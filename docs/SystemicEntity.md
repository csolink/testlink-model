---
parent: Entities
title: testlink:SystemicEntity
grand_parent: Classes
layout: default
---

# Class: SystemicEntity


A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities

URI: [testlink:SystemicEntity](https://w3id.org/testlink/vocab/SystemicEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]%3Chas%20attribute%200..%2A-++[SystemicEntity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[Deployment]uses%20-.-%3E[SystemicEntity],[SystemicEntity]%5E-[ServerType],[SystemicEntity]%5E-[DeploymentEntity],[SystemicEntity]%5E-[ComponentType],[SystemicEntity]%5E-[ApplicationType],[ComputationalEntity]%5E-[SystemicEntity],[ServerType],[NamedThing],[DeploymentEntity],[Deployment],[ComputationalEntity],[ComponentType],[Attribute],[ApplicationType])

---


## Parents

 *  is_a: [ComputationalEntity](ComputationalEntity.md)

## Children

 * [ApplicationType](ApplicationType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
 * [ComponentType](ComponentType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
 * [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part
 * [ServerType](ServerType.md) - A type of server

## Mixin for

 * [Deployment](Deployment.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [systemic entity➞has attribute](systemic_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may often be an system attribute
    * range: [Attribute](Attribute.md)

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

 * [systemic entity➞has attribute](systemic_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may often be an system attribute
    * range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Narrow Mappings:** | | CSO:operating_system |
|  | | csrc:Operations_System |
|  | | sosa:Platform |
|  | | ssn:deployedSystem |
|  | | ssn:Deployment |
|  | | ssn:inDeployment |
|  | | sumo:OperatingSystem |
|  | | sumo:MonitoringProgram |
|  | | sumo:RegulatoryProcess |
| **Broad Mappings:** | | ssn:System |
| **Related Mappings:** | | WIKIDATA:Q17089065 |


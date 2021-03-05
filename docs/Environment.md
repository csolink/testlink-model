---
parent: Entities
title: testlink:Environment
grand_parent: Classes
layout: default
---

# Class: Environment


An environment

URI: [testlink:Environment](https://w3id.org/testlink/vocab/Environment)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[EnvironmentConfigurationToEnvironmentAssociation],[DomainEnvironmentToEnvironmentAssociation]-%20object%201..1%3E[Environment%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[EnvironmentConfigurationToEnvironmentAssociation]-%20object%201..1%3E[Environment],[Environment]%5E-[DomainEnvironment],[NamedThing]%5E-[Environment],[DomainEnvironmentToEnvironmentAssociation],[DomainEnvironment])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [DomainEnvironment](DomainEnvironment.md)

## Referenced by class

 *  **[DomainEnvironmentToEnvironmentAssociation](DomainEnvironmentToEnvironmentAssociation.md)** *[domain environment to environment association➞object](domain_environment_to_environment_association_object.md)*  <sub>REQ</sub>  **[Environment](Environment.md)**
 *  **[EnvironmentConfigurationToEnvironmentAssociation](EnvironmentConfigurationToEnvironmentAssociation.md)** *[environment configuration to environment association➞object](environment_configuration_to_environment_association_object.md)*  <sub>REQ</sub>  **[Environment](Environment.md)**

## Attributes


### Own

 * [archived](archived.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (samples)
 * [note](note.md)  <sub>OPT</sub>
    * range: [NarrativeText](types/NarrativeText.md)

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

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |
| **Exact Mappings:** | | NCIT:C16551 |
| **Broad Mappings:** | | ENVO:01000254 |
|  | | SIO:000955 |


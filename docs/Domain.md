---
parent: Entities
title: testlink:Domain
grand_parent: Classes
layout: default
---

# Class: Domain




URI: [testlink:Domain](https://w3id.org/testlink/vocab/Domain)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DomainEnvironmentToDomainAssociation],[DomainEnvironmentToDomainAssociation]-%20object%201..1%3E[Domain%7Cfqdn:label_type%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[AdministrativeEntity]%5E-[Domain],[AdministrativeEntity])

---


## Parents

 *  is_a: [AdministrativeEntity](AdministrativeEntity.md)

## Referenced by class

 *  **[DomainEnvironmentToDomainAssociation](DomainEnvironmentToDomainAssociation.md)** *[domain environment to domain association➞object](domain_environment_to_domain_association_object.md)*  <sub>REQ</sub>  **[Domain](Domain.md)**

## Attributes


### Own

 * [fqdn](fqdn.md)  <sub>OPT</sub>
    * range: [LabelType](types/LabelType.md)

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
| **In Subsets:** | | my_system_model |


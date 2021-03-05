---
parent: Entities
title: testlink:DomainEnvironment
grand_parent: Classes
layout: default
---

# Class: DomainEnvironment




URI: [testlink:DomainEnvironment](https://w3id.org/testlink/vocab/DomainEnvironment)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ServerGroupHubToDomainEnvironmentAssociation],[RealmConfigurationToDomainEnvironmentAssociation],[NamedThing],[Environment],[DomainEnvironmentToEnvironmentAssociation],[DomainEnvironmentToDomainAssociation],[ApplicationInstanceToDomainEnvironmentAssociation]-%20object%201..1%3E[DomainEnvironment%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[DomainConfigurationToDomainEnvironmentAssociation]-%20object%201..1%3E[DomainEnvironment],[DomainEnvironmentToDomainAssociation]-%20subject%201..1%3E[DomainEnvironment],[DomainEnvironmentToEnvironmentAssociation]-%20subject%201..1%3E[DomainEnvironment],[RealmConfigurationToDomainEnvironmentAssociation]-%20object%201..1%3E[DomainEnvironment],[ServerGroupHubToDomainEnvironmentAssociation]-%20object%201..1%3E[DomainEnvironment],[Environment]%5E-[DomainEnvironment],[DomainConfigurationToDomainEnvironmentAssociation],[ApplicationInstanceToDomainEnvironmentAssociation])

---


## Parents

 *  is_a: [Environment](Environment.md) - An environment

## Referenced by class

 *  **[ApplicationInstanceToDomainEnvironmentAssociation](ApplicationInstanceToDomainEnvironmentAssociation.md)** *[application instance to domain environment association➞object](application_instance_to_domain_environment_association_object.md)*  <sub>REQ</sub>  **[DomainEnvironment](DomainEnvironment.md)**
 *  **[DomainConfigurationToDomainEnvironmentAssociation](DomainConfigurationToDomainEnvironmentAssociation.md)** *[domain configuration to domain environment association➞object](domain_configuration_to_domain_environment_association_object.md)*  <sub>REQ</sub>  **[DomainEnvironment](DomainEnvironment.md)**
 *  **[DomainEnvironmentToDomainAssociation](DomainEnvironmentToDomainAssociation.md)** *[domain environment to domain association➞subject](domain_environment_to_domain_association_subject.md)*  <sub>REQ</sub>  **[DomainEnvironment](DomainEnvironment.md)**
 *  **[DomainEnvironmentToEnvironmentAssociation](DomainEnvironmentToEnvironmentAssociation.md)** *[domain environment to environment association➞subject](domain_environment_to_environment_association_subject.md)*  <sub>REQ</sub>  **[DomainEnvironment](DomainEnvironment.md)**
 *  **[RealmConfigurationToDomainEnvironmentAssociation](RealmConfigurationToDomainEnvironmentAssociation.md)** *[realm configuration to domain environment association➞object](realm_configuration_to_domain_environment_association_object.md)*  <sub>REQ</sub>  **[DomainEnvironment](DomainEnvironment.md)**
 *  **[ServerGroupHubToDomainEnvironmentAssociation](ServerGroupHubToDomainEnvironmentAssociation.md)** *[server group hub to domain environment association➞object](server_group_hub_to_domain_environment_association_object.md)*  <sub>REQ</sub>  **[DomainEnvironment](DomainEnvironment.md)**

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
| **In Subsets:** | | my_system_model |


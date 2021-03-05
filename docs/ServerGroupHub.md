---
parent: Entities
title: testlink:ServerGroupHub
grand_parent: Classes
layout: default
---

# Class: ServerGroupHub




URI: [testlink:ServerGroupHub](https://w3id.org/testlink/vocab/ServerGroupHub)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ServerHubToServerGroupHubAssociation],[ServerGroupHubToServerGroupAssociation],[ServerGroupHubToDomainEnvironmentAssociation],[ApplicationInstanceToServerGroupHubAssociation]-%20object%201..1%3E[ServerGroupHub%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[ServerGroupHubToDomainEnvironmentAssociation]-%20subject%201..1%3E[ServerGroupHub],[ServerGroupHubToServerGroupAssociation]-%20subject%201..1%3E[ServerGroupHub],[ServerHubToServerGroupHubAssociation]-%20object%201..1%3E[ServerGroupHub],[Hub]%5E-[ServerGroupHub],[NamedThing],[Hub],[ApplicationInstanceToServerGroupHubAssociation])

---


## Parents

 *  is_a: [Hub](Hub.md)

## Referenced by class

 *  **[ApplicationInstanceToServerGroupHubAssociation](ApplicationInstanceToServerGroupHubAssociation.md)** *[application instance to server group hub association➞object](application_instance_to_server_group_hub_association_object.md)*  <sub>REQ</sub>  **[ServerGroupHub](ServerGroupHub.md)**
 *  **[ServerGroupHubToDomainEnvironmentAssociation](ServerGroupHubToDomainEnvironmentAssociation.md)** *[server group hub to domain environment association➞subject](server_group_hub_to_domain_environment_association_subject.md)*  <sub>REQ</sub>  **[ServerGroupHub](ServerGroupHub.md)**
 *  **[ServerGroupHubToServerGroupAssociation](ServerGroupHubToServerGroupAssociation.md)** *[server group hub to server group association➞subject](server_group_hub_to_server_group_association_subject.md)*  <sub>REQ</sub>  **[ServerGroupHub](ServerGroupHub.md)**
 *  **[ServerHubToServerGroupHubAssociation](ServerHubToServerGroupHubAssociation.md)** *[server hub to server group hub association➞object](server_hub_to_server_group_hub_association_object.md)*  <sub>REQ</sub>  **[ServerGroupHub](ServerGroupHub.md)**

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


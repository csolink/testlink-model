---
parent: Entities
title: testlink:ApplicationInstance
grand_parent: Classes
layout: default
---

# Class: ApplicationInstance


The unit of service workload the component is capable of providing or protecting.

URI: [testlink:ApplicationInstance](https://w3id.org/testlink/vocab/ApplicationInstance)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkloadEntity],[SystemTaxon],[NamedThing],[BuildToApplicationInstanceAssociation],[ApplicationInstanceToServerGroupHubAssociation],[ApplicationInstanceToRealmAssociation],[ApplicationInstanceToDomainEnvironmentAssociation],[ApplicationInstanceToApplicationAssociation],[ApplicationInstanceConfigurationToApplicationInstanceAssociation],[ApplicationInstanceConfigurationToApplicationInstanceAssociation]-%20object%201..1%3E[ApplicationInstance%7Cinternal_version:string%20%3F;has_computational_sequence(i):computational_sequence%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[ApplicationInstanceToApplicationAssociation]-%20subject%201..1%3E[ApplicationInstance],[ApplicationInstanceToDomainEnvironmentAssociation]-%20subject%201..1%3E[ApplicationInstance],[ApplicationInstanceToRealmAssociation]-%20subject%201..1%3E[ApplicationInstance],[ApplicationInstanceToServerGroupHubAssociation]-%20subject%201..1%3E[ApplicationInstance],[BuildToApplicationInstanceAssociation]-%20object%201..1%3E[ApplicationInstance],[WorkloadEntity]%5E-[ApplicationInstance])

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

 *  is_a: [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)

## Referenced by class

 *  **[ApplicationInstanceConfigurationToApplicationInstanceAssociation](ApplicationInstanceConfigurationToApplicationInstanceAssociation.md)** *[application instance configuration to application instance association➞object](application_instance_configuration_to_application_instance_association_object.md)*  <sub>REQ</sub>  **[ApplicationInstance](ApplicationInstance.md)**
 *  **[ApplicationInstanceToApplicationAssociation](ApplicationInstanceToApplicationAssociation.md)** *[application instance to application association➞subject](application_instance_to_application_association_subject.md)*  <sub>REQ</sub>  **[ApplicationInstance](ApplicationInstance.md)**
 *  **[ApplicationInstanceToDomainEnvironmentAssociation](ApplicationInstanceToDomainEnvironmentAssociation.md)** *[application instance to domain environment association➞subject](application_instance_to_domain_environment_association_subject.md)*  <sub>REQ</sub>  **[ApplicationInstance](ApplicationInstance.md)**
 *  **[ApplicationInstanceToRealmAssociation](ApplicationInstanceToRealmAssociation.md)** *[application instance to realm association➞subject](application_instance_to_realm_association_subject.md)*  <sub>REQ</sub>  **[ApplicationInstance](ApplicationInstance.md)**
 *  **[ApplicationInstanceToServerGroupHubAssociation](ApplicationInstanceToServerGroupHubAssociation.md)** *[application instance to server group hub association➞subject](application_instance_to_server_group_hub_association_subject.md)*  <sub>REQ</sub>  **[ApplicationInstance](ApplicationInstance.md)**
 *  **[BuildToApplicationInstanceAssociation](BuildToApplicationInstanceAssociation.md)** *[build to application instance association➞object](build_to_application_instance_association_object.md)*  <sub>REQ</sub>  **[ApplicationInstance](ApplicationInstance.md)**

## Attributes


### Own

 * [internal version](internal_version.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

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

### Inherited from workload entity:

 * [has computational sequence](has_computational_sequence.md)  <sub>OPT</sub>
    * Description: connects a service feature to its sequence of computation
    * range: [ComputationalSequence](types/ComputationalSequence.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |
| **Exact Mappings:** | | csrc:Proximity_Services |
| **Broad Mappings:** | | csrc:service |
|  | | csrc:Service_Agent |
|  | | schema:Service |
|  | | sumo:instance |


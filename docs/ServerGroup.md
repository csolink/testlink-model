---
parent: Entities
title: testlink:ServerGroup
grand_parent: Classes
layout: default
---

# Class: ServerGroup


An group of servers

URI: [testlink:ServerGroup](https://w3id.org/testlink/vocab/ServerGroup)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkloadEntity],[SystemTaxon],[ServerGroupToServerTypeAssociation],[ServerGroupHubToServerGroupAssociation],[Homogeneity]%3Chas%20homogeneity%200..1-++[ServerGroup%7Chas_computational_sequence(i):computational_sequence%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[ServerGroupHubToServerGroupAssociation]-%20object%201..1%3E[ServerGroup],[ServerGroupToServerTypeAssociation]-%20subject%201..1%3E[ServerGroup],[WorkloadEntity]%5E-[ServerGroup],[NamedThing],[Homogeneity])

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

 *  **[ServerGroupHubToServerGroupAssociation](ServerGroupHubToServerGroupAssociation.md)** *[server group hub to server group association➞object](server_group_hub_to_server_group_association_object.md)*  <sub>REQ</sub>  **[ServerGroup](ServerGroup.md)**
 *  **[ServerGroupToServerTypeAssociation](ServerGroupToServerTypeAssociation.md)** *[server group to server type association➞subject](server_group_to_server_type_association_subject.md)*  <sub>REQ</sub>  **[ServerGroup](ServerGroup.md)**

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

### Inherited from workload entity:

 * [has computational sequence](has_computational_sequence.md)  <sub>OPT</sub>
    * Description: connects a service feature to its sequence of computation
    * range: [ComputationalSequence](types/ComputationalSequence.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |
| **Broad Mappings:** | | sumo:controlGroup |


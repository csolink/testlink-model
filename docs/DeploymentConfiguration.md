---
parent: Entities
title: testlink:DeploymentConfiguration
grand_parent: Classes
layout: default
---

# Class: DeploymentConfiguration




URI: [testlink:DeploymentConfiguration](https://w3id.org/testlink/vocab/DeploymentConfiguration)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[NamedThing],[DeploymentConfigurationToDeploymentAssociation],[DeploymentConfigurationToDeploymentAssociation]-%20subject%201..1%3E[DeploymentConfiguration%7Cversion(i):string%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[Configuration]%5E-[DeploymentConfiguration],[Configuration])

---


## Parents

 *  is_a: [Configuration](Configuration.md) - Configuration is the manner in which components are arranged to make up the computer system. Configuration consists of both hardware and software components.

## Referenced by class

 *  **[DeploymentConfigurationToDeploymentAssociation](DeploymentConfigurationToDeploymentAssociation.md)** *[deployment configuration to deployment association➞subject](deployment_configuration_to_deployment_association_subject.md)*  <sub>REQ</sub>  **[DeploymentConfiguration](DeploymentConfiguration.md)**

## Attributes


### Inherited from configuration:

 * [has part](has_part.md)  <sub>0..*</sub>
    * Description: holds between wholes and their parts (resource entities or processes)
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

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

### Inherited from information content entity:

 * [license](license.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [format](format.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [creation date](creation_date.md)  <sub>OPT</sub>
    * Description: date on which an entity was created. This can be applied to nodes or edges
    * range: [Date](types/Date.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |


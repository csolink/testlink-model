---
parent: Entities
title: testlink:Deployment
grand_parent: Classes
layout: default
---

# Class: Deployment




URI: [testlink:Deployment](https://w3id.org/testlink/vocab/Deployment)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemicEntity],[SystemTaxon],[NamedThing],[DeploymentToBuildAssociation],[DeploymentToApplicationUserLoginAssociation],[DeploymentEntity],[DeploymentConfigurationToDeploymentAssociation],[DeploymentConfigurationToDeploymentAssociation]-%20object%201..1%3E[Deployment%7Capplication_user_login:string%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[DeploymentToApplicationUserLoginAssociation]-%20subject%201..1%3E[Deployment],[DeploymentToBuildAssociation]-%20subject%201..1%3E[Deployment],[Deployment]uses%20-.-%3E[Application],[Deployment]uses%20-.-%3E[SystemicEntity],[DeploymentEntity]%5E-[Deployment],[ControlActor],[Attribute],[Application])

---


## Parents

 *  is_a: [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part

## Uses Mixins

 *  mixin: [Application](Application.md) - The cyper combination of one or more components, serviceunits (pod), in which the identities are retained and mixed in the form of solutions,
 *  mixin: [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities

## Referenced by class

 *  **[DeploymentConfigurationToDeploymentAssociation](DeploymentConfigurationToDeploymentAssociation.md)** *[deployment configuration to deployment association➞object](deployment_configuration_to_deployment_association_object.md)*  <sub>REQ</sub>  **[Deployment](Deployment.md)**
 *  **[DeploymentToApplicationUserLoginAssociation](DeploymentToApplicationUserLoginAssociation.md)** *[deployment to application user login association➞subject](deployment_to_application_user_login_association_subject.md)*  <sub>REQ</sub>  **[Deployment](Deployment.md)**
 *  **[DeploymentToBuildAssociation](DeploymentToBuildAssociation.md)** *[deployment to build association➞subject](deployment_to_build_association_subject.md)*  <sub>REQ</sub>  **[Deployment](Deployment.md)**

## Attributes


### Own

 * [application user login](application_user_login.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * in subsets: (my_system_model)

### Inherited from application:

 * [has control actor](has_control_actor.md)  <sub>0..*</sub>
    * Description: one or more control actors within a cluster
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

### Inherited from systemic entity:

 * [systemic entity➞has attribute](systemic_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may often be an system attribute
    * range: [Attribute](Attribute.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (samples)

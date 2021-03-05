---
parent: Entities
title: testlink:Build
grand_parent: Classes
layout: default
---

# Class: Build




URI: [testlink:Build](https://w3id.org/testlink/vocab/Build)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DeploymentToBuildAssociation],[Dataset],[BuildToVcsRootAssociation],[BuildToProjectAssociation],[BuildToApplicationUserLoginAssociation],[BuildToApplicationInstanceAssociation],[BuildConfigurationToBuildAssociation],[BuildConfigurationToBuildAssociation]-%20object%201..1%3E[Build%7Ccreated:date%20%3F;updated:date%20%3F;vcs_location:string%20%3F;vcs_revision:string%20%3F;internal_version:string%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[BuildToApplicationInstanceAssociation]-%20subject%201..1%3E[Build],[BuildToApplicationUserLoginAssociation]-%20subject%201..1%3E[Build],[BuildToProjectAssociation]-%20subject%201..1%3E[Build],[BuildToVcsRootAssociation]-%20subject%201..1%3E[Build],[DeploymentToBuildAssociation]-%20object%201..1%3E[Build],[Dataset]%5E-[Build])

---


## Parents

 *  is_a: [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.

## Referenced by class

 *  **[BuildConfigurationToBuildAssociation](BuildConfigurationToBuildAssociation.md)** *[build configuration to build association➞object](build_configuration_to_build_association_object.md)*  <sub>REQ</sub>  **[Build](Build.md)**
 *  **[BuildToApplicationInstanceAssociation](BuildToApplicationInstanceAssociation.md)** *[build to application instance association➞subject](build_to_application_instance_association_subject.md)*  <sub>REQ</sub>  **[Build](Build.md)**
 *  **[BuildToApplicationUserLoginAssociation](BuildToApplicationUserLoginAssociation.md)** *[build to application user login association➞subject](build_to_application_user_login_association_subject.md)*  <sub>REQ</sub>  **[Build](Build.md)**
 *  **[BuildToProjectAssociation](BuildToProjectAssociation.md)** *[build to project association➞subject](build_to_project_association_subject.md)*  <sub>REQ</sub>  **[Build](Build.md)**
 *  **[BuildToVcsRootAssociation](BuildToVcsRootAssociation.md)** *[build to vcs root association➞subject](build_to_vcs_root_association_subject.md)*  <sub>REQ</sub>  **[Build](Build.md)**
 *  **[DeploymentToBuildAssociation](DeploymentToBuildAssociation.md)** *[deployment to build association➞object](deployment_to_build_association_object.md)*  <sub>REQ</sub>  **[Build](Build.md)**

## Attributes


### Own

 * [updated](updated.md)  <sub>OPT</sub>
    * range: [Date](types/Date.md)
 * [vcs location](vcs_location.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [vcs revision](vcs_revision.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from application instance:

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

### Inherited from inventory:

 * [created](created.md)  <sub>OPT</sub>
    * range: [Date](types/Date.md)
 * [component fixed](component_fixed.md)  <sub>OPT</sub>
    * range: [LabelType](types/LabelType.md)
 * [tag](tag.md)  <sub>OPT</sub>
    * range: [LabelType](types/LabelType.md)
 * [user login](user_login.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [svn tag url](svn_tag_url.md)  <sub>OPT</sub>
    * range: [IriType](types/IriType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |
| **Exact Mappings:** | | NCIT:C47904 |
| **Related Mappings:** | | NCIT:C165085 |
|  | | NCIT:C164461 |
|  | | SIO:000654 |


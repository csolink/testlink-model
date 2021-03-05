---
parent: Entities
title: testlink:ApplicationUserLogin
grand_parent: Classes
layout: default
---

# Class: ApplicationUserLogin




URI: [testlink:ApplicationUserLogin](https://w3id.org/testlink/vocab/ApplicationUserLogin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DeploymentToApplicationUserLoginAssociation],[BuildToApplicationUserLoginAssociation],[ApplicationUserLoginToApplicationUserAssociation],[ApplicationUserLoginToApplicationUserAssociation]-%20subject%201..1%3E[ApplicationUserLogin%7Cuser_name:label_type%20%3F;domain_name:label_type%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[BuildToApplicationUserLoginAssociation]-%20object%201..1%3E[ApplicationUserLogin],[DeploymentToApplicationUserLoginAssociation]-%20object%201..1%3E[ApplicationUserLogin],[AdministrativeEntity]%5E-[ApplicationUserLogin],[AdministrativeEntity])

---


## Parents

 *  is_a: [AdministrativeEntity](AdministrativeEntity.md)

## Mixin for


## Referenced by class

 *  **[ApplicationUserLoginToApplicationUserAssociation](ApplicationUserLoginToApplicationUserAssociation.md)** *[application user login to application user association➞subject](application_user_login_to_application_user_association_subject.md)*  <sub>REQ</sub>  **[ApplicationUserLogin](ApplicationUserLogin.md)**
 *  **[BuildToApplicationUserLoginAssociation](BuildToApplicationUserLoginAssociation.md)** *[build to application user login association➞object](build_to_application_user_login_association_object.md)*  <sub>REQ</sub>  **[ApplicationUserLogin](ApplicationUserLogin.md)**
 *  **[DeploymentToApplicationUserLoginAssociation](DeploymentToApplicationUserLoginAssociation.md)** *[deployment to application user login association➞object](deployment_to_application_user_login_association_object.md)*  <sub>REQ</sub>  **[ApplicationUserLogin](ApplicationUserLogin.md)**

## Attributes


### Own

 * [domain name](domain_name.md)  <sub>OPT</sub>
    * range: [LabelType](types/LabelType.md)
 * [user name](user_name.md)  <sub>OPT</sub>
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

---
parent: Entities
title: testlink:ApplicationUser
grand_parent: Classes
layout: default
---

# Class: ApplicationUser




URI: [testlink:ApplicationUser](https://w3id.org/testlink/vocab/ApplicationUser)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[EmailToApplicationUserAssociation],[ComponentOwnerToApplicationUserAssociation],[ApplicationUserLoginToApplicationUserAssociation],[ApplicationUserLoginToApplicationUserAssociation]-%20object%201..1%3E[ApplicationUser%7Cfirst_name:label_type%20%3F;last_name:label_type%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[ComponentOwnerToApplicationUserAssociation]-%20object%201..1%3E[ApplicationUser],[EmailToApplicationUserAssociation]-%20object%201..1%3E[ApplicationUser],[AdministrativeEntity]%5E-[ApplicationUser],[AdministrativeEntity])

---


## Parents

 *  is_a: [AdministrativeEntity](AdministrativeEntity.md)

## Referenced by class

 *  **[ApplicationUserLoginToApplicationUserAssociation](ApplicationUserLoginToApplicationUserAssociation.md)** *[application user login to application user association➞object](application_user_login_to_application_user_association_object.md)*  <sub>REQ</sub>  **[ApplicationUser](ApplicationUser.md)**
 *  **[ComponentOwnerToApplicationUserAssociation](ComponentOwnerToApplicationUserAssociation.md)** *[component owner to application user association➞object](component_owner_to_application_user_association_object.md)*  <sub>REQ</sub>  **[ApplicationUser](ApplicationUser.md)**
 *  **[EmailToApplicationUserAssociation](EmailToApplicationUserAssociation.md)** *[email to application user association➞object](email_to_application_user_association_object.md)*  <sub>REQ</sub>  **[ApplicationUser](ApplicationUser.md)**

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


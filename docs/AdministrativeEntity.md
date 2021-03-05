---
parent: Entities
title: testlink:AdministrativeEntity
grand_parent: Classes
layout: default
---

# Class: AdministrativeEntity




URI: [testlink:AdministrativeEntity](https://w3id.org/testlink/vocab/AdministrativeEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VcsRoot],[Realm],[Project],[NamedThing],[Hub],[Email],[Domain],[ComponentOwner],[ApplicationUserLogin],[ApplicationUser],[Agent],[AdministrativeEntity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]%5E-[VcsRoot],[AdministrativeEntity]%5E-[Realm],[AdministrativeEntity]%5E-[Project],[AdministrativeEntity]%5E-[Hub],[AdministrativeEntity]%5E-[Email],[AdministrativeEntity]%5E-[Domain],[AdministrativeEntity]%5E-[ComponentOwner],[AdministrativeEntity]%5E-[ApplicationUserLogin],[AdministrativeEntity]%5E-[ApplicationUser],[AdministrativeEntity]%5E-[Agent],[NamedThing]%5E-[AdministrativeEntity])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [Agent](Agent.md) - service, group, organization or project that provides a piece of information (i.e. a knowledge association)
 * [ApplicationUser](ApplicationUser.md)
 * [ApplicationUserLogin](ApplicationUserLogin.md)
 * [ComponentOwner](ComponentOwner.md)
 * [Domain](Domain.md)
 * [Email](Email.md) - A text string identifier location for e-mail delivery.
 * [Hub](Hub.md)
 * [Project](Project.md)
 * [Realm](Realm.md)
 * [VcsRoot](VcsRoot.md)

## Referenced by class


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

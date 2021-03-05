---
parent: Entities
title: testlink:Configuration
grand_parent: Classes
layout: default
---

# Class: Configuration


Configuration is the manner in which components are arranged to make up the computer system. Configuration consists of both hardware and software components.

URI: [testlink:Configuration](https://w3id.org/testlink/vocab/Configuration)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[RealmConfiguration],[QuantityValue],[NamedThing],[InformationContentEntity],[EnvironmentConfiguration],[DomainConfiguration],[DeploymentConfiguration],[QuantityValue]%3Chas%20quantitative%20value%200..%2A-++[Configuration%7Cversion:string%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[NamedThing]%3Chas%20part%200..%2A-%20[Configuration],[Configuration]%5E-[RealmConfiguration],[Configuration]%5E-[EnvironmentConfiguration],[Configuration]%5E-[DomainConfiguration],[Configuration]%5E-[DeploymentConfiguration],[Configuration]%5E-[ComponentConfiguration],[Configuration]%5E-[BuildConfiguration],[Configuration]%5E-[ApplicationInstanceConfiguration],[Configuration]%5E-[ApplicationConfiguration],[InformationContentEntity]%5E-[Configuration],[ComponentConfiguration],[BuildConfiguration],[ApplicationInstanceConfiguration],[ApplicationConfiguration])

---


## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.

## Children

 * [ApplicationConfiguration](ApplicationConfiguration.md)
 * [ApplicationInstanceConfiguration](ApplicationInstanceConfiguration.md)
 * [BuildConfiguration](BuildConfiguration.md)
 * [ComponentConfiguration](ComponentConfiguration.md)
 * [DeploymentConfiguration](DeploymentConfiguration.md)
 * [DomainConfiguration](DomainConfiguration.md)
 * [EnvironmentConfiguration](EnvironmentConfiguration.md)
 * [RealmConfiguration](RealmConfiguration.md)

## Referenced by class


## Attributes


### Own

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
| **Exact Mappings:** | | MAID:2989454740 |
| **Narrow Mappings:** | | NCIT:C85235 |
|  | | NCIT:C164721 |


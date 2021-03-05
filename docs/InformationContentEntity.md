---
parent: Entities
title: testlink:InformationContentEntity
grand_parent: Classes
layout: default
---

# Class: InformationContentEntity


a piece of information that typically describes some topic of discourse or is used as support.

URI: [testlink:InformationContentEntity](https://w3id.org/testlink/vocab/InformationContentEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[NamedThing],[InformationContentEntity%7Clicense:string%20%3F;rights:string%20%3F;format:string%20%3F;creation_date:date%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]%5E-[Publication],[InformationContentEntity]%5E-[DatasetDistribution],[InformationContentEntity]%5E-[Dataset],[InformationContentEntity]%5E-[Configuration],[NamedThing]%5E-[InformationContentEntity],[DatasetDistribution],[Dataset],[Configuration])

---


## Identifier prefixes

 * doi

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [Configuration](Configuration.md) - Configuration is the manner in which components are arranged to make up the computer system. Configuration consists of both hardware and software components.
 * [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.
 * [DatasetDistribution](DatasetDistribution.md) - an item that holds distribution level information about a dataset.
 * [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed resources, either directly or in one of the Publication testlink category subclasses.

## Referenced by class


## Attributes


### Own

 * [creation date](creation_date.md)  <sub>OPT</sub>
    * Description: date on which an entity was created. This can be applied to nodes or edges
    * range: [Date](types/Date.md)
 * [format](format.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [license](license.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
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

### Domain for slot:

 * [format](format.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [license](license.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | information |
|  | | information artefact |
|  | | information entity |
| **Exact Mappings:** | | IAO:0000030 |
| **Narrow Mappings:** | | schema:Language |
|  | | sumo:Language |
|  | | schema:inCodeSet |


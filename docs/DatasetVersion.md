---
parent: Entities
title: testlink:DatasetVersion
grand_parent: Classes
layout: default
---

# Class: DatasetVersion




URI: [testlink:DatasetVersion](https://w3id.org/testlink/vocab/DatasetVersion)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DistributionLevel],[DatasetDistribution]%3Chas%20distribution%200..1-%20[DatasetVersion%7Cingest_date:string%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[Dataset]%3Chas%20dataset%200..1-%20[DatasetVersion],[DatasetVersion]%5E-[DistributionLevel],[Dataset]%5E-[DatasetVersion],[DatasetDistribution],[Dataset])

---


## Parents

 *  is_a: [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.

## Children

 * [DistributionLevel](DistributionLevel.md)

## Referenced by class


## Attributes


### Own

 * [has dataset](has_dataset.md)  <sub>OPT</sub>
    * range: [Dataset](Dataset.md)
 * [has distribution](has_distribution.md)  <sub>OPT</sub>
    * range: [DatasetDistribution](DatasetDistribution.md)
 * [ingest date](ingest_date.md)  <sub>OPT</sub>
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

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [has dataset](has_dataset.md)  <sub>OPT</sub>
    * range: [Dataset](Dataset.md)
 * [has distribution](has_distribution.md)  <sub>OPT</sub>
    * range: [DatasetDistribution](DatasetDistribution.md)
 * [ingest date](ingest_date.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

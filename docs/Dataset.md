---
parent: Entities
title: testlink:Dataset
grand_parent: Classes
layout: default
---

# Class: Dataset


an item that refers to a collection of data from a data source.

URI: [testlink:Dataset](https://w3id.org/testlink/vocab/Dataset)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[Inventory],[InformationContentEntity],[DatasetVersion],[DatasetVersion]-%20has%20dataset%200..1%3E[Dataset%7Clicense(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[Dataset]%5E-[Inventory],[Dataset]%5E-[DatasetVersion],[Dataset]%5E-[Build],[Dataset]%5E-[Archive],[InformationContentEntity]%5E-[Dataset],[Build],[Archive])

---


## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.

## Children

 * [Archive](Archive.md)
 * [Build](Build.md)
 * [DatasetVersion](DatasetVersion.md)
 * [Inventory](Inventory.md)

## Referenced by class

 *  **[DatasetVersion](DatasetVersion.md)** *[has dataset](has_dataset.md)*  <sub>OPT</sub>  **[Dataset](Dataset.md)**

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
| **Exact Mappings:** | | csrc:Dataset |
|  | | IAO:0000100 |
|  | | dctypes:Dataset |
|  | | EFO:0004095 |
|  | | MAID:58489278 |
|  | | schema:Dataset |
|  | | SIO:000089 |
|  | | WIKIDATA:Q1172284 |
| **Narrow Mappings:** | | csrc:limited_dataset |
|  | | CSO:spatial_datasets |
|  | | MAID:3017436576 |


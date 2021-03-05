---
parent: Entities
title: testlink:ApplicationType
grand_parent: Classes
layout: default
---

# Class: ApplicationType


A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.

URI: [testlink:ApplicationType](https://w3id.org/testlink/vocab/ApplicationType)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemicEntity],[NamedThing],[Attribute],[ApplicationToApplicationTypeAssociation]-%20object%201..1%3E[ApplicationType%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[SystemicEntity]%5E-[ApplicationType],[ApplicationToApplicationTypeAssociation])

---


## Identifier prefixes

 * XXXX

## Parents

 *  is_a: [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities

## Referenced by class

 *  **[ApplicationToApplicationTypeAssociation](ApplicationToApplicationTypeAssociation.md)** *[application to application type association➞object](application_to_application_type_association_object.md)*  <sub>REQ</sub>  **[ApplicationType](ApplicationType.md)**

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

### Inherited from systemic entity:

 * [systemic entity➞has attribute](systemic_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may often be an system attribute
    * range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |
| **Broad Mappings:** | | dct:type |
| **Related Mappings:** | | RO:0002261 |


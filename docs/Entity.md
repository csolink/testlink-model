---
parent: Other Classes
title: testlink:Entity
grand_parent: Classes
layout: default
---

# Class: Entity


Root testlink Model class for all things and informational relationships, real or imagined.

URI: [testlink:Entity](https://w3id.org/testlink/vocab/Entity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[Entity%7Cid:string;name:label_type%20%3F;enabled:boolean%20%3F;archived:boolean%20%3F;description:narrative_text%20%3F;note:narrative_text%20%3F]%5E-[NamedThing],[Entity]%5E-[Association],[Association])

---


## Children

 * [Association](Association.md) - A typed association between two entities, supported by evidence
 * [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class


## Attributes


### Own

 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (samples)

### Inherited from email:

 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for an attribute or entity.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (samples)
 * [enabled](enabled.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)

### Inherited from environment:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (samples)
 * [note](note.md)  <sub>OPT</sub>
    * range: [NarrativeText](types/NarrativeText.md)
 * [archived](archived.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)

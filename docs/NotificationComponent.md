---
parent: Entities
title: testlink:NotificationComponent
grand_parent: Classes
layout: default
---

# Class: NotificationComponent




URI: [testlink:NotificationComponent](https://w3id.org/testlink/vocab/NotificationComponent)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[NotificationComponent%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F]%5E-[Data],[ControlActor]%5E-[NotificationComponent],[Notification],[NamedThing],[Data],[ControlActor])

---


## Parents

 *  is_a: [ControlActor](ControlActor.md) - May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part

## Children

 * [Data](Data.md)

## Referenced by class

 *  **[Notification](Notification.md)** *[has notification component](has_notification_component.md)*  <sub>0..*</sub>  **[NotificationComponent](NotificationComponent.md)**

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (samples)

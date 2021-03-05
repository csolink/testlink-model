---
parent: Entities
title: testlink:Notification
grand_parent: Classes
layout: default
---

# Class: Notification


A event consumed by a healthy system as a source of information

URI: [testlink:Notification](https://w3id.org/testlink/vocab/Notification)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[OperationalEntity],[NotificationComponent],[Data]%3Chas%20data%200..%2A-%20[Notification%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[Notification]uses%20-.-%3E[Application],[OperationalEntity]%5E-[Notification],[NamedThing],[Data],[ControlActor],[Application])

---


## Identifier prefixes

 * sumo
 * csrc
 * NCIT
 * CSO

## Parents

 *  is_a: [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

## Uses Mixins

 *  mixin: [Application](Application.md) - The cyper combination of one or more components, serviceunits (pod), in which the identities are retained and mixed in the form of solutions,

## Referenced by class

 *  **[NotificationComponent](NotificationComponent.md)** *[data of](data_of.md)*  <sub>0..*</sub>  **[Notification](Notification.md)**
 *  **[NotificationComponent](NotificationComponent.md)** *[notification component of](notification_component_of.md)*  <sub>0..*</sub>  **[Notification](Notification.md)**

## Attributes


### Own

 * [has data](has_data.md)  <sub>0..*</sub>
    * Description: one or more datas which are growth factors for a system
    * range: [Data](Data.md)
    * in subsets: (samples)

### Inherited from application:

 * [has control actor](has_control_actor.md)  <sub>0..*</sub>
    * Description: one or more control actors within a cluster
    * range: [ControlActor](ControlActor.md)

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

### Domain for slot:

 * [has data](has_data.md)  <sub>0..*</sub>
    * Description: one or more datas which are growth factors for a system
    * range: [Data](Data.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | csrc:Alarm |
|  | | csrc:alert |
|  | | NCIT:C93411 |
|  | | NCIT:C93412 |
|  | | NCIT:C93413 |
|  | | NCIT:C93414 |
|  | | NCIT:C25297 |
| **Close Mappings:** | | sumo:Message |
|  | | sumo:Packet |
| **Narrow Mappings:** | | CSO:explicit_congestion_notification |
|  | | csrc:Apple_Push_Notification |
|  | | csrc:cryptographic_alarm |
|  | | csrc:Delivery_Status_Notification |
|  | | csrc:information_assurance_vulnerability_alert |
|  | | csrc:Received_Signal_Strength_Indication |
|  | | csrc:Revoked_Key_Notification |
|  | | schema:ConfirmAction |
| **Broad Mappings:** | | sumo:NetworkMessaging |
|  | | sumo:internet_traffic |
|  | | sumo:network_traffic |
|  | | sumo:Signalling |
| **Related Mappings:** | | WIKIDATA:Q7063032 |


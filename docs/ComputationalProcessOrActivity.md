---
parent: Entities
title: testlink:ComputationalProcessOrActivity
grand_parent: Classes
layout: default
---

# Class: ComputationalProcessOrActivity


Either an individual operational activity, or a collection of causally connected operational activities

URI: [testlink:ComputationalProcessOrActivity](https://w3id.org/testlink/vocab/ComputationalProcessOrActivity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OperationalActivity],[Occurrent],[NamedThing],[CyberEntity],[CyberEntity]%3Cenabled%20by%200..%2A-%20[ComputationalProcessOrActivity%7Cid(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[NamedThing]%3Chas%20output%200..%2A-%20[ComputationalProcessOrActivity],[NamedThing]%3Chas%20input%200..%2A-%20[ComputationalProcessOrActivity],[ComputationalProcessOrActivity]uses%20-.-%3E[Occurrent],[ComputationalProcessOrActivity]%5E-[OperationalActivity],[ComputationalEntity]%5E-[ComputationalProcessOrActivity],[ComputationalEntity])

---


## Identifier prefixes

 * CSO
 * csrc

## Parents

 *  is_a: [ComputationalEntity](ComputationalEntity.md)

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity.

## Children

 * [OperationalActivity](OperationalActivity.md) - An execution of a operational function carried out by a servicetype or macrooperational complex.

## Referenced by class

 *  **[CyberEntity](CyberEntity.md)** *[enables](enables.md)*  <sub>0..*</sub>  **[ComputationalProcessOrActivity](ComputationalProcessOrActivity.md)**

## Attributes


### Own

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a cyber entity, where the cyber entity executes the process
    * range: [CyberEntity](CyberEntity.md)
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

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a cyber entity, where the cyber entity executes the process
    * range: [CyberEntity](CyberEntity.md)
    * in subsets: (samples)

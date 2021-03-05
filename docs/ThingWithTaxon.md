---
parent: Class Mixins
title: testlink:ThingWithTaxon
grand_parent: Classes
layout: default
---

# Class: ThingWithTaxon


A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes

URI: [testlink:ThingWithTaxon](https://w3id.org/testlink/vocab/ThingWithTaxon)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon]%3Cin%20taxon%200..%2A-%20[ThingWithTaxon],[OperationalEntity]uses%20-.-%3E[ThingWithTaxon],[DeploymentEntity]uses%20-.-%3E[ThingWithTaxon],[SystemTaxon],[OperationalEntity],[DeploymentEntity])

---


## Mixin for

 * [DeploymentEntity](DeploymentEntity.md) (mixin)  - A process location, serviceunit type or gross deployment part
 * [OperationalEntity](OperationalEntity.md) (mixin)  - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

## Referenced by class


## Attributes


### Own

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (samples)

### Domain for slot:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (samples)

---
parent: Class Mixins
title: testlink:Cluster
grand_parent: Classes
layout: default
---

# Class: Cluster


The cyber combination of two or more operational entities in which the identities are retained and are mixed in the form of solutions,

URI: [testlink:Cluster](https://w3id.org/testlink/vocab/Cluster)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ControlActor],[ControlActor]%3Chas%20control%20actor%200..%2A-%20[Cluster],[ConsumedResource]uses%20-.-%3E[Cluster],[AdministrativeOperation]uses%20-.-%3E[Cluster],[ConsumedResource],[AdministrativeOperation])

---


## Mixin for

 * [AdministrativeOperation](AdministrativeOperation.md) (mixin)  - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
 * [ConsumedResource](ConsumedResource.md) (mixin)  - A control actor (often a cluster) consumed for information, engineering or technical use.

## Referenced by class


## Attributes


### Inherited from application:

 * [has control actor](has_control_actor.md)  <sub>0..*</sub>
    * Description: one or more control actors within a cluster
    * range: [ControlActor](ControlActor.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | CSO:cluster_system |
|  | | csrc:Cluster |
|  | | NCIT:C43418 |
|  | | WIKIDATA:Q21157127 |
| **Narrow Mappings:** | | CSO:cluster_nodes |
|  | | CSO:computing_cluster |
|  | | CSO:heterogeneous_cluster |
|  | | CSO:hpc_cluster |
|  | | CSO:large_cluster |
|  | | WIKIDATA:Q206637 |
|  | | sosa:hosts |
| **Broad Mappings:** | | CSO:cluster_computing |


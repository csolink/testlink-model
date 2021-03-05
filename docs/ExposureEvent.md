---
parent: Class Mixins
title: testlink:ExposureEvent
grand_parent: Classes
layout: default
---

# Class: ExposureEvent


A (possibly time bounded) incidence of a feature of the environment of an system that influences one or more observability of that system, potentially mediated by serviceunits

URI: [testlink:ExposureEvent](https://w3id.org/testlink/vocab/ExposureEvent)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrchestrationExposure]uses%20-.-%3E[ExposureEvent%7Ctimepoint:time_type%20%3F],[OrchestrationExposure])

---


## Mixin for

 * [OrchestrationExposure](OrchestrationExposure.md) (mixin)  - A orchestration exposure is an intake of a particular control actor, other than a administrative operation.

## Referenced by class


## Attributes


### Own

 * [timepoint](timepoint.md)  <sub>OPT</sub>
    * Description: a point in time
    * range: [TimeType](types/TimeType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | exposure |
|  | | experimental condition |
| **Exact Mappings:** | | REPR:ExperimentalCondition |
| **Narrow Mappings:** | | csrc:Threat_Event |
|  | | RO:0002244 |
|  | | sumo:exclusiveEvent |
| **Broad Mappings:** | | schema:event |


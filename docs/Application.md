---
parent: Class Mixins
title: testlink:Application
grand_parent: Classes
layout: default
---

# Class: Application


The cyper combination of one or more components, serviceunits (pod), in which the identities are retained and mixed in the form of solutions,

URI: [testlink:Application](https://w3id.org/testlink/vocab/Application)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ControlActor],[ApplicationToComponentAssociation],[ApplicationToApplicationTypeAssociation],[ApplicationInstanceToApplicationAssociation],[ApplicationConfigurationToApplicationAssociation],[ControlActor]%3Chas%20control%20actor%200..%2A-%20[Application],[ApplicationConfigurationToApplicationAssociation]++-%20object%201..1%3E[Application],[ApplicationInstanceToApplicationAssociation]++-%20object%201..1%3E[Application],[ApplicationToApplicationTypeAssociation]++-%20subject%201..1%3E[Application],[ApplicationToComponentAssociation]++-%20subject%201..1%3E[Application],[Notification]uses%20-.-%3E[Application],[Deployment]uses%20-.-%3E[Application],[ConsumedResource]uses%20-.-%3E[Application],[Component]uses%20-.-%3E[Application],[AdministrativeOperation]uses%20-.-%3E[Application],[Notification],[Deployment],[ConsumedResource],[Component],[AdministrativeOperation])

---


## Mixin for

 * [AdministrativeOperation](AdministrativeOperation.md) (mixin)  - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
 * [Component](Component.md) (mixin)  - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
 * [ConsumedResource](ConsumedResource.md) (mixin)  - A control actor (often a cluster) consumed for information, engineering or technical use.
 * [Deployment](Deployment.md) (mixin) 
 * [Notification](Notification.md) (mixin)  - A event consumed by a healthy system as a source of information

## Referenced by class

 *  **[ApplicationConfigurationToApplicationAssociation](ApplicationConfigurationToApplicationAssociation.md)** *[application configuration to application association➞object](application_configuration_to_application_association_object.md)*  <sub>REQ</sub>  **[Application](Application.md)**
 *  **[ApplicationInstanceToApplicationAssociation](ApplicationInstanceToApplicationAssociation.md)** *[application instance to application association➞object](application_instance_to_application_association_object.md)*  <sub>REQ</sub>  **[Application](Application.md)**
 *  **[ApplicationToApplicationTypeAssociation](ApplicationToApplicationTypeAssociation.md)** *[application to application type association➞subject](application_to_application_type_association_subject.md)*  <sub>REQ</sub>  **[Application](Application.md)**
 *  **[ApplicationToComponentAssociation](ApplicationToComponentAssociation.md)** *[application to component association➞subject](application_to_component_association_subject.md)*  <sub>REQ</sub>  **[Application](Application.md)**

## Attributes


### Own

 * [has control actor](has_control_actor.md)  <sub>0..*</sub>
    * Description: one or more control actors within a cluster
    * range: [ControlActor](ControlActor.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |
| **Exact Mappings:** | | NCIT:C42608 |


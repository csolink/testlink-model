---
parent: Entities
title: testlink:Component
grand_parent: Classes
layout: default
---

# Class: Component


The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.

URI: [testlink:Component](https://w3id.org/testlink/vocab/Component)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[NamedThing],[DeploymentEntity],[ControlActor],[ComponentToVcsRootAssociation],[ComponentOwnerToComponentAssociation],[ComponentConfigurationToComponentAssociation],[ApplicationToComponentAssociation]-%20object%201..1%3E[Component%7Cvcs_location:string%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[ComponentConfigurationToComponentAssociation]-%20object%201..1%3E[Component],[ComponentOwnerToComponentAssociation]-%20object%201..1%3E[Component],[ComponentToVcsRootAssociation]-%20subject%201..1%3E[Component],[Component]uses%20-.-%3E[Application],[DeploymentEntity]%5E-[Component],[Attribute],[ApplicationToComponentAssociation],[Application])

---


## Identifier prefixes

 * LCSH

## Parents

 *  is_a: [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part

## Uses Mixins

 *  mixin: [Application](Application.md) - The cyper combination of one or more components, serviceunits (pod), in which the identities are retained and mixed in the form of solutions,

## Referenced by class

 *  **[ApplicationToComponentAssociation](ApplicationToComponentAssociation.md)** *[application to component association➞object](application_to_component_association_object.md)*  <sub>REQ</sub>  **[Component](Component.md)**
 *  **[ComponentConfigurationToComponentAssociation](ComponentConfigurationToComponentAssociation.md)** *[component configuration to component association➞object](component_configuration_to_component_association_object.md)*  <sub>REQ</sub>  **[Component](Component.md)**
 *  **[ComponentOwnerToComponentAssociation](ComponentOwnerToComponentAssociation.md)** *[component owner to component association➞object](component_owner_to_component_association_object.md)*  <sub>REQ</sub>  **[Component](Component.md)**
 *  **[ComponentToVcsRootAssociation](ComponentToVcsRootAssociation.md)** *[component to vcs root association➞subject](component_to_vcs_root_association_subject.md)*  <sub>REQ</sub>  **[Component](Component.md)**

## Attributes


### Inherited from application:

 * [has control actor](has_control_actor.md)  <sub>0..*</sub>
    * Description: one or more control actors within a cluster
    * range: [ControlActor](ControlActor.md)

### Inherited from build:

 * [updated](updated.md)  <sub>OPT</sub>
    * range: [Date](types/Date.md)
 * [vcs location](vcs_location.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [vcs revision](vcs_revision.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |
| **Exact Mappings:** | | csrc:component |
|  | | NCIT:C48792 |
|  | | prov:component |
|  | | sumo:component |
|  | | WIKIDATA:Q1310239 |
| **Narrow Mappings:** | | CTRL:AnnotatedElement |
|  | | csrc:Authorization_Component |
|  | | csrc:CKMS_component |
|  | | csrc:critical_component |
|  | | csrc:cryptographic_component |
|  | | csrc:Cryptographic_key_component |
|  | | csrc:information_system_component |
|  | | csrc:Key_component |
|  | | csrc:Key_management_components |
|  | | csrc:Root_of_Trust_for_Update_verification_component |
|  | | csrc:SCAP_component |
|  | | csrc:Stream_component |
|  | | csrc:system_component |
|  | | SIO:000171 |
|  | | WIKIDATA:Q11653 |
|  | | WIKIDATA:Q839546 |


---
parent: Other Classes
title: testlink:Attribute
grand_parent: Classes
layout: default
---

# Class: Attribute


A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, resource.

URI: [testlink:Attribute](https://w3id.org/testlink/vocab/Attribute)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemicEntity],[SeverityValue],[QuantityValue],[OntologyClass],[NamedThing],[Homogeneity],[FrequencyValue],[NamedThing]%3Chas%20qualitative%20value%200..1-%20[Attribute%7Cname:label_type%20%3F;iri:iri_type%20%3F;source:label_type%20%3F],[QuantityValue]%3Chas%20quantitative%20value%200..%2A-++[Attribute],[OntologyClass]%3Chas%20attribute%20type%201..1-%20[Attribute],[SystemicEntity]++-%20has%20attribute%200..%2A%3E[Attribute],[Attribute]%5E-[SeverityValue],[Attribute]%5E-[Homogeneity],[Attribute]%5E-[FrequencyValue],[Annotation]%5E-[Attribute],[Annotation])

---


## Identifier prefixes

 * EDAM-DATA
 * EDAM-FORMAT
 * EDAM-OPERATION
 * EDAM-TOPIC

## Parents

 *  is_a: [Annotation](Annotation.md) - testlink Model root class for entity annotations.

## Children

 * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
 * [Homogeneity](Homogeneity.md)
 * [SeverityValue](SeverityValue.md) - describes the severity of a observable feature or error

## Referenced by class

 *  **None** *[has attribute](has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**
 *  **[SystemicEntity](SystemicEntity.md)** *[systemic entity➞has attribute](systemic_entity_has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (samples)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (samples)

### Inherited from configuration:

 * [has part](has_part.md)  <sub>0..*</sub>
    * Description: holds between wholes and their parts (resource entities or processes)
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

### Domain for slot:

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | samples |
| **Exact Mappings:** | | csrc:attribute |
|  | | SIO:000614 |
|  | | sumo:Attribute |
|  | | sumo:attribute |
|  | | WIKIDATA:Q758243 |
| **Close Mappings:** | | SAN:property |
|  | | schema:property |
|  | | ssn:Property |
| **Narrow Mappings:** | | CSO:quantitative_attributes |
|  | | csrc:Application_virtualization |
|  | | csrc:Capability |
|  | | csrc:Capability_Anomalous_Event_Detection_Management |
|  | | csrc:Capability_Anomalous_Event_Response_and_Recovery_Management |
|  | | csrc:Capability_Behavior_Management |
|  | | csrc:Capability_Boundary_Management |
|  | | csrc:Capability_Configuration_Settings_Management |
|  | | csrc:Capability_Credentials_and_Authentication_Management |
|  | | csrc:Capability_Event_Preparation_Management |
|  | | csrc:Capability_Hardware_Asset_Management |
|  | | csrc:Capability_ISCM |
|  | | csrc:Capability_Manage_and_Assess_Risk |
|  | | csrc:Capability_Perform_Resilient_Systems_Engineering |
|  | | csrc:Capability_Privilege_and_Account_Management |
|  | | csrc:Capability_Software_Asset_Management |
|  | | csrc:Capability_Trust_Management |
|  | | csrc:Capability_Vulnerability_Management |
|  | | CSO:release_date |
|  | | csrc:security_attribute |
|  | | dwc:identificationQualifier |
|  | | dwc:typeStatus |
|  | | dwc:usewithiri |
|  | | gr:UnitPriceSpecification |
|  | | PATO:0000001 |
|  | | SAN:impactedProperty |
|  | | sumo:TimeMeasure |
|  | | schema:releaseDate |
|  | | schema:Softwareapplication |
|  | | sosa:actsOnProperty |
|  | | sosa:ActuatableProperty |
|  | | sosa:DateTime |
|  | | sosa:FeatureOfInterest |
|  | | sosa:implementedBy |
|  | | sosa:ObservableProperty |
|  | | sosa:observedProperty |
|  | | ssn:Stimulus |
|  | | ssn:detects |
|  | | ssn:MeasurementProperty |
|  | | ssn:OperatingProperty |
|  | | ssn:SurvivalProperty |
|  | | sumo:criticalityLevel |
|  | | sumo:duration |
|  | | sumo:deviceAccount |
|  | | sumo:deviceOS |
|  | | sumo:DeviceClosed |
|  | | sumo:deviceState |
|  | | sumo:DeviceDamaged |
|  | | sumo:DeviceOff |
|  | | sumo:DeviceOn |
|  | | sumo:DeviceOff |
|  | | sumo:DeviceOpen |
|  | | sumo:DeviceStateAttribute |
|  | | sumo:FormOfAdaptationAttribute |
|  | | sumo:greaterThan |
|  | | sumo:greaterThanOrEqualTo |
|  | | sumo:lessThan |
|  | | sumo:lessThanOrEqualTo |
|  | | sumo:load |
|  | | sumo:most |
|  | | sumo:magneticVariation |
|  | | sumo:onboard |
|  | | sumo:providesDestination |
|  | | sumo:publishes |
|  | | sumo:validityPeriod |
|  | | sumo:VirtualAddress |


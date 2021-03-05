---
parent: Other Classes
title: testlink:QuantityValue
grand_parent: Classes
layout: default
---

# Class: QuantityValue


A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric value

URI: [testlink:QuantityValue](https://w3id.org/testlink/vocab/QuantityValue)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]++-%20has%20quantitative%20value%200..%2A%3E[QuantityValue%7Chas_unit:unit%20%3F;has_numeric_value:double%20%3F],[Configuration]++-%20has%20quantitative%20value%200..%2A%3E[QuantityValue],[Annotation]%5E-[QuantityValue],[NamedThing],[Configuration],[Attribute],[Annotation])

---


## Parents

 *  is_a: [Annotation](Annotation.md) - testlink Model root class for entity annotations.

## Referenced by class

 *  **[Attribute](Attribute.md)** *[has quantitative value](has_quantitative_value.md)*  <sub>0..*</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[NamedThing](NamedThing.md)** *[value](value.md)*  <sub>OPT</sub>  **[QuantityValue](QuantityValue.md)**

## Attributes


### Own

 * [has numeric value](has_numeric_value.md)  <sub>OPT</sub>
    * Description: connects a quantity value to a number
    * range: [Double](types/Double.md)
    * in subsets: (samples)
 * [has unit](has_unit.md)  <sub>OPT</sub>
    * Description: connects a quantity value to a unit
    * range: [Unit](types/Unit.md)
    * in subsets: (samples)

### Domain for slot:

 * [has numeric value](has_numeric_value.md)  <sub>OPT</sub>
    * Description: connects a quantity value to a number
    * range: [Double](types/Double.md)
    * in subsets: (samples)
 * [has unit](has_unit.md)  <sub>OPT</sub>
    * Description: connects a quantity value to a unit
    * range: [Unit](types/Unit.md)
    * in subsets: (samples)

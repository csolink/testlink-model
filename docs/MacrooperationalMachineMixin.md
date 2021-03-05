---
parent: Class Mixins
title: testlink:MacrooperationalMachineMixin
grand_parent: Classes
layout: default
---

# Class: MacrooperationalMachineMixin


A union of componentservice, servicetype, and macrooperational complex. These are the basic units of function in a component. They either carry out individual computational activities, or they encode tasks which do this.

URI: [testlink:MacrooperationalMachineMixin](https://w3id.org/testlink/vocab/MacrooperationalMachineMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OperationalActivity],[OperationalActivity]++-%20enabled%20by%200..%2A%3E[MacrooperationalMachineMixin%7Cname:symbol_type%20%3F])

---


## Referenced by class

 *  **[OperationalActivity](OperationalActivity.md)** *[operational activity➞enabled by](operational_activity_enabled_by.md)*  <sub>0..*</sub>  **[MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)**

## Attributes


### Own

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Domain for slot:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

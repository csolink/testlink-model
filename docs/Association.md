---
parent: Associations
title: testlink:Association
grand_parent: Classes
layout: default
---

# Class: Association


A typed association between two entities, supported by evidence

URI: [testlink:Association](https://w3id.org/testlink/vocab/Association)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ServerHubToServerGroupHubAssociation],[ServerHubToServerAssociation],[ServerGroupToServerTypeAssociation],[ServerGroupHubToServerGroupAssociation],[ServerGroupHubToDomainEnvironmentAssociation],[RealmConfigurationToRealmAssociation],[RealmConfigurationToDomainEnvironmentAssociation],[Publication],[OntologyClass],[NamedThing],[EnvironmentConfigurationToEnvironmentAssociation],[Entity],[EmailToApplicationUserAssociation],[DomainEnvironmentToEnvironmentAssociation],[DomainEnvironmentToDomainAssociation],[DomainConfigurationToDomainEnvironmentAssociation],[DeploymentToBuildAssociation],[DeploymentToApplicationUserLoginAssociation],[DeploymentConfigurationToDeploymentAssociation],[ComponentToVcsRootAssociation],[ComponentOwnerToComponentAssociation],[ComponentOwnerToApplicationUserAssociation],[ComponentConfigurationToComponentAssociation],[BuildToVcsRootAssociation],[BuildToProjectAssociation],[BuildToApplicationUserLoginAssociation],[BuildToApplicationInstanceAssociation],[BuildConfigurationToBuildAssociation],[Association]%3Ccategory%201..%2A-%20[Association%7Cpredicate:predicate_type;negated:boolean%20%3F;relation:uriorcurie;type:string%20%3F;id(i):string;name(i):label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[Publication]%3Cpublications%200..%2A-%20[Association],[OntologyClass]%3Cqualifiers%200..%2A-%20[Association],[NamedThing]%3Cobject%201..1-%20[Association],[NamedThing]%3Csubject%201..1-%20[Association],[Association]%5E-[ServerHubToServerGroupHubAssociation],[Association]%5E-[ServerHubToServerAssociation],[Association]%5E-[ServerGroupToServerTypeAssociation],[Association]%5E-[ServerGroupHubToServerGroupAssociation],[Association]%5E-[ServerGroupHubToDomainEnvironmentAssociation],[Association]%5E-[RealmConfigurationToRealmAssociation],[Association]%5E-[RealmConfigurationToDomainEnvironmentAssociation],[Association]%5E-[EnvironmentConfigurationToEnvironmentAssociation],[Association]%5E-[EmailToApplicationUserAssociation],[Association]%5E-[DomainEnvironmentToEnvironmentAssociation],[Association]%5E-[DomainEnvironmentToDomainAssociation],[Association]%5E-[DomainConfigurationToDomainEnvironmentAssociation],[Association]%5E-[DeploymentToBuildAssociation],[Association]%5E-[DeploymentToApplicationUserLoginAssociation],[Association]%5E-[DeploymentConfigurationToDeploymentAssociation],[Association]%5E-[ComponentToVcsRootAssociation],[Association]%5E-[ComponentOwnerToComponentAssociation],[Association]%5E-[ComponentOwnerToApplicationUserAssociation],[Association]%5E-[ComponentConfigurationToComponentAssociation],[Association]%5E-[BuildToVcsRootAssociation],[Association]%5E-[BuildToProjectAssociation],[Association]%5E-[BuildToApplicationUserLoginAssociation],[Association]%5E-[BuildToApplicationInstanceAssociation],[Association]%5E-[BuildConfigurationToBuildAssociation],[Association]%5E-[ApplicationUserLoginToApplicationUserAssociation],[Association]%5E-[ApplicationToComponentAssociation],[Association]%5E-[ApplicationToApplicationTypeAssociation],[Association]%5E-[ApplicationInstanceToServerGroupHubAssociation],[Association]%5E-[ApplicationInstanceToRealmAssociation],[Association]%5E-[ApplicationInstanceToDomainEnvironmentAssociation],[Association]%5E-[ApplicationInstanceToApplicationAssociation],[Association]%5E-[ApplicationInstanceConfigurationToApplicationInstanceAssociation],[Association]%5E-[ApplicationConfigurationToApplicationAssociation],[Entity]%5E-[Association],[ApplicationUserLoginToApplicationUserAssociation],[ApplicationToComponentAssociation],[ApplicationToApplicationTypeAssociation],[ApplicationInstanceToServerGroupHubAssociation],[ApplicationInstanceToRealmAssociation],[ApplicationInstanceToDomainEnvironmentAssociation],[ApplicationInstanceToApplicationAssociation],[ApplicationInstanceConfigurationToApplicationInstanceAssociation],[ApplicationConfigurationToApplicationAssociation])

---


## Parents

 *  is_a: [Entity](Entity.md) - Root testlink Model class for all things and informational relationships, real or imagined.

## Children

 * [ApplicationConfigurationToApplicationAssociation](ApplicationConfigurationToApplicationAssociation.md) - Any association between a application configuration and a application. There is no assumption of cardinality
 * [ApplicationInstanceConfigurationToApplicationInstanceAssociation](ApplicationInstanceConfigurationToApplicationInstanceAssociation.md) - Any association between a application instance configuration and a application instance. There is no assumption of cardinality
 * [ApplicationInstanceToApplicationAssociation](ApplicationInstanceToApplicationAssociation.md) - Any association between a application instance and a application. There is no assumption of cardinality
 * [ApplicationInstanceToDomainEnvironmentAssociation](ApplicationInstanceToDomainEnvironmentAssociation.md) - Any association between a application instance and a domain environment. There is no assumption of cardinality
 * [ApplicationInstanceToRealmAssociation](ApplicationInstanceToRealmAssociation.md) - Any association between a application instance and a realm. There is no assumption of cardinality
 * [ApplicationInstanceToServerGroupHubAssociation](ApplicationInstanceToServerGroupHubAssociation.md) - Any association between a application instance and a server group hub. There is no assumption of cardinality
 * [ApplicationToApplicationTypeAssociation](ApplicationToApplicationTypeAssociation.md) - Any association between a application and a application type. There is no assumption of cardinality
 * [ApplicationToComponentAssociation](ApplicationToComponentAssociation.md) - Any association between a application and a component. There is no assumption of cardinality
 * [ApplicationUserLoginToApplicationUserAssociation](ApplicationUserLoginToApplicationUserAssociation.md) - Any association between a application user login and a application user. There is no assumption of cardinality
 * [BuildConfigurationToBuildAssociation](BuildConfigurationToBuildAssociation.md) - Any association between a build configuration and a build. There is no assumption of cardinality
 * [BuildToApplicationInstanceAssociation](BuildToApplicationInstanceAssociation.md) - Any association between a build and a application instance. There is no assumption of cardinality
 * [BuildToApplicationUserLoginAssociation](BuildToApplicationUserLoginAssociation.md) - Any association between a build and a application user login. There is no assumption of cardinality
 * [BuildToProjectAssociation](BuildToProjectAssociation.md) - Any association between a build and a project. There is no assumption of cardinality
 * [BuildToVcsRootAssociation](BuildToVcsRootAssociation.md) - Any association between a build and a vcs root. There is no assumption of cardinality
 * [ComponentConfigurationToComponentAssociation](ComponentConfigurationToComponentAssociation.md) - Any association between a component configuration and a component. There is no assumption of cardinality
 * [ComponentOwnerToApplicationUserAssociation](ComponentOwnerToApplicationUserAssociation.md) - Any association between a component owner and a application user. There is no assumption of cardinality
 * [ComponentOwnerToComponentAssociation](ComponentOwnerToComponentAssociation.md) - Any association between a component owner and a component. There is no assumption of cardinality
 * [ComponentToVcsRootAssociation](ComponentToVcsRootAssociation.md) - Any association between a component and a vcs root. There is no assumption of cardinality
 * [DeploymentConfigurationToDeploymentAssociation](DeploymentConfigurationToDeploymentAssociation.md) - Any association between a deployment configuration and a deployment. There is no assumption of cardinality
 * [DeploymentToApplicationUserLoginAssociation](DeploymentToApplicationUserLoginAssociation.md) - Any association between a deployment and a application user login. There is no assumption of cardinality
 * [DeploymentToBuildAssociation](DeploymentToBuildAssociation.md) - Any association between a deployment and a build. There is no assumption of cardinality
 * [DomainConfigurationToDomainEnvironmentAssociation](DomainConfigurationToDomainEnvironmentAssociation.md) - Any association between a domain configuration and a domain environment. There is no assumption of cardinality
 * [DomainEnvironmentToDomainAssociation](DomainEnvironmentToDomainAssociation.md) - Any association between a domain environment and a domain. There is no assumption of cardinality
 * [DomainEnvironmentToEnvironmentAssociation](DomainEnvironmentToEnvironmentAssociation.md) - Any association between a domain environment and a environment. There is no assumption of cardinality
 * [EmailToApplicationUserAssociation](EmailToApplicationUserAssociation.md) - Any association between a email and a application user. There is no assumption of cardinality
 * [EnvironmentConfigurationToEnvironmentAssociation](EnvironmentConfigurationToEnvironmentAssociation.md) - Any association between a environment configuration and a environment. There is no assumption of cardinality
 * [RealmConfigurationToDomainEnvironmentAssociation](RealmConfigurationToDomainEnvironmentAssociation.md) - Any association between a realm configuration and a domain environment. There is no assumption of cardinality
 * [RealmConfigurationToRealmAssociation](RealmConfigurationToRealmAssociation.md) - Any association between a realm configuration and a realm. There is no assumption of cardinality
 * [ServerGroupHubToDomainEnvironmentAssociation](ServerGroupHubToDomainEnvironmentAssociation.md) - Any association between a server group hub and a domain environment. There is no assumption of cardinality
 * [ServerGroupHubToServerGroupAssociation](ServerGroupHubToServerGroupAssociation.md) - Any association between a server group hub and a server group. There is no assumption of cardinality
 * [ServerGroupToServerTypeAssociation](ServerGroupToServerTypeAssociation.md) - Any association between a server group and a server type. There is no assumption of cardinality
 * [ServerHubToServerAssociation](ServerHubToServerAssociation.md) - Any association between a server hub and a server. There is no assumption of cardinality
 * [ServerHubToServerGroupHubAssociation](ServerHubToServerGroupHubAssociation.md) - Any association between a server hub and a server group hub. There is no assumption of cardinality

## Referenced by class

 *  **[Association](Association.md)** *[association➞category](association_category.md)*  <sub>1..*</sub>  **[Association](Association.md)**

## Attributes


### Own

 * [association➞category](association_category.md)  <sub>1..*</sub>
    * range: [Association](Association.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of testlink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)

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

### Domain for slot:

 * [association➞category](association_category.md)  <sub>1..*</sub>
    * range: [Association](Association.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of testlink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | csrc:Association |
|  | | rdf:Statement |
|  | | owl:Axiom |
| **Narrow Mappings:** | | CSO:data_association |
|  | | MAID:117220453 |
|  | | MAID:79714647 |
|  | | WIKIDATA:Q382571 |
| **Broad Mappings:** | | WIKIDATA:Q186290 |


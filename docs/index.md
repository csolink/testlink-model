---
title: Browse Organization
has_children: true
nav_order: 2
layout: default
has_toc: false
---




## Classes


### Entities


### Associations


### Class Mixins

 * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral healthy, organization or mechanical actor in the world
 * [ApexInventoryArchive](ApexInventoryArchive.md)
 * [Application](Application.md) - The cyper combination of one or more components, serviceunits (pod), in which the identities are retained and mixed in the form of solutions,
 * [ApplicationConfiguration](ApplicationConfiguration.md)
 * [ApplicationInstanceConfiguration](ApplicationInstanceConfiguration.md)
 * [BuildConfiguration](BuildConfiguration.md)
 * [Cluster](Cluster.md) - The cyber combination of two or more operational entities in which the identities are retained and are mixed in the form of solutions,
 * [ComponentConfiguration](ComponentConfiguration.md)
 * [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.
 * [CyberEssenceOrOccurrent](CyberEssenceOrOccurrent.md) - Either a cyber or processual entity.
    * [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.
    * [Occurrent](Occurrent.md) - A processual entity.
       * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral healthy, organization or mechanical actor in the world
 * [DeploymentConfiguration](DeploymentConfiguration.md)
 * [DistributionLevel](DistributionLevel.md)
 * [DomainConfiguration](DomainConfiguration.md)
 * [DomainEnvironment](DomainEnvironment.md)
 * [EnvironmentConfiguration](EnvironmentConfiguration.md)
 * [Event](Event.md) - An exposure event
 * [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an system that influences one or more observability of that system, potentially mediated by serviceunits
 * [MacrooperationalMachineMixin](MacrooperationalMachineMixin.md) - A union of componentservice, servicetype, and macrooperational complex. These are the basic units of function in a component. They either carry out individual computational activities, or they encode tasks which do this.
 * [RealmConfiguration](RealmConfiguration.md)
 * [ServerGroupHub](ServerGroupHub.md)
 * [ServerHub](ServerHub.md)
 * [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes

### Other Classes

 * [Activity](Activity.md) - An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
 * [AdministrativeEntity](AdministrativeEntity.md)
    * [Agent](Agent.md) - service, group, organization or project that provides a piece of information (i.e. a knowledge association)
    * [ApplicationUser](ApplicationUser.md)
    * [ApplicationUserLogin](ApplicationUserLogin.md)
    * [ComponentOwner](ComponentOwner.md)
    * [Domain](Domain.md)
    * [Email](Email.md) - A text string identifier location for e-mail delivery.
    * [Hub](Hub.md)
       * [ServerGroupHub](ServerGroupHub.md)
       * [ServerHub](ServerHub.md)
    * [Project](Project.md)
    * [Realm](Realm.md)
    * [VcsRoot](VcsRoot.md)
 * [AdministrativeOperation](AdministrativeOperation.md) - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
 * [Annotation](Annotation.md) - testlink Model root class for entity annotations.
    * [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, resource.
       * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
       * [Homogeneity](Homogeneity.md)
       * [SeverityValue](SeverityValue.md) - describes the severity of a observable feature or error
    * [QuantityValue](QuantityValue.md) - A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric value
 * [ApplicationConfigurationToApplicationAssociation](ApplicationConfigurationToApplicationAssociation.md) - Any association between a application configuration and a application. There is no assumption of cardinality
 * [ApplicationInstance](ApplicationInstance.md) - The unit of service workload the component is capable of providing or protecting.
 * [ApplicationInstanceConfigurationToApplicationInstanceAssociation](ApplicationInstanceConfigurationToApplicationInstanceAssociation.md) - Any association between a application instance configuration and a application instance. There is no assumption of cardinality
 * [ApplicationInstanceToApplicationAssociation](ApplicationInstanceToApplicationAssociation.md) - Any association between a application instance and a application. There is no assumption of cardinality
 * [ApplicationInstanceToDomainEnvironmentAssociation](ApplicationInstanceToDomainEnvironmentAssociation.md) - Any association between a application instance and a domain environment. There is no assumption of cardinality
 * [ApplicationInstanceToRealmAssociation](ApplicationInstanceToRealmAssociation.md) - Any association between a application instance and a realm. There is no assumption of cardinality
 * [ApplicationInstanceToServerGroupHubAssociation](ApplicationInstanceToServerGroupHubAssociation.md) - Any association between a application instance and a server group hub. There is no assumption of cardinality
 * [ApplicationToApplicationTypeAssociation](ApplicationToApplicationTypeAssociation.md) - Any association between a application and a application type. There is no assumption of cardinality
 * [ApplicationToComponentAssociation](ApplicationToComponentAssociation.md) - Any association between a application and a component. There is no assumption of cardinality
 * [ApplicationType](ApplicationType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
 * [ApplicationUserLoginToApplicationUserAssociation](ApplicationUserLoginToApplicationUserAssociation.md) - Any association between a application user login and a application user. There is no assumption of cardinality
 * [Archive](Archive.md)
    * [ApexInventoryArchive](ApexInventoryArchive.md)
 * [Association](Association.md) - A typed association between two entities, supported by evidence
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
 * [AttributeType](AttributeType.md) - A property or characteristic type of an entity. For example, an apple may have properties types such as color type, shape type, age type, crispiness type.
 * [Build](Build.md)
 * [Component](Component.md) - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
 * [ComponentType](ComponentType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
 * [ComputationalEntity](ComputationalEntity.md)
    * [ComputationalProcessOrActivity](ComputationalProcessOrActivity.md) - Either an individual operational activity, or a collection of causally connected operational activities
       * [OperationalActivity](OperationalActivity.md) - An execution of a operational function carried out by a servicetype or macrooperational complex.
    * [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
       * [AdministrativeOperation](AdministrativeOperation.md) - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
       * [ControlActor](ControlActor.md) - May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part
          * [ConsumedResource](ConsumedResource.md) - A control actor (often a cluster) consumed for information, engineering or technical use.
          * [NotificationComponent](NotificationComponent.md)
             * [Data](Data.md)
          * [OrchestrationExposure](OrchestrationExposure.md) - A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
       * [Notification](Notification.md) - A event consumed by a healthy system as a source of information
       * [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)
          * [ApplicationInstance](ApplicationInstance.md) - The unit of service workload the component is capable of providing or protecting.
          * [ServerGroup](ServerGroup.md) - An group of servers
          * [Workload](Workload.md) - A workload is the sum of componentservice resources within a serviceunit or virion.
    * [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities
       * [ApplicationType](ApplicationType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
       * [ComponentType](ComponentType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
       * [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part
          * [Component](Component.md) - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
          * [Deployment](Deployment.md)
       * [ServerType](ServerType.md) - A type of server
 * [Configuration](Configuration.md) - Configuration is the manner in which components are arranged to make up the computer system. Configuration consists of both hardware and software components.
    * [ApplicationConfiguration](ApplicationConfiguration.md)
    * [ApplicationInstanceConfiguration](ApplicationInstanceConfiguration.md)
    * [BuildConfiguration](BuildConfiguration.md)
    * [ComponentConfiguration](ComponentConfiguration.md)
    * [DeploymentConfiguration](DeploymentConfiguration.md)
    * [DomainConfiguration](DomainConfiguration.md)
    * [EnvironmentConfiguration](EnvironmentConfiguration.md)
    * [RealmConfiguration](RealmConfiguration.md)
 * [CyberEntity](CyberEntity.md) - An entity that has digital reality (a.k.a. cyber essence).
 * [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.
    * [Archive](Archive.md)
       * [ApexInventoryArchive](ApexInventoryArchive.md)
    * [Build](Build.md)
    * [DatasetVersion](DatasetVersion.md)
       * [DistributionLevel](DistributionLevel.md)
    * [Inventory](Inventory.md)
 * [DatasetDistribution](DatasetDistribution.md) - an item that holds distribution level information about a dataset.
 * [Entity](Entity.md) - Root testlink Model class for all things and informational relationships, real or imagined.
    * [Association](Association.md) - A typed association between two entities, supported by evidence
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
    * [NamedThing](NamedThing.md) - a databased entity or concept/class
       * [Activity](Activity.md) - An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
       * [AdministrativeEntity](AdministrativeEntity.md)
          * [Agent](Agent.md) - service, group, organization or project that provides a piece of information (i.e. a knowledge association)
          * [ApplicationUser](ApplicationUser.md)
          * [ApplicationUserLogin](ApplicationUserLogin.md)
          * [ComponentOwner](ComponentOwner.md)
          * [Domain](Domain.md)
          * [Email](Email.md) - A text string identifier location for e-mail delivery.
          * [Hub](Hub.md)
             * [ServerGroupHub](ServerGroupHub.md)
             * [ServerHub](ServerHub.md)
          * [Project](Project.md)
          * [Realm](Realm.md)
          * [VcsRoot](VcsRoot.md)
       * [ComputationalEntity](ComputationalEntity.md)
          * [ComputationalProcessOrActivity](ComputationalProcessOrActivity.md) - Either an individual operational activity, or a collection of causally connected operational activities
             * [OperationalActivity](OperationalActivity.md) - An execution of a operational function carried out by a servicetype or macrooperational complex.
          * [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
             * [AdministrativeOperation](AdministrativeOperation.md) - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
             * [ControlActor](ControlActor.md) - May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part
                * [ConsumedResource](ConsumedResource.md) - A control actor (often a cluster) consumed for information, engineering or technical use.
                * [NotificationComponent](NotificationComponent.md)
                   * [Data](Data.md)
                * [OrchestrationExposure](OrchestrationExposure.md) - A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
             * [Notification](Notification.md) - A event consumed by a healthy system as a source of information
             * [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)
                * [ApplicationInstance](ApplicationInstance.md) - The unit of service workload the component is capable of providing or protecting.
                * [ServerGroup](ServerGroup.md) - An group of servers
                * [Workload](Workload.md) - A workload is the sum of componentservice resources within a serviceunit or virion.
          * [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities
             * [ApplicationType](ApplicationType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
             * [ComponentType](ComponentType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
             * [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part
                * [Component](Component.md) - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
                * [Deployment](Deployment.md)
             * [ServerType](ServerType.md) - A type of server
       * [CyberEntity](CyberEntity.md) - An entity that has digital reality (a.k.a. cyber essence).
       * [Environment](Environment.md) - An environment
          * [DomainEnvironment](DomainEnvironment.md)
       * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.
          * [Configuration](Configuration.md) - Configuration is the manner in which components are arranged to make up the computer system. Configuration consists of both hardware and software components.
             * [ApplicationConfiguration](ApplicationConfiguration.md)
             * [ApplicationInstanceConfiguration](ApplicationInstanceConfiguration.md)
             * [BuildConfiguration](BuildConfiguration.md)
             * [ComponentConfiguration](ComponentConfiguration.md)
             * [DeploymentConfiguration](DeploymentConfiguration.md)
             * [DomainConfiguration](DomainConfiguration.md)
             * [EnvironmentConfiguration](EnvironmentConfiguration.md)
             * [RealmConfiguration](RealmConfiguration.md)
          * [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.
             * [Archive](Archive.md)
                * [ApexInventoryArchive](ApexInventoryArchive.md)
             * [Build](Build.md)
             * [DatasetVersion](DatasetVersion.md)
                * [DistributionLevel](DistributionLevel.md)
             * [Inventory](Inventory.md)
          * [DatasetDistribution](DatasetDistribution.md) - an item that holds distribution level information about a dataset.
          * [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed resources, either directly or in one of the Publication testlink category subclasses.
       * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
          * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
          * [SystemTaxon](SystemTaxon.md) - A classification of a set of systems.
          * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
       * [Server](Server.md) - A piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called "clients"

## Slots


### Predicates

 * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
 * [contributor](contributor.md)
    * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
 * [data of](data_of.md)
 * [enabled by](enabled_by.md) - holds between a process and a cyber entity, where the cyber entity executes the process
 * [enables](enables.md) - holds between a cyber entity and a process, where the cyber entity executes the process
 * [has data](has_data.md) - one or more datas which are growth factors for a system
 * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
 * [has notification component](has_notification_component.md) - holds between notification and one or more control actors composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
    * [has data](has_data.md) - one or more datas which are growth factors for a system
 * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
 * [has part](has_part.md) - holds between wholes and their parts (resource entities or processes)
    * [has notification component](has_notification_component.md) - holds between notification and one or more control actors composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
       * [has data](has_data.md) - one or more datas which are growth factors for a system
 * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
    * [enabled by](enabled_by.md) - holds between a process and a cyber entity, where the cyber entity executes the process
    * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
    * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
 * [in taxon](in_taxon.md) - connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
 * [interacts with](interacts_with.md) - holds between any two entities that directly or indirectly interact with each other
 * [notification component of](notification_component_of.md) - holds between a one or more control actors present in notification, irrespective of nutritional value (i.e. could also be a contaminant or additive)
    * [data of](data_of.md)
 * [overlaps](overlaps.md) - holds between entities that overlap in their extents (resources or processes)
    * [has part](has_part.md) - holds between wholes and their parts (resource entities or processes)
       * [has notification component](has_notification_component.md) - holds between notification and one or more control actors composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
          * [has data](has_data.md) - one or more datas which are growth factors for a system
    * [part of](part_of.md) - holds between parts and wholes (resource entities or processes)
       * [notification component of](notification_component_of.md) - holds between a one or more control actors present in notification, irrespective of nutritional value (i.e. could also be a contaminant or additive)
          * [data of](data_of.md)
 * [part of](part_of.md) - holds between parts and wholes (resource entities or processes)
    * [notification component of](notification_component_of.md) - holds between a one or more control actors present in notification, irrespective of nutritional value (i.e. could also be a contaminant or additive)
       * [data of](data_of.md)
 * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
    * [enables](enables.md) - holds between a cyber entity and a process, where the cyber entity executes the process
 * [produced by](produced_by.md)
 * [produces](produces.md) - holds between a resource entity and a servicetype that is generated through the intentional actions or functioning of the resource entity
 * [related to](related_to.md) - A relationship that is asserted between two named things
    * [contributor](contributor.md)
       * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
    * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
       * [enabled by](enabled_by.md) - holds between a process and a cyber entity, where the cyber entity executes the process
       * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
       * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
    * [in taxon](in_taxon.md) - connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * [interacts with](interacts_with.md) - holds between any two entities that directly or indirectly interact with each other
    * [overlaps](overlaps.md) - holds between entities that overlap in their extents (resources or processes)
       * [has part](has_part.md) - holds between wholes and their parts (resource entities or processes)
          * [has notification component](has_notification_component.md) - holds between notification and one or more control actors composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
             * [has data](has_data.md) - one or more datas which are growth factors for a system
       * [part of](part_of.md) - holds between parts and wholes (resource entities or processes)
          * [notification component of](notification_component_of.md) - holds between a one or more control actors present in notification, irrespective of nutritional value (i.e. could also be a contaminant or additive)
             * [data of](data_of.md)
    * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
       * [enables](enables.md) - holds between a cyber entity and a process, where the cyber entity executes the process
    * [produced by](produced_by.md)
    * [produces](produces.md) - holds between a resource entity and a servicetype that is generated through the intentional actions or functioning of the resource entity

### Node Properties

 * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
    * [location](location.md)
       * [vcs location](vcs_location.md)
 * [affiliation](affiliation.md) - a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
 * [archived](archived.md)
 * [authors](authors.md) - connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in csolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
 * [created](created.md)
 * [creation date](creation_date.md) - date on which an entity was created. This can be applied to nodes or edges
    * [created](created.md)
    * [release date](release_date.md)
 * [dataset download url](dataset_download_url.md)
 * [distribution download url](distribution_download_url.md)
 * [download url](download_url.md)
 * [enabled](enabled.md)
 * [first name](first_name.md)
 * [format](format.md)
 * [global version](global_version.md)
 * [has computational sequence](has_computational_sequence.md) - connects a service feature to its sequence of computation
 * [has control actor](has_control_actor.md) - one or more control actors within a cluster
 * [has dataset](has_dataset.md)
 * [has distribution](has_distribution.md)
 * [has homogeneity](has_homogeneity.md)
 * [ingest date](ingest_date.md)
 * [internal version](internal_version.md)
    * [vcs revision](vcs_revision.md)
 * [keywords](keywords.md) - keywords tagging a publication
 * [last name](last_name.md)
 * [lcsh terms](lcsh_terms.md) - lcsh terms tagging a publication
 * [license](license.md)
 * [location](location.md)
    * [vcs location](vcs_location.md)
 * [login](login.md)
    * [user login](user_login.md)
 * [node property](node_property.md) - A grouping for any property that holds between a node and a value
    * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
       * [location](location.md)
          * [vcs location](vcs_location.md)
    * [affiliation](affiliation.md) - a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
    * [archived](archived.md)
    * [authors](authors.md) - connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in csolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
    * [creation date](creation_date.md) - date on which an entity was created. This can be applied to nodes or edges
       * [created](created.md)
       * [release date](release_date.md)
    * [dataset download url](dataset_download_url.md)
    * [distribution download url](distribution_download_url.md)
    * [download url](download_url.md)
    * [enabled](enabled.md)
    * [first name](first_name.md)
    * [format](format.md)
    * [has computational sequence](has_computational_sequence.md) - connects a service feature to its sequence of computation
    * [has control actor](has_control_actor.md) - one or more control actors within a cluster
    * [has dataset](has_dataset.md)
    * [has distribution](has_distribution.md)
    * [has homogeneity](has_homogeneity.md)
    * [ingest date](ingest_date.md)
    * [keywords](keywords.md) - keywords tagging a publication
    * [last name](last_name.md)
    * [lcsh terms](lcsh_terms.md) - lcsh terms tagging a publication
    * [license](license.md)
    * [login](login.md)
       * [user login](user_login.md)
    * [note](note.md)
    * [pages](pages.md) - page number of source referenced for statement or publication
    * [rights](rights.md)
    * [summary](summary.md) - executive  summary of a publication
    * [timepoint](timepoint.md) - a point in time
    * [update date](update_date.md) - date on which an entity was migrated. This can be applied to nodes or edges
       * [updated](updated.md)
    * [value](value.md)
    * [version](version.md)
       * [global version](global_version.md)
       * [internal version](internal_version.md)
          * [vcs revision](vcs_revision.md)
    * [xref](xref.md) - Alternate CURIEs for a thing
 * [note](note.md)
 * [pages](pages.md) - page number of source referenced for statement or publication
 * [release date](release_date.md)
 * [rights](rights.md)
 * [summary](summary.md) - executive  summary of a publication
 * [timepoint](timepoint.md) - a point in time
 * [update date](update_date.md) - date on which an entity was migrated. This can be applied to nodes or edges
    * [updated](updated.md)
 * [updated](updated.md)
 * [user login](user_login.md)
 * [value](value.md)
 * [vcs location](vcs_location.md)
 * [vcs revision](vcs_revision.md)
 * [version](version.md)
    * [global version](global_version.md)
    * [internal version](internal_version.md)
       * [vcs revision](vcs_revision.md)
 * [xref](xref.md) - Alternate CURIEs for a thing

### Edge Properties

 * [association slot](association_slot.md) - any slot that relates an association to another entity
    * [association type](association_type.md) - connects an association to the category of association (e.g. componentservice to observability)
    * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a observable association to state how frequent the observability is observed in the subject
    * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
    * [object](object.md) - connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * [predicate](predicate.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * [provided by](provided_by.md) - connects an association to the agent (service, organization or group) that provided it
    * [publications](publications.md) - connects an association to publications supporting the association
    * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
    * [relation](relation.md) - The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * [severity qualifier](severity_qualifier.md) - a qualifier used in a observable association to state how severe the observability is in the subject
    * [subject](subject.md) - connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
 * [association type](association_type.md) - connects an association to the category of association (e.g. componentservice to observability)
 * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a observable association to state how frequent the observability is observed in the subject
 * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
 * [object](object.md) - connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
 * [predicate](predicate.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
 * [provided by](provided_by.md) - connects an association to the agent (service, organization or group) that provided it
 * [publications](publications.md) - connects an association to publications supporting the association
 * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
 * [relation](relation.md) - The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
 * [severity qualifier](severity_qualifier.md) - a qualifier used in a observable association to state how severe the observability is in the subject
 * [subject](subject.md) - connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.

### Slot Mixins

 * [application user login](application_user_login.md)

### Other Slots

 * [application id](application_id.md)
 * [application instance id](application_instance_id.md)
 * [application user id](application_user_id.md)
 * [application user login id](application_user_login_id.md)
 * [build number](build_number.md)
    * [production build number](production_build_number.md)
 * [category](category.md) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the csolink entity type class.
 * [component fixed](component_fixed.md)
 * [component id](component_id.md)
 * [description](description.md) - a human-readable description of an entity
 * [domain name](domain_name.md)
 * [environment id](environment_id.md)
 * [fqdn](fqdn.md)
 * [g c number](g_c_number.md)
 * [has attribute](has_attribute.md) - connects any entity to an attribute
 * [has attribute type](has_attribute_type.md) - connects an attribute to a class that describes it
 * [has numeric value](has_numeric_value.md) - connects a quantity value to a number
 * [has qualitative value](has_qualitative_value.md) - connects an attribute to a value
 * [has quantitative value](has_quantitative_value.md) - connects an attribute to a value
 * [has taxonomic rank](has_taxonomic_rank.md)
 * [has unit](has_unit.md) - connects a quantity value to a unit
 * [id](id.md) - A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * [application id](application_id.md)
    * [application instance id](application_instance_id.md)
    * [application user id](application_user_id.md)
    * [application user login id](application_user_login_id.md)
    * [build number](build_number.md)
       * [production build number](production_build_number.md)
    * [component id](component_id.md)
    * [environment id](environment_id.md)
    * [project id](project_id.md)
    * [release id](release_id.md)
       * [production release id](production_release_id.md)
    * [ticket id](ticket_id.md)
    * [vcs root id](vcs_root_id.md)
 * [iri](iri.md) - An IRI for an entity. This is determined by the id using expansion rules.
    * [svn tag url](svn_tag_url.md)
 * [name](name.md) - A human-readable name for an attribute or entity.
    * [component](component.md)
    * [component fixed](component_fixed.md)
    * [domain name](domain_name.md)
    * [environment](environment.md)
    * [fqdn](fqdn.md)
    * [g c number](g_c_number.md)
    * [tag](tag.md)
    * [tag name](tag_name.md)
    * [user name](user_name.md)
       * [application user](application_user.md)
 * [source](source.md) - a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
 * [subclass of](subclass_of.md) - subclass of holds between two taxa, e.g. subclass of superclass
 * [type](type.md)
    * [category](category.md) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the csolink entity type class.

## Types


### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [CategoryType](types/CategoryType.md)  ([Uriorcurie](types/Uriorcurie.md))  - A primitive type in which the value denotes a class within the csolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the csolink class, for example csolink:Service. For an RDF representation, the value should be a URI such as https://w3id.org/csolink/vocab/Service
 * [ComputationalSequence](types/ComputationalSequence.md)  ([String](types/String.md)) 
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Frequency](types/Frequency.md)  ([String](types/String.md)) 
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [IriType](types/IriType.md)  ([Uriorcurie](types/Uriorcurie.md))  - An IRI
 * [LabelType](types/LabelType.md)  ([String](types/String.md))  - A string that provides a human-readable name for an entity
 * [NarrativeText](types/NarrativeText.md)  ([String](types/String.md))  - A string that provides a human-readable description of something
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [PredicateType](types/PredicateType.md)  ([Uriorcurie](types/Uriorcurie.md))  - A CURIE from the testlink related_to hierarchy. For example, testlink:related_to, testlink:causes, testlink:repairs
 * [String](types/String.md)  (**str**)  - A character string
 * [SymbolType](types/SymbolType.md)  ([String](types/String.md)) 
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [TimeType](types/TimeType.md)  ([Time](types/Time.md)) 
 * [Unit](types/Unit.md)  ([String](types/String.md)) 
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE

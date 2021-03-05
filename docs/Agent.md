---
parent: Entities
title: testlink:Agent
grand_parent: Classes
layout: default
---

# Class: Agent


service, group, organization or project that provides a piece of information (i.e. a knowledge association)

URI: [testlink:Agent](https://w3id.org/testlink/vocab/Agent)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[NamedThing],[InformationContentEntity],[Association],[AdministrativeEntity]%5E-[Agent%7Caffiliation:uriorcurie%20%2A;address:string%20%3F;id:string;name:label_type%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[AdministrativeEntity])

---


## Identifier prefixes

 * isbn
 * ORCID
 * ScopusID
 * ResearchID
 * GSID
 * isni

## Parents

 *  is_a: [AdministrativeEntity](AdministrativeEntity.md)

## Referenced by class

 *  **[Publication](Publication.md)** *[author](author.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**
 *  **[InformationContentEntity](InformationContentEntity.md)** *[contributor](contributor.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**
 *  **[Association](Association.md)** *[provided by](provided_by.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**

## Attributes


### Own

 * [address](address.md)  <sub>OPT</sub>
    * Description: the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
    * range: [String](types/String.md)
 * [affiliation](affiliation.md)  <sub>0..*</sub>
    * Description: a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [agent➞id](agent_id.md)  <sub>REQ</sub>
    * Description: Different classes of agents have distinct preferred identifiers. For publishers, use the ISBN publisher code. See https://grp.isbn-international.org/ for publisher code lookups. For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, ResearchID or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code.
    * range: [String](types/String.md)
 * [agent➞name](agent_name.md)  <sub>OPT</sub>
    * Description: it is recommended that an author's 'name' property be formatted as "surname, firstname initial."
    * range: [LabelType](types/LabelType.md)

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

### Domain for slot:

 * [affiliation](affiliation.md)  <sub>0..*</sub>
    * Description: a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [agent➞id](agent_id.md)  <sub>REQ</sub>
    * Description: Different classes of agents have distinct preferred identifiers. For publishers, use the ISBN publisher code. See https://grp.isbn-international.org/ for publisher code lookups. For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, ResearchID or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code.
    * range: [String](types/String.md)
 * [agent➞name](agent_name.md)  <sub>OPT</sub>
    * Description: it is recommended that an author's 'name' property be formatted as "surname, firstname initial."
    * range: [LabelType](types/LabelType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | group |
| **Exact Mappings:** | | csrc:Agent |
|  | | CSO:single-agent |
|  | | dct:Agent |
|  | | prov:Agent |
|  | | schema:agent |
|  | | sumo:Agent |
|  | | WIKIDATA:Q24229398 |
| **Narrow Mappings:** | | csrc:Healthcare_Delivery_Organization |
|  | | csrc:Information_Sharing_and_Analysis_Organization |
|  | | csrc:organization |
|  | | csrc:Organizational_Unit |
|  | | CSO:intelligent_agents |
|  | | CSO:autonomous_agents |
|  | | CSO:multi-agent |
|  | | CSO:software_agents |
|  | | CSO:mobile_agents |
|  | | CSO:intelligent_virtual_agents |
|  | | CSO:virtual_agent |
|  | | CSO:intelligent_software_agent |
|  | | CSO:pedagogical_agents |
|  | | CSO:single-agent |
|  | | CSO:reinforcement_learning_agent |
|  | | CSO:learning_agents |
|  | | CSO:home_agents |
|  | | CSO:ultrasound_contrast_agent |
|  | | CSO:embodied_agent |
|  | | schema:department |
|  | | sumo:affiliatedOrganization |
|  | | sumo:CopyrightAuthority |
|  | | sumo:affiliatedOrganization |
|  | | sumo:CopyrightAuthority |
|  | | sumo:ProfessionalOrganizations |


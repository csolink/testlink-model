---
parent: Entities
title: testlink:Publication
grand_parent: Classes
layout: default
---

# Class: Publication


Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed resources, either directly or in one of the Publication testlink category subclasses.

URI: [testlink:Publication](https://w3id.org/testlink/vocab/Publication)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Association]-%20publications%200..%2A%3E[Publication%7Cauthors:string%20%2A;pages:string%20%2A;summary:string%20%3F;keywords:string%20%2A;lcsh_terms:uriorcurie%20%2A;xref:iri_type%20%2A;id:string;name:label_type%20%3F;type:string;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;enabled(i):boolean%20%3F;archived(i):boolean%20%3F;description(i):narrative_text%20%3F;note(i):narrative_text%20%3F],[InformationContentEntity]%5E-[Publication],[NamedThing],[InformationContentEntity],[Association])

---


## Identifier prefixes

 * ACMJOURNALS

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.

## Referenced by class

 *  **[Association](Association.md)** *[publications](publications.md)*  <sub>0..*</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [authors](authors.md)  <sub>0..*</sub>
    * Description: connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in csolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
    * range: [String](types/String.md)
 * [keywords](keywords.md)  <sub>0..*</sub>
    * Description: keywords tagging a publication
    * range: [String](types/String.md)
 * [lcsh terms](lcsh_terms.md)  <sub>0..*</sub>
    * Description: lcsh terms tagging a publication
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [publication➞id](publication_id.md)  <sub>REQ</sub>
    * Description: Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN.
    * range: [String](types/String.md)
 * [publication➞name](publication_name.md)  <sub>OPT</sub>
    * Description: the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).
    * range: [LabelType](types/LabelType.md)
 * [publication➞pages](publication_pages.md)  <sub>0..*</sub>
    * Description: When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.
    * range: [String](types/String.md)
 * [publication➞type](publication_type.md)  <sub>REQ</sub>
    * Description: Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of testlink:category testlink:OntologyClass.
    * range: [String](types/String.md)
 * [summary](summary.md)  <sub>OPT</sub>
    * Description: executive  summary of a publication
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

### Inherited from information content entity:

 * [license](license.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [format](format.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [creation date](creation_date.md)  <sub>OPT</sub>
    * Description: date on which an entity was created. This can be applied to nodes or edges
    * range: [Date](types/Date.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [authors](authors.md)  <sub>0..*</sub>
    * Description: connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in csolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
    * range: [String](types/String.md)
 * [keywords](keywords.md)  <sub>0..*</sub>
    * Description: keywords tagging a publication
    * range: [String](types/String.md)
 * [lcsh terms](lcsh_terms.md)  <sub>0..*</sub>
    * Description: lcsh terms tagging a publication
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [publication➞id](publication_id.md)  <sub>REQ</sub>
    * Description: Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN.
    * range: [String](types/String.md)
 * [publication➞name](publication_name.md)  <sub>OPT</sub>
    * Description: the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).
    * range: [LabelType](types/LabelType.md)
 * [publication➞pages](publication_pages.md)  <sub>0..*</sub>
    * Description: When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.
    * range: [String](types/String.md)
 * [publication➞type](publication_type.md)  <sub>REQ</sub>
    * Description: Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of testlink:category testlink:OntologyClass.
    * range: [String](types/String.md)
 * [summary](summary.md)  <sub>OPT</sub>
    * Description: executive  summary of a publication
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | my_system_model |
| **Exact Mappings:** | | csrc:Publication |
|  | | IAO:0000311 |
|  | | schema:publication |
|  | | sumo:Publication |
|  | | WIKIDATA:Q732577 |
| **Narrow Mappings:** | | geolink:Document |
|  | | IAO:0000013 |


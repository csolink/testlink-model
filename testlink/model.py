# Auto generated from testlink-model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-03-05 02:33
# Schema: organization
#
# id: http://example.org/sample/organization
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime
from includes.types import Boolean, Date, Double, String, Time, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ACMBOOKS = CurieNamespace('ACMBOOKS', 'https://dl.acm.org/action/doSearch?SeriesKey=acmbooks&AllField=')
ACMJOURNALS = CurieNamespace('ACMJOURNALS', 'https://dl.acm.org/action/doSearch?ConceptID=118230&AllField=')
AML = CurieNamespace('AML', 'https://w3id.org/i40/aml#')
COAR_RESOURCE = CurieNamespace('COAR_RESOURCE', 'http://vocabularies.coar-repositories.org/documentation/resource_types/')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
CTRL = CurieNamespace('CTRL', 'https://w3id.org/ibp/CTRLont#')
CVE = CurieNamespace('CVE', 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=')
ECO = CurieNamespace('ECO', 'https://evidenceontology.org/term/')
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/')
EDAM_DATA = CurieNamespace('EDAM-DATA', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('EDAM-FORMAT', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('EDAM-OPERATION', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('EDAM-TOPIC', 'http://edamontology.org/topic_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/')
EXO = CurieNamespace('EXO', 'http://purl.obolibrary.org/obo/ExO_')
GSID = CurieNamespace('GSID', 'https://scholar.google.com/citations?user=')
LCSH = CurieNamespace('LCSH', 'http://id.loc.gov/authorities/subjects/')
LCSH_PUB = CurieNamespace('LCSH_PUB', 'http://id.loc.gov/vocabulary/mgovtpubtype/')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
MAID = CurieNamespace('MAID', 'https://academic.microsoft.com/#/detail/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://example.org/UNKNOWN/NCBITaxon/')
NCIT = CurieNamespace('NCIT', 'http://example.org/UNKNOWN/NCIT/')
OM = CurieNamespace('OM', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/pato#')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RESEARCHID = CurieNamespace('ResearchID', 'https://publons.com/researcher/')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SCOPUSID = CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId=')
TAXRANK = CurieNamespace('TAXRANK', 'http://example.org/UNKNOWN/TAXRANK/')
UO = CurieNamespace('UO', 'https://www.ebi.ac.uk/ols/ontologies/uo')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
XXXX = CurieNamespace('XXXX', 'http://example.org/UNKNOWN/XXXX/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'http://example.org/UNKNOWN/doi/')
DWC = CurieNamespace('dwc', 'https://dwc.tdwg.org/terms/#dc:')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
ISBN = CurieNamespace('isbn', 'https://grp.isbn-international.org/content/using-register')
ISNI = CurieNamespace('isni', 'http://example.org/UNKNOWN/isni/')
OPENVOCAB = CurieNamespace('openvocab', 'https://vocab.org/open/#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RR = CurieNamespace('rr', 'https://www.w3.org/ns/r2rml#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'http://example.org/UNKNOWN/skos/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'https://www.w3.org/TR/vocab-ssn/#')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
SUMO = CurieNamespace('sumo', 'http://sigma.ontologyportal.org:8080/sigma/TreeView.jsp?flang=SUO-KIF&kb=SUMO&simple=yes&term=')
SUMO_WN = CurieNamespace('sumo-wn', 'http://sigma.ontologyportal.org:8080/sigma/WordNet.jsp?POS=0&word=')
TESTLINK = CurieNamespace('testlink', 'https://w3id.org/testlink/vocab/')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TESTLINK


# Types
class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the csolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the csolink class, for example csolink:Service. For an RDF representation, the value should be a URI such as https://w3id.org/csolink/vocab/Service """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = TESTLINK.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = TESTLINK.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = TESTLINK.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the testlink related_to hierarchy. For example, testlink:related_to, testlink:causes, testlink:repairs """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = TESTLINK.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = TESTLINK.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = TESTLINK.SymbolType


class Frequency(String):
    type_class_uri = UO["0000105"]
    type_class_curie = "UO:0000105"
    type_name = "frequency"
    type_model_uri = TESTLINK.Frequency


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = TESTLINK.Unit


class TimeType(Time):
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = TESTLINK.TimeType


class ComputationalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "computational sequence"
    type_model_uri = TESTLINK.ComputationalSequence


# Class references
class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class ComputationalEntityId(NamedThingId):
    pass


class OperationalEntityId(ComputationalEntityId):
    pass


class ComputationalProcessOrActivityId(ComputationalEntityId):
    pass


class OperationalActivityId(ComputationalProcessOrActivityId):
    pass


class ControlActorId(OperationalEntityId):
    pass


class ConsumedResourceId(ControlActorId):
    pass


class AdministrativeOperationId(OperationalEntityId):
    pass


class NotificationComponentId(ControlActorId):
    pass


class NotificationId(OperationalEntityId):
    pass


class DataId(NotificationComponentId):
    pass


class EnvironmentId(NamedThingId):
    pass


class SystemicEntityId(ComputationalEntityId):
    pass


class ApplicationTypeId(SystemicEntityId):
    pass


class DeploymentEntityId(SystemicEntityId):
    pass


class DeploymentId(DeploymentEntityId):
    pass


class ComponentId(DeploymentEntityId):
    pass


class ComponentTypeId(SystemicEntityId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class TaxonomicRankId(OntologyClassId):
    pass


class SystemTaxonId(OntologyClassId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class ProjectId(AdministrativeEntityId):
    pass


class RealmId(AdministrativeEntityId):
    pass


class DomainId(AdministrativeEntityId):
    pass


class HubId(AdministrativeEntityId):
    pass


class VcsRootId(AdministrativeEntityId):
    pass


class ApplicationUserId(AdministrativeEntityId):
    pass


class ApplicationUserLoginId(AdministrativeEntityId):
    pass


class ComponentOwnerId(AdministrativeEntityId):
    pass


class EmailId(AdministrativeEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class DatasetId(InformationContentEntityId):
    pass


class DatasetDistributionId(InformationContentEntityId):
    pass


class DatasetVersionId(DatasetId):
    pass


class DistributionLevelId(DatasetVersionId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class BuildId(DatasetId):
    pass


class ArchiveId(DatasetId):
    pass


class InventoryId(DatasetId):
    pass


class ConfigurationId(InformationContentEntityId):
    pass


class EnvironmentConfigurationId(ConfigurationId):
    pass


class DomainEnvironmentId(EnvironmentId):
    pass


class DomainConfigurationId(ConfigurationId):
    pass


class RealmConfigurationId(ConfigurationId):
    pass


class ComponentConfigurationId(ConfigurationId):
    pass


class ApplicationConfigurationId(ConfigurationId):
    pass


class ApplicationInstanceConfigurationId(ConfigurationId):
    pass


class DeploymentConfigurationId(ConfigurationId):
    pass


class BuildConfigurationId(ConfigurationId):
    pass


class ServerHubId(HubId):
    pass


class ServerGroupHubId(HubId):
    pass


class ApexInventoryArchiveId(ArchiveId):
    pass


class CyberEntityId(NamedThingId):
    pass


class ActivityId(NamedThingId):
    pass


class ServerId(NamedThingId):
    pass


class ServerTypeId(SystemicEntityId):
    pass


class WorkloadEntityId(OperationalEntityId):
    pass


class WorkloadId(WorkloadEntityId):
    pass


class ApplicationInstanceId(WorkloadEntityId):
    pass


class ServerGroupId(WorkloadEntityId):
    pass


class OrchestrationExposureId(ControlActorId):
    pass


class AssociationId(EntityId):
    pass


class ApplicationInstanceToServerGroupHubAssociationId(AssociationId):
    pass


class ApplicationInstanceToRealmAssociationId(AssociationId):
    pass


class ApplicationInstanceToDomainEnvironmentAssociationId(AssociationId):
    pass


class ApplicationInstanceToApplicationAssociationId(AssociationId):
    pass


class EnvironmentConfigurationToEnvironmentAssociationId(AssociationId):
    pass


class DomainEnvironmentToDomainAssociationId(AssociationId):
    pass


class DomainEnvironmentToEnvironmentAssociationId(AssociationId):
    pass


class DomainConfigurationToDomainEnvironmentAssociationId(AssociationId):
    pass


class RealmConfigurationToRealmAssociationId(AssociationId):
    pass


class RealmConfigurationToDomainEnvironmentAssociationId(AssociationId):
    pass


class ComponentToVcsRootAssociationId(AssociationId):
    pass


class ComponentConfigurationToComponentAssociationId(AssociationId):
    pass


class ApplicationToComponentAssociationId(AssociationId):
    pass


class ApplicationToApplicationTypeAssociationId(AssociationId):
    pass


class ApplicationConfigurationToApplicationAssociationId(AssociationId):
    pass


class ApplicationInstanceConfigurationToApplicationInstanceAssociationId(AssociationId):
    pass


class ApplicationUserLoginToApplicationUserAssociationId(AssociationId):
    pass


class EmailToApplicationUserAssociationId(AssociationId):
    pass


class ComponentOwnerToApplicationUserAssociationId(AssociationId):
    pass


class ComponentOwnerToComponentAssociationId(AssociationId):
    pass


class BuildToApplicationUserLoginAssociationId(AssociationId):
    pass


class BuildToVcsRootAssociationId(AssociationId):
    pass


class BuildToProjectAssociationId(AssociationId):
    pass


class BuildToApplicationInstanceAssociationId(AssociationId):
    pass


class BuildConfigurationToBuildAssociationId(AssociationId):
    pass


class DeploymentToBuildAssociationId(AssociationId):
    pass


class DeploymentToApplicationUserLoginAssociationId(AssociationId):
    pass


class DeploymentConfigurationToDeploymentAssociationId(AssociationId):
    pass


class ServerGroupToServerTypeAssociationId(AssociationId):
    pass


class ServerHubToServerAssociationId(AssociationId):
    pass


class ServerHubToServerGroupHubAssociationId(AssociationId):
    pass


class ServerGroupHubToDomainEnvironmentAssociationId(AssociationId):
    pass


class ServerGroupHubToServerGroupAssociationId(AssociationId):
    pass


class Annotation(YAMLRoot):
    """
    testlink Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Annotation
    class_class_curie: ClassVar[str] = "testlink:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Annotation


@dataclass
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.QuantityValue
    class_class_curie: ClassVar[str] = "testlink:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = TESTLINK.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(Annotation):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Attribute
    class_class_curie: ClassVar[str] = "testlink:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Attribute

    has_attribute_type: Union[str, OntologyClassId] = None
    name: Optional[Union[str, LabelType]] = None
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    has_qualitative_value: Optional[Union[str, NamedThingId]] = None
    iri: Optional[Union[str, IriType]] = None
    source: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_attribute_type is None:
            raise ValueError("has_attribute_type must be supplied")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.has_quantitative_value is None:
            self.has_quantitative_value = []
        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value]
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**v) for v in self.has_quantitative_value]

        if self.has_qualitative_value is not None and not isinstance(self.has_qualitative_value, NamedThingId):
            self.has_qualitative_value = NamedThingId(self.has_qualitative_value)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if self.source is not None and not isinstance(self.source, LabelType):
            self.source = LabelType(self.source)

        super().__post_init__(**kwargs)


class AttributeType(YAMLRoot):
    """
    A property or characteristic type of an entity. For example, an apple may have properties types such as color
    type, shape type, age type, crispiness type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.AttributeType
    class_class_curie: ClassVar[str] = "testlink:AttributeType"
    class_name: ClassVar[str] = "attribute type"
    class_model_uri: ClassVar[URIRef] = TESTLINK.AttributeType


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a observable feature or error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SeverityValue
    class_class_curie: ClassVar[str] = "testlink:SeverityValue"
    class_name: ClassVar[str] = "severity value"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SeverityValue

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.FrequencyValue
    class_class_curie: ClassVar[str] = "testlink:FrequencyValue"
    class_name: ClassVar[str] = "frequency value"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FrequencyValue

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Entity(YAMLRoot):
    """
    Root testlink Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Entity
    class_class_curie: ClassVar[str] = "testlink:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Entity

    id: Union[str, EntityId] = None
    name: Optional[Union[str, LabelType]] = None
    enabled: Optional[Union[bool, Bool]] = None
    archived: Optional[Union[bool, Bool]] = None
    description: Optional[Union[str, NarrativeText]] = None
    note: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.enabled is not None and not isinstance(self.enabled, Bool):
            self.enabled = Bool(self.enabled)

        if self.archived is not None and not isinstance(self.archived, Bool):
            self.archived = Bool(self.archived)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        if self.note is not None and not isinstance(self.note, NarrativeText):
            self.note = NarrativeText(self.note)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.NamedThing
    class_class_curie: ClassVar[str] = "testlink:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = TESTLINK.NamedThing

    id: Union[str, NamedThingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.category is None:
            raise ValueError("category must be supplied")
        elif not isinstance(self.category, list):
            self.category = [self.category]
        elif len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.category]

        super().__post_init__(**kwargs)


@dataclass
class ComputationalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComputationalEntity
    class_class_curie: ClassVar[str] = "testlink:ComputationalEntity"
    class_name: ClassVar[str] = "computational entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComputationalEntity

    id: Union[str, ComputationalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems;
    componentservices, their servicetypes and other operation entities; computer parts; computational processes
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ThingWithTaxon
    class_class_curie: ClassVar[str] = "testlink:ThingWithTaxon"
    class_name: ClassVar[str] = "thing with taxon"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ThingWithTaxon

    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class OperationalEntity(ComputationalEntity):
    """
    A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.OperationalEntity
    class_class_curie: ClassVar[str] = "testlink:OperationalEntity"
    class_name: ClassVar[str] = "operational entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OperationalEntity

    id: Union[str, OperationalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OperationalEntityId):
            self.id = OperationalEntityId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class ComputationalProcessOrActivity(ComputationalEntity):
    """
    Either an individual operational activity, or a collection of causally connected operational activities
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComputationalProcessOrActivity
    class_class_curie: ClassVar[str] = "testlink:ComputationalProcessOrActivity"
    class_name: ClassVar[str] = "computational process or activity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComputationalProcessOrActivity

    id: Union[str, ComputationalProcessOrActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    enabled_by: Optional[Union[Union[str, CyberEntityId], List[Union[str, CyberEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComputationalProcessOrActivityId):
            self.id = ComputationalProcessOrActivityId(self.id)

        if self.has_input is None:
            self.has_input = []
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input]
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self.has_output is None:
            self.has_output = []
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output]
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if self.enabled_by is None:
            self.enabled_by = []
        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by]
        self.enabled_by = [v if isinstance(v, CyberEntityId) else CyberEntityId(v) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class OperationalActivity(ComputationalProcessOrActivity):
    """
    An execution of a operational function carried out by a servicetype or macrooperational complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.OperationalActivity
    class_class_curie: ClassVar[str] = "testlink:OperationalActivity"
    class_name: ClassVar[str] = "operational activity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OperationalActivity

    id: Union[str, OperationalActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_input: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()
    enabled_by: Optional[Union[Union[dict, "MacrooperationalMachineMixin"], List[Union[dict, "MacrooperationalMachineMixin"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OperationalActivityId):
            self.id = OperationalActivityId(self.id)

        if self.has_input is None:
            self.has_input = []
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input]
        self.has_input = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_input]

        if self.has_output is None:
            self.has_output = []
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output]
        self.has_output = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_output]

        if self.enabled_by is None:
            self.enabled_by = []
        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by]
        self.enabled_by = [v if isinstance(v, MacrooperationalMachineMixin) else MacrooperationalMachineMixin(**v) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class Cluster(YAMLRoot):
    """
    The cyber combination of two or more operational entities in which the identities are retained and are mixed in
    the form of solutions,
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Cluster
    class_class_curie: ClassVar[str] = "testlink:Cluster"
    class_name: ClassVar[str] = "cluster"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Cluster

    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class ControlActor(OperationalEntity):
    """
    May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex
    resource with multiple orchestration entities as part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ControlActor
    class_class_curie: ClassVar[str] = "testlink:ControlActor"
    class_name: ClassVar[str] = "control actor"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ControlActor

    id: Union[str, ControlActorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ControlActorId):
            self.id = ControlActorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ConsumedResource(ControlActor):
    """
    A control actor (often a cluster) consumed for information, engineering or technical use.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ConsumedResource
    class_class_curie: ClassVar[str] = "testlink:ConsumedResource"
    class_name: ClassVar[str] = "consumed resource"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ConsumedResource

    id: Union[str, ConsumedResourceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ConsumedResourceId):
            self.id = ConsumedResourceId(self.id)

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperation(OperationalEntity):
    """
    A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperation
    class_class_curie: ClassVar[str] = "testlink:AdministrativeOperation"
    class_name: ClassVar[str] = "administrative operation"
    class_model_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperation

    id: Union[str, AdministrativeOperationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AdministrativeOperationId):
            self.id = AdministrativeOperationId(self.id)

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class Application(YAMLRoot):
    """
    The cyper combination of one or more components, serviceunits (pod), in which the identities are retained and
    mixed in the form of solutions,
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Application
    class_class_curie: ClassVar[str] = "testlink:Application"
    class_name: ClassVar[str] = "application"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Application

    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class NotificationComponent(ControlActor):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.NotificationComponent
    class_class_curie: ClassVar[str] = "testlink:NotificationComponent"
    class_name: ClassVar[str] = "notification component"
    class_model_uri: ClassVar[URIRef] = TESTLINK.NotificationComponent

    id: Union[str, NotificationComponentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NotificationComponentId):
            self.id = NotificationComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Notification(OperationalEntity):
    """
    A event consumed by a healthy system as a source of information
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_data"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Notification
    class_class_curie: ClassVar[str] = "testlink:Notification"
    class_name: ClassVar[str] = "notification"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Notification

    id: Union[str, NotificationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_data: Optional[Union[Union[str, DataId], List[Union[str, DataId]]]] = empty_list()
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NotificationId):
            self.id = NotificationId(self.id)

        if self.has_data is None:
            self.has_data = []
        if not isinstance(self.has_data, list):
            self.has_data = [self.has_data]
        self.has_data = [v if isinstance(v, DataId) else DataId(v) for v in self.has_data]

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class Data(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Data
    class_class_curie: ClassVar[str] = "testlink:Data"
    class_name: ClassVar[str] = "data"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Data

    id: Union[str, DataId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DataId):
            self.id = DataId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Environment(NamedThing):
    """
    An environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Environment
    class_class_curie: ClassVar[str] = "testlink:Environment"
    class_name: ClassVar[str] = "environment"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Environment

    id: Union[str, EnvironmentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    name: Optional[Union[str, LabelType]] = None
    note: Optional[Union[str, NarrativeText]] = None
    enabled: Optional[Union[bool, Bool]] = None
    archived: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentId):
            self.id = EnvironmentId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.note is not None and not isinstance(self.note, NarrativeText):
            self.note = NarrativeText(self.note)

        if self.enabled is not None and not isinstance(self.enabled, Bool):
            self.enabled = Bool(self.enabled)

        if self.archived is not None and not isinstance(self.archived, Bool):
            self.archived = Bool(self.archived)

        super().__post_init__(**kwargs)


@dataclass
class SystemicEntity(ComputationalEntity):
    """
    A named entity that is either a part of a system, a whole system, population or clade of systems, excluding
    operational entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SystemicEntity
    class_class_curie: ClassVar[str] = "testlink:SystemicEntity"
    class_name: ClassVar[str] = "systemic entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SystemicEntity

    id: Union[str, SystemicEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=Attribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationType(SystemicEntity):
    """
    A component type defines the set of components running the same software and sharing the same configuration. It's
    a single point of configuration control.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationType
    class_class_curie: ClassVar[str] = "testlink:ApplicationType"
    class_name: ClassVar[str] = "application type"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationType

    id: Union[str, ApplicationTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationTypeId):
            self.id = ApplicationTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntity(SystemicEntity):
    """
    A process location, serviceunit type or gross deployment part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.DeploymentEntity
    class_class_curie: ClassVar[str] = "testlink:DeploymentEntity"
    class_name: ClassVar[str] = "deployment entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DeploymentEntity

    id: Union[str, DeploymentEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentEntityId):
            self.id = DeploymentEntityId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class Deployment(DeploymentEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Deployment
    class_class_curie: ClassVar[str] = "testlink:Deployment"
    class_name: ClassVar[str] = "deployment"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Deployment

    id: Union[str, DeploymentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()
    application_user_login: Optional[str] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentId):
            self.id = DeploymentId(self.id)

        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=Attribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        if self.application_user_login is not None and not isinstance(self.application_user_login, str):
            self.application_user_login = str(self.application_user_login)

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class Component(DeploymentEntity):
    """
    The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and
    repaired independently. Each component belongs to one, and only one, serviceunit.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Component
    class_class_curie: ClassVar[str] = "testlink:Component"
    class_name: ClassVar[str] = "component"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Component

    id: Union[str, ComponentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    vcs_location: Optional[str] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentId):
            self.id = ComponentId(self.id)

        if self.vcs_location is not None and not isinstance(self.vcs_location, str):
            self.vcs_location = str(self.vcs_location)

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class ComponentType(SystemicEntity):
    """
    A component type defines the set of components running the same software and sharing the same configuration. It's
    a single point of configuration control.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentType
    class_class_curie: ClassVar[str] = "testlink:ComponentType"
    class_name: ClassVar[str] = "component type"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentType

    id: Union[str, ComponentTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentTypeId):
            self.id = ComponentTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixin(YAMLRoot):
    """
    A union of componentservice, servicetype, and macrooperational complex. These are the basic units of function in a
    component. They either carry out individual computational activities, or they encode tasks which do this.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixin
    class_class_curie: ClassVar[str] = "testlink:MacrooperationalMachineMixin"
    class_name: ClassVar[str] = "macrooperational machine mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixin

    name: Optional[Union[str, SymbolType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OntologyClass
    class_class_curie: ClassVar[str] = "testlink:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OntologyClass

    id: Union[str, OntologyClassId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.RelationshipType
    class_class_curie: ClassVar[str] = "testlink:RelationshipType"
    class_name: ClassVar[str] = "relationship type"
    class_model_uri: ClassVar[URIRef] = TESTLINK.RelationshipType

    id: Union[str, RelationshipTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.TaxonomicRank
    class_class_curie: ClassVar[str] = "testlink:TaxonomicRank"
    class_name: ClassVar[str] = "taxonomic rank"
    class_model_uri: ClassVar[URIRef] = TESTLINK.TaxonomicRank

    id: Union[str, TaxonomicRankId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, TaxonomicRankId):
            self.id = TaxonomicRankId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SystemTaxon(OntologyClass):
    """
    A classification of a set of systems.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SystemTaxon
    class_class_curie: ClassVar[str] = "testlink:SystemTaxon"
    class_name: ClassVar[str] = "system taxon"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SystemTaxon

    id: Union[str, SystemTaxonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_taxonomic_rank: Optional[Union[str, TaxonomicRankId]] = None
    subclass_of: Optional[Union[str, SystemTaxonId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SystemTaxonId):
            self.id = SystemTaxonId(self.id)

        if self.has_taxonomic_rank is not None and not isinstance(self.has_taxonomic_rank, TaxonomicRankId):
            self.has_taxonomic_rank = TaxonomicRankId(self.has_taxonomic_rank)

        if self.subclass_of is not None and not isinstance(self.subclass_of, SystemTaxonId):
            self.subclass_of = SystemTaxonId(self.subclass_of)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.AdministrativeEntity
    class_class_curie: ClassVar[str] = "testlink:AdministrativeEntity"
    class_name: ClassVar[str] = "administrative entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class Agent(AdministrativeEntity):
    """
    service, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Agent
    class_class_curie: ClassVar[str] = "testlink:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Agent

    id: Union[str, AgentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    affiliation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if self.affiliation is None:
            self.affiliation = []
        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation]
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Project(AdministrativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Project
    class_class_curie: ClassVar[str] = "testlink:Project"
    class_name: ClassVar[str] = "project"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Project

    id: Union[str, ProjectId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Realm(AdministrativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Realm
    class_class_curie: ClassVar[str] = "testlink:Realm"
    class_name: ClassVar[str] = "realm"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Realm

    id: Union[str, RealmId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RealmId):
            self.id = RealmId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Domain(AdministrativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Domain
    class_class_curie: ClassVar[str] = "testlink:Domain"
    class_name: ClassVar[str] = "domain"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Domain

    id: Union[str, DomainId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    fqdn: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DomainId):
            self.id = DomainId(self.id)

        if self.fqdn is not None and not isinstance(self.fqdn, LabelType):
            self.fqdn = LabelType(self.fqdn)

        super().__post_init__(**kwargs)


@dataclass
class Hub(AdministrativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Hub
    class_class_curie: ClassVar[str] = "testlink:Hub"
    class_name: ClassVar[str] = "hub"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Hub

    id: Union[str, HubId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, HubId):
            self.id = HubId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class VcsRoot(AdministrativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.VcsRoot
    class_class_curie: ClassVar[str] = "testlink:VcsRoot"
    class_name: ClassVar[str] = "vcs root"
    class_model_uri: ClassVar[URIRef] = TESTLINK.VcsRoot

    id: Union[str, VcsRootId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VcsRootId):
            self.id = VcsRootId(self.id)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationUser(AdministrativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationUser
    class_class_curie: ClassVar[str] = "testlink:ApplicationUser"
    class_name: ClassVar[str] = "application user"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationUser

    id: Union[str, ApplicationUserId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    first_name: Optional[Union[str, LabelType]] = None
    last_name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationUserId):
            self.id = ApplicationUserId(self.id)

        if self.first_name is not None and not isinstance(self.first_name, LabelType):
            self.first_name = LabelType(self.first_name)

        if self.last_name is not None and not isinstance(self.last_name, LabelType):
            self.last_name = LabelType(self.last_name)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationUserLogin(AdministrativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationUserLogin
    class_class_curie: ClassVar[str] = "testlink:ApplicationUserLogin"
    class_name: ClassVar[str] = "application user login"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationUserLogin

    id: Union[str, ApplicationUserLoginId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    user_name: Optional[Union[str, LabelType]] = None
    domain_name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationUserLoginId):
            self.id = ApplicationUserLoginId(self.id)

        if self.user_name is not None and not isinstance(self.user_name, LabelType):
            self.user_name = LabelType(self.user_name)

        if self.domain_name is not None and not isinstance(self.domain_name, LabelType):
            self.domain_name = LabelType(self.domain_name)

        super().__post_init__(**kwargs)


@dataclass
class ComponentOwner(AdministrativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentOwner
    class_class_curie: ClassVar[str] = "testlink:ComponentOwner"
    class_name: ClassVar[str] = "component owner"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentOwner

    id: Union[str, ComponentOwnerId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentOwnerId):
            self.id = ComponentOwnerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Email(AdministrativeEntity):
    """
    A text string identifier location for e-mail delivery.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Email
    class_class_curie: ClassVar[str] = "testlink:Email"
    class_name: ClassVar[str] = "email"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Email

    id: Union[str, EmailId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    name: Optional[Union[str, LabelType]] = None
    enabled: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmailId):
            self.id = EmailId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.enabled is not None and not isinstance(self.enabled, Bool):
            self.enabled = Bool(self.enabled)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.InformationContentEntity
    class_class_curie: ClassVar[str] = "testlink:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Dataset
    class_class_curie: ClassVar[str] = "testlink:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Dataset

    id: Union[str, DatasetId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DatasetDistribution(InformationContentEntity):
    """
    an item that holds distribution level information about a dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DatasetDistribution
    class_class_curie: ClassVar[str] = "testlink:DatasetDistribution"
    class_name: ClassVar[str] = "dataset distribution"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DatasetDistribution

    id: Union[str, DatasetDistributionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    distribution_download_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatasetDistributionId):
            self.id = DatasetDistributionId(self.id)

        if self.distribution_download_url is not None and not isinstance(self.distribution_download_url, str):
            self.distribution_download_url = str(self.distribution_download_url)

        super().__post_init__(**kwargs)


@dataclass
class DatasetVersion(Dataset):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DatasetVersion
    class_class_curie: ClassVar[str] = "testlink:DatasetVersion"
    class_name: ClassVar[str] = "dataset version"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DatasetVersion

    id: Union[str, DatasetVersionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_dataset: Optional[Union[str, DatasetId]] = None
    ingest_date: Optional[str] = None
    has_distribution: Optional[Union[str, DatasetDistributionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatasetVersionId):
            self.id = DatasetVersionId(self.id)

        if self.has_dataset is not None and not isinstance(self.has_dataset, DatasetId):
            self.has_dataset = DatasetId(self.has_dataset)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        if self.has_distribution is not None and not isinstance(self.has_distribution, DatasetDistributionId):
            self.has_distribution = DatasetDistributionId(self.has_distribution)

        super().__post_init__(**kwargs)


@dataclass
class DistributionLevel(DatasetVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DistributionLevel
    class_class_curie: ClassVar[str] = "testlink:DistributionLevel"
    class_name: ClassVar[str] = "distribution level"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DistributionLevel

    id: Union[str, DistributionLevelId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    download_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.download_url is not None and not isinstance(self.download_url, str):
            self.download_url = str(self.download_url)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed resources, either directly or in one of the Publication testlink category subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Publication
    class_class_curie: ClassVar[str] = "testlink:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Publication

    id: Union[str, PublicationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    pages: Optional[Union[str, List[str]]] = empty_list()
    summary: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    lcsh_terms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self.type is None:
            raise ValueError("type must be supplied")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.authors is None:
            self.authors = []
        if not isinstance(self.authors, list):
            self.authors = [self.authors]
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.pages is None:
            self.pages = []
        if not isinstance(self.pages, list):
            self.pages = [self.pages]
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.keywords is None:
            self.keywords = []
        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords]
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.lcsh_terms is None:
            self.lcsh_terms = []
        if not isinstance(self.lcsh_terms, list):
            self.lcsh_terms = [self.lcsh_terms]
        self.lcsh_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.lcsh_terms]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Build(Dataset):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Build
    class_class_curie: ClassVar[str] = "testlink:Build"
    class_name: ClassVar[str] = "build"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Build

    id: Union[str, BuildId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    created: Optional[Union[str, XSDDate]] = None
    updated: Optional[Union[str, XSDDate]] = None
    vcs_location: Optional[str] = None
    vcs_revision: Optional[str] = None
    internal_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BuildId):
            self.id = BuildId(self.id)

        if self.created is not None and not isinstance(self.created, XSDDate):
            self.created = XSDDate(self.created)

        if self.updated is not None and not isinstance(self.updated, XSDDate):
            self.updated = XSDDate(self.updated)

        if self.vcs_location is not None and not isinstance(self.vcs_location, str):
            self.vcs_location = str(self.vcs_location)

        if self.vcs_revision is not None and not isinstance(self.vcs_revision, str):
            self.vcs_revision = str(self.vcs_revision)

        if self.internal_version is not None and not isinstance(self.internal_version, str):
            self.internal_version = str(self.internal_version)

        super().__post_init__(**kwargs)


@dataclass
class Archive(Dataset):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Archive
    class_class_curie: ClassVar[str] = "testlink:Archive"
    class_name: ClassVar[str] = "archive"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Archive

    id: Union[str, ArchiveId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ArchiveId):
            self.id = ArchiveId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Inventory(Dataset):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Inventory
    class_class_curie: ClassVar[str] = "testlink:Inventory"
    class_name: ClassVar[str] = "inventory"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Inventory

    id: Union[str, InventoryId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    created: Optional[Union[str, XSDDate]] = None
    component_fixed: Optional[Union[str, LabelType]] = None
    tag: Optional[Union[str, LabelType]] = None
    tag_name: Optional[Union[str, LabelType]] = None
    user_login: Optional[str] = None
    svn_tag_url: Optional[Union[str, IriType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, InventoryId):
            self.id = InventoryId(self.id)

        if self.created is not None and not isinstance(self.created, XSDDate):
            self.created = XSDDate(self.created)

        if self.component_fixed is not None and not isinstance(self.component_fixed, LabelType):
            self.component_fixed = LabelType(self.component_fixed)

        if self.tag is not None and not isinstance(self.tag, LabelType):
            self.tag = LabelType(self.tag)

        if self.tag_name is not None and not isinstance(self.tag_name, LabelType):
            self.tag_name = LabelType(self.tag_name)

        if self.user_login is not None and not isinstance(self.user_login, str):
            self.user_login = str(self.user_login)

        if self.svn_tag_url is not None and not isinstance(self.svn_tag_url, IriType):
            self.svn_tag_url = IriType(self.svn_tag_url)

        super().__post_init__(**kwargs)


@dataclass
class Configuration(InformationContentEntity):
    """
    Configuration is the manner in which components are arranged to make up the computer system. Configuration
    consists of both hardware and software components.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Configuration
    class_class_curie: ClassVar[str] = "testlink:Configuration"
    class_name: ClassVar[str] = "configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Configuration

    id: Union[str, ConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_part: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ConfigurationId):
            self.id = ConfigurationId(self.id)

        if self.has_part is None:
            self.has_part = []
        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part]
        self.has_part = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_part]

        if self.has_quantitative_value is None:
            self.has_quantitative_value = []
        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value]
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**v) for v in self.has_quantitative_value]

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentConfiguration(Configuration):
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.EnvironmentConfiguration
    class_class_curie: ClassVar[str] = "testlink:EnvironmentConfiguration"
    class_name: ClassVar[str] = "environment configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EnvironmentConfiguration

    id: Union[str, EnvironmentConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class DomainEnvironment(Environment):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DomainEnvironment
    class_class_curie: ClassVar[str] = "testlink:DomainEnvironment"
    class_name: ClassVar[str] = "domain environment"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DomainEnvironment

    id: Union[str, DomainEnvironmentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class DomainConfiguration(Configuration):
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.DomainConfiguration
    class_class_curie: ClassVar[str] = "testlink:DomainConfiguration"
    class_name: ClassVar[str] = "domain configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DomainConfiguration

    id: Union[str, DomainConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class RealmConfiguration(Configuration):
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.RealmConfiguration
    class_class_curie: ClassVar[str] = "testlink:RealmConfiguration"
    class_name: ClassVar[str] = "realm configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.RealmConfiguration

    id: Union[str, RealmConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ComponentConfiguration(Configuration):
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentConfiguration
    class_class_curie: ClassVar[str] = "testlink:ComponentConfiguration"
    class_name: ClassVar[str] = "component configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentConfiguration

    id: Union[str, ComponentConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ApplicationConfiguration(Configuration):
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationConfiguration
    class_class_curie: ClassVar[str] = "testlink:ApplicationConfiguration"
    class_name: ClassVar[str] = "application configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationConfiguration

    id: Union[str, ApplicationConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ApplicationInstanceConfiguration(Configuration):
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceConfiguration
    class_class_curie: ClassVar[str] = "testlink:ApplicationInstanceConfiguration"
    class_name: ClassVar[str] = "application instance configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceConfiguration

    id: Union[str, ApplicationInstanceConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class DeploymentConfiguration(Configuration):
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.DeploymentConfiguration
    class_class_curie: ClassVar[str] = "testlink:DeploymentConfiguration"
    class_name: ClassVar[str] = "deployment configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DeploymentConfiguration

    id: Union[str, DeploymentConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class BuildConfiguration(Configuration):
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.BuildConfiguration
    class_class_curie: ClassVar[str] = "testlink:BuildConfiguration"
    class_name: ClassVar[str] = "build configuration"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BuildConfiguration

    id: Union[str, BuildConfigurationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ServerHub(Hub):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerHub
    class_class_curie: ClassVar[str] = "testlink:ServerHub"
    class_name: ClassVar[str] = "server hub"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerHub

    id: Union[str, ServerHubId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ServerGroupHub(Hub):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerGroupHub
    class_class_curie: ClassVar[str] = "testlink:ServerGroupHub"
    class_name: ClassVar[str] = "server group hub"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerGroupHub

    id: Union[str, ServerGroupHubId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ApexInventoryArchive(Archive):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApexInventoryArchive
    class_class_curie: ClassVar[str] = "testlink:ApexInventoryArchive"
    class_name: ClassVar[str] = "apex inventory archive"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApexInventoryArchive

    id: Union[str, ApexInventoryArchiveId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    release_date: Optional[Union[str, XSDDate]] = None
    tag_name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self.tag_name is not None and not isinstance(self.tag_name, LabelType):
            self.tag_name = LabelType(self.tag_name)

        super().__post_init__(**kwargs)


class CyberEssenceOrOccurrent(YAMLRoot):
    """
    Either a cyber or processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.CyberEssenceOrOccurrent
    class_class_curie: ClassVar[str] = "testlink:CyberEssenceOrOccurrent"
    class_name: ClassVar[str] = "cyber essence or occurrent"
    class_model_uri: ClassVar[URIRef] = TESTLINK.CyberEssenceOrOccurrent


class CyberEssence(CyberEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.CyberEssence
    class_class_curie: ClassVar[str] = "testlink:CyberEssence"
    class_name: ClassVar[str] = "cyber essence"
    class_model_uri: ClassVar[URIRef] = TESTLINK.CyberEssence


@dataclass
class CyberEntity(NamedThing):
    """
    An entity that has digital reality (a.k.a. cyber essence).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.CyberEntity
    class_class_curie: ClassVar[str] = "testlink:CyberEntity"
    class_name: ClassVar[str] = "cyber entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.CyberEntity

    id: Union[str, CyberEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CyberEntityId):
            self.id = CyberEntityId(self.id)

        super().__post_init__(**kwargs)


class Occurrent(CyberEssenceOrOccurrent):
    """
    A processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Occurrent
    class_class_curie: ClassVar[str] = "testlink:Occurrent"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Occurrent


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral healthy, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ActivityAndBehavior
    class_class_curie: ClassVar[str] = "testlink:ActivityAndBehavior"
    class_name: ClassVar[str] = "activity and behavior"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ActivityAndBehavior


@dataclass
class Activity(NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Activity
    class_class_curie: ClassVar[str] = "testlink:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Activity

    id: Union[str, ActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Server(NamedThing):
    """
    A piece of computer hardware or software (computer program) that provides functionality for other programs or
    devices, called "clients"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Server
    class_class_curie: ClassVar[str] = "testlink:Server"
    class_name: ClassVar[str] = "server"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Server

    id: Union[str, ServerId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServerId):
            self.id = ServerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ServerType(SystemicEntity):
    """
    A type of server
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerType
    class_class_curie: ClassVar[str] = "testlink:ServerType"
    class_name: ClassVar[str] = "server type"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerType

    id: Union[str, ServerTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServerTypeId):
            self.id = ServerTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class WorkloadEntity(OperationalEntity):
    """
    An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon,
    regulatory region) or is encoded in a workload (serviceinstance)
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.WorkloadEntity
    class_class_curie: ClassVar[str] = "testlink:WorkloadEntity"
    class_name: ClassVar[str] = "workload entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.WorkloadEntity

    id: Union[str, WorkloadEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, WorkloadEntityId):
            self.id = WorkloadEntityId(self.id)

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class Workload(WorkloadEntity):
    """
    A workload is the sum of componentservice resources within a serviceunit or virion.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Workload
    class_class_curie: ClassVar[str] = "testlink:Workload"
    class_name: ClassVar[str] = "workload"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Workload

    id: Union[str, WorkloadId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, WorkloadId):
            self.id = WorkloadId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationInstance(WorkloadEntity):
    """
    The unit of service workload the component is capable of providing or protecting.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstance
    class_class_curie: ClassVar[str] = "testlink:ApplicationInstance"
    class_name: ClassVar[str] = "application instance"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstance

    id: Union[str, ApplicationInstanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    internal_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationInstanceId):
            self.id = ApplicationInstanceId(self.id)

        if self.internal_version is not None and not isinstance(self.internal_version, str):
            self.internal_version = str(self.internal_version)

        super().__post_init__(**kwargs)


@dataclass
class Homogeneity(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Homogeneity
    class_class_curie: ClassVar[str] = "testlink:Homogeneity"
    class_name: ClassVar[str] = "homogeneity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Homogeneity

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ServerGroup(WorkloadEntity):
    """
    An group of servers
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerGroup
    class_class_curie: ClassVar[str] = "testlink:ServerGroup"
    class_name: ClassVar[str] = "server group"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerGroup

    id: Union[str, ServerGroupId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_homogeneity: Optional[Union[dict, Homogeneity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServerGroupId):
            self.id = ServerGroupId(self.id)

        if self.has_homogeneity is not None and not isinstance(self.has_homogeneity, Homogeneity):
            self.has_homogeneity = Homogeneity(**self.has_homogeneity)

        super().__post_init__(**kwargs)


@dataclass
class Event(YAMLRoot):
    """
    An exposure event
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Event
    class_class_curie: ClassVar[str] = "testlink:Event"
    class_name: ClassVar[str] = "event"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Event

    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEvent(YAMLRoot):
    """
    A (possibly time bounded) incidence of a feature of the environment of an system that influences one or more
    observability of that system, potentially mediated by serviceunits
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ExposureEvent
    class_class_curie: ClassVar[str] = "testlink:ExposureEvent"
    class_name: ClassVar[str] = "exposure event"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ExposureEvent

    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationExposure(ControlActor):
    """
    A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.OrchestrationExposure
    class_class_curie: ClassVar[str] = "testlink:OrchestrationExposure"
    class_name: ClassVar[str] = "orchestration exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OrchestrationExposure

    id: Union[str, OrchestrationExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationExposureId):
            self.id = OrchestrationExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Association
    class_class_curie: ClassVar[str] = "testlink:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Association

    id: Union[str, AssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.relation is None:
            raise ValueError("relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        if self.category is None:
            raise ValueError("category must be supplied")
        elif not isinstance(self.category, list):
            self.category = [self.category]
        elif len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, AssociationId) else AssociationId(v) for v in self.category]

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.qualifiers is None:
            self.qualifiers = []
        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers]
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        if self.publications is None:
            self.publications = []
        if not isinstance(self.publications, list):
            self.publications = [self.publications]
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationInstanceToServerGroupHubAssociation(Association):
    """
    Any association between a application instance and a server group hub. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceToServerGroupHubAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationInstanceToServerGroupHubAssociation"
    class_name: ClassVar[str] = "application instance to server group hub association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceToServerGroupHubAssociation

    id: Union[str, ApplicationInstanceToServerGroupHubAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ApplicationInstanceId] = None
    object: Union[str, ServerGroupHubId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationInstanceToServerGroupHubAssociationId):
            self.id = ApplicationInstanceToServerGroupHubAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ApplicationInstanceId):
            self.subject = ApplicationInstanceId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServerGroupHubId):
            self.object = ServerGroupHubId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationInstanceToRealmAssociation(Association):
    """
    Any association between a application instance and a realm. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceToRealmAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationInstanceToRealmAssociation"
    class_name: ClassVar[str] = "application instance to realm association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceToRealmAssociation

    id: Union[str, ApplicationInstanceToRealmAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ApplicationInstanceId] = None
    object: Union[str, RealmId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationInstanceToRealmAssociationId):
            self.id = ApplicationInstanceToRealmAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ApplicationInstanceId):
            self.subject = ApplicationInstanceId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, RealmId):
            self.object = RealmId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationInstanceToDomainEnvironmentAssociation(Association):
    """
    Any association between a application instance and a domain environment. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceToDomainEnvironmentAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationInstanceToDomainEnvironmentAssociation"
    class_name: ClassVar[str] = "application instance to domain environment association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceToDomainEnvironmentAssociation

    id: Union[str, ApplicationInstanceToDomainEnvironmentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ApplicationInstanceId] = None
    object: Union[str, DomainEnvironmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationInstanceToDomainEnvironmentAssociationId):
            self.id = ApplicationInstanceToDomainEnvironmentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ApplicationInstanceId):
            self.subject = ApplicationInstanceId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DomainEnvironmentId):
            self.object = DomainEnvironmentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationInstanceToApplicationAssociation(Association):
    """
    Any association between a application instance and a application. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceToApplicationAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationInstanceToApplicationAssociation"
    class_name: ClassVar[str] = "application instance to application association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceToApplicationAssociation

    id: Union[str, ApplicationInstanceToApplicationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ApplicationInstanceId] = None
    object: Union[dict, Application] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationInstanceToApplicationAssociationId):
            self.id = ApplicationInstanceToApplicationAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ApplicationInstanceId):
            self.subject = ApplicationInstanceId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Application):
            self.object = Application(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentConfigurationToEnvironmentAssociation(Association):
    """
    Any association between a environment configuration and a environment. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EnvironmentConfigurationToEnvironmentAssociation
    class_class_curie: ClassVar[str] = "testlink:EnvironmentConfigurationToEnvironmentAssociation"
    class_name: ClassVar[str] = "environment configuration to environment association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EnvironmentConfigurationToEnvironmentAssociation

    id: Union[str, EnvironmentConfigurationToEnvironmentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, EnvironmentConfigurationId] = None
    object: Union[str, EnvironmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentConfigurationToEnvironmentAssociationId):
            self.id = EnvironmentConfigurationToEnvironmentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, EnvironmentConfigurationId):
            self.subject = EnvironmentConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, EnvironmentId):
            self.object = EnvironmentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DomainEnvironmentToDomainAssociation(Association):
    """
    Any association between a domain environment and a domain. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DomainEnvironmentToDomainAssociation
    class_class_curie: ClassVar[str] = "testlink:DomainEnvironmentToDomainAssociation"
    class_name: ClassVar[str] = "domain environment to domain association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DomainEnvironmentToDomainAssociation

    id: Union[str, DomainEnvironmentToDomainAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, DomainEnvironmentId] = None
    object: Union[str, DomainId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DomainEnvironmentToDomainAssociationId):
            self.id = DomainEnvironmentToDomainAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DomainEnvironmentId):
            self.subject = DomainEnvironmentId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DomainId):
            self.object = DomainId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DomainEnvironmentToEnvironmentAssociation(Association):
    """
    Any association between a domain environment and a environment. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DomainEnvironmentToEnvironmentAssociation
    class_class_curie: ClassVar[str] = "testlink:DomainEnvironmentToEnvironmentAssociation"
    class_name: ClassVar[str] = "domain environment to environment association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DomainEnvironmentToEnvironmentAssociation

    id: Union[str, DomainEnvironmentToEnvironmentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, DomainEnvironmentId] = None
    object: Union[str, EnvironmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DomainEnvironmentToEnvironmentAssociationId):
            self.id = DomainEnvironmentToEnvironmentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DomainEnvironmentId):
            self.subject = DomainEnvironmentId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, EnvironmentId):
            self.object = EnvironmentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DomainConfigurationToDomainEnvironmentAssociation(Association):
    """
    Any association between a domain configuration and a domain environment. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DomainConfigurationToDomainEnvironmentAssociation
    class_class_curie: ClassVar[str] = "testlink:DomainConfigurationToDomainEnvironmentAssociation"
    class_name: ClassVar[str] = "domain configuration to domain environment association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DomainConfigurationToDomainEnvironmentAssociation

    id: Union[str, DomainConfigurationToDomainEnvironmentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, DomainConfigurationId] = None
    object: Union[str, DomainEnvironmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DomainConfigurationToDomainEnvironmentAssociationId):
            self.id = DomainConfigurationToDomainEnvironmentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DomainConfigurationId):
            self.subject = DomainConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DomainEnvironmentId):
            self.object = DomainEnvironmentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class RealmConfigurationToRealmAssociation(Association):
    """
    Any association between a realm configuration and a realm. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.RealmConfigurationToRealmAssociation
    class_class_curie: ClassVar[str] = "testlink:RealmConfigurationToRealmAssociation"
    class_name: ClassVar[str] = "realm configuration to realm association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.RealmConfigurationToRealmAssociation

    id: Union[str, RealmConfigurationToRealmAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, RealmConfigurationId] = None
    object: Union[str, RealmId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RealmConfigurationToRealmAssociationId):
            self.id = RealmConfigurationToRealmAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, RealmConfigurationId):
            self.subject = RealmConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, RealmId):
            self.object = RealmId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class RealmConfigurationToDomainEnvironmentAssociation(Association):
    """
    Any association between a realm configuration and a domain environment. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.RealmConfigurationToDomainEnvironmentAssociation
    class_class_curie: ClassVar[str] = "testlink:RealmConfigurationToDomainEnvironmentAssociation"
    class_name: ClassVar[str] = "realm configuration to domain environment association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.RealmConfigurationToDomainEnvironmentAssociation

    id: Union[str, RealmConfigurationToDomainEnvironmentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, RealmConfigurationId] = None
    object: Union[str, DomainEnvironmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RealmConfigurationToDomainEnvironmentAssociationId):
            self.id = RealmConfigurationToDomainEnvironmentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, RealmConfigurationId):
            self.subject = RealmConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DomainEnvironmentId):
            self.object = DomainEnvironmentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentToVcsRootAssociation(Association):
    """
    Any association between a component and a vcs root. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentToVcsRootAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentToVcsRootAssociation"
    class_name: ClassVar[str] = "component to vcs root association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentToVcsRootAssociation

    id: Union[str, ComponentToVcsRootAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, VcsRootId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentToVcsRootAssociationId):
            self.id = ComponentToVcsRootAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentId):
            self.subject = ComponentId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, VcsRootId):
            self.object = VcsRootId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentConfigurationToComponentAssociation(Association):
    """
    Any association between a component configuration and a component. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentConfigurationToComponentAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentConfigurationToComponentAssociation"
    class_name: ClassVar[str] = "component configuration to component association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentConfigurationToComponentAssociation

    id: Union[str, ComponentConfigurationToComponentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ComponentConfigurationId] = None
    object: Union[str, ComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentConfigurationToComponentAssociationId):
            self.id = ComponentConfigurationToComponentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentConfigurationId):
            self.subject = ComponentConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationToComponentAssociation(Association):
    """
    Any association between a application and a component. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationToComponentAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationToComponentAssociation"
    class_name: ClassVar[str] = "application to component association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationToComponentAssociation

    id: Union[str, ApplicationToComponentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, Application] = None
    object: Union[str, ComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationToComponentAssociationId):
            self.id = ApplicationToComponentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, Application):
            self.subject = Application(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationToApplicationTypeAssociation(Association):
    """
    Any association between a application and a application type. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationToApplicationTypeAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationToApplicationTypeAssociation"
    class_name: ClassVar[str] = "application to application type association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationToApplicationTypeAssociation

    id: Union[str, ApplicationToApplicationTypeAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, Application] = None
    object: Union[str, ApplicationTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationToApplicationTypeAssociationId):
            self.id = ApplicationToApplicationTypeAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, Application):
            self.subject = Application(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ApplicationTypeId):
            self.object = ApplicationTypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationConfigurationToApplicationAssociation(Association):
    """
    Any association between a application configuration and a application. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationConfigurationToApplicationAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationConfigurationToApplicationAssociation"
    class_name: ClassVar[str] = "application configuration to application association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationConfigurationToApplicationAssociation

    id: Union[str, ApplicationConfigurationToApplicationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ApplicationConfigurationId] = None
    object: Union[dict, Application] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationConfigurationToApplicationAssociationId):
            self.id = ApplicationConfigurationToApplicationAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ApplicationConfigurationId):
            self.subject = ApplicationConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Application):
            self.object = Application(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationInstanceConfigurationToApplicationInstanceAssociation(Association):
    """
    Any association between a application instance configuration and a application instance. There is no assumption of
    cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceConfigurationToApplicationInstanceAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationInstanceConfigurationToApplicationInstanceAssociation"
    class_name: ClassVar[str] = "application instance configuration to application instance association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationInstanceConfigurationToApplicationInstanceAssociation

    id: Union[str, ApplicationInstanceConfigurationToApplicationInstanceAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ApplicationInstanceConfigurationId] = None
    object: Union[str, ApplicationInstanceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationInstanceConfigurationToApplicationInstanceAssociationId):
            self.id = ApplicationInstanceConfigurationToApplicationInstanceAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ApplicationInstanceConfigurationId):
            self.subject = ApplicationInstanceConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ApplicationInstanceId):
            self.object = ApplicationInstanceId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationUserLoginToApplicationUserAssociation(Association):
    """
    Any association between a application user login and a application user. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ApplicationUserLoginToApplicationUserAssociation
    class_class_curie: ClassVar[str] = "testlink:ApplicationUserLoginToApplicationUserAssociation"
    class_name: ClassVar[str] = "application user login to application user association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ApplicationUserLoginToApplicationUserAssociation

    id: Union[str, ApplicationUserLoginToApplicationUserAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ApplicationUserLoginId] = None
    object: Union[str, ApplicationUserId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ApplicationUserLoginToApplicationUserAssociationId):
            self.id = ApplicationUserLoginToApplicationUserAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ApplicationUserLoginId):
            self.subject = ApplicationUserLoginId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ApplicationUserId):
            self.object = ApplicationUserId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EmailToApplicationUserAssociation(Association):
    """
    Any association between a email and a application user. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmailToApplicationUserAssociation
    class_class_curie: ClassVar[str] = "testlink:EmailToApplicationUserAssociation"
    class_name: ClassVar[str] = "email to application user association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmailToApplicationUserAssociation

    id: Union[str, EmailToApplicationUserAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, EmailId] = None
    object: Union[str, ApplicationUserId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmailToApplicationUserAssociationId):
            self.id = EmailToApplicationUserAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, EmailId):
            self.subject = EmailId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ApplicationUserId):
            self.object = ApplicationUserId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentOwnerToApplicationUserAssociation(Association):
    """
    Any association between a component owner and a application user. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentOwnerToApplicationUserAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentOwnerToApplicationUserAssociation"
    class_name: ClassVar[str] = "component owner to application user association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentOwnerToApplicationUserAssociation

    id: Union[str, ComponentOwnerToApplicationUserAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ComponentOwnerId] = None
    object: Union[str, ApplicationUserId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentOwnerToApplicationUserAssociationId):
            self.id = ComponentOwnerToApplicationUserAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentOwnerId):
            self.subject = ComponentOwnerId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ApplicationUserId):
            self.object = ApplicationUserId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentOwnerToComponentAssociation(Association):
    """
    Any association between a component owner and a component. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentOwnerToComponentAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentOwnerToComponentAssociation"
    class_name: ClassVar[str] = "component owner to component association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentOwnerToComponentAssociation

    id: Union[str, ComponentOwnerToComponentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ComponentOwnerId] = None
    object: Union[str, ComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentOwnerToComponentAssociationId):
            self.id = ComponentOwnerToComponentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentOwnerId):
            self.subject = ComponentOwnerId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class BuildToApplicationUserLoginAssociation(Association):
    """
    Any association between a build and a application user login. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.BuildToApplicationUserLoginAssociation
    class_class_curie: ClassVar[str] = "testlink:BuildToApplicationUserLoginAssociation"
    class_name: ClassVar[str] = "build to application user login association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BuildToApplicationUserLoginAssociation

    id: Union[str, BuildToApplicationUserLoginAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, BuildId] = None
    object: Union[str, ApplicationUserLoginId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BuildToApplicationUserLoginAssociationId):
            self.id = BuildToApplicationUserLoginAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, BuildId):
            self.subject = BuildId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ApplicationUserLoginId):
            self.object = ApplicationUserLoginId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class BuildToVcsRootAssociation(Association):
    """
    Any association between a build and a vcs root. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.BuildToVcsRootAssociation
    class_class_curie: ClassVar[str] = "testlink:BuildToVcsRootAssociation"
    class_name: ClassVar[str] = "build to vcs root association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BuildToVcsRootAssociation

    id: Union[str, BuildToVcsRootAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, BuildId] = None
    object: Union[str, VcsRootId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BuildToVcsRootAssociationId):
            self.id = BuildToVcsRootAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, BuildId):
            self.subject = BuildId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, VcsRootId):
            self.object = VcsRootId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class BuildToProjectAssociation(Association):
    """
    Any association between a build and a project. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.BuildToProjectAssociation
    class_class_curie: ClassVar[str] = "testlink:BuildToProjectAssociation"
    class_name: ClassVar[str] = "build to project association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BuildToProjectAssociation

    id: Union[str, BuildToProjectAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, BuildId] = None
    object: Union[str, ProjectId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BuildToProjectAssociationId):
            self.id = BuildToProjectAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, BuildId):
            self.subject = BuildId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ProjectId):
            self.object = ProjectId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class BuildToApplicationInstanceAssociation(Association):
    """
    Any association between a build and a application instance. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.BuildToApplicationInstanceAssociation
    class_class_curie: ClassVar[str] = "testlink:BuildToApplicationInstanceAssociation"
    class_name: ClassVar[str] = "build to application instance association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BuildToApplicationInstanceAssociation

    id: Union[str, BuildToApplicationInstanceAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, BuildId] = None
    object: Union[str, ApplicationInstanceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BuildToApplicationInstanceAssociationId):
            self.id = BuildToApplicationInstanceAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, BuildId):
            self.subject = BuildId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ApplicationInstanceId):
            self.object = ApplicationInstanceId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class BuildConfigurationToBuildAssociation(Association):
    """
    Any association between a build configuration and a build. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.BuildConfigurationToBuildAssociation
    class_class_curie: ClassVar[str] = "testlink:BuildConfigurationToBuildAssociation"
    class_name: ClassVar[str] = "build configuration to build association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BuildConfigurationToBuildAssociation

    id: Union[str, BuildConfigurationToBuildAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, BuildConfigurationId] = None
    object: Union[str, BuildId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BuildConfigurationToBuildAssociationId):
            self.id = BuildConfigurationToBuildAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, BuildConfigurationId):
            self.subject = BuildConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, BuildId):
            self.object = BuildId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentToBuildAssociation(Association):
    """
    Any association between a deployment and a build. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DeploymentToBuildAssociation
    class_class_curie: ClassVar[str] = "testlink:DeploymentToBuildAssociation"
    class_name: ClassVar[str] = "deployment to build association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DeploymentToBuildAssociation

    id: Union[str, DeploymentToBuildAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, DeploymentId] = None
    object: Union[str, BuildId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentToBuildAssociationId):
            self.id = DeploymentToBuildAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentId):
            self.subject = DeploymentId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, BuildId):
            self.object = BuildId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentToApplicationUserLoginAssociation(Association):
    """
    Any association between a deployment and a application user login. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DeploymentToApplicationUserLoginAssociation
    class_class_curie: ClassVar[str] = "testlink:DeploymentToApplicationUserLoginAssociation"
    class_name: ClassVar[str] = "deployment to application user login association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DeploymentToApplicationUserLoginAssociation

    id: Union[str, DeploymentToApplicationUserLoginAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, DeploymentId] = None
    object: Union[str, ApplicationUserLoginId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentToApplicationUserLoginAssociationId):
            self.id = DeploymentToApplicationUserLoginAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentId):
            self.subject = DeploymentId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ApplicationUserLoginId):
            self.object = ApplicationUserLoginId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentConfigurationToDeploymentAssociation(Association):
    """
    Any association between a deployment configuration and a deployment. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DeploymentConfigurationToDeploymentAssociation
    class_class_curie: ClassVar[str] = "testlink:DeploymentConfigurationToDeploymentAssociation"
    class_name: ClassVar[str] = "deployment configuration to deployment association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DeploymentConfigurationToDeploymentAssociation

    id: Union[str, DeploymentConfigurationToDeploymentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, DeploymentConfigurationId] = None
    object: Union[str, DeploymentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentConfigurationToDeploymentAssociationId):
            self.id = DeploymentConfigurationToDeploymentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentConfigurationId):
            self.subject = DeploymentConfigurationId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentId):
            self.object = DeploymentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServerGroupToServerTypeAssociation(Association):
    """
    Any association between a server group and a server type. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerGroupToServerTypeAssociation
    class_class_curie: ClassVar[str] = "testlink:ServerGroupToServerTypeAssociation"
    class_name: ClassVar[str] = "server group to server type association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerGroupToServerTypeAssociation

    id: Union[str, ServerGroupToServerTypeAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServerGroupId] = None
    object: Union[str, ServerTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServerGroupToServerTypeAssociationId):
            self.id = ServerGroupToServerTypeAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServerGroupId):
            self.subject = ServerGroupId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServerTypeId):
            self.object = ServerTypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServerHubToServerAssociation(Association):
    """
    Any association between a server hub and a server. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerHubToServerAssociation
    class_class_curie: ClassVar[str] = "testlink:ServerHubToServerAssociation"
    class_name: ClassVar[str] = "server hub to server association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerHubToServerAssociation

    id: Union[str, ServerHubToServerAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServerHubId] = None
    object: Union[str, ServerId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServerHubToServerAssociationId):
            self.id = ServerHubToServerAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServerHubId):
            self.subject = ServerHubId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServerId):
            self.object = ServerId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServerHubToServerGroupHubAssociation(Association):
    """
    Any association between a server hub and a server group hub. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerHubToServerGroupHubAssociation
    class_class_curie: ClassVar[str] = "testlink:ServerHubToServerGroupHubAssociation"
    class_name: ClassVar[str] = "server hub to server group hub association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerHubToServerGroupHubAssociation

    id: Union[str, ServerHubToServerGroupHubAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServerHubId] = None
    object: Union[str, ServerGroupHubId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServerHubToServerGroupHubAssociationId):
            self.id = ServerHubToServerGroupHubAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServerHubId):
            self.subject = ServerHubId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServerGroupHubId):
            self.object = ServerGroupHubId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServerGroupHubToDomainEnvironmentAssociation(Association):
    """
    Any association between a server group hub and a domain environment. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerGroupHubToDomainEnvironmentAssociation
    class_class_curie: ClassVar[str] = "testlink:ServerGroupHubToDomainEnvironmentAssociation"
    class_name: ClassVar[str] = "server group hub to domain environment association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerGroupHubToDomainEnvironmentAssociation

    id: Union[str, ServerGroupHubToDomainEnvironmentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServerGroupHubId] = None
    object: Union[str, DomainEnvironmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServerGroupHubToDomainEnvironmentAssociationId):
            self.id = ServerGroupHubToDomainEnvironmentAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServerGroupHubId):
            self.subject = ServerGroupHubId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DomainEnvironmentId):
            self.object = DomainEnvironmentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServerGroupHubToServerGroupAssociation(Association):
    """
    Any association between a server group hub and a server group. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServerGroupHubToServerGroupAssociation
    class_class_curie: ClassVar[str] = "testlink:ServerGroupHubToServerGroupAssociation"
    class_name: ClassVar[str] = "server group hub to server group association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServerGroupHubToServerGroupAssociation

    id: Union[str, ServerGroupHubToServerGroupAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServerGroupHubId] = None
    object: Union[str, ServerGroupId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServerGroupHubToServerGroupAssociationId):
            self.id = ServerGroupHubToServerGroupAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServerGroupHubId):
            self.subject = ServerGroupHubId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServerGroupId):
            self.object = ServerGroupId(self.object)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.has_attribute = Slot(uri=TESTLINK.has_attribute, name="has attribute", curie=TESTLINK.curie('has_attribute'),
                   model_uri=TESTLINK.has_attribute, domain=None, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.has_attribute_type = Slot(uri=TESTLINK.has_attribute_type, name="has attribute type", curie=TESTLINK.curie('has_attribute_type'),
                   model_uri=TESTLINK.has_attribute_type, domain=AttributeType, range=Union[str, OntologyClassId])

slots.has_qualitative_value = Slot(uri=TESTLINK.has_qualitative_value, name="has qualitative value", curie=TESTLINK.curie('has_qualitative_value'),
                   model_uri=TESTLINK.has_qualitative_value, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.has_quantitative_value = Slot(uri=TESTLINK.has_quantitative_value, name="has quantitative value", curie=TESTLINK.curie('has_quantitative_value'),
                   model_uri=TESTLINK.has_quantitative_value, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.has_numeric_value = Slot(uri=TESTLINK.has_numeric_value, name="has numeric value", curie=TESTLINK.curie('has_numeric_value'),
                   model_uri=TESTLINK.has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.has_unit = Slot(uri=TESTLINK.has_unit, name="has unit", curie=TESTLINK.curie('has_unit'),
                   model_uri=TESTLINK.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.node_property = Slot(uri=TESTLINK.node_property, name="node property", curie=TESTLINK.curie('node_property'),
                   model_uri=TESTLINK.node_property, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=TESTLINK.id, name="id", curie=TESTLINK.curie('id'),
                   model_uri=TESTLINK.id, domain=None, range=URIRef)

slots.iri = Slot(uri=TESTLINK.iri, name="iri", curie=TESTLINK.curie('iri'),
                   model_uri=TESTLINK.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=TESTLINK.type, domain=None, range=Optional[str])

slots.category = Slot(uri=TESTLINK.category, name="category", curie=TESTLINK.curie('category'),
                   model_uri=TESTLINK.category, domain=Entity, range=Union[Union[str, CategoryType], List[Union[str, CategoryType]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=TESTLINK.name, domain=None, range=Optional[Union[str, LabelType]])

slots.first_name = Slot(uri=TESTLINK.first_name, name="first name", curie=TESTLINK.curie('first_name'),
                   model_uri=TESTLINK.first_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.last_name = Slot(uri=TESTLINK.last_name, name="last name", curie=TESTLINK.curie('last_name'),
                   model_uri=TESTLINK.last_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.source = Slot(uri=TESTLINK.source, name="source", curie=TESTLINK.curie('source'),
                   model_uri=TESTLINK.source, domain=None, range=Optional[Union[str, LabelType]])

slots.xref = Slot(uri=TESTLINK.xref, name="xref", curie=TESTLINK.curie('xref'),
                   model_uri=TESTLINK.xref, domain=NamedThing, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=TESTLINK.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.affiliation = Slot(uri=TESTLINK.affiliation, name="affiliation", curie=TESTLINK.curie('affiliation'),
                   model_uri=TESTLINK.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=TESTLINK.address, name="address", curie=TESTLINK.curie('address'),
                   model_uri=TESTLINK.address, domain=NamedThing, range=Optional[str])

slots.timepoint = Slot(uri=TESTLINK.timepoint, name="timepoint", curie=TESTLINK.curie('timepoint'),
                   model_uri=TESTLINK.timepoint, domain=NamedThing, range=Optional[Union[str, TimeType]])

slots.creation_date = Slot(uri=TESTLINK.creation_date, name="creation date", curie=TESTLINK.curie('creation_date'),
                   model_uri=TESTLINK.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.created = Slot(uri=TESTLINK.created, name="created", curie=TESTLINK.curie('created'),
                   model_uri=TESTLINK.created, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.release_date = Slot(uri=TESTLINK.release_date, name="release date", curie=TESTLINK.curie('release_date'),
                   model_uri=TESTLINK.release_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.update_date = Slot(uri=TESTLINK.update_date, name="update date", curie=TESTLINK.curie('update_date'),
                   model_uri=TESTLINK.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.updated = Slot(uri=TESTLINK.updated, name="updated", curie=TESTLINK.curie('updated'),
                   model_uri=TESTLINK.updated, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.has_dataset = Slot(uri=DCT.source, name="has dataset", curie=DCT.curie('source'),
                   model_uri=TESTLINK.has_dataset, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.version = Slot(uri=TESTLINK.version, name="version", curie=TESTLINK.curie('version'),
                   model_uri=TESTLINK.version, domain=Dataset, range=Optional[str])

slots.license = Slot(uri=TESTLINK.license, name="license", curie=TESTLINK.curie('license'),
                   model_uri=TESTLINK.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=TESTLINK.rights, name="rights", curie=TESTLINK.curie('rights'),
                   model_uri=TESTLINK.rights, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=TESTLINK.format, name="format", curie=TESTLINK.curie('format'),
                   model_uri=TESTLINK.format, domain=InformationContentEntity, range=Optional[str])

slots.download_url = Slot(uri=DCAT.downloadURL, name="download url", curie=DCAT.curie('downloadURL'),
                   model_uri=TESTLINK.download_url, domain=None, range=Optional[str])

slots.dataset_download_url = Slot(uri=DCAT.downloadURL, name="dataset download url", curie=DCAT.curie('downloadURL'),
                   model_uri=TESTLINK.dataset_download_url, domain=Dataset, range=Optional[str])

slots.distribution_download_url = Slot(uri=TESTLINK.distribution_download_url, name="distribution download url", curie=TESTLINK.curie('distribution_download_url'),
                   model_uri=TESTLINK.distribution_download_url, domain=DatasetDistribution, range=Optional[str])

slots.ingest_date = Slot(uri=PAV.version, name="ingest date", curie=PAV.curie('version'),
                   model_uri=TESTLINK.ingest_date, domain=DatasetVersion, range=Optional[str])

slots.has_distribution = Slot(uri=DCT.distribution, name="has distribution", curie=DCT.curie('distribution'),
                   model_uri=TESTLINK.has_distribution, domain=DatasetVersion, range=Optional[Union[str, DatasetDistributionId]])

slots.authors = Slot(uri=TESTLINK.authors, name="authors", curie=TESTLINK.curie('authors'),
                   model_uri=TESTLINK.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.pages = Slot(uri=TESTLINK.pages, name="pages", curie=TESTLINK.curie('pages'),
                   model_uri=TESTLINK.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=TESTLINK.summary, name="summary", curie=TESTLINK.curie('summary'),
                   model_uri=TESTLINK.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=TESTLINK.keywords, name="keywords", curie=TESTLINK.curie('keywords'),
                   model_uri=TESTLINK.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.lcsh_terms = Slot(uri=TESTLINK.lcsh_terms, name="lcsh terms", curie=TESTLINK.curie('lcsh_terms'),
                   model_uri=TESTLINK.lcsh_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.has_computational_sequence = Slot(uri=TESTLINK.has_computational_sequence, name="has computational sequence", curie=TESTLINK.curie('has_computational_sequence'),
                   model_uri=TESTLINK.has_computational_sequence, domain=NamedThing, range=Optional[Union[str, ComputationalSequence]])

slots.has_homogeneity = Slot(uri=TESTLINK.has_homogeneity, name="has homogeneity", curie=TESTLINK.curie('has_homogeneity'),
                   model_uri=TESTLINK.has_homogeneity, domain=WorkloadEntity, range=Optional[Union[dict, "Homogeneity"]])

slots.has_control_actor = Slot(uri=TESTLINK.has_control_actor, name="has control actor", curie=TESTLINK.curie('has_control_actor'),
                   model_uri=TESTLINK.has_control_actor, domain=NamedThing, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.related_to = Slot(uri=TESTLINK.related_to, name="related to", curie=TESTLINK.curie('related_to'),
                   model_uri=TESTLINK.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributor = Slot(uri=TESTLINK.contributor, name="contributor", curie=TESTLINK.curie('contributor'),
                   model_uri=TESTLINK.contributor, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.author = Slot(uri=TESTLINK.author, name="author", curie=TESTLINK.curie('author'),
                   model_uri=TESTLINK.author, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.interacts_with = Slot(uri=TESTLINK.interacts_with, name="interacts with", curie=TESTLINK.curie('interacts_with'),
                   model_uri=TESTLINK.interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.overlaps = Slot(uri=TESTLINK.overlaps, name="overlaps", curie=TESTLINK.curie('overlaps'),
                   model_uri=TESTLINK.overlaps, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_part = Slot(uri=TESTLINK.has_part, name="has part", curie=TESTLINK.curie('has_part'),
                   model_uri=TESTLINK.has_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.part_of = Slot(uri=TESTLINK.part_of, name="part of", curie=TESTLINK.curie('part_of'),
                   model_uri=TESTLINK.part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_input = Slot(uri=TESTLINK.has_input, name="has input", curie=TESTLINK.curie('has_input'),
                   model_uri=TESTLINK.has_input, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_output = Slot(uri=TESTLINK.has_output, name="has output", curie=TESTLINK.curie('has_output'),
                   model_uri=TESTLINK.has_output, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_participant = Slot(uri=TESTLINK.has_participant, name="has participant", curie=TESTLINK.curie('has_participant'),
                   model_uri=TESTLINK.has_participant, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.participates_in = Slot(uri=TESTLINK.participates_in, name="participates in", curie=TESTLINK.curie('participates_in'),
                   model_uri=TESTLINK.participates_in, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.enables = Slot(uri=TESTLINK.enables, name="enables", curie=TESTLINK.curie('enables'),
                   model_uri=TESTLINK.enables, domain=CyberEntity, range=Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]])

slots.enabled_by = Slot(uri=TESTLINK.enabled_by, name="enabled by", curie=TESTLINK.curie('enabled_by'),
                   model_uri=TESTLINK.enabled_by, domain=ComputationalProcessOrActivity, range=Optional[Union[Union[str, CyberEntityId], List[Union[str, CyberEntityId]]]])

slots.notification_component_of = Slot(uri=TESTLINK.notification_component_of, name="notification component of", curie=TESTLINK.curie('notification_component_of'),
                   model_uri=TESTLINK.notification_component_of, domain=NotificationComponent, range=Optional[Union[Union[str, NotificationId], List[Union[str, NotificationId]]]])

slots.has_notification_component = Slot(uri=TESTLINK.has_notification_component, name="has notification component", curie=TESTLINK.curie('has_notification_component'),
                   model_uri=TESTLINK.has_notification_component, domain=Notification, range=Optional[Union[Union[str, NotificationComponentId], List[Union[str, NotificationComponentId]]]])

slots.data_of = Slot(uri=TESTLINK.data_of, name="data of", curie=TESTLINK.curie('data_of'),
                   model_uri=TESTLINK.data_of, domain=NotificationComponent, range=Optional[Union[Union[str, NotificationId], List[Union[str, NotificationId]]]])

slots.has_data = Slot(uri=TESTLINK.has_data, name="has data", curie=TESTLINK.curie('has_data'),
                   model_uri=TESTLINK.has_data, domain=Notification, range=Optional[Union[Union[str, DataId], List[Union[str, DataId]]]])

slots.produces = Slot(uri=TESTLINK.produces, name="produces", curie=TESTLINK.curie('produces'),
                   model_uri=TESTLINK.produces, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.produced_by = Slot(uri=TESTLINK.produced_by, name="produced by", curie=TESTLINK.curie('produced_by'),
                   model_uri=TESTLINK.produced_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_taxon = Slot(uri=TESTLINK.in_taxon, name="in taxon", curie=TESTLINK.curie('in_taxon'),
                   model_uri=TESTLINK.in_taxon, domain=None, range=Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]])

slots.internal_version = Slot(uri=TESTLINK.internal_version, name="internal version", curie=TESTLINK.curie('internal_version'),
                   model_uri=TESTLINK.internal_version, domain=Dataset, range=Optional[str])

slots.vcs_revision = Slot(uri=TESTLINK.vcs_revision, name="vcs revision", curie=TESTLINK.curie('vcs_revision'),
                   model_uri=TESTLINK.vcs_revision, domain=Dataset, range=Optional[str])

slots.enabled = Slot(uri=TESTLINK.enabled, name="enabled", curie=TESTLINK.curie('enabled'),
                   model_uri=TESTLINK.enabled, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.archived = Slot(uri=TESTLINK.archived, name="archived", curie=TESTLINK.curie('archived'),
                   model_uri=TESTLINK.archived, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.note = Slot(uri=TESTLINK.note, name="note", curie=TESTLINK.curie('note'),
                   model_uri=TESTLINK.note, domain=NamedThing, range=Optional[Union[str, NarrativeText]])

slots.fqdn = Slot(uri=TESTLINK.fqdn, name="fqdn", curie=TESTLINK.curie('fqdn'),
                   model_uri=TESTLINK.fqdn, domain=None, range=Optional[Union[str, LabelType]])

slots.value = Slot(uri=TESTLINK.value, name="value", curie=TESTLINK.curie('value'),
                   model_uri=TESTLINK.value, domain=NamedThing, range=Optional[Union[dict, QuantityValue]])

slots.project_id = Slot(uri=TESTLINK.project_id, name="project id", curie=TESTLINK.curie('project_id'),
                   model_uri=TESTLINK.project_id, domain=None, range=URIRef)

slots.ticket_id = Slot(uri=TESTLINK.ticket_id, name="ticket id", curie=TESTLINK.curie('ticket_id'),
                   model_uri=TESTLINK.ticket_id, domain=None, range=URIRef)

slots.environment = Slot(uri=TESTLINK.environment, name="environment", curie=TESTLINK.curie('environment'),
                   model_uri=TESTLINK.environment, domain=None, range=Optional[Union[str, LabelType]])

slots.component = Slot(uri=TESTLINK.component, name="component", curie=TESTLINK.curie('component'),
                   model_uri=TESTLINK.component, domain=None, range=Optional[Union[str, LabelType]])

slots.component_fixed = Slot(uri=TESTLINK.component_fixed, name="component fixed", curie=TESTLINK.curie('component_fixed'),
                   model_uri=TESTLINK.component_fixed, domain=None, range=Optional[Union[str, LabelType]])

slots.tag = Slot(uri=TESTLINK.tag, name="tag", curie=TESTLINK.curie('tag'),
                   model_uri=TESTLINK.tag, domain=None, range=Optional[Union[str, LabelType]])

slots.tag_name = Slot(uri=TESTLINK.tag_name, name="tag name", curie=TESTLINK.curie('tag_name'),
                   model_uri=TESTLINK.tag_name, domain=None, range=Optional[Union[str, LabelType]])

slots.g_c_number = Slot(uri=TESTLINK.g_c_number, name="g c number", curie=TESTLINK.curie('g_c_number'),
                   model_uri=TESTLINK.g_c_number, domain=None, range=Optional[Union[str, LabelType]])

slots.global_version = Slot(uri=TESTLINK.global_version, name="global version", curie=TESTLINK.curie('global_version'),
                   model_uri=TESTLINK.global_version, domain=Dataset, range=Optional[str])

slots.login = Slot(uri=TESTLINK.login, name="login", curie=TESTLINK.curie('login'),
                   model_uri=TESTLINK.login, domain=None, range=Optional[str])

slots.user_login = Slot(uri=TESTLINK.user_login, name="user login", curie=TESTLINK.curie('user_login'),
                   model_uri=TESTLINK.user_login, domain=None, range=Optional[str])

slots.build_number = Slot(uri=TESTLINK.build_number, name="build number", curie=TESTLINK.curie('build_number'),
                   model_uri=TESTLINK.build_number, domain=None, range=URIRef)

slots.production_build_number = Slot(uri=TESTLINK.production_build_number, name="production build number", curie=TESTLINK.curie('production_build_number'),
                   model_uri=TESTLINK.production_build_number, domain=None, range=URIRef)

slots.release_id = Slot(uri=TESTLINK.release_id, name="release id", curie=TESTLINK.curie('release_id'),
                   model_uri=TESTLINK.release_id, domain=None, range=URIRef)

slots.production_release_id = Slot(uri=TESTLINK.production_release_id, name="production release id", curie=TESTLINK.curie('production_release_id'),
                   model_uri=TESTLINK.production_release_id, domain=None, range=URIRef)

slots.svn_tag_url = Slot(uri=TESTLINK.svn_tag_url, name="svn tag url", curie=TESTLINK.curie('svn_tag_url'),
                   model_uri=TESTLINK.svn_tag_url, domain=None, range=Optional[Union[str, IriType]])

slots.environment_id = Slot(uri=TESTLINK.environment_id, name="environment id", curie=TESTLINK.curie('environment_id'),
                   model_uri=TESTLINK.environment_id, domain=None, range=URIRef)

slots.application_id = Slot(uri=TESTLINK.application_id, name="application id", curie=TESTLINK.curie('application_id'),
                   model_uri=TESTLINK.application_id, domain=None, range=URIRef)

slots.application_instance_id = Slot(uri=TESTLINK.application_instance_id, name="application instance id", curie=TESTLINK.curie('application_instance_id'),
                   model_uri=TESTLINK.application_instance_id, domain=None, range=URIRef)

slots.user_name = Slot(uri=TESTLINK.user_name, name="user name", curie=TESTLINK.curie('user_name'),
                   model_uri=TESTLINK.user_name, domain=None, range=Optional[Union[str, LabelType]])

slots.domain_name = Slot(uri=TESTLINK.domain_name, name="domain name", curie=TESTLINK.curie('domain_name'),
                   model_uri=TESTLINK.domain_name, domain=None, range=Optional[Union[str, LabelType]])

slots.application_user = Slot(uri=TESTLINK.application_user, name="application user", curie=TESTLINK.curie('application_user'),
                   model_uri=TESTLINK.application_user, domain=None, range=Optional[Union[str, LabelType]])

slots.application_user_login = Slot(uri=TESTLINK.application_user_login, name="application user login", curie=TESTLINK.curie('application_user_login'),
                   model_uri=TESTLINK.application_user_login, domain=None, range=Optional[str])

slots.component_id = Slot(uri=TESTLINK.component_id, name="component id", curie=TESTLINK.curie('component_id'),
                   model_uri=TESTLINK.component_id, domain=None, range=URIRef)

slots.application_user_id = Slot(uri=TESTLINK.application_user_id, name="application user id", curie=TESTLINK.curie('application_user_id'),
                   model_uri=TESTLINK.application_user_id, domain=None, range=URIRef)

slots.application_user_login_id = Slot(uri=TESTLINK.application_user_login_id, name="application user login id", curie=TESTLINK.curie('application_user_login_id'),
                   model_uri=TESTLINK.application_user_login_id, domain=None, range=URIRef)

slots.vcs_root_id = Slot(uri=TESTLINK.vcs_root_id, name="vcs root id", curie=TESTLINK.curie('vcs_root_id'),
                   model_uri=TESTLINK.vcs_root_id, domain=None, range=URIRef)

slots.location = Slot(uri=TESTLINK.location, name="location", curie=TESTLINK.curie('location'),
                   model_uri=TESTLINK.location, domain=NamedThing, range=Optional[str])

slots.vcs_location = Slot(uri=TESTLINK.vcs_location, name="vcs location", curie=TESTLINK.curie('vcs_location'),
                   model_uri=TESTLINK.vcs_location, domain=NamedThing, range=Optional[str])

slots.association_slot = Slot(uri=TESTLINK.association_slot, name="association slot", curie=TESTLINK.curie('association_slot'),
                   model_uri=TESTLINK.association_slot, domain=Association, range=Optional[str])

slots.association_id = Slot(uri=TESTLINK.id, name="association_id", curie=TESTLINK.curie('id'),
                   model_uri=TESTLINK.association_id, domain=Association, range=Union[str, AssociationId])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=TESTLINK.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=TESTLINK.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=TESTLINK.predicate, domain=Association, range=Union[str, PredicateType])

slots.relation = Slot(uri=TESTLINK.relation, name="relation", curie=TESTLINK.curie('relation'),
                   model_uri=TESTLINK.relation, domain=Association, range=Union[str, URIorCURIE])

slots.negated = Slot(uri=TESTLINK.negated, name="negated", curie=TESTLINK.curie('negated'),
                   model_uri=TESTLINK.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.provided_by = Slot(uri=TESTLINK.provided_by, name="provided by", curie=TESTLINK.curie('provided_by'),
                   model_uri=TESTLINK.provided_by, domain=Association, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.association_type = Slot(uri=TESTLINK.association_type, name="association type", curie=TESTLINK.curie('association_type'),
                   model_uri=TESTLINK.association_type, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.qualifiers = Slot(uri=TESTLINK.qualifiers, name="qualifiers", curie=TESTLINK.curie('qualifiers'),
                   model_uri=TESTLINK.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.frequency_qualifier = Slot(uri=TESTLINK.frequency_qualifier, name="frequency qualifier", curie=TESTLINK.curie('frequency_qualifier'),
                   model_uri=TESTLINK.frequency_qualifier, domain=Association, range=Optional[Union[dict, FrequencyValue]])

slots.severity_qualifier = Slot(uri=TESTLINK.severity_qualifier, name="severity qualifier", curie=TESTLINK.curie('severity_qualifier'),
                   model_uri=TESTLINK.severity_qualifier, domain=Association, range=Optional[Union[dict, SeverityValue]])

slots.publications = Slot(uri=TESTLINK.publications, name="publications", curie=TESTLINK.curie('publications'),
                   model_uri=TESTLINK.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.has_taxonomic_rank = Slot(uri=TESTLINK.has_taxonomic_rank, name="has taxonomic rank", curie=TESTLINK.curie('has_taxonomic_rank'),
                   model_uri=TESTLINK.has_taxonomic_rank, domain=None, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.subclass_of = Slot(uri=TESTLINK.subclass_of, name="subclass of", curie=TESTLINK.curie('subclass_of'),
                   model_uri=TESTLINK.subclass_of, domain=None, range=Optional[Union[str, SystemTaxonId]])

slots.attribute_name = Slot(uri=TESTLINK.name, name="attribute_name", curie=TESTLINK.curie('name'),
                   model_uri=TESTLINK.attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.named_thing_category = Slot(uri=TESTLINK.category, name="named thing_category", curie=TESTLINK.curie('category'),
                   model_uri=TESTLINK.named_thing_category, domain=NamedThing, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.operational_activity_has_input = Slot(uri=TESTLINK.has_input, name="operational activity_has input", curie=TESTLINK.curie('has_input'),
                   model_uri=TESTLINK.operational_activity_has_input, domain=OperationalActivity, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.operational_activity_has_output = Slot(uri=TESTLINK.has_output, name="operational activity_has output", curie=TESTLINK.curie('has_output'),
                   model_uri=TESTLINK.operational_activity_has_output, domain=OperationalActivity, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.operational_activity_enabled_by = Slot(uri=TESTLINK.enabled_by, name="operational activity_enabled by", curie=TESTLINK.curie('enabled_by'),
                   model_uri=TESTLINK.operational_activity_enabled_by, domain=OperationalActivity, range=Optional[Union[Union[dict, "MacrooperationalMachineMixin"], List[Union[dict, "MacrooperationalMachineMixin"]]]])

slots.systemic_entity_has_attribute = Slot(uri=TESTLINK.has_attribute, name="systemic entity_has attribute", curie=TESTLINK.curie('has_attribute'),
                   model_uri=TESTLINK.systemic_entity_has_attribute, domain=SystemicEntity, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.macrooperational_machine_mixin_name = Slot(uri=TESTLINK.name, name="macrooperational machine mixin_name", curie=TESTLINK.curie('name'),
                   model_uri=TESTLINK.macrooperational_machine_mixin_name, domain=None, range=Optional[Union[str, SymbolType]])

slots.system_taxon_has_taxonomic_rank = Slot(uri=TESTLINK.has_taxonomic_rank, name="system taxon_has taxonomic rank", curie=TESTLINK.curie('has_taxonomic_rank'),
                   model_uri=TESTLINK.system_taxon_has_taxonomic_rank, domain=SystemTaxon, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.system_taxon_subclass_of = Slot(uri=TESTLINK.subclass_of, name="system taxon_subclass of", curie=TESTLINK.curie('subclass_of'),
                   model_uri=TESTLINK.system_taxon_subclass_of, domain=SystemTaxon, range=Optional[Union[str, SystemTaxonId]])

slots.agent_id = Slot(uri=TESTLINK.id, name="agent_id", curie=TESTLINK.curie('id'),
                   model_uri=TESTLINK.agent_id, domain=Agent, range=Union[str, AgentId])

slots.agent_name = Slot(uri=TESTLINK.name, name="agent_name", curie=TESTLINK.curie('name'),
                   model_uri=TESTLINK.agent_name, domain=Agent, range=Optional[Union[str, LabelType]])

slots.publication_id = Slot(uri=TESTLINK.id, name="publication_id", curie=TESTLINK.curie('id'),
                   model_uri=TESTLINK.publication_id, domain=Publication, range=Union[str, PublicationId])

slots.publication_name = Slot(uri=TESTLINK.name, name="publication_name", curie=TESTLINK.curie('name'),
                   model_uri=TESTLINK.publication_name, domain=Publication, range=Optional[Union[str, LabelType]])

slots.publication_type = Slot(uri=DCT.type, name="publication_type", curie=DCT.curie('type'),
                   model_uri=TESTLINK.publication_type, domain=Publication, range=str)

slots.publication_pages = Slot(uri=TESTLINK.pages, name="publication_pages", curie=TESTLINK.curie('pages'),
                   model_uri=TESTLINK.publication_pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.association_type = Slot(uri=TESTLINK.type, name="association_type", curie=TESTLINK.curie('type'),
                   model_uri=TESTLINK.association_type, domain=Association, range=Optional[str])

slots.association_category = Slot(uri=TESTLINK.category, name="association_category", curie=TESTLINK.curie('category'),
                   model_uri=TESTLINK.association_category, domain=Association, range=Union[Union[str, AssociationId], List[Union[str, AssociationId]]])

slots.application_instance_to_server_group_hub_association_predicate = Slot(uri=TESTLINK.predicate, name="application instance to server group hub association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_instance_to_server_group_hub_association_predicate, domain=ApplicationInstanceToServerGroupHubAssociation, range=Union[str, PredicateType])

slots.application_instance_to_server_group_hub_association_subject = Slot(uri=TESTLINK.subject, name="application instance to server group hub association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_instance_to_server_group_hub_association_subject, domain=ApplicationInstanceToServerGroupHubAssociation, range=Union[str, ApplicationInstanceId])

slots.application_instance_to_server_group_hub_association_object = Slot(uri=TESTLINK.object, name="application instance to server group hub association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_instance_to_server_group_hub_association_object, domain=ApplicationInstanceToServerGroupHubAssociation, range=Union[str, ServerGroupHubId])

slots.application_instance_to_realm_association_predicate = Slot(uri=TESTLINK.predicate, name="application instance to realm association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_instance_to_realm_association_predicate, domain=ApplicationInstanceToRealmAssociation, range=Union[str, PredicateType])

slots.application_instance_to_realm_association_subject = Slot(uri=TESTLINK.subject, name="application instance to realm association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_instance_to_realm_association_subject, domain=ApplicationInstanceToRealmAssociation, range=Union[str, ApplicationInstanceId])

slots.application_instance_to_realm_association_object = Slot(uri=TESTLINK.object, name="application instance to realm association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_instance_to_realm_association_object, domain=ApplicationInstanceToRealmAssociation, range=Union[str, RealmId])

slots.application_instance_to_domain_environment_association_predicate = Slot(uri=TESTLINK.predicate, name="application instance to domain environment association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_instance_to_domain_environment_association_predicate, domain=ApplicationInstanceToDomainEnvironmentAssociation, range=Union[str, PredicateType])

slots.application_instance_to_domain_environment_association_subject = Slot(uri=TESTLINK.subject, name="application instance to domain environment association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_instance_to_domain_environment_association_subject, domain=ApplicationInstanceToDomainEnvironmentAssociation, range=Union[str, ApplicationInstanceId])

slots.application_instance_to_domain_environment_association_object = Slot(uri=TESTLINK.object, name="application instance to domain environment association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_instance_to_domain_environment_association_object, domain=ApplicationInstanceToDomainEnvironmentAssociation, range=Union[str, DomainEnvironmentId])

slots.application_instance_to_application_association_predicate = Slot(uri=TESTLINK.predicate, name="application instance to application association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_instance_to_application_association_predicate, domain=ApplicationInstanceToApplicationAssociation, range=Union[str, PredicateType])

slots.application_instance_to_application_association_subject = Slot(uri=TESTLINK.subject, name="application instance to application association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_instance_to_application_association_subject, domain=ApplicationInstanceToApplicationAssociation, range=Union[str, ApplicationInstanceId])

slots.application_instance_to_application_association_object = Slot(uri=TESTLINK.object, name="application instance to application association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_instance_to_application_association_object, domain=ApplicationInstanceToApplicationAssociation, range=Union[dict, Application])

slots.environment_configuration_to_environment_association_predicate = Slot(uri=TESTLINK.predicate, name="environment configuration to environment association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.environment_configuration_to_environment_association_predicate, domain=EnvironmentConfigurationToEnvironmentAssociation, range=Union[str, PredicateType])

slots.environment_configuration_to_environment_association_subject = Slot(uri=TESTLINK.subject, name="environment configuration to environment association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.environment_configuration_to_environment_association_subject, domain=EnvironmentConfigurationToEnvironmentAssociation, range=Union[str, EnvironmentConfigurationId])

slots.environment_configuration_to_environment_association_object = Slot(uri=TESTLINK.object, name="environment configuration to environment association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.environment_configuration_to_environment_association_object, domain=EnvironmentConfigurationToEnvironmentAssociation, range=Union[str, EnvironmentId])

slots.domain_environment_to_domain_association_predicate = Slot(uri=TESTLINK.predicate, name="domain environment to domain association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.domain_environment_to_domain_association_predicate, domain=DomainEnvironmentToDomainAssociation, range=Union[str, PredicateType])

slots.domain_environment_to_domain_association_subject = Slot(uri=TESTLINK.subject, name="domain environment to domain association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.domain_environment_to_domain_association_subject, domain=DomainEnvironmentToDomainAssociation, range=Union[str, DomainEnvironmentId])

slots.domain_environment_to_domain_association_object = Slot(uri=TESTLINK.object, name="domain environment to domain association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.domain_environment_to_domain_association_object, domain=DomainEnvironmentToDomainAssociation, range=Union[str, DomainId])

slots.domain_environment_to_environment_association_predicate = Slot(uri=TESTLINK.predicate, name="domain environment to environment association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.domain_environment_to_environment_association_predicate, domain=DomainEnvironmentToEnvironmentAssociation, range=Union[str, PredicateType])

slots.domain_environment_to_environment_association_subject = Slot(uri=TESTLINK.subject, name="domain environment to environment association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.domain_environment_to_environment_association_subject, domain=DomainEnvironmentToEnvironmentAssociation, range=Union[str, DomainEnvironmentId])

slots.domain_environment_to_environment_association_object = Slot(uri=TESTLINK.object, name="domain environment to environment association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.domain_environment_to_environment_association_object, domain=DomainEnvironmentToEnvironmentAssociation, range=Union[str, EnvironmentId])

slots.domain_configuration_to_domain_environment_association_predicate = Slot(uri=TESTLINK.predicate, name="domain configuration to domain environment association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.domain_configuration_to_domain_environment_association_predicate, domain=DomainConfigurationToDomainEnvironmentAssociation, range=Union[str, PredicateType])

slots.domain_configuration_to_domain_environment_association_subject = Slot(uri=TESTLINK.subject, name="domain configuration to domain environment association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.domain_configuration_to_domain_environment_association_subject, domain=DomainConfigurationToDomainEnvironmentAssociation, range=Union[str, DomainConfigurationId])

slots.domain_configuration_to_domain_environment_association_object = Slot(uri=TESTLINK.object, name="domain configuration to domain environment association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.domain_configuration_to_domain_environment_association_object, domain=DomainConfigurationToDomainEnvironmentAssociation, range=Union[str, DomainEnvironmentId])

slots.realm_configuration_to_realm_association_predicate = Slot(uri=TESTLINK.predicate, name="realm configuration to realm association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.realm_configuration_to_realm_association_predicate, domain=RealmConfigurationToRealmAssociation, range=Union[str, PredicateType])

slots.realm_configuration_to_realm_association_subject = Slot(uri=TESTLINK.subject, name="realm configuration to realm association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.realm_configuration_to_realm_association_subject, domain=RealmConfigurationToRealmAssociation, range=Union[str, RealmConfigurationId])

slots.realm_configuration_to_realm_association_object = Slot(uri=TESTLINK.object, name="realm configuration to realm association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.realm_configuration_to_realm_association_object, domain=RealmConfigurationToRealmAssociation, range=Union[str, RealmId])

slots.realm_configuration_to_domain_environment_association_predicate = Slot(uri=TESTLINK.predicate, name="realm configuration to domain environment association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.realm_configuration_to_domain_environment_association_predicate, domain=RealmConfigurationToDomainEnvironmentAssociation, range=Union[str, PredicateType])

slots.realm_configuration_to_domain_environment_association_subject = Slot(uri=TESTLINK.subject, name="realm configuration to domain environment association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.realm_configuration_to_domain_environment_association_subject, domain=RealmConfigurationToDomainEnvironmentAssociation, range=Union[str, RealmConfigurationId])

slots.realm_configuration_to_domain_environment_association_object = Slot(uri=TESTLINK.object, name="realm configuration to domain environment association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.realm_configuration_to_domain_environment_association_object, domain=RealmConfigurationToDomainEnvironmentAssociation, range=Union[str, DomainEnvironmentId])

slots.component_to_vcs_root_association_predicate = Slot(uri=TESTLINK.predicate, name="component to vcs root association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.component_to_vcs_root_association_predicate, domain=ComponentToVcsRootAssociation, range=Union[str, PredicateType])

slots.component_to_vcs_root_association_subject = Slot(uri=TESTLINK.subject, name="component to vcs root association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.component_to_vcs_root_association_subject, domain=ComponentToVcsRootAssociation, range=Union[str, ComponentId])

slots.component_to_vcs_root_association_object = Slot(uri=TESTLINK.object, name="component to vcs root association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.component_to_vcs_root_association_object, domain=ComponentToVcsRootAssociation, range=Union[str, VcsRootId])

slots.component_configuration_to_component_association_predicate = Slot(uri=TESTLINK.predicate, name="component configuration to component association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.component_configuration_to_component_association_predicate, domain=ComponentConfigurationToComponentAssociation, range=Union[str, PredicateType])

slots.component_configuration_to_component_association_subject = Slot(uri=TESTLINK.subject, name="component configuration to component association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.component_configuration_to_component_association_subject, domain=ComponentConfigurationToComponentAssociation, range=Union[str, ComponentConfigurationId])

slots.component_configuration_to_component_association_object = Slot(uri=TESTLINK.object, name="component configuration to component association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.component_configuration_to_component_association_object, domain=ComponentConfigurationToComponentAssociation, range=Union[str, ComponentId])

slots.application_to_component_association_predicate = Slot(uri=TESTLINK.predicate, name="application to component association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_to_component_association_predicate, domain=ApplicationToComponentAssociation, range=Union[str, PredicateType])

slots.application_to_component_association_subject = Slot(uri=TESTLINK.subject, name="application to component association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_to_component_association_subject, domain=ApplicationToComponentAssociation, range=Union[dict, Application])

slots.application_to_component_association_object = Slot(uri=TESTLINK.object, name="application to component association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_to_component_association_object, domain=ApplicationToComponentAssociation, range=Union[str, ComponentId])

slots.application_to_application_type_association_predicate = Slot(uri=TESTLINK.predicate, name="application to application type association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_to_application_type_association_predicate, domain=ApplicationToApplicationTypeAssociation, range=Union[str, PredicateType])

slots.application_to_application_type_association_subject = Slot(uri=TESTLINK.subject, name="application to application type association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_to_application_type_association_subject, domain=ApplicationToApplicationTypeAssociation, range=Union[dict, Application])

slots.application_to_application_type_association_object = Slot(uri=TESTLINK.object, name="application to application type association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_to_application_type_association_object, domain=ApplicationToApplicationTypeAssociation, range=Union[str, ApplicationTypeId])

slots.application_configuration_to_application_association_predicate = Slot(uri=TESTLINK.predicate, name="application configuration to application association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_configuration_to_application_association_predicate, domain=ApplicationConfigurationToApplicationAssociation, range=Union[str, PredicateType])

slots.application_configuration_to_application_association_subject = Slot(uri=TESTLINK.subject, name="application configuration to application association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_configuration_to_application_association_subject, domain=ApplicationConfigurationToApplicationAssociation, range=Union[str, ApplicationConfigurationId])

slots.application_configuration_to_application_association_object = Slot(uri=TESTLINK.object, name="application configuration to application association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_configuration_to_application_association_object, domain=ApplicationConfigurationToApplicationAssociation, range=Union[dict, Application])

slots.application_instance_configuration_to_application_instance_association_predicate = Slot(uri=TESTLINK.predicate, name="application instance configuration to application instance association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_instance_configuration_to_application_instance_association_predicate, domain=ApplicationInstanceConfigurationToApplicationInstanceAssociation, range=Union[str, PredicateType])

slots.application_instance_configuration_to_application_instance_association_subject = Slot(uri=TESTLINK.subject, name="application instance configuration to application instance association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_instance_configuration_to_application_instance_association_subject, domain=ApplicationInstanceConfigurationToApplicationInstanceAssociation, range=Union[str, ApplicationInstanceConfigurationId])

slots.application_instance_configuration_to_application_instance_association_object = Slot(uri=TESTLINK.object, name="application instance configuration to application instance association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_instance_configuration_to_application_instance_association_object, domain=ApplicationInstanceConfigurationToApplicationInstanceAssociation, range=Union[str, ApplicationInstanceId])

slots.application_user_login_to_application_user_association_predicate = Slot(uri=TESTLINK.predicate, name="application user login to application user association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.application_user_login_to_application_user_association_predicate, domain=ApplicationUserLoginToApplicationUserAssociation, range=Union[str, PredicateType])

slots.application_user_login_to_application_user_association_subject = Slot(uri=TESTLINK.subject, name="application user login to application user association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.application_user_login_to_application_user_association_subject, domain=ApplicationUserLoginToApplicationUserAssociation, range=Union[str, ApplicationUserLoginId])

slots.application_user_login_to_application_user_association_object = Slot(uri=TESTLINK.object, name="application user login to application user association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.application_user_login_to_application_user_association_object, domain=ApplicationUserLoginToApplicationUserAssociation, range=Union[str, ApplicationUserId])

slots.email_to_application_user_association_predicate = Slot(uri=TESTLINK.predicate, name="email to application user association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.email_to_application_user_association_predicate, domain=EmailToApplicationUserAssociation, range=Union[str, PredicateType])

slots.email_to_application_user_association_subject = Slot(uri=TESTLINK.subject, name="email to application user association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.email_to_application_user_association_subject, domain=EmailToApplicationUserAssociation, range=Union[str, EmailId])

slots.email_to_application_user_association_object = Slot(uri=TESTLINK.object, name="email to application user association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.email_to_application_user_association_object, domain=EmailToApplicationUserAssociation, range=Union[str, ApplicationUserId])

slots.component_owner_to_application_user_association_predicate = Slot(uri=TESTLINK.predicate, name="component owner to application user association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.component_owner_to_application_user_association_predicate, domain=ComponentOwnerToApplicationUserAssociation, range=Union[str, PredicateType])

slots.component_owner_to_application_user_association_subject = Slot(uri=TESTLINK.subject, name="component owner to application user association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.component_owner_to_application_user_association_subject, domain=ComponentOwnerToApplicationUserAssociation, range=Union[str, ComponentOwnerId])

slots.component_owner_to_application_user_association_object = Slot(uri=TESTLINK.object, name="component owner to application user association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.component_owner_to_application_user_association_object, domain=ComponentOwnerToApplicationUserAssociation, range=Union[str, ApplicationUserId])

slots.component_owner_to_component_association_predicate = Slot(uri=TESTLINK.predicate, name="component owner to component association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.component_owner_to_component_association_predicate, domain=ComponentOwnerToComponentAssociation, range=Union[str, PredicateType])

slots.component_owner_to_component_association_subject = Slot(uri=TESTLINK.subject, name="component owner to component association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.component_owner_to_component_association_subject, domain=ComponentOwnerToComponentAssociation, range=Union[str, ComponentOwnerId])

slots.component_owner_to_component_association_object = Slot(uri=TESTLINK.object, name="component owner to component association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.component_owner_to_component_association_object, domain=ComponentOwnerToComponentAssociation, range=Union[str, ComponentId])

slots.build_to_application_user_login_association_predicate = Slot(uri=TESTLINK.predicate, name="build to application user login association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.build_to_application_user_login_association_predicate, domain=BuildToApplicationUserLoginAssociation, range=Union[str, PredicateType])

slots.build_to_application_user_login_association_subject = Slot(uri=TESTLINK.subject, name="build to application user login association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.build_to_application_user_login_association_subject, domain=BuildToApplicationUserLoginAssociation, range=Union[str, BuildId])

slots.build_to_application_user_login_association_object = Slot(uri=TESTLINK.object, name="build to application user login association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.build_to_application_user_login_association_object, domain=BuildToApplicationUserLoginAssociation, range=Union[str, ApplicationUserLoginId])

slots.build_to_vcs_root_association_predicate = Slot(uri=TESTLINK.predicate, name="build to vcs root association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.build_to_vcs_root_association_predicate, domain=BuildToVcsRootAssociation, range=Union[str, PredicateType])

slots.build_to_vcs_root_association_subject = Slot(uri=TESTLINK.subject, name="build to vcs root association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.build_to_vcs_root_association_subject, domain=BuildToVcsRootAssociation, range=Union[str, BuildId])

slots.build_to_vcs_root_association_object = Slot(uri=TESTLINK.object, name="build to vcs root association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.build_to_vcs_root_association_object, domain=BuildToVcsRootAssociation, range=Union[str, VcsRootId])

slots.build_to_project_association_predicate = Slot(uri=TESTLINK.predicate, name="build to project association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.build_to_project_association_predicate, domain=BuildToProjectAssociation, range=Union[str, PredicateType])

slots.build_to_project_association_subject = Slot(uri=TESTLINK.subject, name="build to project association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.build_to_project_association_subject, domain=BuildToProjectAssociation, range=Union[str, BuildId])

slots.build_to_project_association_object = Slot(uri=TESTLINK.object, name="build to project association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.build_to_project_association_object, domain=BuildToProjectAssociation, range=Union[str, ProjectId])

slots.build_to_application_instance_association_predicate = Slot(uri=TESTLINK.predicate, name="build to application instance association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.build_to_application_instance_association_predicate, domain=BuildToApplicationInstanceAssociation, range=Union[str, PredicateType])

slots.build_to_application_instance_association_subject = Slot(uri=TESTLINK.subject, name="build to application instance association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.build_to_application_instance_association_subject, domain=BuildToApplicationInstanceAssociation, range=Union[str, BuildId])

slots.build_to_application_instance_association_object = Slot(uri=TESTLINK.object, name="build to application instance association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.build_to_application_instance_association_object, domain=BuildToApplicationInstanceAssociation, range=Union[str, ApplicationInstanceId])

slots.build_configuration_to_build_association_predicate = Slot(uri=TESTLINK.predicate, name="build configuration to build association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.build_configuration_to_build_association_predicate, domain=BuildConfigurationToBuildAssociation, range=Union[str, PredicateType])

slots.build_configuration_to_build_association_subject = Slot(uri=TESTLINK.subject, name="build configuration to build association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.build_configuration_to_build_association_subject, domain=BuildConfigurationToBuildAssociation, range=Union[str, BuildConfigurationId])

slots.build_configuration_to_build_association_object = Slot(uri=TESTLINK.object, name="build configuration to build association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.build_configuration_to_build_association_object, domain=BuildConfigurationToBuildAssociation, range=Union[str, BuildId])

slots.deployment_to_build_association_predicate = Slot(uri=TESTLINK.predicate, name="deployment to build association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.deployment_to_build_association_predicate, domain=DeploymentToBuildAssociation, range=Union[str, PredicateType])

slots.deployment_to_build_association_subject = Slot(uri=TESTLINK.subject, name="deployment to build association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.deployment_to_build_association_subject, domain=DeploymentToBuildAssociation, range=Union[str, DeploymentId])

slots.deployment_to_build_association_object = Slot(uri=TESTLINK.object, name="deployment to build association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.deployment_to_build_association_object, domain=DeploymentToBuildAssociation, range=Union[str, BuildId])

slots.deployment_to_application_user_login_association_predicate = Slot(uri=TESTLINK.predicate, name="deployment to application user login association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.deployment_to_application_user_login_association_predicate, domain=DeploymentToApplicationUserLoginAssociation, range=Union[str, PredicateType])

slots.deployment_to_application_user_login_association_subject = Slot(uri=TESTLINK.subject, name="deployment to application user login association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.deployment_to_application_user_login_association_subject, domain=DeploymentToApplicationUserLoginAssociation, range=Union[str, DeploymentId])

slots.deployment_to_application_user_login_association_object = Slot(uri=TESTLINK.object, name="deployment to application user login association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.deployment_to_application_user_login_association_object, domain=DeploymentToApplicationUserLoginAssociation, range=Union[str, ApplicationUserLoginId])

slots.deployment_configuration_to_deployment_association_predicate = Slot(uri=TESTLINK.predicate, name="deployment configuration to deployment association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.deployment_configuration_to_deployment_association_predicate, domain=DeploymentConfigurationToDeploymentAssociation, range=Union[str, PredicateType])

slots.deployment_configuration_to_deployment_association_subject = Slot(uri=TESTLINK.subject, name="deployment configuration to deployment association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.deployment_configuration_to_deployment_association_subject, domain=DeploymentConfigurationToDeploymentAssociation, range=Union[str, DeploymentConfigurationId])

slots.deployment_configuration_to_deployment_association_object = Slot(uri=TESTLINK.object, name="deployment configuration to deployment association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.deployment_configuration_to_deployment_association_object, domain=DeploymentConfigurationToDeploymentAssociation, range=Union[str, DeploymentId])

slots.server_group_to_server_type_association_predicate = Slot(uri=TESTLINK.predicate, name="server group to server type association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.server_group_to_server_type_association_predicate, domain=ServerGroupToServerTypeAssociation, range=Union[str, PredicateType])

slots.server_group_to_server_type_association_subject = Slot(uri=TESTLINK.subject, name="server group to server type association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.server_group_to_server_type_association_subject, domain=ServerGroupToServerTypeAssociation, range=Union[str, ServerGroupId])

slots.server_group_to_server_type_association_object = Slot(uri=TESTLINK.object, name="server group to server type association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.server_group_to_server_type_association_object, domain=ServerGroupToServerTypeAssociation, range=Union[str, ServerTypeId])

slots.server_hub_to_server_association_predicate = Slot(uri=TESTLINK.predicate, name="server hub to server association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.server_hub_to_server_association_predicate, domain=ServerHubToServerAssociation, range=Union[str, PredicateType])

slots.server_hub_to_server_association_subject = Slot(uri=TESTLINK.subject, name="server hub to server association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.server_hub_to_server_association_subject, domain=ServerHubToServerAssociation, range=Union[str, ServerHubId])

slots.server_hub_to_server_association_object = Slot(uri=TESTLINK.object, name="server hub to server association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.server_hub_to_server_association_object, domain=ServerHubToServerAssociation, range=Union[str, ServerId])

slots.server_hub_to_server_group_hub_association_predicate = Slot(uri=TESTLINK.predicate, name="server hub to server group hub association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.server_hub_to_server_group_hub_association_predicate, domain=ServerHubToServerGroupHubAssociation, range=Union[str, PredicateType])

slots.server_hub_to_server_group_hub_association_subject = Slot(uri=TESTLINK.subject, name="server hub to server group hub association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.server_hub_to_server_group_hub_association_subject, domain=ServerHubToServerGroupHubAssociation, range=Union[str, ServerHubId])

slots.server_hub_to_server_group_hub_association_object = Slot(uri=TESTLINK.object, name="server hub to server group hub association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.server_hub_to_server_group_hub_association_object, domain=ServerHubToServerGroupHubAssociation, range=Union[str, ServerGroupHubId])

slots.server_group_hub_to_domain_environment_association_predicate = Slot(uri=TESTLINK.predicate, name="server group hub to domain environment association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.server_group_hub_to_domain_environment_association_predicate, domain=ServerGroupHubToDomainEnvironmentAssociation, range=Union[str, PredicateType])

slots.server_group_hub_to_domain_environment_association_subject = Slot(uri=TESTLINK.subject, name="server group hub to domain environment association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.server_group_hub_to_domain_environment_association_subject, domain=ServerGroupHubToDomainEnvironmentAssociation, range=Union[str, ServerGroupHubId])

slots.server_group_hub_to_domain_environment_association_object = Slot(uri=TESTLINK.object, name="server group hub to domain environment association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.server_group_hub_to_domain_environment_association_object, domain=ServerGroupHubToDomainEnvironmentAssociation, range=Union[str, DomainEnvironmentId])

slots.server_group_hub_to_server_group_association_predicate = Slot(uri=TESTLINK.predicate, name="server group hub to server group association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.server_group_hub_to_server_group_association_predicate, domain=ServerGroupHubToServerGroupAssociation, range=Union[str, PredicateType])

slots.server_group_hub_to_server_group_association_subject = Slot(uri=TESTLINK.subject, name="server group hub to server group association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.server_group_hub_to_server_group_association_subject, domain=ServerGroupHubToServerGroupAssociation, range=Union[str, ServerGroupHubId])

slots.server_group_hub_to_server_group_association_object = Slot(uri=TESTLINK.object, name="server group hub to server group association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.server_group_hub_to_server_group_association_object, domain=ServerGroupHubToServerGroupAssociation, range=Union[str, ServerGroupId])

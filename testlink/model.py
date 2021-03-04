# Auto generated from testlink-model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-17 00:01
# Schema: testlink-Model
#
# id: https://w3id.org/testlink/testlink-model
# description: Entity and association taxonomy and datamodel for computer services data
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
from includes.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ACMBOOKS = CurieNamespace('ACMBOOKS', 'https://dl.acm.org/action/doSearch?SeriesKey=acmbooks&AllField=')
ACMJOURNALS = CurieNamespace('ACMJOURNALS', 'https://dl.acm.org/action/doSearch?ConceptID=118230&AllField=')
AML = CurieNamespace('AML', 'https://w3id.org/i40/aml#')
CCDM = CurieNamespace('CCDM', 'http://cookingbigdata.com/linkeddata/ccdm#')
CCINSTANCES = CurieNamespace('CCINSTANCES', 'http://cookingbigdata.com/linkeddata/ccinstances#')
CCPRICING = CurieNamespace('CCPRICING', 'http://cookingbigdata.com/linkeddata/ccpricing#')
CCREGIONS = CurieNamespace('CCREGIONS', 'http://cookingbigdata.com/linkeddata/ccregions#')
CCSLA = CurieNamespace('CCSLA', 'http://cookingbigdata.com/linkeddata/ccsla#')
CNCF = CurieNamespace('CNCF', 'https://landscape.cncf.io/selected=')
CNTT = CurieNamespace('CNTT', 'https://cntt-n.github.io/CNTT/doc/common/glossary.html#1.1')
COAR_ACCESS = CurieNamespace('COAR_ACCESS', 'http://vocabularies.coar-repositories.org/documentation/access_rights/')
COAR_RESOURCE = CurieNamespace('COAR_RESOURCE', 'http://vocabularies.coar-repositories.org/documentation/resource_types/')
COAR_VERSION = CurieNamespace('COAR_VERSION', 'http://vocabularies.coar-repositories.org/documentation/version_types/')
CORR = CurieNamespace('CORR', 'https://arxiv.org/corr')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
CTRL = CurieNamespace('CTRL', 'https://w3id.org/ibp/CTRLont#')
CVE = CurieNamespace('CVE', 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=')
DCMI = CurieNamespace('DCMI', 'http://purl.org/dc/elements/1.1/')
DID = CurieNamespace('DID', 'https://www.w3.org/TR/did-core/#')
DMCC = CurieNamespace('DMCC', 'http://cookingbigdata.com/linkeddata/dmcc-schema/documentation/#')
DNB = CurieNamespace('DNB', 'https://d-nb.info/gnd/')
DPN = CurieNamespace('DPN', 'http://purl.org/dpn#')
DPS = CurieNamespace('DPS', 'http://purl.org/dpn/services#')
DOCKERHUB = CurieNamespace('DockerHub', 'https://hub.docker.com/')
ECO = CurieNamespace('ECO', 'https://evidenceontology.org/term/')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/')
EDAM_DATA = CurieNamespace('EDAM-DATA', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('EDAM-FORMAT', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('EDAM-OPERATION', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('EDAM-TOPIC', 'http://edamontology.org/topic_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/')
ETSINFV = CurieNamespace('ETSINFV', 'https://www.etsi.org/deliver/etsi_gr/NFV/001_099/003/01.05.01_60/gr_NFV003v010501p.pdf')
ETSINFV_MANO = CurieNamespace('ETSINFV-MANO', 'https://nfvwiki.etsi.org/index.php?title=API_specifications#API_conventions')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
GEANT = CurieNamespace('GEANT', 'https://wiki.geant.org/display/OAV/OAV+Terminology+and+Glossary')
GOIOTP = CurieNamespace('GOIotP', 'http://inter-iot.eu/GOIoTP#')
GOLD_META = CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/')
GSID = CurieNamespace('GSID', 'https://scholar.google.com/citations?user=')
IOTM3L = CurieNamespace('IOTM3L', 'http://smart-ics.ee.surrey.ac.uk/ontology/fiesta-iot/doc#')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
LOV = CurieNamespace('LOV', 'https://lov.linkeddata.es/dataset/lov/terms?q=')
MAID = CurieNamespace('MAID', 'https://academic.microsoft.com/#/detail/')
MOBI = CurieNamespace('MOBI', 'http://schema.mobivoc.org/#')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NOSQL = CurieNamespace('NOSQL', 'http://purl.org/db/nosql#')
OCO = CurieNamespace('OCO', 'https://www.openlinksw.com/describe/?url=http://www.openlinksw.com/ontology/components%23')
OCRM = CurieNamespace('OCRM', 'https://www.openlinksw.com/describe/?url=http://www.openlinksw.com/ontology/ecrm%23')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OM = CurieNamespace('OM', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OMG_SPECS = CurieNamespace('OMG-SPECS', 'https://www.omg.org/spec/')
ONAP = CurieNamespace('ONAP', 'https://wiki.onap.org/display/DW/Glossary')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
OSO = CurieNamespace('OSO', 'https://www.openlinksw.com/describe/?url=http://www.openlinksw.com/ontology/software%23')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/pato#')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
PEERINGDB = CurieNamespace('PeeringDb', 'https://www.peeringdb.com/ix/')
PEERINGDB_FAC = CurieNamespace('PeeringDb_fac', 'https://www.peeringdb.com/fac/')
PEERINGDB_PEERS = CurieNamespace('PeeringDb_peers', 'https://www.peeringdb.com/net/')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RNACENTRAL = CurieNamespace('RNACENTRAL', 'http://identifiers.org/rnacentral/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RTXKG1 = CurieNamespace('RTXKG1', 'http://kg1endpoint.rtx.ai/')
RESEARCHID = CurieNamespace('ResearchID', 'https://publons.com/researcher/')
SAF = CurieNamespace('SAF', 'https://opensaf.sourceforge.io/SAI-Overview-B.05.03.AL.pdf')
SAFAISAMF = CurieNamespace('SAFAISAMF', 'https://opensaf.sourceforge.io/SAI-AIS-AMF-B.04.01.AL.pdf')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN')
SEMMEDDB = CurieNamespace('SEMMEDDB', 'https://skr3.nlm.nih.gov/SemMedDB')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SCOPUSID = CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId=')
TAXRANK = CurieNamespace('TAXRANK', 'http://purl.obolibrary.org/obo/TAXRANK_')
UBERON_CORE = CurieNamespace('UBERON_CORE', 'http://purl.obolibrary.org/obo/uberon/core#')
UMLSSC = CurieNamespace('UMLSSC', 'https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt/code#')
UMLSSG = CurieNamespace('UMLSSG', 'https://metamap.nlm.nih.gov/Docs/SemGroups_2018.txt/group#')
UMLSST = CurieNamespace('UMLSST', 'https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt/type#')
UO = CurieNamespace('UO', 'https://www.ebi.ac.uk/ols/ontologies/uo')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
XXXX = CurieNamespace('XXXX', 'http://example.org/UNKNOWN/XXXX/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
TESTLINK = CurieNamespace('testlink', 'https://w3id.org/testlink/vocab/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
DWC = CurieNamespace('dwc', 'https://dwc.tdwg.org/terms/#dc:')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
FOLDOC = CurieNamespace('foldoc', 'https://foldoc.org/')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
ISBN = CurieNamespace('isbn', 'https://grp.isbn-international.org/content/using-register')
ISNI = CurieNamespace('isni', 'https://isni.org/isni/')
ISSN = CurieNamespace('issn', 'https://portal.issn.org/resource/ISSN/')
OPENVOCAB = CurieNamespace('openvocab', 'https://vocab.org/open/#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RR = CurieNamespace('rr', 'https://www.w3.org/ns/r2rml#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'https://www.w3.org/TR/vocab-ssn/#')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
SUMO = CurieNamespace('sumo', 'http://sigma.ontologyportal.org:8080/sigma/TreeView.jsp?flang=SUO-KIF&kb=SUMO&simple=yes&term=')
SUMO_WN = CurieNamespace('sumo-wn', 'http://sigma.ontologyportal.org:8080/sigma/WordNet.jsp?POS=0&word=')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TESTLINK


# Types
class ControlPlaneValue(str):
    """ A control plane """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "control plane value"
    type_model_uri = TESTLINK.ControlPlaneValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the testlink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the testlink class, for example testlink:Service. For an RDF representation, the value should be a URI such as https://w3id.org/testlink/vocab/Service """
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
    """ A CURIE from the testlink related_to hierarchy. For example, testlink:related_to, testlink:causes, testlink:repairs. """
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


class PercentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percentage frequency value"
    type_model_uri = TESTLINK.PercentageFrequencyValue


class Quotient(Double):
    type_class_uri = UO["0010006"]
    type_class_curie = "UO:0010006"
    type_name = "quotient"
    type_model_uri = TESTLINK.Quotient


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


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class ComponentserviceOntologyClassId(OntologyClassId):
    pass


class TaxonomicRankId(OntologyClassId):
    pass


class SystemTaxonId(OntologyClassId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
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


class DatasetSummaryId(DatasetVersionId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class BookId(PublicationId):
    pass


class BookChapterId(PublicationId):
    pass


class SerialId(PublicationId):
    pass


class ArticleId(PublicationId):
    pass


class CyberEntityId(NamedThingId):
    pass


class ActivityId(NamedThingId):
    pass


class ProcedureId(NamedThingId):
    pass


class PhenomenonId(NamedThingId):
    pass


class DeviceId(NamedThingId):
    pass


class ResourceSampleId(CyberEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class ComputationalEntityId(NamedThingId):
    pass


class OperationalEntityId(ComputationalEntityId):
    pass


class ComputationalProcessOrActivityId(ComputationalEntityId):
    pass


class OperationalActivityId(ComputationalProcessOrActivityId):
    pass


class ComputationalProcessId(ComputationalProcessOrActivityId):
    pass


class PathwayId(ComputationalProcessId):
    pass


class CyberProcessId(ComputationalProcessId):
    pass


class BehaviorId(ComputationalProcessId):
    pass


class DeathId(ComputationalProcessId):
    pass


class ControlActorId(OperationalEntityId):
    pass


class PowerId(ControlActorId):
    pass


class ConsumedResourceId(ControlActorId):
    pass


class AdministrativeOperationId(OperationalEntityId):
    pass


class NotificationComponentId(ControlActorId):
    pass


class EnvironmentalNotificationContaminantId(NotificationComponentId):
    pass


class AwarenessId(NotificationComponentId):
    pass


class DataId(NotificationComponentId):
    pass


class DatastreamId(DataId):
    pass


class BitstreamId(DataId):
    pass


class MessagePassingId(BitstreamId):
    pass


class NotificationId(OperationalEntityId):
    pass


class ControllerId(ControlActorId):
    pass


class SystemicEntityId(ComputationalEntityId):
    pass


class LifecycleStageId(SystemicEntityId):
    pass


class IndividualSystemId(SystemicEntityId):
    pass


class PopulationOfIndividualSystemsId(SystemicEntityId):
    pass


class StudyPopulationId(PopulationOfIndividualSystemsId):
    pass


class ErrorOrObservableFeatureId(ComputationalEntityId):
    pass


class ErrorId(ErrorOrObservableFeatureId):
    pass


class ObservableFeatureId(ErrorOrObservableFeatureId):
    pass


class BehavioralFeatureId(ObservableFeatureId):
    pass


class DeploymentEntityId(SystemicEntityId):
    pass


class ServiceunitId(DeploymentEntityId):
    pass


class ComponentId(DeploymentEntityId):
    pass


class ComponentTypeId(SystemicEntityId):
    pass


class GrossDeploymentStructureId(DeploymentEntityId):
    pass


class WorkloadEntityId(OperationalEntityId):
    pass


class WorkloadId(WorkloadEntityId):
    pass


class ComponentserviceinstanceId(WorkloadEntityId):
    pass


class DaemonId(WorkloadEntityId):
    pass


class CodingSequenceId(WorkloadEntityId):
    pass


class ServiceinstanceId(WorkloadEntityId):
    pass


class ServiceinstanceIsoformId(ServiceinstanceId):
    pass


class KernelServicetypeId(ComponentserviceinstanceId):
    pass


class KernelServicetypeIsoformId(KernelServicetypeId):
    pass


class NoncodingKernelServicetypeId(KernelServicetypeId):
    pass


class KernelMessageId(NoncodingKernelServicetypeId):
    pass


class KernelInterruptId(NoncodingKernelServicetypeId):
    pass


class ComponentserviceFamilyId(OperationalEntityId):
    pass


class ServiceunittypeId(WorkloadEntityId):
    pass


class VariantcomponentservicetypeId(WorkloadEntityId):
    pass


class SequenceVariantId(WorkloadEntityId):
    pass


class MonomericVariantId(SequenceVariantId):
    pass


class ReagentTargetedComponentserviceId(WorkloadEntityId):
    pass


class EmpiricalEntityId(NamedThingId):
    pass


class EmpiricalTrialId(EmpiricalEntityId):
    pass


class EmpiricalInterventionId(EmpiricalEntityId):
    pass


class EmpiricalFindingId(ObservableFeatureId):
    pass


class OfflineMaintenanceId(EmpiricalInterventionId):
    pass


class CaseId(IndividualSystemId):
    pass


class CohortId(StudyPopulationId):
    pass


class ServiceBackgroundExposureId(WorkloadEntityId):
    pass


class FaultyProcessId(ComputationalProcessId):
    pass


class ErrorOrObservableFeatureExposureId(ErrorOrObservableFeatureId):
    pass


class FaultyProcessExposureId(FaultyProcessId):
    pass


class FaultyDeploymentStructureId(DeploymentEntityId):
    pass


class FaultyDeploymentExposureId(FaultyDeploymentStructureId):
    pass


class OrchestrationExposureId(ControlActorId):
    pass


class ComplexOrchestrationExposureId(OrchestrationExposureId):
    pass


class AdministrativeOperationalExposureId(AdministrativeOperationId):
    pass


class AdministrativeOperationalToComponentserviceInteractionExposureId(AdministrativeOperationalExposureId):
    pass


class RepairingId(NamedThingId):
    pass


class BioticExposureId(SystemTaxonId):
    pass


class GeographicExposureId(GeographicLocationId):
    pass


class EnvironmentalExposureId(EnvironmentalProcessId):
    pass


class BehavioralExposureId(BehaviorId):
    pass


class SocioeconomicExposureId(BehaviorId):
    pass


class FaultyProcessOutcomeId(FaultyProcessId):
    pass


class FaultyDeploymentOutcomeId(FaultyDeploymentStructureId):
    pass


class ErrorOrObservableFeatureOutcomeId(ErrorOrObservableFeatureId):
    pass


class BehavioralOutcomeId(BehaviorId):
    pass


class OfflineMaintenanceOutcomeId(OfflineMaintenanceId):
    pass


class MortalityOutcomeId(DeathId):
    pass


class EpidemiologicalOutcomeId(ComputationalEntityId):
    pass


class SocioeconomicOutcomeId(BehaviorId):
    pass


class AssociationId(EntityId):
    pass


class ContributorAssociationId(AssociationId):
    pass


class ServiceunittypeToServiceunittypePartAssociationId(AssociationId):
    pass


class ServiceunittypeToComponentserviceAssociationId(AssociationId):
    pass


class ServiceunittypeToVariantAssociationId(AssociationId):
    pass


class ComponentserviceToComponentserviceAssociationId(AssociationId):
    pass


class ComponentserviceToComponentserviceHomologyAssociationId(ComponentserviceToComponentserviceAssociationId):
    pass


class ComponentserviceToComponentserviceCoavailabilityAssociationId(ComponentserviceToComponentserviceAssociationId):
    pass


class PairwiseComponentserviceToComponentserviceInteractionId(ComponentserviceToComponentserviceAssociationId):
    pass


class PairwiseOperationallyInteractionId(PairwiseComponentserviceToComponentserviceInteractionId):
    pass


class ComponentTypeToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class OrchestrationToOrchestrationAssociationId(AssociationId):
    pass


class OrchestrationToOrchestrationDerivationAssociationId(OrchestrationToOrchestrationAssociationId):
    pass


class OrchestrationToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class OrchestrationToPathwayAssociationId(AssociationId):
    pass


class OrchestrationToComponentserviceAssociationId(AssociationId):
    pass


class AdministrativeOperationalToComponentserviceAssociationId(AssociationId):
    pass


class ResourceSampleDerivationAssociationId(AssociationId):
    pass


class ResourceSampleToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class ErrorToExposureEventAssociationId(AssociationId):
    pass


class ExposureEventToOutcomeAssociationId(AssociationId):
    pass


class ErrorOrObservableFeatureAssociationToLocationAssociationId(AssociationId):
    pass


class ErrorOrObservableFeatureToLocationAssociationId(AssociationId):
    pass


class ServiceunittypeToObservableFeatureAssociationId(AssociationId):
    pass


class ExposureEventToObservableFeatureAssociationId(AssociationId):
    pass


class ErrorToObservableFeatureAssociationId(AssociationId):
    pass


class CaseToObservableFeatureAssociationId(AssociationId):
    pass


class BehaviorToBehavioralFeatureAssociationId(AssociationId):
    pass


class ComponentserviceToObservableFeatureAssociationId(AssociationId):
    pass


class ComponentserviceToErrorAssociationId(AssociationId):
    pass


class VariantToComponentserviceAssociationId(AssociationId):
    pass


class VariantToComponentserviceAvailabilityAssociationId(VariantToComponentserviceAssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToObservableFeatureAssociationId(AssociationId):
    pass


class VariantToErrorAssociationId(AssociationId):
    pass


class ServiceunittypeToErrorAssociationId(AssociationId):
    pass


class ComponentserviceAsAModelOfErrorAssociationId(ComponentserviceToErrorAssociationId):
    pass


class VariantAsAModelOfErrorAssociationId(VariantToErrorAssociationId):
    pass


class ServiceunittypeAsAModelOfErrorAssociationId(ServiceunittypeToErrorAssociationId):
    pass


class ComponentTypeAsAModelOfErrorAssociationId(ComponentTypeToErrorOrObservableFeatureAssociationId):
    pass


class SystemicEntityAsAModelOfErrorAssociationId(AssociationId):
    pass


class ComponentserviceHasVariantThatContributesToErrorAssociationId(ComponentserviceToErrorAssociationId):
    pass


class ComponentserviceToAvailabilitySiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesRepairingAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacrooperationalMachineMixinToOperationalActivityAssociationId(FunctionalAssociationId):
    pass


class MacrooperationalMachineMixinToComputationalProcessAssociationId(FunctionalAssociationId):
    pass


class MacrooperationalMachineMixinToComponentAssociationId(FunctionalAssociationId):
    pass


class ComponentserviceToGoTermAssociationId(FunctionalAssociationId):
    pass


class SequenceAssociationId(AssociationId):
    pass


class ServiceSequenceLocalizationId(SequenceAssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class ComponentserviceinstanceToComponentserviceRelationshipId(SequenceFeatureRelationshipId):
    pass


class ComponentserviceToServicetypeRelationshipId(SequenceFeatureRelationshipId):
    pass


class DaemonToComponentserviceinstanceRelationshipId(SequenceFeatureRelationshipId):
    pass


class ComponentserviceRegulatoryRelationshipId(AssociationId):
    pass


class DeploymentEntityToDeploymentEntityAssociationId(AssociationId):
    pass


class DeploymentEntityToDeploymentEntityPartOfAssociationId(DeploymentEntityToDeploymentEntityAssociationId):
    pass


class DeploymentEntityToDeploymentEntityOntogenicAssociationId(DeploymentEntityToDeploymentEntityAssociationId):
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
class ComputationalArchitecturalStyle(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComputationalArchitecturalStyle
    class_class_curie: ClassVar[str] = "testlink:ComputationalArchitecturalStyle"
    class_name: ClassVar[str] = "computational architectural style"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComputationalArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ObservableArchitecturalStyle(ComputationalArchitecturalStyle):
    """
    An attribute corresponding to the observable architectural style of the individual, based upon the reproductive
    applications present.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ObservableArchitecturalStyle
    class_class_curie: ClassVar[str] = "testlink:ObservableArchitecturalStyle"
    class_name: ClassVar[str] = "observable architectural style"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ObservableArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class MicroserviceArchitecturalStyle(ComputationalArchitecturalStyle):
    """
    An attribute corresponding to the microservice architectural style of the individual, based upon microservice
    composition of architectural style containers.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.MicroserviceArchitecturalStyle
    class_class_curie: ClassVar[str] = "testlink:MicroserviceArchitecturalStyle"
    class_name: ClassVar[str] = "microservice architectural style"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MicroserviceArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

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

class RelationshipQuantifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.RelationshipQuantifier
    class_class_curie: ClassVar[str] = "testlink:RelationshipQuantifier"
    class_name: ClassVar[str] = "relationship quantifier"
    class_model_uri: ClassVar[URIRef] = TESTLINK.RelationshipQuantifier


class SensitivityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SensitivityQuantifier
    class_class_curie: ClassVar[str] = "testlink:SensitivityQuantifier"
    class_name: ClassVar[str] = "sensitivity quantifier"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SensitivityQuantifier


class SpecificityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SpecificityQuantifier
    class_class_curie: ClassVar[str] = "testlink:SpecificityQuantifier"
    class_name: ClassVar[str] = "specificity quantifier"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SpecificityQuantifier


class PathognomonicityQuantifier(SpecificityQuantifier):
    """
    A relationship quantifier between a variant or symptom and a error, which is high when the presence of the feature
    implies the existence of the error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.PathognomonicityQuantifier
    class_class_curie: ClassVar[str] = "testlink:PathognomonicityQuantifier"
    class_name: ClassVar[str] = "pathognomonicity quantifier"
    class_model_uri: ClassVar[URIRef] = TESTLINK.PathognomonicityQuantifier


@dataclass
class FrequencyQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.FrequencyQuantifier
    class_class_curie: ClassVar[str] = "testlink:FrequencyQuantifier"
    class_name: ClassVar[str] = "frequency quantifier"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FrequencyQuantifier

    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        super().__post_init__(**kwargs)


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
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    iri: Optional[Union[str, IriType]] = None
    type: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    source: Optional[Union[str, LabelType]] = None
    provided_by: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.category is None:
            raise ValueError("category must be supplied")
        elif not isinstance(self.category, list):
            self.category = [self.category]
        elif len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        if self.source is not None and not isinstance(self.source, LabelType):
            self.source = LabelType(self.source)

        if self.provided_by is None:
            self.provided_by = []
        if not isinstance(self.provided_by, list):
            self.provided_by = [self.provided_by]
        self.provided_by = [v if isinstance(v, AgentId) else AgentId(v) for v in self.provided_by]

        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=Attribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

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
class ComponentserviceOntologyClass(OntologyClass):
    """
    an ontology class that describes a controlling aspect of a componentservice, servicetype or complex
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceOntologyClass
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceOntologyClass"
    class_name: ClassVar[str] = "componentservice ontology class"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceOntologyClass

    id: Union[str, ComponentserviceOntologyClassId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceOntologyClassId):
            self.id = ComponentserviceOntologyClassId(self.id)

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
    A classification of a set of systems. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria).
    Can also be used to represent strains or subspecies.
    """
    _inherited_slots: ClassVar[List[str]] = ["subclass_of"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.SystemTaxon
    class_class_curie: ClassVar[str] = "testlink:SystemTaxon"
    class_name: ClassVar[str] = "system taxon"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SystemTaxon

    id: Union[str, SystemTaxonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_taxonomic_rank: Optional[Union[str, TaxonomicRankId]] = None
    subclass_of: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SystemTaxonId):
            self.id = SystemTaxonId(self.id)

        if self.has_taxonomic_rank is not None and not isinstance(self.has_taxonomic_rank, TaxonomicRankId):
            self.has_taxonomic_rank = TaxonomicRankId(self.has_taxonomic_rank)

        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.subclass_of]

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
class DatasetSummary(DatasetVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DatasetSummary
    class_class_curie: ClassVar[str] = "testlink:DatasetSummary"
    class_name: ClassVar[str] = "dataset summary"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DatasetSummary

    id: Union[str, DatasetSummaryId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    source_web_page: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source_web_page is not None and not isinstance(self.source_web_page, str):
            self.source_web_page = str(self.source_web_page)

        super().__post_init__(**kwargs)


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ConfidenceLevel
    class_class_curie: ClassVar[str] = "testlink:ConfidenceLevel"
    class_name: ClassVar[str] = "confidence level"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ConfidenceLevel

    id: Union[str, ConfidenceLevelId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EvidenceType
    class_class_curie: ClassVar[str] = "testlink:EvidenceType"
    class_name: ClassVar[str] = "evidence type"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

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
    sumo_terms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
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

        if self.sumo_terms is None:
            self.sumo_terms = []
        if not isinstance(self.sumo_terms, list):
            self.sumo_terms = [self.sumo_terms]
        self.sumo_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.sumo_terms]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Book(Publication):
    """
    This class may rarely be available except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Book
    class_class_curie: ClassVar[str] = "testlink:Book"
    class_name: ClassVar[str] = "book"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Book

    id: Union[str, BookId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BookId):
            self.id = BookId(self.id)

        if self.type is None:
            raise ValueError("type must be supplied")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class BookChapter(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.BookChapter
    class_class_curie: ClassVar[str] = "testlink:BookChapter"
    class_name: ClassVar[str] = "book chapter"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BookChapter

    id: Union[str, BookChapterId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    volume: Optional[str] = None
    chapter: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BookChapterId):
            self.id = BookChapterId(self.id)

        if self.published_in is None:
            raise ValueError("published_in must be supplied")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.chapter is not None and not isinstance(self.chapter, str):
            self.chapter = str(self.chapter)

        super().__post_init__(**kwargs)


@dataclass
class Serial(Publication):
    """
    This class may rarely be available except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Serial
    class_class_curie: ClassVar[str] = "testlink:Serial"
    class_name: ClassVar[str] = "serial"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Serial

    id: Union[str, SerialId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SerialId):
            self.id = SerialId(self.id)

        if self.type is None:
            raise ValueError("type must be supplied")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


@dataclass
class Article(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Article
    class_class_curie: ClassVar[str] = "testlink:Article"
    class_name: ClassVar[str] = "article"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Article

    id: Union[str, ArticleId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ArticleId):
            self.id = ArticleId(self.id)

        if self.published_in is None:
            raise ValueError("published_in must be supplied")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

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
class Procedure(NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Procedure
    class_class_curie: ClassVar[str] = "testlink:Procedure"
    class_name: ClassVar[str] = "procedure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Procedure

    id: Union[str, ProcedureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Phenomenon(NamedThing):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Phenomenon
    class_class_curie: ClassVar[str] = "testlink:Phenomenon"
    class_name: ClassVar[str] = "phenomenon"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Phenomenon

    id: Union[str, PhenomenonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Device
    class_class_curie: ClassVar[str] = "testlink:Device"
    class_name: ClassVar[str] = "device"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Device

    id: Union[str, DeviceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)


class SubjectOfInvestigation(YAMLRoot):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SubjectOfInvestigation
    class_class_curie: ClassVar[str] = "testlink:SubjectOfInvestigation"
    class_name: ClassVar[str] = "subject of investigation"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SubjectOfInvestigation


@dataclass
class ResourceSample(CyberEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a event) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ResourceSample
    class_class_curie: ClassVar[str] = "testlink:ResourceSample"
    class_name: ClassVar[str] = "resource sample"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ResourceSample

    id: Union[str, ResourceSampleId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ResourceSampleId):
            self.id = ResourceSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.PlanetaryEntity
    class_class_curie: ClassVar[str] = "testlink:PlanetaryEntity"
    class_name: ClassVar[str] = "planetary entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.PlanetaryEntity

    id: Union[str, PlanetaryEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EnvironmentalProcess
    class_class_curie: ClassVar[str] = "testlink:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EnvironmentalProcess

    id: Union[str, EnvironmentalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EnvironmentalFeature
    class_class_curie: ClassVar[str] = "testlink:EnvironmentalFeature"
    class_name: ClassVar[str] = "environmental feature"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EnvironmentalFeature

    id: Union[str, EnvironmentalFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.GeographicLocation
    class_class_curie: ClassVar[str] = "testlink:GeographicLocation"
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = TESTLINK.GeographicLocation

    id: Union[str, GeographicLocationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.GeographicLocationAtTime
    class_class_curie: ClassVar[str] = "testlink:GeographicLocationAtTime"
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = TESTLINK.GeographicLocationAtTime

    id: Union[str, GeographicLocationAtTimeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

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
class ComputationalProcess(ComputationalProcessOrActivity):
    """
    One or more causally connected executions of operational functions
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComputationalProcess
    class_class_curie: ClassVar[str] = "testlink:ComputationalProcess"
    class_name: ClassVar[str] = "computational process"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComputationalProcess

    id: Union[str, ComputationalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComputationalProcessId):
            self.id = ComputationalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Pathway(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Pathway
    class_class_curie: ClassVar[str] = "testlink:Pathway"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Pathway

    id: Union[str, PathwayId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CyberProcess(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.CyberProcess
    class_class_curie: ClassVar[str] = "testlink:CyberProcess"
    class_name: ClassVar[str] = "cyber process"
    class_model_uri: ClassVar[URIRef] = TESTLINK.CyberProcess

    id: Union[str, CyberProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CyberProcessId):
            self.id = CyberProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Behavior(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Behavior
    class_class_curie: ClassVar[str] = "testlink:Behavior"
    class_name: ClassVar[str] = "behavior"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Behavior

    id: Union[str, BehaviorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehaviorId):
            self.id = BehaviorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Death(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Death
    class_class_curie: ClassVar[str] = "testlink:Death"
    class_name: ClassVar[str] = "death"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Death

    id: Union[str, DeathId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeathId):
            self.id = DeathId(self.id)

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
class Power(ControlActor):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Power
    class_class_curie: ClassVar[str] = "testlink:Power"
    class_name: ClassVar[str] = "power"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Power

    id: Union[str, PowerId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PowerId):
            self.id = PowerId(self.id)

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
class EnvironmentalNotificationContaminant(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.EnvironmentalNotificationContaminant
    class_class_curie: ClassVar[str] = "testlink:EnvironmentalNotificationContaminant"
    class_name: ClassVar[str] = "environmental notification contaminant"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EnvironmentalNotificationContaminant

    id: Union[str, EnvironmentalNotificationContaminantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentalNotificationContaminantId):
            self.id = EnvironmentalNotificationContaminantId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Awareness(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Awareness
    class_class_curie: ClassVar[str] = "testlink:Awareness"
    class_name: ClassVar[str] = "awareness"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Awareness

    id: Union[str, AwarenessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AwarenessId):
            self.id = AwarenessId(self.id)

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
class Datastream(Data):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Datastream
    class_class_curie: ClassVar[str] = "testlink:Datastream"
    class_name: ClassVar[str] = "datastream"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Datastream

    id: Union[str, DatastreamId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatastreamId):
            self.id = DatastreamId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Bitstream(Data):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Bitstream
    class_class_curie: ClassVar[str] = "testlink:Bitstream"
    class_name: ClassVar[str] = "bitstream"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Bitstream

    id: Union[str, BitstreamId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BitstreamId):
            self.id = BitstreamId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MessagePassing(Bitstream):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.MessagePassing
    class_class_curie: ClassVar[str] = "testlink:MessagePassing"
    class_name: ClassVar[str] = "message passing"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MessagePassing

    id: Union[str, MessagePassingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MessagePassingId):
            self.id = MessagePassingId(self.id)

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
class Controller(ControlActor):
    """
    Any intermediate or servicetype resulting from director supervision. Includes primary and secondary controllers.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Controller
    class_class_curie: ClassVar[str] = "testlink:Controller"
    class_name: ClassVar[str] = "controller"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Controller

    id: Union[str, ControllerId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    is_controller: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ControllerId):
            self.id = ControllerId(self.id)

        if self.is_controller is not None and not isinstance(self.is_controller, Bool):
            self.is_controller = Bool(self.is_controller)

        super().__post_init__(**kwargs)


@dataclass
class SystemAttribute(Attribute):
    """
    describes a characteristic of an systemic entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SystemAttribute
    class_class_curie: ClassVar[str] = "testlink:SystemAttribute"
    class_name: ClassVar[str] = "system attribute"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SystemAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ObservableQuality(SystemAttribute):
    """
    A property of a observable
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ObservableQuality
    class_class_curie: ClassVar[str] = "testlink:ObservableQuality"
    class_name: ClassVar[str] = "observable quality"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ObservableQuality

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Inheritance(SystemAttribute):
    """
    The pattern or 'mode' in which a particular service trait or disorder is passed from one generation to the next,
    e.g. autosomal dominant, autosomal recessive, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Inheritance
    class_class_curie: ClassVar[str] = "testlink:Inheritance"
    class_name: ClassVar[str] = "inheritance"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Inheritance

    has_attribute_type: Union[str, OntologyClassId] = None

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
class LifecycleStage(SystemicEntity):
    """
    A stage of development or growth of a system.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.LifecycleStage
    class_class_curie: ClassVar[str] = "testlink:LifecycleStage"
    class_name: ClassVar[str] = "lifecycle stage"
    class_model_uri: ClassVar[URIRef] = TESTLINK.LifecycleStage

    id: Union[str, LifecycleStageId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, LifecycleStageId):
            self.id = LifecycleStageId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class IndividualSystem(SystemicEntity):
    """
    An instance of an system. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID:
    ORCID:0000-0002-5355-2576
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.IndividualSystem
    class_class_curie: ClassVar[str] = "testlink:IndividualSystem"
    class_name: ClassVar[str] = "individual system"
    class_model_uri: ClassVar[URIRef] = TESTLINK.IndividualSystem

    id: Union[str, IndividualSystemId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, IndividualSystemId):
            self.id = IndividualSystemId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class PopulationOfIndividualSystems(SystemicEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, services, observabilitys.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.PopulationOfIndividualSystems
    class_class_curie: ClassVar[str] = "testlink:PopulationOfIndividualSystems"
    class_name: ClassVar[str] = "population of individual systems"
    class_model_uri: ClassVar[URIRef] = TESTLINK.PopulationOfIndividualSystems

    id: Union[str, PopulationOfIndividualSystemsId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PopulationOfIndividualSystemsId):
            self.id = PopulationOfIndividualSystemsId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class StudyPopulation(PopulationOfIndividualSystems):
    """
    A group of individuals banded together or repaired as a group as participants in a research study.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.StudyPopulation
    class_class_curie: ClassVar[str] = "testlink:StudyPopulation"
    class_name: ClassVar[str] = "study population"
    class_model_uri: ClassVar[URIRef] = TESTLINK.StudyPopulation

    id: Union[str, StudyPopulationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, StudyPopulationId):
            self.id = StudyPopulationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeature(ComputationalEntity):
    """
    Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as
    distinct, others conflate.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeature
    class_class_curie: ClassVar[str] = "testlink:ErrorOrObservableFeature"
    class_name: ClassVar[str] = "error or observable feature"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeature

    id: Union[str, ErrorOrObservableFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureId):
            self.id = ErrorOrObservableFeatureId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class Error(ErrorOrObservableFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Error
    class_class_curie: ClassVar[str] = "testlink:Error"
    class_name: ClassVar[str] = "error"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Error

    id: Union[str, ErrorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorId):
            self.id = ErrorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ObservableFeature(ErrorOrObservableFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ObservableFeature
    class_class_curie: ClassVar[str] = "testlink:ObservableFeature"
    class_name: ClassVar[str] = "observable feature"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ObservableFeature

    id: Union[str, ObservableFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ObservableFeatureId):
            self.id = ObservableFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralFeature(ObservableFeature):
    """
    A observable feature which is behavioral in nature.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.BehavioralFeature
    class_class_curie: ClassVar[str] = "testlink:BehavioralFeature"
    class_name: ClassVar[str] = "behavioral feature"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BehavioralFeature

    id: Union[str, BehavioralFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehavioralFeatureId):
            self.id = BehavioralFeatureId(self.id)

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
class Serviceunit(DeploymentEntity):
    """
    The set of components, whose part functionalily combines to form a desired service, must tightly collaborate as a
    group, logically named serviceunit (pod). A serviceunit represents a single instance of a running process in a
    cluster. It can be deployed, isolated, and repaired independently.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Serviceunit
    class_class_curie: ClassVar[str] = "testlink:Serviceunit"
    class_name: ClassVar[str] = "serviceunit"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Serviceunit

    id: Union[str, ServiceunitId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunitId):
            self.id = ServiceunitId(self.id)

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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentId):
            self.id = ComponentId(self.id)

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
class GrossDeploymentStructure(DeploymentEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.GrossDeploymentStructure
    class_class_curie: ClassVar[str] = "testlink:GrossDeploymentStructure"
    class_name: ClassVar[str] = "gross deployment structure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.GrossDeploymentStructure

    id: Union[str, GrossDeploymentStructureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GrossDeploymentStructureId):
            self.id = GrossDeploymentStructureId(self.id)

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


class ComponentserviceOrServicetype(MacrooperationalMachineMixin):
    """
    a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for
    another
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceOrServicetype
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceOrServicetype"
    class_name: ClassVar[str] = "componentservice or servicetype"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceOrServicetype


@dataclass
class Componentservice(ComponentserviceOrServicetype):
    """
    A component service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Componentservice
    class_class_curie: ClassVar[str] = "testlink:Componentservice"
    class_name: ClassVar[str] = "componentservice"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Componentservice

    symbol: Optional[str] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.synonym is None:
            self.synonym = []
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym]
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ServicetypeMixin(ComponentserviceOrServicetype):
    """
    The controlling operational servicetype of a single componentservice locus. ServiceType product are either
    serviceinstances or supervisor tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServicetypeMixin
    class_class_curie: ClassVar[str] = "testlink:ServicetypeMixin"
    class_name: ClassVar[str] = "servicetype mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServicetypeMixin

    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.synonym is None:
            self.synonym = []
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym]
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


class ServicetypeIsoformMixin(ServicetypeMixin):
    """
    This is an abstract class that can be mixed in with different kinds of servicetypes to indicate that the
    servicetype is intended to represent a specific isoform rather than a canonical or reference or generic
    servicetype. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all
    isoforms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServicetypeIsoformMixin
    class_class_curie: ClassVar[str] = "testlink:ServicetypeIsoformMixin"
    class_name: ClassVar[str] = "servicetype isoform mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServicetypeIsoformMixin


class MacrooperationalComplexMixin(MacrooperationalMachineMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalComplexMixin
    class_class_curie: ClassVar[str] = "testlink:MacrooperationalComplexMixin"
    class_name: ClassVar[str] = "macrooperational complex mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalComplexMixin


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
class Componentserviceinstance(WorkloadEntity):
    """
    The unit of service workload the component is capable of providing or protecting.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Componentserviceinstance
    class_class_curie: ClassVar[str] = "testlink:Componentserviceinstance"
    class_name: ClassVar[str] = "componentserviceinstance"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Componentserviceinstance

    id: Union[str, ComponentserviceinstanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceinstanceId):
            self.id = ComponentserviceinstanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Daemon(WorkloadEntity):
    """
    A region of the componentserviceinstance sequence within a componentservice.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Daemon
    class_class_curie: ClassVar[str] = "testlink:Daemon"
    class_name: ClassVar[str] = "daemon"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Daemon

    id: Union[str, DaemonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DaemonId):
            self.id = DaemonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CodingSequence(WorkloadEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.CodingSequence
    class_class_curie: ClassVar[str] = "testlink:CodingSequence"
    class_name: ClassVar[str] = "coding sequence"
    class_model_uri: ClassVar[URIRef] = TESTLINK.CodingSequence

    id: Union[str, CodingSequenceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Serviceinstance(WorkloadEntity):
    """
    A servicetype that is composed of a chain of instruction sequences and is produced by translation of kernel message
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Serviceinstance
    class_class_curie: ClassVar[str] = "testlink:Serviceinstance"
    class_name: ClassVar[str] = "serviceinstance"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Serviceinstance

    id: Union[str, ServiceinstanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceinstanceId):
            self.id = ServiceinstanceId(self.id)

        if self.synonym is None:
            self.synonym = []
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym]
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ServiceinstanceIsoform(Serviceinstance):
    """
    Represents a serviceinstance that is a specific isoform of the canonical or reference serviceinstance.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceinstanceIsoform
    class_class_curie: ClassVar[str] = "testlink:ServiceinstanceIsoform"
    class_name: ClassVar[str] = "serviceinstance isoform"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceinstanceIsoform

    id: Union[str, ServiceinstanceIsoformId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceinstanceIsoformId):
            self.id = ServiceinstanceIsoformId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelServicetype(Componentserviceinstance):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.KernelServicetype
    class_class_curie: ClassVar[str] = "testlink:KernelServicetype"
    class_name: ClassVar[str] = "kernel servicetype"
    class_model_uri: ClassVar[URIRef] = TESTLINK.KernelServicetype

    id: Union[str, KernelServicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, KernelServicetypeId):
            self.id = KernelServicetypeId(self.id)

        if self.synonym is None:
            self.synonym = []
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym]
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class KernelServicetypeIsoform(KernelServicetype):
    """
    Represents a serviceinstance that is a specific isoform of the canonical or reference kernel
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.KernelServicetypeIsoform
    class_class_curie: ClassVar[str] = "testlink:KernelServicetypeIsoform"
    class_name: ClassVar[str] = "kernel servicetype isoform"
    class_model_uri: ClassVar[URIRef] = TESTLINK.KernelServicetypeIsoform

    id: Union[str, KernelServicetypeIsoformId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, KernelServicetypeIsoformId):
            self.id = KernelServicetypeIsoformId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NoncodingKernelServicetype(KernelServicetype):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.NoncodingKernelServicetype
    class_class_curie: ClassVar[str] = "testlink:NoncodingKernelServicetype"
    class_name: ClassVar[str] = "noncoding kernel servicetype"
    class_model_uri: ClassVar[URIRef] = TESTLINK.NoncodingKernelServicetype

    id: Union[str, NoncodingKernelServicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NoncodingKernelServicetypeId):
            self.id = NoncodingKernelServicetypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelMessage(NoncodingKernelServicetype):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.KernelMessage
    class_class_curie: ClassVar[str] = "testlink:KernelMessage"
    class_name: ClassVar[str] = "kernel message"
    class_model_uri: ClassVar[URIRef] = TESTLINK.KernelMessage

    id: Union[str, KernelMessageId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, KernelMessageId):
            self.id = KernelMessageId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelInterrupt(NoncodingKernelServicetype):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.KernelInterrupt
    class_class_curie: ClassVar[str] = "testlink:KernelInterrupt"
    class_name: ClassVar[str] = "kernel interrupt"
    class_model_uri: ClassVar[URIRef] = TESTLINK.KernelInterrupt

    id: Union[str, KernelInterruptId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, KernelInterruptId):
            self.id = KernelInterruptId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceGroupingMixin(YAMLRoot):
    """
    any grouping of multiple componentservices or servicetypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceGroupingMixin
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceGroupingMixin"
    class_name: ClassVar[str] = "componentservice grouping mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceGroupingMixin

    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_componentservice_or_servicetype is None:
            self.has_componentservice_or_servicetype = []
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype]
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceFamily(OperationalEntity):
    """
    any grouping of multiple componentservices or servicetypes related by common descent
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceFamily
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceFamily"
    class_name: ClassVar[str] = "componentservice family"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceFamily

    id: Union[str, ComponentserviceFamilyId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceFamilyId):
            self.id = ComponentserviceFamilyId(self.id)

        if self.has_componentservice_or_servicetype is None:
            self.has_componentservice_or_servicetype = []
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype]
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice_or_servicetype]

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
class Serviceunittype(WorkloadEntity):
    """
    An information content entity that describes a workload by specifying the total variation in service sequence
    and/or componentservice availability, relative to some established background
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Serviceunittype
    class_class_curie: ClassVar[str] = "testlink:Serviceunittype"
    class_name: ClassVar[str] = "serviceunittype"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Serviceunittype

    id: Union[str, ServiceunittypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_homogeneity: Optional[Union[dict, Homogeneity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeId):
            self.id = ServiceunittypeId(self.id)

        if self.has_homogeneity is not None and not isinstance(self.has_homogeneity, Homogeneity):
            self.has_homogeneity = Homogeneity(**self.has_homogeneity)

        super().__post_init__(**kwargs)


@dataclass
class Variantcomponentservicetype(WorkloadEntity):
    """
    A set of zero or more variantcomponentservices on a single instance of a Sequence
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Variantcomponentservicetype
    class_class_curie: ClassVar[str] = "testlink:Variantcomponentservicetype"
    class_name: ClassVar[str] = "variantcomponentservicetype"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Variantcomponentservicetype

    id: Union[str, VariantcomponentservicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantcomponentservicetypeId):
            self.id = VariantcomponentservicetypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SequenceVariant(WorkloadEntity):
    """
    A variantcomponentservice that varies in its sequence from what is considered the reference
    variantcomponentservice at that locus.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.SequenceVariant
    class_class_curie: ClassVar[str] = "testlink:SequenceVariant"
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SequenceVariant

    id: Union[str, SequenceVariantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)

        if self.has_componentservice is None:
            self.has_componentservice = []
        if not isinstance(self.has_componentservice, list):
            self.has_componentservice = [self.has_componentservice]
        self.has_componentservice = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice]

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class MonomericVariant(SequenceVariant):
    """
    A single monomeric position in the service monomeric variants are single monomeric positions in service DNA at
    which different sequence alternatives exist
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.MonomericVariant
    class_class_curie: ClassVar[str] = "testlink:MonomericVariant"
    class_name: ClassVar[str] = "monomeric variant"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MonomericVariant

    id: Union[str, MonomericVariantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MonomericVariantId):
            self.id = MonomericVariantId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ReagentTargetedComponentservice(WorkloadEntity):
    """
    A componentservice altered in its availability level in the context of some experiment as a result of being
    targeted by componentservice-knockdown reagent(s).
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ReagentTargetedComponentservice
    class_class_curie: ClassVar[str] = "testlink:ReagentTargetedComponentservice"
    class_name: ClassVar[str] = "reagent targeted componentservice"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ReagentTargetedComponentservice

    id: Union[str, ReagentTargetedComponentserviceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ReagentTargetedComponentserviceId):
            self.id = ReagentTargetedComponentserviceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalAttribute(Attribute):
    """
    Attributes relating to a empirical manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmpiricalAttribute
    class_class_curie: ClassVar[str] = "testlink:EmpiricalAttribute"
    class_name: ClassVar[str] = "empirical attribute"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmpiricalAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalMeasurement(EmpiricalAttribute):
    """
    A empirical measurement is a special kind of attribute which results from a quality of serviceunit observation
    from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmpiricalMeasurement
    class_class_curie: ClassVar[str] = "testlink:EmpiricalMeasurement"
    class_name: ClassVar[str] = "empirical measurement"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmpiricalMeasurement

    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_attribute_type is None:
            raise ValueError("has_attribute_type must be supplied")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalModifier(EmpiricalAttribute):
    """
    Used to characterize and specify the observable abnormalities defined in the observable abnormality sub-ontology,
    with respect to severity, laterality, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmpiricalModifier
    class_class_curie: ClassVar[str] = "testlink:EmpiricalModifier"
    class_name: ClassVar[str] = "empirical modifier"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmpiricalModifier

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalCourse(EmpiricalAttribute):
    """
    The course a error typically takes from its onset, progression in time, and eventual resolution or death of the
    affected individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmpiricalCourse
    class_class_curie: ClassVar[str] = "testlink:EmpiricalCourse"
    class_name: ClassVar[str] = "empirical course"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmpiricalCourse

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Onset(EmpiricalCourse):
    """
    The age group in which (error) symptom manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Onset
    class_class_curie: ClassVar[str] = "testlink:Onset"
    class_name: ClassVar[str] = "onset"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Onset

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalEntity(NamedThing):
    """
    Any entity or process that exists in the empirical domain and outside the computational realm. Errors are placed
    under computational entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmpiricalEntity
    class_class_curie: ClassVar[str] = "testlink:EmpiricalEntity"
    class_name: ClassVar[str] = "empirical entity"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmpiricalEntity

    id: Union[str, EmpiricalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmpiricalEntityId):
            self.id = EmpiricalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalTrial(EmpiricalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmpiricalTrial
    class_class_curie: ClassVar[str] = "testlink:EmpiricalTrial"
    class_name: ClassVar[str] = "empirical trial"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmpiricalTrial

    id: Union[str, EmpiricalTrialId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmpiricalTrialId):
            self.id = EmpiricalTrialId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalIntervention(EmpiricalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmpiricalIntervention
    class_class_curie: ClassVar[str] = "testlink:EmpiricalIntervention"
    class_name: ClassVar[str] = "empirical intervention"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmpiricalIntervention

    id: Union[str, EmpiricalInterventionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmpiricalInterventionId):
            self.id = EmpiricalInterventionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalFinding(ObservableFeature):
    """
    this category is currently considered broad enough to tag empirical lab measurements and other computational
    attributes taken as 'empirical traits' with some statistical score, for example, a p value in service
    associations.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.EmpiricalFinding
    class_class_curie: ClassVar[str] = "testlink:EmpiricalFinding"
    class_name: ClassVar[str] = "empirical finding"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EmpiricalFinding

    id: Union[str, EmpiricalFindingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, EmpiricalAttribute], List[Union[dict, EmpiricalAttribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmpiricalFindingId):
            self.id = EmpiricalFindingId(self.id)

        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=EmpiricalAttribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class OfflineMaintenance(EmpiricalIntervention):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OfflineMaintenance
    class_class_curie: ClassVar[str] = "testlink:OfflineMaintenance"
    class_name: ClassVar[str] = "offline maintenance"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OfflineMaintenance

    id: Union[str, OfflineMaintenanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OfflineMaintenanceId):
            self.id = OfflineMaintenanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicAttribute(Attribute):
    """
    Attributes relating to a socioeconomic manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SocioeconomicAttribute
    class_class_curie: ClassVar[str] = "testlink:SocioeconomicAttribute"
    class_name: ClassVar[str] = "socioeconomic attribute"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SocioeconomicAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Case(IndividualSystem):
    """
    An individual system that has a patient role in some empirical context.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Case
    class_class_curie: ClassVar[str] = "testlink:Case"
    class_name: ClassVar[str] = "case"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Case

    id: Union[str, CaseId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cohort(StudyPopulation):
    """
    A group of individuals banded together or repaired as a group who share common characteristics. A cohort 'study'
    is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through
    time.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.Cohort
    class_class_curie: ClassVar[str] = "testlink:Cohort"
    class_name: ClassVar[str] = "cohort"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Cohort

    id: Union[str, CohortId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

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
class ServiceBackgroundExposure(WorkloadEntity):
    """
    A service background exposure is where an individual's specific service background of serviceunits, sequence
    variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or
    influencing an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceBackgroundExposure
    class_class_curie: ClassVar[str] = "testlink:ServiceBackgroundExposure"
    class_name: ClassVar[str] = "service background exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceBackgroundExposure

    id: Union[str, ServiceBackgroundExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceBackgroundExposureId):
            self.id = ServiceBackgroundExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if self.has_componentservice_or_servicetype is None:
            self.has_componentservice_or_servicetype = []
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype]
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


class FaultyEntityMixin(YAMLRoot):
    """
    A faulty (abnormal) structure or process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.FaultyEntityMixin
    class_class_curie: ClassVar[str] = "testlink:FaultyEntityMixin"
    class_name: ClassVar[str] = "faulty entity mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FaultyEntityMixin


@dataclass
class FaultyProcess(ComputationalProcess):
    """
    A compulogic function or a process having an abnormal or deleterious effect at the subcomponent, component,
    multi-component, node, or system level.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.FaultyProcess
    class_class_curie: ClassVar[str] = "testlink:FaultyProcess"
    class_name: ClassVar[str] = "faulty process"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FaultyProcess

    id: Union[str, FaultyProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyProcessId):
            self.id = FaultyProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureExposure(ErrorOrObservableFeature):
    """
    A error or observable feature exposure is where a error state is manifested which represents an precondition,
    leading to or influencing an outcome, e.g. hypertension leading to a related error outcome such as cardiovascular
    error.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureExposure
    class_class_curie: ClassVar[str] = "testlink:ErrorOrObservableFeatureExposure"
    class_name: ClassVar[str] = "error or observable feature exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureExposure

    id: Union[str, ErrorOrObservableFeatureExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureExposureId):
            self.id = ErrorOrObservableFeatureExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class FaultyProcessExposure(FaultyProcess):
    """
    A faulty process, when viewed as an exposure, representing an precondition, leading to or influencing an outcome,
    e.g. autoimmunity leading to disease.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.FaultyProcessExposure
    class_class_curie: ClassVar[str] = "testlink:FaultyProcessExposure"
    class_name: ClassVar[str] = "faulty process exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FaultyProcessExposure

    id: Union[str, FaultyProcessExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyProcessExposureId):
            self.id = FaultyProcessExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentStructure(DeploymentEntity):
    """
    An deployment structure with the potential of have an abnormal or deleterious effect at the process, serviceunit,
    multiserviceunit, or systemal level.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.FaultyDeploymentStructure
    class_class_curie: ClassVar[str] = "testlink:FaultyDeploymentStructure"
    class_name: ClassVar[str] = "faulty deployment structure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FaultyDeploymentStructure

    id: Union[str, FaultyDeploymentStructureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyDeploymentStructureId):
            self.id = FaultyDeploymentStructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentExposure(FaultyDeploymentStructure):
    """
    An abnormal deployment structure, when viewed as an exposure, representing an precondition, leading to or
    influencing an outcome,
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.FaultyDeploymentExposure
    class_class_curie: ClassVar[str] = "testlink:FaultyDeploymentExposure"
    class_name: ClassVar[str] = "faulty deployment exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FaultyDeploymentExposure

    id: Union[str, FaultyDeploymentExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyDeploymentExposureId):
            self.id = FaultyDeploymentExposureId(self.id)

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
class ComplexOrchestrationExposure(OrchestrationExposure):
    """
    A complex orchestration exposure is an intake of a orchestration cluster (e.g. gasoline), other than a
    administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComplexOrchestrationExposure
    class_class_curie: ClassVar[str] = "testlink:ComplexOrchestrationExposure"
    class_name: ClassVar[str] = "complex orchestration exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComplexOrchestrationExposure

    id: Union[str, ComplexOrchestrationExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComplexOrchestrationExposureId):
            self.id = ComplexOrchestrationExposureId(self.id)

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalExposure(AdministrativeOperation):
    """
    A administrative operational exposure is an intake of a particular administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperationalExposure
    class_class_curie: ClassVar[str] = "testlink:AdministrativeOperationalExposure"
    class_name: ClassVar[str] = "administrative operational exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperationalExposure

    id: Union[str, AdministrativeOperationalExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AdministrativeOperationalExposureId):
            self.id = AdministrativeOperationalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToComponentserviceInteractionExposure(AdministrativeOperationalExposure):
    """
    administrative operational to componentservice interaction exposure is a administrative operational exposure is
    where the interactions of the administrative operational with specific componentservices are known to constitute
    an 'exposure' to the system, leading to or influencing an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperationalToComponentserviceInteractionExposure
    class_class_curie: ClassVar[str] = "testlink:AdministrativeOperationalToComponentserviceInteractionExposure"
    class_name: ClassVar[str] = "administrative operational to componentservice interaction exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperationalToComponentserviceInteractionExposure

    id: Union[str, AdministrativeOperationalToComponentserviceInteractionExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AdministrativeOperationalToComponentserviceInteractionExposureId):
            self.id = AdministrativeOperationalToComponentserviceInteractionExposureId(self.id)

        if self.has_componentservice_or_servicetype is None:
            self.has_componentservice_or_servicetype = []
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype]
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


@dataclass
class Repairing(NamedThing):
    """
    A repairing is targeted at a error or observability and may involve multiple administrative operational
    'exposures', engineering devices and/or procedures
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Repairing
    class_class_curie: ClassVar[str] = "testlink:Repairing"
    class_name: ClassVar[str] = "repairing"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Repairing

    id: Union[str, RepairingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_administrative_operation: Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]] = empty_list()
    has_device: Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]] = empty_list()
    has_procedure: Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RepairingId):
            self.id = RepairingId(self.id)

        if self.has_administrative_operation is None:
            self.has_administrative_operation = []
        if not isinstance(self.has_administrative_operation, list):
            self.has_administrative_operation = [self.has_administrative_operation]
        self.has_administrative_operation = [v if isinstance(v, AdministrativeOperationId) else AdministrativeOperationId(v) for v in self.has_administrative_operation]

        if self.has_device is None:
            self.has_device = []
        if not isinstance(self.has_device, list):
            self.has_device = [self.has_device]
        self.has_device = [v if isinstance(v, DeviceId) else DeviceId(v) for v in self.has_device]

        if self.has_procedure is None:
            self.has_procedure = []
        if not isinstance(self.has_procedure, list):
            self.has_procedure = [self.has_procedure]
        self.has_procedure = [v if isinstance(v, ProcedureId) else ProcedureId(v) for v in self.has_procedure]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class BioticExposure(SystemTaxon):
    """
    A biotic exposure is an intake of (sometimes faulty) computational systems (including viruses)
    """
    _inherited_slots: ClassVar[List[str]] = ["subclass_of"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.BioticExposure
    class_class_curie: ClassVar[str] = "testlink:BioticExposure"
    class_name: ClassVar[str] = "biotic exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BioticExposure

    id: Union[str, BioticExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BioticExposureId):
            self.id = BioticExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class GeographicExposure(GeographicLocation):
    """
    A geographic exposure is a factor relating to geographic proximity to some impactful entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.GeographicExposure
    class_class_curie: ClassVar[str] = "testlink:GeographicExposure"
    class_name: ClassVar[str] = "geographic exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.GeographicExposure

    id: Union[str, GeographicExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeographicExposureId):
            self.id = GeographicExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalExposure(EnvironmentalProcess):
    """
    A environmental exposure is a factor relating to abiotic processes in the environment including atmospheric (heat,
    cold, general pollution) and water-born contaminants
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EnvironmentalExposure
    class_class_curie: ClassVar[str] = "testlink:EnvironmentalExposure"
    class_name: ClassVar[str] = "environmental exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EnvironmentalExposure

    id: Union[str, EnvironmentalExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentalExposureId):
            self.id = EnvironmentalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralExposure(Behavior):
    """
    A behavioral exposure is a factor relating to behavior impacting an individual.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.BehavioralExposure
    class_class_curie: ClassVar[str] = "testlink:BehavioralExposure"
    class_name: ClassVar[str] = "behavioral exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BehavioralExposure

    id: Union[str, BehavioralExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehavioralExposureId):
            self.id = BehavioralExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicExposure(Behavior):
    """
    A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g.
    poverty).
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.SocioeconomicExposure
    class_class_curie: ClassVar[str] = "testlink:SocioeconomicExposure"
    class_name: ClassVar[str] = "socioeconomic exposure"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SocioeconomicExposure

    id: Union[str, SocioeconomicExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Union[Union[dict, SocioeconomicAttribute], List[Union[dict, SocioeconomicAttribute]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SocioeconomicExposureId):
            self.id = SocioeconomicExposureId(self.id)

        if self.has_attribute is None:
            raise ValueError("has_attribute must be supplied")
        elif not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        elif len(self.has_attribute) == 0:
            raise ValueError(f"has_attribute must be a non-empty list")
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=SocioeconomicAttribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


class Outcome(YAMLRoot):
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of
    various categories of possible computational or non-computational (e.g. empirical) outcomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.Outcome
    class_class_curie: ClassVar[str] = "testlink:Outcome"
    class_name: ClassVar[str] = "outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.Outcome


@dataclass
class FaultyProcessOutcome(FaultyProcess):
    """
    An outcome resulting from an exposure event which is the manifestation of a faulty process.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.FaultyProcessOutcome
    class_class_curie: ClassVar[str] = "testlink:FaultyProcessOutcome"
    class_name: ClassVar[str] = "faulty process outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FaultyProcessOutcome

    id: Union[str, FaultyProcessOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyProcessOutcomeId):
            self.id = FaultyProcessOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentOutcome(FaultyDeploymentStructure):
    """
    An outcome resulting from an exposure event which is the manifestation of an abnormal deployment structure.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.FaultyDeploymentOutcome
    class_class_curie: ClassVar[str] = "testlink:FaultyDeploymentOutcome"
    class_name: ClassVar[str] = "faulty deployment outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FaultyDeploymentOutcome

    id: Union[str, FaultyDeploymentOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyDeploymentOutcomeId):
            self.id = FaultyDeploymentOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureOutcome(ErrorOrObservableFeature):
    """
    logical outcomes resulting from an exposure event which is the manifestation of a error or other characteristic
    observability.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureOutcome
    class_class_curie: ClassVar[str] = "testlink:ErrorOrObservableFeatureOutcome"
    class_name: ClassVar[str] = "error or observable feature outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureOutcome

    id: Union[str, ErrorOrObservableFeatureOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureOutcomeId):
            self.id = ErrorOrObservableFeatureOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralOutcome(Behavior):
    """
    An outcome resulting from an exposure event which is the manifestation of individual behavior.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.BehavioralOutcome
    class_class_curie: ClassVar[str] = "testlink:BehavioralOutcome"
    class_name: ClassVar[str] = "behavioral outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BehavioralOutcome

    id: Union[str, BehavioralOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehavioralOutcomeId):
            self.id = BehavioralOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OfflineMaintenanceOutcome(OfflineMaintenance):
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room
    visit) or chronic (inpatient) offline maintenance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OfflineMaintenanceOutcome
    class_class_curie: ClassVar[str] = "testlink:OfflineMaintenanceOutcome"
    class_name: ClassVar[str] = "offline maintenance outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OfflineMaintenanceOutcome

    id: Union[str, OfflineMaintenanceOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OfflineMaintenanceOutcomeId):
            self.id = OfflineMaintenanceOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MortalityOutcome(Death):
    """
    An outcome of death from resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.MortalityOutcome
    class_class_curie: ClassVar[str] = "testlink:MortalityOutcome"
    class_name: ClassVar[str] = "mortality outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MortalityOutcome

    id: Union[str, MortalityOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MortalityOutcomeId):
            self.id = MortalityOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EpidemiologicalOutcome(ComputationalEntity):
    """
    An epidemiological outcome, such as societal error burden, resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EpidemiologicalOutcome
    class_class_curie: ClassVar[str] = "testlink:EpidemiologicalOutcome"
    class_name: ClassVar[str] = "epidemiological outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EpidemiologicalOutcome

    id: Union[str, EpidemiologicalOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EpidemiologicalOutcomeId):
            self.id = EpidemiologicalOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicOutcome(Behavior):
    """
    An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure
    event
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = TESTLINK.SocioeconomicOutcome
    class_class_curie: ClassVar[str] = "testlink:SocioeconomicOutcome"
    class_name: ClassVar[str] = "socioeconomic outcome"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SocioeconomicOutcome

    id: Union[str, SocioeconomicOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SocioeconomicOutcomeId):
            self.id = SocioeconomicOutcomeId(self.id)

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
class ContributorAssociation(Association):
    """
    Any association between an entity (such as a publication) and various agents that contribute to its realisation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ContributorAssociation
    class_class_curie: ClassVar[str] = "testlink:ContributorAssociation"
    class_name: ClassVar[str] = "contributor association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ContributorAssociation

    id: Union[str, ContributorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, InformationContentEntityId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, AgentId] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ContributorAssociationId):
            self.id = ContributorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, InformationContentEntityId):
            self.subject = InformationContentEntityId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AgentId):
            self.object = AgentId(self.object)

        if self.qualifiers is None:
            self.qualifiers = []
        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers]
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToServiceunittypePartAssociation(Association):
    """
    Any association between one serviceunittype and a microservice entity that is a subset of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToServiceunittypePartAssociation
    class_class_curie: ClassVar[str] = "testlink:ServiceunittypeToServiceunittypePartAssociation"
    class_name: ClassVar[str] = "serviceunittype to serviceunittype part association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToServiceunittypePartAssociation

    id: Union[str, ServiceunittypeToServiceunittypePartAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToServiceunittypePartAssociationId):
            self.id = ServiceunittypeToServiceunittypePartAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServiceunittypeId):
            self.object = ServiceunittypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToComponentserviceAssociation(Association):
    """
    Any association between a serviceunittype and a componentservice. The serviceunittype have have multiple variants
    in that componentservice or a single one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "testlink:ServiceunittypeToComponentserviceAssociation"
    class_name: ClassVar[str] = "serviceunittype to componentservice association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToComponentserviceAssociation

    id: Union[str, ServiceunittypeToComponentserviceAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[dict, Componentservice] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToComponentserviceAssociationId):
            self.id = ServiceunittypeToComponentserviceAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToVariantAssociation(Association):
    """
    Any association between a serviceunittype and a sequence variant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToVariantAssociation
    class_class_curie: ClassVar[str] = "testlink:ServiceunittypeToVariantAssociation"
    class_name: ClassVar[str] = "serviceunittype to variant association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToVariantAssociation

    id: Union[str, ServiceunittypeToVariantAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToVariantAssociationId):
            self.id = ServiceunittypeToVariantAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceAssociation(Association):
    """
    abstract parent class for different kinds of componentservice-serviceunit or servicetype to servicetype
    relationships. Includes homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToComponentserviceAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToComponentserviceAssociation

    id: Union[str, ComponentserviceToComponentserviceAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceHomologyAssociation(ComponentserviceToComponentserviceAssociation):
    """
    A homology association between two componentservices. May be orthology (in which case the species of subject and
    object should differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToComponentserviceHomologyAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToComponentserviceHomologyAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice homology association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToComponentserviceHomologyAssociation

    id: Union[str, ComponentserviceToComponentserviceHomologyAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToComponentserviceHomologyAssociationId):
            self.id = ComponentserviceToComponentserviceHomologyAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceAvailabilityMixin(YAMLRoot):
    """
    Observed componentservice availability intensity, context (site, stage) and associated observable status within
    which the availability occurs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceAvailabilityMixin
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceAvailabilityMixin"
    class_name: ClassVar[str] = "componentservice availability mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceAvailabilityMixin

    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceCoavailabilityAssociation(ComponentserviceToComponentserviceAssociation):
    """
    Indicates that two componentservices are co-available, generally under the same conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToComponentserviceCoavailabilityAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToComponentserviceCoavailabilityAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice coavailability association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToComponentserviceCoavailabilityAssociation

    id: Union[str, ComponentserviceToComponentserviceCoavailabilityAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToComponentserviceCoavailabilityAssociationId):
            self.id = ComponentserviceToComponentserviceCoavailabilityAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseComponentserviceToComponentserviceInteraction(ComponentserviceToComponentserviceAssociation):
    """
    An interaction between two componentservices or two servicetypes. May be cyber (e.g. serviceinstance binding) or
    service (between componentservices). May be symmetric (e.g. serviceinstance interaction) or directed (e.g.
    phosphorylation)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.PairwiseComponentserviceToComponentserviceInteraction
    class_class_curie: ClassVar[str] = "testlink:PairwiseComponentserviceToComponentserviceInteraction"
    class_name: ClassVar[str] = "pairwise componentservice to componentservice interaction"
    class_model_uri: ClassVar[URIRef] = TESTLINK.PairwiseComponentserviceToComponentserviceInteraction

    id: Union[str, PairwiseComponentserviceToComponentserviceInteractionId] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PairwiseComponentserviceToComponentserviceInteractionId):
            self.id = PairwiseComponentserviceToComponentserviceInteractionId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.relation is None:
            raise ValueError("relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseOperationallyInteraction(PairwiseComponentserviceToComponentserviceInteraction):
    """
    An interaction at the operational level between two cyber entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.PairwiseOperationallyInteraction
    class_class_curie: ClassVar[str] = "testlink:PairwiseOperationallyInteraction"
    class_name: ClassVar[str] = "pairwise operationally interaction"
    class_model_uri: ClassVar[URIRef] = TESTLINK.PairwiseOperationallyInteraction

    id: Union[str, PairwiseOperationallyInteractionId] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, OperationalEntityId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, OperationalEntityId] = None
    interacting_tasks_category: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PairwiseOperationallyInteractionId):
            self.id = PairwiseOperationallyInteractionId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.relation is None:
            raise ValueError("relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, OperationalEntityId):
            self.object = OperationalEntityId(self.object)

        if self.interacting_tasks_category is not None and not isinstance(self.interacting_tasks_category, OntologyClassId):
            self.interacting_tasks_category = OntologyClassId(self.interacting_tasks_category)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeToEntityAssociationMixin(YAMLRoot):
    """
    An relationship between a component type and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentTypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:ComponentTypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "component type to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentTypeToEntityAssociationMixin

    subject: Union[str, ComponentTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentTypeId):
            self.subject = ComponentTypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeToErrorOrObservableFeatureAssociation(Association):
    """
    An relationship between a component type and a error or a observability, where the component type is derived from
    an individual with that error or observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentTypeToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentTypeToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "component type to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentTypeToErrorOrObservableFeatureAssociation

    id: Union[str, ComponentTypeToErrorOrObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentTypeToErrorOrObservableFeatureAssociationId):
            self.id = ComponentTypeToErrorOrObservableFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ErrorOrObservableFeatureId):
            self.subject = ErrorOrObservableFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OperationalEntityToEntityAssociationMixin(YAMLRoot):
    """
    An interaction between a operational entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OperationalEntityToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:OperationalEntityToEntityAssociationMixin"
    class_name: ClassVar[str] = "operational entity to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OperationalEntityToEntityAssociationMixin

    subject: Union[str, OperationalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToEntityAssociationMixin(OperationalEntityToEntityAssociationMixin):
    """
    An interaction between a administrative operational and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperationalToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:AdministrativeOperationalToEntityAssociationMixin"
    class_name: ClassVar[str] = "administrative operational to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperationalToEntityAssociationMixin

    subject: Union[str, AdministrativeOperationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, AdministrativeOperationId):
            self.subject = AdministrativeOperationId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToEntityAssociationMixin(OperationalEntityToEntityAssociationMixin):
    """
    An interaction between a orchestration entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:OrchestrationToEntityAssociationMixin"
    class_name: ClassVar[str] = "orchestration to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToEntityAssociationMixin

    subject: Union[str, ControlActorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ControlActorId):
            self.subject = ControlActorId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class CaseToEntityAssociationMixin(YAMLRoot):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.CaseToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:CaseToEntityAssociationMixin"
    class_name: ClassVar[str] = "case to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.CaseToEntityAssociationMixin

    subject: Union[str, CaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToOrchestrationAssociation(Association):
    """
    A relationship between two orchestration entities. This can encompass actual interactions as well as temporal
    causal edges, e.g. one orchestration converted to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToOrchestrationAssociation
    class_class_curie: ClassVar[str] = "testlink:OrchestrationToOrchestrationAssociation"
    class_name: ClassVar[str] = "orchestration to orchestration association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToOrchestrationAssociation

    id: Union[str, OrchestrationToOrchestrationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, ControlActorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToOrchestrationAssociationId):
            self.id = OrchestrationToOrchestrationAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ControlActorId):
            self.object = ControlActorId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToOrchestrationDerivationAssociation(OrchestrationToOrchestrationAssociation):
    """
    A causal relationship between two orchestration entities, where the subject represents the upstream entity and the
    object represents the downstream. For any such association there is an implicit reaction:
    IF
    R has-input C1 AND
    R has-output C2 AND
    R enabled-by P AND
    R type Reaction
    THEN
    C1 derives-into C2 <<catalyst qualifier P>>
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToOrchestrationDerivationAssociation
    class_class_curie: ClassVar[str] = "testlink:OrchestrationToOrchestrationDerivationAssociation"
    class_name: ClassVar[str] = "orchestration to orchestration derivation association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToOrchestrationDerivationAssociation

    id: Union[str, OrchestrationToOrchestrationDerivationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ControlActorId] = None
    object: Union[str, ControlActorId] = None
    predicate: Union[str, PredicateType] = None
    catalyst_qualifier: Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToOrchestrationDerivationAssociationId):
            self.id = OrchestrationToOrchestrationDerivationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ControlActorId):
            self.subject = ControlActorId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ControlActorId):
            self.object = ControlActorId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.catalyst_qualifier is None:
            self.catalyst_qualifier = []
        if not isinstance(self.catalyst_qualifier, list):
            self.catalyst_qualifier = [self.catalyst_qualifier]
        self.catalyst_qualifier = [v if isinstance(v, MacrooperationalMachineMixin) else MacrooperationalMachineMixin(**v) for v in self.catalyst_qualifier]

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToErrorOrObservableFeatureAssociation(Association):
    """
    An interaction between a orchestration entity and a observability or error, where the presence of the
    orchestration gives rise to or exacerbates the observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:OrchestrationToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "orchestration to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToErrorOrObservableFeatureAssociation

    id: Union[str, OrchestrationToErrorOrObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToErrorOrObservableFeatureAssociationId):
            self.id = OrchestrationToErrorOrObservableFeatureAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ErrorOrObservableFeatureId):
            self.object = ErrorOrObservableFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToPathwayAssociation(Association):
    """
    An interaction between a orchestration entity and a computational process or pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToPathwayAssociation
    class_class_curie: ClassVar[str] = "testlink:OrchestrationToPathwayAssociation"
    class_name: ClassVar[str] = "orchestration to pathway association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToPathwayAssociation

    id: Union[str, OrchestrationToPathwayAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToPathwayAssociationId):
            self.id = OrchestrationToPathwayAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToComponentserviceAssociation(Association):
    """
    An interaction between a orchestration entity and a componentservice or servicetype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "testlink:OrchestrationToComponentserviceAssociation"
    class_name: ClassVar[str] = "orchestration to componentservice association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.OrchestrationToComponentserviceAssociation

    id: Union[str, OrchestrationToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToComponentserviceAssociationId):
            self.id = OrchestrationToComponentserviceAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToComponentserviceAssociation(Association):
    """
    An interaction between a administrative operational and a componentservice or servicetype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperationalToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "testlink:AdministrativeOperationalToComponentserviceAssociation"
    class_name: ClassVar[str] = "administrative operational to componentservice association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.AdministrativeOperationalToComponentserviceAssociation

    id: Union[str, AdministrativeOperationalToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AdministrativeOperationalToComponentserviceAssociationId):
            self.id = AdministrativeOperationalToComponentserviceAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleToEntityAssociationMixin(YAMLRoot):
    """
    An association between a resource sample and something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ResourceSampleToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:ResourceSampleToEntityAssociationMixin"
    class_name: ClassVar[str] = "resource sample to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ResourceSampleToEntityAssociationMixin

    subject: Union[str, ResourceSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ResourceSampleId):
            self.subject = ResourceSampleId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleDerivationAssociation(Association):
    """
    An association between a resource sample and the resource entity from which it is derived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ResourceSampleDerivationAssociation
    class_class_curie: ClassVar[str] = "testlink:ResourceSampleDerivationAssociation"
    class_name: ClassVar[str] = "resource sample derivation association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ResourceSampleDerivationAssociation

    id: Union[str, ResourceSampleDerivationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ResourceSampleId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ResourceSampleDerivationAssociationId):
            self.id = ResourceSampleDerivationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ResourceSampleId):
            self.subject = ResourceSampleId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleToErrorOrObservableFeatureAssociation(Association):
    """
    An association between a resource sample and a error or observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ResourceSampleToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:ResourceSampleToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "resource sample to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ResourceSampleToErrorOrObservableFeatureAssociation

    id: Union[str, ResourceSampleToErrorOrObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ResourceSampleToErrorOrObservableFeatureAssociationId):
            self.id = ResourceSampleToErrorOrObservableFeatureAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:ErrorToEntityAssociationMixin"
    class_name: ClassVar[str] = "error to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorToEntityAssociationMixin

    subject: Union[str, ErrorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ErrorId):
            self.subject = ErrorId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class EntityToExposureEventAssociationMixin(YAMLRoot):
    """
    An association between some entity and an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EntityToExposureEventAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:EntityToExposureEventAssociationMixin"
    class_name: ClassVar[str] = "entity to exposure event association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EntityToExposureEventAssociationMixin

    object: Union[dict, ExposureEvent] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ExposureEvent):
            self.object = ExposureEvent(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ErrorToExposureEventAssociation(Association):
    """
    An association between an exposure event and a error.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorToExposureEventAssociation
    class_class_curie: ClassVar[str] = "testlink:ErrorToExposureEventAssociation"
    class_name: ClassVar[str] = "error to exposure event association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorToExposureEventAssociation

    id: Union[str, ErrorToExposureEventAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorToExposureEventAssociationId):
            self.id = ErrorToExposureEventAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToEntityAssociationMixin(YAMLRoot):
    """
    An association between some exposure event and some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ExposureEventToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:ExposureEventToEntityAssociationMixin"
    class_name: ClassVar[str] = "exposure event to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ExposureEventToEntityAssociationMixin

    subject: Union[dict, ExposureEvent] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ExposureEvent):
            self.subject = ExposureEvent(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class EntityToOutcomeAssociationMixin(YAMLRoot):
    """
    An association between some entity and an outcome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EntityToOutcomeAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:EntityToOutcomeAssociationMixin"
    class_name: ClassVar[str] = "entity to outcome association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EntityToOutcomeAssociationMixin

    object: Union[dict, Outcome] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Outcome):
            self.object = Outcome()

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToOutcomeAssociation(Association):
    """
    An association between an exposure event and an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ExposureEventToOutcomeAssociation
    class_class_curie: ClassVar[str] = "testlink:ExposureEventToOutcomeAssociation"
    class_name: ClassVar[str] = "exposure event to outcome association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ExposureEventToOutcomeAssociation

    id: Union[str, ExposureEventToOutcomeAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    has_population_context: Optional[Union[str, PopulationOfIndividualSystemsId]] = None
    has_temporal_context: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExposureEventToOutcomeAssociationId):
            self.id = ExposureEventToOutcomeAssociationId(self.id)

        if self.has_population_context is not None and not isinstance(self.has_population_context, PopulationOfIndividualSystemsId):
            self.has_population_context = PopulationOfIndividualSystemsId(self.has_population_context)

        if self.has_temporal_context is not None and not isinstance(self.has_temporal_context, TimeType):
            self.has_temporal_context = TimeType(self.has_temporal_context)

        super().__post_init__(**kwargs)


@dataclass
class FrequencyQualifierMixin(YAMLRoot):
    """
    Qualifier for frequency type associations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.FrequencyQualifierMixin
    class_class_curie: ClassVar[str] = "testlink:FrequencyQualifierMixin"
    class_name: ClassVar[str] = "frequency qualifier mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FrequencyQualifierMixin

    frequency_qualifier: Optional[Union[dict, FrequencyValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(**self.frequency_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class EntityToFeatureOrErrorQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to error or observability associations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EntityToFeatureOrErrorQualifiersMixin
    class_class_curie: ClassVar[str] = "testlink:EntityToFeatureOrErrorQualifiersMixin"
    class_name: ClassVar[str] = "entity to feature or error qualifiers mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EntityToFeatureOrErrorQualifiersMixin

    severity_qualifier: Optional[Union[dict, SeverityValue]] = None
    onset_qualifier: Optional[Union[dict, Onset]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValue):
            self.severity_qualifier = SeverityValue(**self.severity_qualifier)

        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, Onset):
            self.onset_qualifier = Onset(**self.onset_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class EntityToObservableFeatureAssociationMixin(EntityToFeatureOrErrorQualifiersMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EntityToObservableFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:EntityToObservableFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to observable feature association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EntityToObservableFeatureAssociationMixin

    object: Union[str, ObservableFeatureId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ObservableFeatureId):
            self.object = ObservableFeatureId(self.object)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        super().__post_init__(**kwargs)


@dataclass
class EntityToErrorAssociationMixin(EntityToFeatureOrErrorQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EntityToErrorAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:EntityToErrorAssociationMixin"
    class_name: ClassVar[str] = "entity to error association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EntityToErrorAssociationMixin

    object: Union[str, ErrorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ErrorId):
            self.object = ErrorId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:ErrorOrObservableFeatureToEntityAssociationMixin"
    class_name: ClassVar[str] = "error or observable feature to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureToEntityAssociationMixin

    subject: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ErrorOrObservableFeatureId):
            self.subject = ErrorOrObservableFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureAssociationToLocationAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureAssociationToLocationAssociation
    class_class_curie: ClassVar[str] = "testlink:ErrorOrObservableFeatureAssociationToLocationAssociation"
    class_name: ClassVar[str] = "error or observable feature association to location association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureAssociationToLocationAssociation

    id: Union[str, ErrorOrObservableFeatureAssociationToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureAssociationToLocationAssociationId):
            self.id = ErrorOrObservableFeatureAssociationToLocationAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureToLocationAssociation(Association):
    """
    An association between either a error or a observable feature and an deployment entity, where the error/feature
    manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureToLocationAssociation
    class_class_curie: ClassVar[str] = "testlink:ErrorOrObservableFeatureToLocationAssociation"
    class_name: ClassVar[str] = "error or observable feature to location association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorOrObservableFeatureToLocationAssociation

    id: Union[str, ErrorOrObservableFeatureToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureToLocationAssociationId):
            self.id = ErrorOrObservableFeatureToLocationAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EntityToErrorOrObservableFeatureAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.EntityToErrorOrObservableFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:EntityToErrorOrObservableFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to error or observable feature association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.EntityToErrorOrObservableFeatureAssociationMixin

    object: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ErrorOrObservableFeatureId):
            self.object = ErrorOrObservableFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:ServiceunittypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "serviceunittype to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToEntityAssociationMixin

    subject: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToObservableFeatureAssociation(Association):
    """
    Any association between one serviceunittype and a observable feature, where having the serviceunittype confers the
    observability, either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:ServiceunittypeToObservableFeatureAssociation"
    class_name: ClassVar[str] = "serviceunittype to observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToObservableFeatureAssociation

    id: Union[str, ServiceunittypeToObservableFeatureAssociationId] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToObservableFeatureAssociationId):
            self.id = ServiceunittypeToObservableFeatureAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToObservableFeatureAssociation(Association):
    """
    Any association between an environment and a observable feature, where being in the environment influences the
    observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ExposureEventToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:ExposureEventToObservableFeatureAssociation"
    class_name: ClassVar[str] = "exposure event to observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ExposureEventToObservableFeatureAssociation

    id: Union[str, ExposureEventToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ExposureEvent] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExposureEventToObservableFeatureAssociationId):
            self.id = ExposureEventToObservableFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ExposureEvent):
            self.subject = ExposureEvent(**self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ErrorToObservableFeatureAssociation(Association):
    """
    An association between a error and a observable feature in which the observable feature is associated with the
    error in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ErrorToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:ErrorToObservableFeatureAssociation"
    class_name: ClassVar[str] = "error to observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ErrorToObservableFeatureAssociation

    id: Union[str, ErrorToObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorToObservableFeatureAssociationId):
            self.id = ErrorToObservableFeatureAssociationId(self.id)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class CaseToObservableFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a observable feature in which the individual has or
    has had the observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.CaseToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:CaseToObservableFeatureAssociation"
    class_name: ClassVar[str] = "case to observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.CaseToObservableFeatureAssociation

    id: Union[str, CaseToObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CaseToObservableFeatureAssociationId):
            self.id = CaseToObservableFeatureAssociationId(self.id)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class BehaviorToBehavioralFeatureAssociation(Association):
    """
    An association between an aggregate behavior and a behavioral feature manifested by the individual exhibited or
    has exhibited the behavior.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.BehaviorToBehavioralFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:BehaviorToBehavioralFeatureAssociation"
    class_name: ClassVar[str] = "behavior to behavioral feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.BehaviorToBehavioralFeatureAssociation

    id: Union[str, BehaviorToBehavioralFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, BehaviorId] = None
    object: Union[str, BehavioralFeatureId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehaviorToBehavioralFeatureAssociationId):
            self.id = BehaviorToBehavioralFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, BehaviorId):
            self.subject = BehaviorId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, BehavioralFeatureId):
            self.object = BehavioralFeatureId(self.object)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToEntityAssociationMixin"
    class_name: ClassVar[str] = "componentservice to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToEntityAssociationMixin

    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.VariantToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:VariantToEntityAssociationMixin"
    class_name: ClassVar[str] = "variant to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.VariantToEntityAssociationMixin

    subject: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToObservableFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToObservableFeatureAssociation"
    class_name: ClassVar[str] = "componentservice to observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToObservableFeatureAssociation

    id: Union[str, ComponentserviceToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToObservableFeatureAssociationId):
            self.id = ComponentserviceToObservableFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToErrorAssociation"
    class_name: ClassVar[str] = "componentservice to error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToErrorAssociation

    id: Union[str, ComponentserviceToErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToErrorAssociationId):
            self.id = ComponentserviceToErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantToComponentserviceAssociation(Association):
    """
    An association between a variant and a componentservice, where the variant has a service association with the
    componentservice (i.e. is in linkage disequilibrium)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.VariantToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "testlink:VariantToComponentserviceAssociation"
    class_name: ClassVar[str] = "variant to componentservice association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.VariantToComponentserviceAssociation

    id: Union[str, VariantToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, Componentservice] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToComponentserviceAssociationId):
            self.id = VariantToComponentserviceAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class VariantToComponentserviceAvailabilityAssociation(VariantToComponentserviceAssociation):
    """
    An association between a variant and availability of a componentservice (i.e. e-QTL)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.VariantToComponentserviceAvailabilityAssociation
    class_class_curie: ClassVar[str] = "testlink:VariantToComponentserviceAvailabilityAssociation"
    class_name: ClassVar[str] = "variant to componentservice availability association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.VariantToComponentserviceAvailabilityAssociation

    id: Union[str, VariantToComponentserviceAvailabilityAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, Componentservice] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToComponentserviceAvailabilityAssociationId):
            self.id = VariantToComponentserviceAvailabilityAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.VariantToPopulationAssociation
    class_class_curie: ClassVar[str] = "testlink:VariantToPopulationAssociation"
    class_name: ClassVar[str] = "variant to population association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.VariantToPopulationAssociation

    id: Union[str, VariantToPopulationAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, PopulationOfIndividualSystemsId] = None
    has_quotient: Optional[float] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_percentage: Optional[float] = None
    frequency_qualifier: Optional[Union[dict, FrequencyValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualSystemsId):
            self.object = PopulationOfIndividualSystemsId(self.object)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(**self.frequency_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.PopulationToPopulationAssociation
    class_class_curie: ClassVar[str] = "testlink:PopulationToPopulationAssociation"
    class_name: ClassVar[str] = "population to population association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.PopulationToPopulationAssociation

    id: Union[str, PopulationToPopulationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, PopulationOfIndividualSystemsId] = None
    object: Union[str, PopulationOfIndividualSystemsId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, PopulationOfIndividualSystemsId):
            self.subject = PopulationOfIndividualSystemsId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualSystemsId):
            self.object = PopulationOfIndividualSystemsId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class VariantToObservableFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.VariantToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "testlink:VariantToObservableFeatureAssociation"
    class_name: ClassVar[str] = "variant to observable feature association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.VariantToObservableFeatureAssociation

    id: Union[str, VariantToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToObservableFeatureAssociationId):
            self.id = VariantToObservableFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class VariantToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.VariantToErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:VariantToErrorAssociation"
    class_name: ClassVar[str] = "variant to error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.VariantToErrorAssociation

    id: Union[str, VariantToErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToErrorAssociationId):
            self.id = VariantToErrorAssociationId(self.id)

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

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:ServiceunittypeToErrorAssociation"
    class_name: ClassVar[str] = "serviceunittype to error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeToErrorAssociation

    id: Union[str, ServiceunittypeToErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToErrorAssociationId):
            self.id = ServiceunittypeToErrorAssociationId(self.id)

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

        super().__post_init__(**kwargs)


@dataclass
class ModelToErrorAssociationMixin(YAMLRoot):
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in
    that it recapitulates some features of the error in a way that is useful for studying the error outside a patient
    carrying the error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ModelToErrorAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:ModelToErrorAssociationMixin"
    class_name: ClassVar[str] = "model to error association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ModelToErrorAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceAsAModelOfErrorAssociation(ComponentserviceToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "componentservice as a model of error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceAsAModelOfErrorAssociation

    id: Union[str, ComponentserviceAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceAsAModelOfErrorAssociationId):
            self.id = ComponentserviceAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantAsAModelOfErrorAssociation(VariantToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.VariantAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:VariantAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "variant as a model of error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.VariantAsAModelOfErrorAssociation

    id: Union[str, VariantAsAModelOfErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantAsAModelOfErrorAssociationId):
            self.id = VariantAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeAsAModelOfErrorAssociation(ServiceunittypeToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:ServiceunittypeAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "serviceunittype as a model of error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceunittypeAsAModelOfErrorAssociation

    id: Union[str, ServiceunittypeAsAModelOfErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeAsAModelOfErrorAssociationId):
            self.id = ServiceunittypeAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeAsAModelOfErrorAssociation(ComponentTypeToErrorOrObservableFeatureAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentTypeAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentTypeAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "component type as a model of error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentTypeAsAModelOfErrorAssociation

    id: Union[str, ComponentTypeAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ComponentTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentTypeAsAModelOfErrorAssociationId):
            self.id = ComponentTypeAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentTypeId):
            self.subject = ComponentTypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class SystemicEntityAsAModelOfErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SystemicEntityAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:SystemicEntityAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "systemic entity as a model of error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SystemicEntityAsAModelOfErrorAssociation

    id: Union[str, SystemicEntityAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SystemicEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SystemicEntityAsAModelOfErrorAssociationId):
            self.id = SystemicEntityAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SystemicEntityId):
            self.subject = SystemicEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceHasVariantThatContributesToErrorAssociation(ComponentserviceToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceHasVariantThatContributesToErrorAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceHasVariantThatContributesToErrorAssociation"
    class_name: ClassVar[str] = "componentservice has variant that contributes to error association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceHasVariantThatContributesToErrorAssociation

    id: Union[str, ComponentserviceHasVariantThatContributesToErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    sequence_variant_qualifier: Optional[Union[str, SequenceVariantId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceHasVariantThatContributesToErrorAssociationId):
            self.id = ComponentserviceHasVariantThatContributesToErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToAvailabilitySiteAssociation(Association):
    """
    An association between a componentservice and an availability site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToAvailabilitySiteAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToAvailabilitySiteAssociation"
    class_name: ClassVar[str] = "componentservice to availability site association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToAvailabilitySiteAssociation

    id: Union[str, ComponentserviceToAvailabilitySiteAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToAvailabilitySiteAssociationId):
            self.id = ComponentserviceToAvailabilitySiteAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class SequenceVariantModulatesRepairingAssociation(Association):
    """
    An association between a sequence variant and a repairing or health intervention. The repairing object itself
    encompasses both the error and the administrative operational used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SequenceVariantModulatesRepairingAssociation
    class_class_curie: ClassVar[str] = "testlink:SequenceVariantModulatesRepairingAssociation"
    class_name: ClassVar[str] = "sequence variant modulates repairing association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SequenceVariantModulatesRepairingAssociation

    id: Union[str, SequenceVariantModulatesRepairingAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, RepairingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, RepairingId):
            self.object = RepairingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macrooperational machine mixin (componentservice, servicetype or complex of servicetypes)
    and either a operational activity, a computational process or a component location in which a function is
    executed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.FunctionalAssociation
    class_class_curie: ClassVar[str] = "testlink:FunctionalAssociation"
    class_name: ClassVar[str] = "functional association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.FunctionalAssociation

    id: Union[str, FunctionalAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComponentserviceOntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, MacrooperationalMachineMixin):
            self.subject = MacrooperationalMachineMixin(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOntologyClassId):
            self.object = ComponentserviceOntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToEntityAssociationMixin(YAMLRoot):
    """
    an association which has a macrooperational machine mixin mixin as a subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixinToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "testlink:MacrooperationalMachineMixinToEntityAssociationMixin"
    class_name: ClassVar[str] = "macrooperational machine mixin to entity association mixin"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixinToEntityAssociationMixin

    subject: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToOperationalActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    operational activity (as represented in the GO operational function branch), where the entity carries out the
    activity, or contributes to its execution
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixinToOperationalActivityAssociation
    class_class_curie: ClassVar[str] = "testlink:MacrooperationalMachineMixinToOperationalActivityAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to operational activity association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixinToOperationalActivityAssociation

    id: Union[str, MacrooperationalMachineMixinToOperationalActivityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, OperationalActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacrooperationalMachineMixinToOperationalActivityAssociationId):
            self.id = MacrooperationalMachineMixinToOperationalActivityAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, OperationalActivityId):
            self.object = OperationalActivityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToComputationalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    computational process or pathway (as represented in the GO computational process branch), where the entity carries
    out some part of the process, regulates it, or acts upstream of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixinToComputationalProcessAssociation
    class_class_curie: ClassVar[str] = "testlink:MacrooperationalMachineMixinToComputationalProcessAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to computational process association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixinToComputationalProcessAssociation

    id: Union[str, MacrooperationalMachineMixinToComputationalProcessAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComputationalProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacrooperationalMachineMixinToComputationalProcessAssociationId):
            self.id = MacrooperationalMachineMixinToComputationalProcessAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComputationalProcessId):
            self.object = ComputationalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    component (as represented in the GO component branch), where the entity carries out its function in the component
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixinToComponentAssociation
    class_class_curie: ClassVar[str] = "testlink:MacrooperationalMachineMixinToComponentAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to component association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.MacrooperationalMachineMixinToComponentAssociation

    id: Union[str, MacrooperationalMachineMixinToComponentAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacrooperationalMachineMixinToComponentAssociationId):
            self.id = MacrooperationalMachineMixinToComponentAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToGoTermAssociation
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToGoTermAssociation"
    class_name: ClassVar[str] = "componentservice to go term association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToGoTermAssociation

    id: Union[str, ComponentserviceToGoTermAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, OperationalEntityId] = None
    object: Union[str, ComponentserviceOntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToGoTermAssociationId):
            self.id = ComponentserviceToGoTermAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOntologyClassId):
            self.object = ComponentserviceOntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class SequenceAssociation(Association):
    """
    An association between a sequence feature and a workload entity it is localized to.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SequenceAssociation
    class_class_curie: ClassVar[str] = "testlink:SequenceAssociation"
    class_name: ClassVar[str] = "sequence association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SequenceAssociation

    id: Union[str, SequenceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceAssociationId):
            self.id = SequenceAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ServiceSequenceLocalization(SequenceAssociation):
    """
    A relationship between a sequence feature and a workload entity it is localized to. The reference entity may be a
    container, componentservice or information entity such as a namespace.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ServiceSequenceLocalization
    class_class_curie: ClassVar[str] = "testlink:ServiceSequenceLocalization"
    class_name: ClassVar[str] = "service sequence localization"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ServiceSequenceLocalization

    id: Union[str, ServiceSequenceLocalizationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, WorkloadEntityId] = None
    object: Union[str, WorkloadEntityId] = None
    predicate: Union[str, PredicateType] = None
    start_interbase_coordinate: Optional[int] = None
    end_interbase_coordinate: Optional[int] = None
    workload_build: Optional[str] = None
    strand: Optional[str] = None
    phase: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceSequenceLocalizationId):
            self.id = ServiceSequenceLocalizationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, WorkloadEntityId):
            self.subject = WorkloadEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, WorkloadEntityId):
            self.object = WorkloadEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.start_interbase_coordinate is not None and not isinstance(self.start_interbase_coordinate, int):
            self.start_interbase_coordinate = int(self.start_interbase_coordinate)

        if self.end_interbase_coordinate is not None and not isinstance(self.end_interbase_coordinate, int):
            self.end_interbase_coordinate = int(self.end_interbase_coordinate)

        if self.workload_build is not None and not isinstance(self.workload_build, str):
            self.workload_build = str(self.workload_build)

        if self.strand is not None and not isinstance(self.strand, str):
            self.strand = str(self.strand)

        if self.phase is not None and not isinstance(self.phase, str):
            self.phase = str(self.phase)

        super().__post_init__(**kwargs)


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular daemon is part of a particular componentserviceinstance or componentservice
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.SequenceFeatureRelationship
    class_class_curie: ClassVar[str] = "testlink:SequenceFeatureRelationship"
    class_name: ClassVar[str] = "sequence feature relationship"
    class_model_uri: ClassVar[URIRef] = TESTLINK.SequenceFeatureRelationship

    id: Union[str, SequenceFeatureRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, WorkloadEntityId] = None
    object: Union[str, WorkloadEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, WorkloadEntityId):
            self.subject = WorkloadEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, WorkloadEntityId):
            self.object = WorkloadEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceinstanceToComponentserviceRelationship(SequenceFeatureRelationship):
    """
    A componentservice is a collection of componentserviceinstances
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceinstanceToComponentserviceRelationship
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceinstanceToComponentserviceRelationship"
    class_name: ClassVar[str] = "componentserviceinstance to componentservice relationship"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceinstanceToComponentserviceRelationship

    id: Union[str, ComponentserviceinstanceToComponentserviceRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ComponentserviceinstanceId] = None
    object: Union[dict, Componentservice] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceinstanceToComponentserviceRelationshipId):
            self.id = ComponentserviceinstanceToComponentserviceRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceinstanceId):
            self.subject = ComponentserviceinstanceId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToServicetypeRelationship(SequenceFeatureRelationship):
    """
    A componentservice is transcribed and potentially translated to a servicetype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToServicetypeRelationship
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceToServicetypeRelationship"
    class_name: ClassVar[str] = "componentservice to servicetype relationship"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceToServicetypeRelationship

    id: Union[str, ComponentserviceToServicetypeRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, Componentservice] = None
    object: Union[dict, ServicetypeMixin] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToServicetypeRelationshipId):
            self.id = ComponentserviceToServicetypeRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, Componentservice):
            self.subject = Componentservice(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServicetypeMixin):
            self.object = ServicetypeMixin(**self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class DaemonToComponentserviceinstanceRelationship(SequenceFeatureRelationship):
    """
    A componentserviceinstance is formed from multiple daemons
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DaemonToComponentserviceinstanceRelationship
    class_class_curie: ClassVar[str] = "testlink:DaemonToComponentserviceinstanceRelationship"
    class_name: ClassVar[str] = "daemon to componentserviceinstance relationship"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DaemonToComponentserviceinstanceRelationship

    id: Union[str, DaemonToComponentserviceinstanceRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DaemonId] = None
    object: Union[str, ComponentserviceinstanceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DaemonToComponentserviceinstanceRelationshipId):
            self.id = DaemonToComponentserviceinstanceRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DaemonId):
            self.subject = DaemonId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceinstanceId):
            self.object = ComponentserviceinstanceId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceRegulatoryRelationship(Association):
    """
    A regulatory relationship between two componentservices
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceRegulatoryRelationship
    class_class_curie: ClassVar[str] = "testlink:ComponentserviceRegulatoryRelationship"
    class_name: ClassVar[str] = "componentservice regulatory relationship"
    class_model_uri: ClassVar[URIRef] = TESTLINK.ComponentserviceRegulatoryRelationship

    id: Union[str, ComponentserviceRegulatoryRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceRegulatoryRelationshipId):
            self.id = ComponentserviceRegulatoryRelationshipId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DeploymentEntityToDeploymentEntityAssociation
    class_class_curie: ClassVar[str] = "testlink:DeploymentEntityToDeploymentEntityAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DeploymentEntityToDeploymentEntityAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityAssociationId):
            self.id = DeploymentEntityToDeploymentEntityAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityPartOfAssociation(DeploymentEntityToDeploymentEntityAssociation):
    """
    A relationship between two deployment entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between components and componentservices, between
    componentservice and servicegroup/replicasets, servicegroup/replicasets and whole systems
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DeploymentEntityToDeploymentEntityPartOfAssociation
    class_class_curie: ClassVar[str] = "testlink:DeploymentEntityToDeploymentEntityPartOfAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity part of association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DeploymentEntityToDeploymentEntityPartOfAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityPartOfAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityPartOfAssociationId):
            self.id = DeploymentEntityToDeploymentEntityPartOfAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityOntogenicAssociation(DeploymentEntityToDeploymentEntityAssociation):
    """
    A relationship between two deployment entities where the relationship is ontogenic, i.e. the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TESTLINK.DeploymentEntityToDeploymentEntityOntogenicAssociation
    class_class_curie: ClassVar[str] = "testlink:DeploymentEntityToDeploymentEntityOntogenicAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity ontogenic association"
    class_model_uri: ClassVar[URIRef] = TESTLINK.DeploymentEntityToDeploymentEntityOntogenicAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityOntogenicAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityOntogenicAssociationId):
            self.id = DeploymentEntityToDeploymentEntityOntogenicAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

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

slots.source = Slot(uri=TESTLINK.source, name="source", curie=TESTLINK.curie('source'),
                   model_uri=TESTLINK.source, domain=None, range=Optional[Union[str, LabelType]])

slots.filler = Slot(uri=TESTLINK.filler, name="filler", curie=TESTLINK.curie('filler'),
                   model_uri=TESTLINK.filler, domain=NamedThing, range=Optional[Union[str, NamedThingId]])

slots.symbol = Slot(uri=TESTLINK.symbol, name="symbol", curie=TESTLINK.curie('symbol'),
                   model_uri=TESTLINK.symbol, domain=NamedThing, range=Optional[str])

slots.synonym = Slot(uri=TESTLINK.synonym, name="synonym", curie=TESTLINK.curie('synonym'),
                   model_uri=TESTLINK.synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.has_topic = Slot(uri=TESTLINK.has_topic, name="has topic", curie=TESTLINK.curie('has_topic'),
                   model_uri=TESTLINK.has_topic, domain=NamedThing, range=Optional[Union[str, OntologyClassId]])

slots.xref = Slot(uri=TESTLINK.xref, name="xref", curie=TESTLINK.curie('xref'),
                   model_uri=TESTLINK.xref, domain=NamedThing, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.full_name = Slot(uri=TESTLINK.full_name, name="full name", curie=TESTLINK.curie('full_name'),
                   model_uri=TESTLINK.full_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=TESTLINK.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=SIO['000122'], name="systematic synonym", curie=SIO.curie('000122'),
                   model_uri=TESTLINK.systematic_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.affiliation = Slot(uri=TESTLINK.affiliation, name="affiliation", curie=TESTLINK.curie('affiliation'),
                   model_uri=TESTLINK.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=TESTLINK.address, name="address", curie=TESTLINK.curie('address'),
                   model_uri=TESTLINK.address, domain=NamedThing, range=Optional[str])

slots.latitude = Slot(uri=TESTLINK.latitude, name="latitude", curie=TESTLINK.curie('latitude'),
                   model_uri=TESTLINK.latitude, domain=NamedThing, range=Optional[float])

slots.longitude = Slot(uri=TESTLINK.longitude, name="longitude", curie=TESTLINK.curie('longitude'),
                   model_uri=TESTLINK.longitude, domain=NamedThing, range=Optional[float])

slots.timepoint = Slot(uri=TESTLINK.timepoint, name="timepoint", curie=TESTLINK.curie('timepoint'),
                   model_uri=TESTLINK.timepoint, domain=NamedThing, range=Optional[Union[str, TimeType]])

slots.creation_date = Slot(uri=TESTLINK.creation_date, name="creation date", curie=TESTLINK.curie('creation_date'),
                   model_uri=TESTLINK.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.update_date = Slot(uri=TESTLINK.update_date, name="update date", curie=TESTLINK.curie('update_date'),
                   model_uri=TESTLINK.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.aggregate_statistic = Slot(uri=TESTLINK.aggregate_statistic, name="aggregate statistic", curie=TESTLINK.curie('aggregate_statistic'),
                   model_uri=TESTLINK.aggregate_statistic, domain=NamedThing, range=Optional[str])

slots.has_count = Slot(uri=TESTLINK.has_count, name="has count", curie=TESTLINK.curie('has_count'),
                   model_uri=TESTLINK.has_count, domain=NamedThing, range=Optional[int])

slots.has_total = Slot(uri=TESTLINK.has_total, name="has total", curie=TESTLINK.curie('has_total'),
                   model_uri=TESTLINK.has_total, domain=NamedThing, range=Optional[int])

slots.has_quotient = Slot(uri=TESTLINK.has_quotient, name="has quotient", curie=TESTLINK.curie('has_quotient'),
                   model_uri=TESTLINK.has_quotient, domain=NamedThing, range=Optional[float])

slots.has_percentage = Slot(uri=TESTLINK.has_percentage, name="has percentage", curie=TESTLINK.curie('has_percentage'),
                   model_uri=TESTLINK.has_percentage, domain=NamedThing, range=Optional[float])

slots.has_dataset = Slot(uri=DCT.source, name="has dataset", curie=DCT.curie('source'),
                   model_uri=TESTLINK.has_dataset, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.source_web_page = Slot(uri=TESTLINK.source_web_page, name="source web page", curie=TESTLINK.curie('source_web_page'),
                   model_uri=TESTLINK.source_web_page, domain=None, range=Optional[str])

slots.source_logo = Slot(uri=SCHEMA.logo, name="source logo", curie=SCHEMA.curie('logo'),
                   model_uri=TESTLINK.source_logo, domain=None, range=Optional[str])

slots.retrieved_on = Slot(uri=TESTLINK.retrieved_on, name="retrieved on", curie=TESTLINK.curie('retrieved_on'),
                   model_uri=TESTLINK.retrieved_on, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.version_of = Slot(uri=TESTLINK.version_of, name="version of", curie=TESTLINK.curie('version_of'),
                   model_uri=TESTLINK.version_of, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.version = Slot(uri=TESTLINK.version, name="version", curie=TESTLINK.curie('version'),
                   model_uri=TESTLINK.version, domain=Dataset, range=Optional[str])

slots.license = Slot(uri=TESTLINK.license, name="license", curie=TESTLINK.curie('license'),
                   model_uri=TESTLINK.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=TESTLINK.rights, name="rights", curie=TESTLINK.curie('rights'),
                   model_uri=TESTLINK.rights, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=TESTLINK.format, name="format", curie=TESTLINK.curie('format'),
                   model_uri=TESTLINK.format, domain=InformationContentEntity, range=Optional[str])

slots.created_with = Slot(uri=TESTLINK.created_with, name="created_with", curie=TESTLINK.curie('created_with'),
                   model_uri=TESTLINK.created_with, domain=Dataset, range=Optional[str])

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

slots.published_in = Slot(uri=TESTLINK.published_in, name="published in", curie=TESTLINK.curie('published_in'),
                   model_uri=TESTLINK.published_in, domain=Publication, range=Optional[Union[str, URIorCURIE]])

slots.iso_abbreviation = Slot(uri=TESTLINK.iso_abbreviation, name="iso abbreviation", curie=TESTLINK.curie('iso_abbreviation'),
                   model_uri=TESTLINK.iso_abbreviation, domain=Publication, range=Optional[str])

slots.authors = Slot(uri=TESTLINK.authors, name="authors", curie=TESTLINK.curie('authors'),
                   model_uri=TESTLINK.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.volume = Slot(uri=TESTLINK.volume, name="volume", curie=TESTLINK.curie('volume'),
                   model_uri=TESTLINK.volume, domain=Publication, range=Optional[str])

slots.chapter = Slot(uri=TESTLINK.chapter, name="chapter", curie=TESTLINK.curie('chapter'),
                   model_uri=TESTLINK.chapter, domain=BookChapter, range=Optional[str])

slots.issue = Slot(uri=TESTLINK.issue, name="issue", curie=TESTLINK.curie('issue'),
                   model_uri=TESTLINK.issue, domain=Publication, range=Optional[str])

slots.pages = Slot(uri=TESTLINK.pages, name="pages", curie=TESTLINK.curie('pages'),
                   model_uri=TESTLINK.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=TESTLINK.summary, name="summary", curie=TESTLINK.curie('summary'),
                   model_uri=TESTLINK.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=TESTLINK.keywords, name="keywords", curie=TESTLINK.curie('keywords'),
                   model_uri=TESTLINK.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.sumo_terms = Slot(uri=TESTLINK.sumo_terms, name="sumo terms", curie=TESTLINK.curie('sumo_terms'),
                   model_uri=TESTLINK.sumo_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.has_computational_sequence = Slot(uri=TESTLINK.has_computational_sequence, name="has computational sequence", curie=TESTLINK.curie('has_computational_sequence'),
                   model_uri=TESTLINK.has_computational_sequence, domain=NamedThing, range=Optional[Union[str, ComputationalSequence]])

slots.has_componentservice_or_servicetype = Slot(uri=TESTLINK.has_componentservice_or_servicetype, name="has componentservice or servicetype", curie=TESTLINK.curie('has_componentservice_or_servicetype'),
                   model_uri=TESTLINK.has_componentservice_or_servicetype, domain=NamedThing, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.has_componentservice = Slot(uri=TESTLINK.has_componentservice, name="has componentservice", curie=TESTLINK.curie('has_componentservice'),
                   model_uri=TESTLINK.has_componentservice, domain=NamedThing, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.has_homogeneity = Slot(uri=TESTLINK.has_homogeneity, name="has homogeneity", curie=TESTLINK.curie('has_homogeneity'),
                   model_uri=TESTLINK.has_homogeneity, domain=WorkloadEntity, range=Optional[Union[dict, "Homogeneity"]])

slots.has_control_plane = Slot(uri=TESTLINK.has_control_plane, name="has control plane", curie=TESTLINK.curie('has_control_plane'),
                   model_uri=TESTLINK.has_control_plane, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.is_controller = Slot(uri=TESTLINK.is_controller, name="is controller", curie=TESTLINK.curie('is_controller'),
                   model_uri=TESTLINK.is_controller, domain=Controller, range=Optional[Union[bool, Bool]])

slots.has_control_actor = Slot(uri=TESTLINK.has_control_actor, name="has control actor", curie=TESTLINK.curie('has_control_actor'),
                   model_uri=TESTLINK.has_control_actor, domain=NamedThing, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.has_administrative_operation = Slot(uri=TESTLINK.has_administrative_operation, name="has administrative operation", curie=TESTLINK.curie('has_administrative_operation'),
                   model_uri=TESTLINK.has_administrative_operation, domain=NamedThing, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]])

slots.has_device = Slot(uri=TESTLINK.has_device, name="has device", curie=TESTLINK.curie('has_device'),
                   model_uri=TESTLINK.has_device, domain=NamedThing, range=Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]])

slots.has_procedure = Slot(uri=TESTLINK.has_procedure, name="has procedure", curie=TESTLINK.curie('has_procedure'),
                   model_uri=TESTLINK.has_procedure, domain=NamedThing, range=Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]])

slots.has_gateway = Slot(uri=TESTLINK.has_gateway, name="has gateway", curie=TESTLINK.curie('has_gateway'),
                   model_uri=TESTLINK.has_gateway, domain=None, range=Optional[Union[str, SystemicEntityId]])

slots.has_stressor = Slot(uri=TESTLINK.has_stressor, name="has stressor", curie=TESTLINK.curie('has_stressor'),
                   model_uri=TESTLINK.has_stressor, domain=None, range=Optional[str])

slots.has_route = Slot(uri=TESTLINK.has_route, name="has route", curie=TESTLINK.curie('has_route'),
                   model_uri=TESTLINK.has_route, domain=None, range=Optional[str])

slots.has_population_context = Slot(uri=TESTLINK.has_population_context, name="has population context", curie=TESTLINK.curie('has_population_context'),
                   model_uri=TESTLINK.has_population_context, domain=Association, range=Optional[Union[str, PopulationOfIndividualSystemsId]])

slots.has_temporal_context = Slot(uri=TESTLINK.has_temporal_context, name="has temporal context", curie=TESTLINK.curie('has_temporal_context'),
                   model_uri=TESTLINK.has_temporal_context, domain=Association, range=Optional[Union[str, TimeType]])

slots.related_to = Slot(uri=TESTLINK.related_to, name="related to", curie=TESTLINK.curie('related_to'),
                   model_uri=TESTLINK.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.superclass_of = Slot(uri=TESTLINK.superclass_of, name="superclass of", curie=TESTLINK.curie('superclass_of'),
                   model_uri=TESTLINK.superclass_of, domain=OntologyClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.subclass_of = Slot(uri=RDFS.subClassOf, name="subclass of", curie=RDFS.curie('subClassOf'),
                   model_uri=TESTLINK.subclass_of, domain=OntologyClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.same_as = Slot(uri=TESTLINK.same_as, name="same as", curie=TESTLINK.curie('same_as'),
                   model_uri=TESTLINK.same_as, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.close_match = Slot(uri=TESTLINK.close_match, name="close match", curie=TESTLINK.curie('close_match'),
                   model_uri=TESTLINK.close_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.exact_match = Slot(uri=TESTLINK.exact_match, name="exact match", curie=TESTLINK.curie('exact_match'),
                   model_uri=TESTLINK.exact_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.broad_match = Slot(uri=TESTLINK.broad_match, name="broad match", curie=TESTLINK.curie('broad_match'),
                   model_uri=TESTLINK.broad_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.narrow_match = Slot(uri=TESTLINK.narrow_match, name="narrow match", curie=TESTLINK.curie('narrow_match'),
                   model_uri=TESTLINK.narrow_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributor = Slot(uri=TESTLINK.contributor, name="contributor", curie=TESTLINK.curie('contributor'),
                   model_uri=TESTLINK.contributor, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.provider = Slot(uri=TESTLINK.provider, name="provider", curie=TESTLINK.curie('provider'),
                   model_uri=TESTLINK.provider, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.publisher = Slot(uri=TESTLINK.publisher, name="publisher", curie=TESTLINK.curie('publisher'),
                   model_uri=TESTLINK.publisher, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.editor = Slot(uri=TESTLINK.editor, name="editor", curie=TESTLINK.curie('editor'),
                   model_uri=TESTLINK.editor, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.author = Slot(uri=TESTLINK.author, name="author", curie=TESTLINK.curie('author'),
                   model_uri=TESTLINK.author, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.interacts_with = Slot(uri=TESTLINK.interacts_with, name="interacts with", curie=TESTLINK.curie('interacts_with'),
                   model_uri=TESTLINK.interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.cyber_interaction_with = Slot(uri=TESTLINK.cyber_interaction_with, name="cyber interaction with", curie=TESTLINK.curie('cyber_interaction_with'),
                   model_uri=TESTLINK.cyber_interaction_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.operationally_interacts_with = Slot(uri=TESTLINK.operationally_interacts_with, name="operationally interacts with", curie=TESTLINK.curie('operationally_interacts_with'),
                   model_uri=TESTLINK.operationally_interacts_with, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.service_interacts_with = Slot(uri=TESTLINK.service_interacts_with, name="service interacts with", curie=TESTLINK.curie('service_interacts_with'),
                   model_uri=TESTLINK.service_interacts_with, domain=Componentservice, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.affects = Slot(uri=TESTLINK.affects, name="affects", curie=TESTLINK.curie('affects'),
                   model_uri=TESTLINK.affects, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affected_by = Slot(uri=TESTLINK.affected_by, name="affected by", curie=TESTLINK.curie('affected_by'),
                   model_uri=TESTLINK.affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.control_role_mixin = Slot(uri=TESTLINK.control_role_mixin, name="control role mixin", curie=TESTLINK.curie('control_role_mixin'),
                   model_uri=TESTLINK.control_role_mixin, domain=None, range=Optional[str])

slots.computational_role_mixin = Slot(uri=TESTLINK.computational_role_mixin, name="computational role mixin", curie=TESTLINK.curie('computational_role_mixin'),
                   model_uri=TESTLINK.computational_role_mixin, domain=None, range=Optional[str])

slots.affects_abundance_of = Slot(uri=TESTLINK.affects_abundance_of, name="affects abundance of", curie=TESTLINK.curie('affects_abundance_of'),
                   model_uri=TESTLINK.affects_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_abundance_of = Slot(uri=TESTLINK.increases_abundance_of, name="increases abundance of", curie=TESTLINK.curie('increases_abundance_of'),
                   model_uri=TESTLINK.increases_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_abundance_of = Slot(uri=TESTLINK.decreases_abundance_of, name="decreases abundance of", curie=TESTLINK.curie('decreases_abundance_of'),
                   model_uri=TESTLINK.decreases_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_activity_of = Slot(uri=TESTLINK.affects_activity_of, name="affects activity of", curie=TESTLINK.curie('affects_activity_of'),
                   model_uri=TESTLINK.affects_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_activity_of = Slot(uri=TESTLINK.increases_activity_of, name="increases activity of", curie=TESTLINK.curie('increases_activity_of'),
                   model_uri=TESTLINK.increases_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_activity_of = Slot(uri=TESTLINK.decreases_activity_of, name="decreases activity of", curie=TESTLINK.curie('decreases_activity_of'),
                   model_uri=TESTLINK.decreases_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_availability_of = Slot(uri=TESTLINK.affects_availability_of, name="affects availability of", curie=TESTLINK.curie('affects_availability_of'),
                   model_uri=TESTLINK.affects_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.increases_availability_of = Slot(uri=TESTLINK.increases_availability_of, name="increases availability of", curie=TESTLINK.curie('increases_availability_of'),
                   model_uri=TESTLINK.increases_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.decreases_availability_of = Slot(uri=TESTLINK.decreases_availability_of, name="decreases availability of", curie=TESTLINK.curie('decreases_availability_of'),
                   model_uri=TESTLINK.decreases_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.affects_assignment_of = Slot(uri=TESTLINK.affects_assignment_of, name="affects assignment of", curie=TESTLINK.curie('affects_assignment_of'),
                   model_uri=TESTLINK.affects_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_assignment_of = Slot(uri=TESTLINK.increases_assignment_of, name="increases assignment of", curie=TESTLINK.curie('increases_assignment_of'),
                   model_uri=TESTLINK.increases_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_assignment_of = Slot(uri=TESTLINK.decreases_assignment_of, name="decreases assignment of", curie=TESTLINK.curie('decreases_assignment_of'),
                   model_uri=TESTLINK.decreases_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_localization_of = Slot(uri=TESTLINK.affects_localization_of, name="affects localization of", curie=TESTLINK.curie('affects_localization_of'),
                   model_uri=TESTLINK.affects_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_localization_of = Slot(uri=TESTLINK.increases_localization_of, name="increases localization of", curie=TESTLINK.curie('increases_localization_of'),
                   model_uri=TESTLINK.increases_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_localization_of = Slot(uri=TESTLINK.decreases_localization_of, name="decreases localization of", curie=TESTLINK.curie('decreases_localization_of'),
                   model_uri=TESTLINK.decreases_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_supervision_of = Slot(uri=TESTLINK.affects_supervision_of, name="affects supervision of", curie=TESTLINK.curie('affects_supervision_of'),
                   model_uri=TESTLINK.affects_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_supervision_of = Slot(uri=TESTLINK.increases_supervision_of, name="increases supervision of", curie=TESTLINK.curie('increases_supervision_of'),
                   model_uri=TESTLINK.increases_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_supervision_of = Slot(uri=TESTLINK.decreases_supervision_of, name="decreases supervision of", curie=TESTLINK.curie('decreases_supervision_of'),
                   model_uri=TESTLINK.decreases_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_operational_modification_of = Slot(uri=TESTLINK.affects_operational_modification_of, name="affects operational modification of", curie=TESTLINK.curie('affects_operational_modification_of'),
                   model_uri=TESTLINK.affects_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_operational_modification_of = Slot(uri=TESTLINK.increases_operational_modification_of, name="increases operational modification of", curie=TESTLINK.curie('increases_operational_modification_of'),
                   model_uri=TESTLINK.increases_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_operational_modification_of = Slot(uri=TESTLINK.decreases_operational_modification_of, name="decreases operational modification of", curie=TESTLINK.curie('decreases_operational_modification_of'),
                   model_uri=TESTLINK.decreases_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_instantiation_of = Slot(uri=TESTLINK.affects_instantiation_of, name="affects instantiation of", curie=TESTLINK.curie('affects_instantiation_of'),
                   model_uri=TESTLINK.affects_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_instantiation_of = Slot(uri=TESTLINK.increases_instantiation_of, name="increases instantiation of", curie=TESTLINK.curie('increases_instantiation_of'),
                   model_uri=TESTLINK.increases_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_instantiation_of = Slot(uri=TESTLINK.decreases_instantiation_of, name="decreases instantiation of", curie=TESTLINK.curie('decreases_instantiation_of'),
                   model_uri=TESTLINK.decreases_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_degradation_of = Slot(uri=TESTLINK.affects_degradation_of, name="affects degradation of", curie=TESTLINK.curie('affects_degradation_of'),
                   model_uri=TESTLINK.affects_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_degradation_of = Slot(uri=TESTLINK.increases_degradation_of, name="increases degradation of", curie=TESTLINK.curie('increases_degradation_of'),
                   model_uri=TESTLINK.increases_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_degradation_of = Slot(uri=TESTLINK.decreases_degradation_of, name="decreases degradation of", curie=TESTLINK.curie('decreases_degradation_of'),
                   model_uri=TESTLINK.decreases_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_updates_rate_of = Slot(uri=TESTLINK.affects_updates_rate_of, name="affects updates rate of", curie=TESTLINK.curie('affects_updates_rate_of'),
                   model_uri=TESTLINK.affects_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.increases_updates_rate_of = Slot(uri=TESTLINK.increases_updates_rate_of, name="increases updates rate of", curie=TESTLINK.curie('increases_updates_rate_of'),
                   model_uri=TESTLINK.increases_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.decreases_updates_rate_of = Slot(uri=TESTLINK.decreases_updates_rate_of, name="decreases updates rate of", curie=TESTLINK.curie('decreases_updates_rate_of'),
                   model_uri=TESTLINK.decreases_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.affects_response_to = Slot(uri=TESTLINK.affects_response_to, name="affects response to", curie=TESTLINK.curie('affects_response_to'),
                   model_uri=TESTLINK.affects_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_response_to = Slot(uri=TESTLINK.increases_response_to, name="increases response to", curie=TESTLINK.curie('increases_response_to'),
                   model_uri=TESTLINK.increases_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_response_to = Slot(uri=TESTLINK.decreases_response_to, name="decreases response to", curie=TESTLINK.curie('decreases_response_to'),
                   model_uri=TESTLINK.decreases_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_splicing_of = Slot(uri=TESTLINK.affects_splicing_of, name="affects splicing of", curie=TESTLINK.curie('affects_splicing_of'),
                   model_uri=TESTLINK.affects_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.increases_splicing_of = Slot(uri=TESTLINK.increases_splicing_of, name="increases splicing of", curie=TESTLINK.curie('increases_splicing_of'),
                   model_uri=TESTLINK.increases_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.decreases_splicing_of = Slot(uri=TESTLINK.decreases_splicing_of, name="decreases splicing of", curie=TESTLINK.curie('decreases_splicing_of'),
                   model_uri=TESTLINK.decreases_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.affects_stability_of = Slot(uri=TESTLINK.affects_stability_of, name="affects stability of", curie=TESTLINK.curie('affects_stability_of'),
                   model_uri=TESTLINK.affects_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_stability_of = Slot(uri=TESTLINK.increases_stability_of, name="increases stability of", curie=TESTLINK.curie('increases_stability_of'),
                   model_uri=TESTLINK.increases_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_stability_of = Slot(uri=TESTLINK.decreases_stability_of, name="decreases stability of", curie=TESTLINK.curie('decreases_stability_of'),
                   model_uri=TESTLINK.decreases_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_transport_of = Slot(uri=TESTLINK.affects_transport_of, name="affects transport of", curie=TESTLINK.curie('affects_transport_of'),
                   model_uri=TESTLINK.affects_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_transport_of = Slot(uri=TESTLINK.increases_transport_of, name="increases transport of", curie=TESTLINK.curie('increases_transport_of'),
                   model_uri=TESTLINK.increases_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_transport_of = Slot(uri=TESTLINK.decreases_transport_of, name="decreases transport of", curie=TESTLINK.curie('decreases_transport_of'),
                   model_uri=TESTLINK.decreases_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_output_of = Slot(uri=TESTLINK.affects_output_of, name="affects output of", curie=TESTLINK.curie('affects_output_of'),
                   model_uri=TESTLINK.affects_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_output_of = Slot(uri=TESTLINK.increases_output_of, name="increases output of", curie=TESTLINK.curie('increases_output_of'),
                   model_uri=TESTLINK.increases_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_output_of = Slot(uri=TESTLINK.decreases_output_of, name="decreases output of", curie=TESTLINK.curie('decreases_output_of'),
                   model_uri=TESTLINK.decreases_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_uptake_of = Slot(uri=TESTLINK.affects_uptake_of, name="affects uptake of", curie=TESTLINK.curie('affects_uptake_of'),
                   model_uri=TESTLINK.affects_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_uptake_of = Slot(uri=TESTLINK.increases_uptake_of, name="increases uptake of", curie=TESTLINK.curie('increases_uptake_of'),
                   model_uri=TESTLINK.increases_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_uptake_of = Slot(uri=TESTLINK.decreases_uptake_of, name="decreases uptake of", curie=TESTLINK.curie('decreases_uptake_of'),
                   model_uri=TESTLINK.decreases_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.regulates = Slot(uri=TESTLINK.regulates, name="regulates", curie=TESTLINK.curie('regulates'),
                   model_uri=TESTLINK.regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.regulated_by = Slot(uri=TESTLINK.regulated_by, name="regulated by", curie=TESTLINK.curie('regulated_by'),
                   model_uri=TESTLINK.regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.positively_regulates = Slot(uri=TESTLINK.positively_regulates, name="positively regulates", curie=TESTLINK.curie('positively_regulates'),
                   model_uri=TESTLINK.positively_regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.positively_regulated_by = Slot(uri=TESTLINK.positively_regulated_by, name="positively regulated by", curie=TESTLINK.curie('positively_regulated_by'),
                   model_uri=TESTLINK.positively_regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.negatively_regulates = Slot(uri=TESTLINK.negatively_regulates, name="negatively regulates", curie=TESTLINK.curie('negatively_regulates'),
                   model_uri=TESTLINK.negatively_regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.negatively_regulated_by = Slot(uri=TESTLINK.negatively_regulated_by, name="negatively regulated by", curie=TESTLINK.curie('negatively_regulated_by'),
                   model_uri=TESTLINK.negatively_regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.regulates_process_to_process = Slot(uri=TESTLINK.regulates_process_to_process, name="regulates, process to process", curie=TESTLINK.curie('regulates_process_to_process'),
                   model_uri=TESTLINK.regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.regulated_by_process_to_process = Slot(uri=TESTLINK.regulated_by_process_to_process, name="regulated by, process to process", curie=TESTLINK.curie('regulated_by_process_to_process'),
                   model_uri=TESTLINK.regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.positively_regulates_process_to_process = Slot(uri=TESTLINK.positively_regulates_process_to_process, name="positively regulates, process to process", curie=TESTLINK.curie('positively_regulates_process_to_process'),
                   model_uri=TESTLINK.positively_regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.positively_regulated_by_process_to_process = Slot(uri=TESTLINK.positively_regulated_by_process_to_process, name="positively regulated by, process to process", curie=TESTLINK.curie('positively_regulated_by_process_to_process'),
                   model_uri=TESTLINK.positively_regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.negatively_regulates_process_to_process = Slot(uri=TESTLINK.negatively_regulates_process_to_process, name="negatively regulates, process to process", curie=TESTLINK.curie('negatively_regulates_process_to_process'),
                   model_uri=TESTLINK.negatively_regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.negatively_regulated_by_process_to_process = Slot(uri=TESTLINK.negatively_regulated_by_process_to_process, name="negatively regulated by, process to process", curie=TESTLINK.curie('negatively_regulated_by_process_to_process'),
                   model_uri=TESTLINK.negatively_regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.regulates_entity_to_entity = Slot(uri=TESTLINK.regulates_entity_to_entity, name="regulates, entity to entity", curie=TESTLINK.curie('regulates_entity_to_entity'),
                   model_uri=TESTLINK.regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.regulated_by_entity_to_entity = Slot(uri=TESTLINK.regulated_by_entity_to_entity, name="regulated by, entity to entity", curie=TESTLINK.curie('regulated_by_entity_to_entity'),
                   model_uri=TESTLINK.regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.positively_regulates_entity_to_entity = Slot(uri=TESTLINK.positively_regulates_entity_to_entity, name="positively regulates, entity to entity", curie=TESTLINK.curie('positively_regulates_entity_to_entity'),
                   model_uri=TESTLINK.positively_regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.positively_regulated_by_entity_to_entity = Slot(uri=TESTLINK.positively_regulated_by_entity_to_entity, name="positively regulated by, entity to entity", curie=TESTLINK.curie('positively_regulated_by_entity_to_entity'),
                   model_uri=TESTLINK.positively_regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.negatively_regulates_entity_to_entity = Slot(uri=TESTLINK.negatively_regulates_entity_to_entity, name="negatively regulates, entity to entity", curie=TESTLINK.curie('negatively_regulates_entity_to_entity'),
                   model_uri=TESTLINK.negatively_regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.negatively_regulated_by_entity_to_entity = Slot(uri=TESTLINK.negatively_regulated_by_entity_to_entity, name="negatively regulated by, entity to entity", curie=TESTLINK.curie('negatively_regulated_by_entity_to_entity'),
                   model_uri=TESTLINK.negatively_regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.disrupts = Slot(uri=TESTLINK.disrupts, name="disrupts", curie=TESTLINK.curie('disrupts'),
                   model_uri=TESTLINK.disrupts, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.disrupted_by = Slot(uri=TESTLINK.disrupted_by, name="disrupted by", curie=TESTLINK.curie('disrupted_by'),
                   model_uri=TESTLINK.disrupted_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_servicetype = Slot(uri=TESTLINK.has_servicetype, name="has servicetype", curie=TESTLINK.curie('has_servicetype'),
                   model_uri=TESTLINK.has_servicetype, domain=Componentservice, range=Optional[Union[Union[dict, "ServicetypeMixin"], List[Union[dict, "ServicetypeMixin"]]]])

slots.homologous_to = Slot(uri=TESTLINK.homologous_to, name="homologous to", curie=TESTLINK.curie('homologous_to'),
                   model_uri=TESTLINK.homologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.paralogous_to = Slot(uri=TESTLINK.paralogous_to, name="paralogous to", curie=TESTLINK.curie('paralogous_to'),
                   model_uri=TESTLINK.paralogous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.orthologous_to = Slot(uri=TESTLINK.orthologous_to, name="orthologous to", curie=TESTLINK.curie('orthologous_to'),
                   model_uri=TESTLINK.orthologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.xenologous_to = Slot(uri=TESTLINK.xenologous_to, name="xenologous to", curie=TESTLINK.curie('xenologous_to'),
                   model_uri=TESTLINK.xenologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coexists_with = Slot(uri=TESTLINK.coexists_with, name="coexists with", curie=TESTLINK.curie('coexists_with'),
                   model_uri=TESTLINK.coexists_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_pathway_with = Slot(uri=TESTLINK.in_pathway_with, name="in pathway with", curie=TESTLINK.curie('in_pathway_with'),
                   model_uri=TESTLINK.in_pathway_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.in_complex_with = Slot(uri=TESTLINK.in_complex_with, name="in complex with", curie=TESTLINK.curie('in_complex_with'),
                   model_uri=TESTLINK.in_complex_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.in_serviceunit_population_with = Slot(uri=TESTLINK.in_serviceunit_population_with, name="in serviceunit population with", curie=TESTLINK.curie('in_serviceunit_population_with'),
                   model_uri=TESTLINK.in_serviceunit_population_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.colocalizes_with = Slot(uri=TESTLINK.colocalizes_with, name="colocalizes with", curie=TESTLINK.curie('colocalizes_with'),
                   model_uri=TESTLINK.colocalizes_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.service_association = Slot(uri=TESTLINK.service_association, name="service association", curie=TESTLINK.curie('service_association'),
                   model_uri=TESTLINK.service_association, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.componentservice_associated_with_condition = Slot(uri=TESTLINK.componentservice_associated_with_condition, name="componentservice associated with condition", curie=TESTLINK.curie('componentservice_associated_with_condition'),
                   model_uri=TESTLINK.componentservice_associated_with_condition, domain=Componentservice, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.condition_associated_with_componentservice = Slot(uri=TESTLINK.condition_associated_with_componentservice, name="condition associated with componentservice", curie=TESTLINK.curie('condition_associated_with_componentservice'),
                   model_uri=TESTLINK.condition_associated_with_componentservice, domain=ErrorOrObservableFeature, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.affects_risk_for = Slot(uri=TESTLINK.affects_risk_for, name="affects risk for", curie=TESTLINK.curie('affects_risk_for'),
                   model_uri=TESTLINK.affects_risk_for, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.predisposes = Slot(uri=TESTLINK.predisposes, name="predisposes", curie=TESTLINK.curie('predisposes'),
                   model_uri=TESTLINK.predisposes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributes_to = Slot(uri=TESTLINK.contributes_to, name="contributes to", curie=TESTLINK.curie('contributes_to'),
                   model_uri=TESTLINK.contributes_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.causes = Slot(uri=TESTLINK.causes, name="causes", curie=TESTLINK.curie('causes'),
                   model_uri=TESTLINK.causes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.caused_by = Slot(uri=TESTLINK.caused_by, name="caused by", curie=TESTLINK.curie('caused_by'),
                   model_uri=TESTLINK.caused_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.ameliorates = Slot(uri=TESTLINK.ameliorates, name="ameliorates", curie=TESTLINK.curie('ameliorates'),
                   model_uri=TESTLINK.ameliorates, domain=ComputationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.exacerbates = Slot(uri=TESTLINK.exacerbates, name="exacerbates", curie=TESTLINK.curie('exacerbates'),
                   model_uri=TESTLINK.exacerbates, domain=ComputationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.repairs = Slot(uri=TESTLINK.repairs, name="repairs", curie=TESTLINK.curie('repairs'),
                   model_uri=TESTLINK.repairs, domain=Repairing, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.repaired_by = Slot(uri=TESTLINK.repaired_by, name="repaired by", curie=TESTLINK.curie('repaired_by'),
                   model_uri=TESTLINK.repaired_by, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, RepairingId], List[Union[str, RepairingId]]]])

slots.approved_to_repair = Slot(uri=TESTLINK.approved_to_repair, name="approved to repair", curie=TESTLINK.curie('approved_to_repair'),
                   model_uri=TESTLINK.approved_to_repair, domain=Repairing, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.approved_for_repairing_by = Slot(uri=TESTLINK.approved_for_repairing_by, name="approved for repairing by", curie=TESTLINK.curie('approved_for_repairing_by'),
                   model_uri=TESTLINK.approved_for_repairing_by, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, RepairingId], List[Union[str, RepairingId]]]])

slots.prevents = Slot(uri=TESTLINK.prevents, name="prevents", curie=TESTLINK.curie('prevents'),
                   model_uri=TESTLINK.prevents, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.prevented_by = Slot(uri=TESTLINK.prevented_by, name="prevented by", curie=TESTLINK.curie('prevented_by'),
                   model_uri=TESTLINK.prevented_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.correlated_with = Slot(uri=TESTLINK.correlated_with, name="correlated with", curie=TESTLINK.curie('correlated_with'),
                   model_uri=TESTLINK.correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.positively_correlated_with = Slot(uri=TESTLINK.positively_correlated_with, name="positively correlated with", curie=TESTLINK.curie('positively_correlated_with'),
                   model_uri=TESTLINK.positively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.negatively_correlated_with = Slot(uri=TESTLINK.negatively_correlated_with, name="negatively correlated with", curie=TESTLINK.curie('negatively_correlated_with'),
                   model_uri=TESTLINK.negatively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coavailable_with = Slot(uri=TESTLINK.coavailable_with, name="coavailable with", curie=TESTLINK.curie('coavailable_with'),
                   model_uri=TESTLINK.coavailable_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.has_marker = Slot(uri=TESTLINK.has_marker, name="has marker", curie=TESTLINK.curie('has_marker'),
                   model_uri=TESTLINK.has_marker, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.marker_for = Slot(uri=TESTLINK.marker_for, name="marker for", curie=TESTLINK.curie('marker_for'),
                   model_uri=TESTLINK.marker_for, domain=OperationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.available_in = Slot(uri=TESTLINK.available_in, name="available in", curie=TESTLINK.curie('available_in'),
                   model_uri=TESTLINK.available_in, domain=None, range=Optional[Union[Union[str, DeploymentEntityId], List[Union[str, DeploymentEntityId]]]])

slots.unavailable_in = Slot(uri=TESTLINK.unavailable_in, name="unavailable in", curie=TESTLINK.curie('unavailable_in'),
                   model_uri=TESTLINK.unavailable_in, domain=DeploymentEntity, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.has_observability = Slot(uri=TESTLINK.has_observability, name="has observability", curie=TESTLINK.curie('has_observability'),
                   model_uri=TESTLINK.has_observability, domain=ComputationalEntity, range=Optional[Union[Union[str, ObservableFeatureId], List[Union[str, ObservableFeatureId]]]])

slots.occurs_in = Slot(uri=TESTLINK.occurs_in, name="occurs in", curie=TESTLINK.curie('occurs_in'),
                   model_uri=TESTLINK.occurs_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.located_in = Slot(uri=TESTLINK.located_in, name="located in", curie=TESTLINK.curie('located_in'),
                   model_uri=TESTLINK.located_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.location_of = Slot(uri=TESTLINK.location_of, name="location of", curie=TESTLINK.curie('location_of'),
                   model_uri=TESTLINK.location_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.similar_to = Slot(uri=TESTLINK.similar_to, name="similar to", curie=TESTLINK.curie('similar_to'),
                   model_uri=TESTLINK.similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.orchestrationly_similar_to = Slot(uri=TESTLINK.orchestrationly_similar_to, name="orchestrationly similar to", curie=TESTLINK.curie('orchestrationly_similar_to'),
                   model_uri=TESTLINK.orchestrationly_similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_sequence_location = Slot(uri=TESTLINK.has_sequence_location, name="has sequence location", curie=TESTLINK.curie('has_sequence_location'),
                   model_uri=TESTLINK.has_sequence_location, domain=WorkloadEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.model_of = Slot(uri=TESTLINK.model_of, name="model of", curie=TESTLINK.curie('model_of'),
                   model_uri=TESTLINK.model_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

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

slots.actively_involved_in = Slot(uri=TESTLINK.actively_involved_in, name="actively involved in", curie=TESTLINK.curie('actively_involved_in'),
                   model_uri=TESTLINK.actively_involved_in, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.capable_of = Slot(uri=TESTLINK.capable_of, name="capable of", curie=TESTLINK.curie('capable_of'),
                   model_uri=TESTLINK.capable_of, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.enables = Slot(uri=TESTLINK.enables, name="enables", curie=TESTLINK.curie('enables'),
                   model_uri=TESTLINK.enables, domain=CyberEntity, range=Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]])

slots.enabled_by = Slot(uri=TESTLINK.enabled_by, name="enabled by", curie=TESTLINK.curie('enabled_by'),
                   model_uri=TESTLINK.enabled_by, domain=ComputationalProcessOrActivity, range=Optional[Union[Union[str, CyberEntityId], List[Union[str, CyberEntityId]]]])

slots.derives_into = Slot(uri=TESTLINK.derives_into, name="derives into", curie=TESTLINK.curie('derives_into'),
                   model_uri=TESTLINK.derives_into, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.derives_from = Slot(uri=TESTLINK.derives_from, name="derives from", curie=TESTLINK.curie('derives_from'),
                   model_uri=TESTLINK.derives_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_controller_of = Slot(uri=TESTLINK.is_controller_of, name="is controller of", curie=TESTLINK.curie('is_controller_of'),
                   model_uri=TESTLINK.is_controller_of, domain=ControlActor, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.has_controller = Slot(uri=TESTLINK.has_controller, name="has controller", curie=TESTLINK.curie('has_controller'),
                   model_uri=TESTLINK.has_controller, domain=ControlActor, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.notification_component_of = Slot(uri=TESTLINK.notification_component_of, name="notification component of", curie=TESTLINK.curie('notification_component_of'),
                   model_uri=TESTLINK.notification_component_of, domain=NotificationComponent, range=Optional[Union[Union[str, NotificationId], List[Union[str, NotificationId]]]])

slots.has_notification_component = Slot(uri=TESTLINK.has_notification_component, name="has notification component", curie=TESTLINK.curie('has_notification_component'),
                   model_uri=TESTLINK.has_notification_component, domain=Notification, range=Optional[Union[Union[str, NotificationComponentId], List[Union[str, NotificationComponentId]]]])

slots.data_of = Slot(uri=TESTLINK.data_of, name="data of", curie=TESTLINK.curie('data_of'),
                   model_uri=TESTLINK.data_of, domain=NotificationComponent, range=Optional[Union[Union[str, NotificationId], List[Union[str, NotificationId]]]])

slots.has_data = Slot(uri=TESTLINK.has_data, name="has data", curie=TESTLINK.curie('has_data'),
                   model_uri=TESTLINK.has_data, domain=Notification, range=Optional[Union[Union[str, DataId], List[Union[str, DataId]]]])

slots.is_active_ingredient_of = Slot(uri=TESTLINK.is_active_ingredient_of, name="is active ingredient of", curie=TESTLINK.curie('is_active_ingredient_of'),
                   model_uri=TESTLINK.is_active_ingredient_of, domain=ControlActor, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]], mappings = [RO["0002249"]])

slots.has_active_ingredient = Slot(uri=TESTLINK.has_active_ingredient, name="has active ingredient", curie=TESTLINK.curie('has_active_ingredient'),
                   model_uri=TESTLINK.has_active_ingredient, domain=AdministrativeOperation, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]], mappings = [RO["0002248"]])

slots.is_excipient_of = Slot(uri=TESTLINK.is_excipient_of, name="is excipient of", curie=TESTLINK.curie('is_excipient_of'),
                   model_uri=TESTLINK.is_excipient_of, domain=ControlActor, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]], mappings = [WIKIDATA.Q902638])

slots.has_excipient = Slot(uri=TESTLINK.has_excipient, name="has excipient", curie=TESTLINK.curie('has_excipient'),
                   model_uri=TESTLINK.has_excipient, domain=AdministrativeOperation, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]], mappings = [WIKIDATA.Q902638])

slots.manifestation_of = Slot(uri=TESTLINK.manifestation_of, name="manifestation of", curie=TESTLINK.curie('manifestation_of'),
                   model_uri=TESTLINK.manifestation_of, domain=NamedThing, range=Optional[Union[Union[str, ErrorId], List[Union[str, ErrorId]]]])

slots.produces = Slot(uri=TESTLINK.produces, name="produces", curie=TESTLINK.curie('produces'),
                   model_uri=TESTLINK.produces, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.produced_by = Slot(uri=TESTLINK.produced_by, name="produced by", curie=TESTLINK.curie('produced_by'),
                   model_uri=TESTLINK.produced_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.temporally_related_to = Slot(uri=TESTLINK.temporally_related_to, name="temporally related to", curie=TESTLINK.curie('temporally_related_to'),
                   model_uri=TESTLINK.temporally_related_to, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.precedes = Slot(uri=TESTLINK.precedes, name="precedes", curie=TESTLINK.curie('precedes'),
                   model_uri=TESTLINK.precedes, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.preceded_by = Slot(uri=TESTLINK.preceded_by, name="preceded by", curie=TESTLINK.curie('preceded_by'),
                   model_uri=TESTLINK.preceded_by, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.directly_interacts_with = Slot(uri=TESTLINK.directly_interacts_with, name="directly interacts with", curie=TESTLINK.curie('directly_interacts_with'),
                   model_uri=TESTLINK.directly_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affects_availability_in = Slot(uri=TESTLINK.affects_availability_in, name="affects availability in", curie=TESTLINK.curie('affects_availability_in'),
                   model_uri=TESTLINK.affects_availability_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_variant_part = Slot(uri=TESTLINK.has_variant_part, name="has variant part", curie=TESTLINK.curie('has_variant_part'),
                   model_uri=TESTLINK.has_variant_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_condition = Slot(uri=TESTLINK.related_condition, name="related condition", curie=TESTLINK.curie('related_condition'),
                   model_uri=TESTLINK.related_condition, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_sequence_variant_of = Slot(uri=TESTLINK.is_sequence_variant_of, name="is sequence variant of", curie=TESTLINK.curie('is_sequence_variant_of'),
                   model_uri=TESTLINK.is_sequence_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.is_missense_variant_of = Slot(uri=TESTLINK.is_missense_variant_of, name="is missense variant of", curie=TESTLINK.curie('is_missense_variant_of'),
                   model_uri=TESTLINK.is_missense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_synonymous_variant_of = Slot(uri=TESTLINK.is_synonymous_variant_of, name="is synonymous variant of", curie=TESTLINK.curie('is_synonymous_variant_of'),
                   model_uri=TESTLINK.is_synonymous_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_nonsense_variant_of = Slot(uri=TESTLINK.is_nonsense_variant_of, name="is nonsense variant of", curie=TESTLINK.curie('is_nonsense_variant_of'),
                   model_uri=TESTLINK.is_nonsense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_protocol_variant_of = Slot(uri=TESTLINK.is_protocol_variant_of, name="is protocol variant of", curie=TESTLINK.curie('is_protocol_variant_of'),
                   model_uri=TESTLINK.is_protocol_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_splice_site_variant_of = Slot(uri=TESTLINK.is_splice_site_variant_of, name="is splice site variant of", curie=TESTLINK.curie('is_splice_site_variant_of'),
                   model_uri=TESTLINK.is_splice_site_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_nearby_variant_of = Slot(uri=TESTLINK.is_nearby_variant_of, name="is nearby variant of", curie=TESTLINK.curie('is_nearby_variant_of'),
                   model_uri=TESTLINK.is_nearby_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_non_coding_variant_of = Slot(uri=TESTLINK.is_non_coding_variant_of, name="is non coding variant of", curie=TESTLINK.curie('is_non_coding_variant_of'),
                   model_uri=TESTLINK.is_non_coding_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.error_has_basis_in = Slot(uri=TESTLINK.error_has_basis_in, name="error has basis in", curie=TESTLINK.curie('error_has_basis_in'),
                   model_uri=TESTLINK.error_has_basis_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.causes_adverse_event = Slot(uri=TESTLINK.causes_adverse_event, name="causes adverse event", curie=TESTLINK.curie('causes_adverse_event'),
                   model_uri=TESTLINK.causes_adverse_event, domain=AdministrativeOperation, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.contraindicated_for = Slot(uri=TESTLINK.contraindicated_for, name="contraindicated for", curie=TESTLINK.curie('contraindicated_for'),
                   model_uri=TESTLINK.contraindicated_for, domain=AdministrativeOperation, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.has_not_completed = Slot(uri=TESTLINK.has_not_completed, name="has not completed", curie=TESTLINK.curie('has_not_completed'),
                   model_uri=TESTLINK.has_not_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_completed = Slot(uri=TESTLINK.has_completed, name="has completed", curie=TESTLINK.curie('has_completed'),
                   model_uri=TESTLINK.has_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.decreases_operational_interaction = Slot(uri=TESTLINK.decreases_operational_interaction, name="decreases operational interaction", curie=TESTLINK.curie('decreases_operational_interaction'),
                   model_uri=TESTLINK.decreases_operational_interaction, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_operational_interaction = Slot(uri=TESTLINK.increases_operational_interaction, name="increases operational interaction", curie=TESTLINK.curie('increases_operational_interaction'),
                   model_uri=TESTLINK.increases_operational_interaction, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.in_linkage_disequilibrium_with = Slot(uri=TESTLINK.in_linkage_disequilibrium_with, name="in linkage disequilibrium with", curie=TESTLINK.curie('in_linkage_disequilibrium_with'),
                   model_uri=TESTLINK.in_linkage_disequilibrium_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_increased_amount = Slot(uri=TESTLINK.has_increased_amount, name="has increased amount", curie=TESTLINK.curie('has_increased_amount'),
                   model_uri=TESTLINK.has_increased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_decreased_amount = Slot(uri=TESTLINK.has_decreased_amount, name="has decreased amount", curie=TESTLINK.curie('has_decreased_amount'),
                   model_uri=TESTLINK.has_decreased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.lacks_part = Slot(uri=TESTLINK.lacks_part, name="lacks part", curie=TESTLINK.curie('lacks_part'),
                   model_uri=TESTLINK.lacks_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.develops_from = Slot(uri=TESTLINK.develops_from, name="develops from", curie=TESTLINK.curie('develops_from'),
                   model_uri=TESTLINK.develops_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_taxon = Slot(uri=TESTLINK.in_taxon, name="in taxon", curie=TESTLINK.curie('in_taxon'),
                   model_uri=TESTLINK.in_taxon, domain=None, range=Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]])

slots.has_operational_consequence = Slot(uri=TESTLINK.has_operational_consequence, name="has operational consequence", curie=TESTLINK.curie('has_operational_consequence'),
                   model_uri=TESTLINK.has_operational_consequence, domain=NamedThing, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

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

slots.edge_label = Slot(uri=RDF.predicate, name="edge label", curie=RDF.curie('predicate'),
                   model_uri=TESTLINK.edge_label, domain=Association, range=Union[str, PredicateType])

slots.relation = Slot(uri=TESTLINK.relation, name="relation", curie=TESTLINK.curie('relation'),
                   model_uri=TESTLINK.relation, domain=Association, range=Union[str, URIorCURIE])

slots.negated = Slot(uri=TESTLINK.negated, name="negated", curie=TESTLINK.curie('negated'),
                   model_uri=TESTLINK.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.has_confidence_level = Slot(uri=TESTLINK.has_confidence_level, name="has confidence level", curie=TESTLINK.curie('has_confidence_level'),
                   model_uri=TESTLINK.has_confidence_level, domain=Association, range=Optional[Union[str, ConfidenceLevelId]])

slots.has_evidence = Slot(uri=TESTLINK.has_evidence, name="has evidence", curie=TESTLINK.curie('has_evidence'),
                   model_uri=TESTLINK.has_evidence, domain=Association, range=Optional[Union[str, EvidenceTypeId]])

slots.provided_by = Slot(uri=TESTLINK.provided_by, name="provided by", curie=TESTLINK.curie('provided_by'),
                   model_uri=TESTLINK.provided_by, domain=Association, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.association_type = Slot(uri=TESTLINK.association_type, name="association type", curie=TESTLINK.curie('association_type'),
                   model_uri=TESTLINK.association_type, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.chi_squared_statistic = Slot(uri=TESTLINK.chi_squared_statistic, name="chi squared statistic", curie=TESTLINK.curie('chi_squared_statistic'),
                   model_uri=TESTLINK.chi_squared_statistic, domain=Association, range=Optional[float])

slots.p_value = Slot(uri=TESTLINK.p_value, name="p value", curie=TESTLINK.curie('p_value'),
                   model_uri=TESTLINK.p_value, domain=Association, range=Optional[float])

slots.interacting_tasks_category = Slot(uri=TESTLINK.interacting_tasks_category, name="interacting tasks category", curie=TESTLINK.curie('interacting_tasks_category'),
                   model_uri=TESTLINK.interacting_tasks_category, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.quantifier_qualifier = Slot(uri=TESTLINK.quantifier_qualifier, name="quantifier qualifier", curie=TESTLINK.curie('quantifier_qualifier'),
                   model_uri=TESTLINK.quantifier_qualifier, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.catalyst_qualifier = Slot(uri=TESTLINK.catalyst_qualifier, name="catalyst qualifier", curie=TESTLINK.curie('catalyst_qualifier'),
                   model_uri=TESTLINK.catalyst_qualifier, domain=Association, range=Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]])

slots.availability_site = Slot(uri=TESTLINK.availability_site, name="availability site", curie=TESTLINK.curie('availability_site'),
                   model_uri=TESTLINK.availability_site, domain=Association, range=Optional[Union[str, DeploymentEntityId]])

slots.stage_qualifier = Slot(uri=TESTLINK.stage_qualifier, name="stage qualifier", curie=TESTLINK.curie('stage_qualifier'),
                   model_uri=TESTLINK.stage_qualifier, domain=Association, range=Optional[Union[str, LifecycleStageId]])

slots.observable_state = Slot(uri=TESTLINK.observable_state, name="observable state", curie=TESTLINK.curie('observable_state'),
                   model_uri=TESTLINK.observable_state, domain=Association, range=Optional[Union[str, ErrorOrObservableFeatureId]])

slots.qualifiers = Slot(uri=TESTLINK.qualifiers, name="qualifiers", curie=TESTLINK.curie('qualifiers'),
                   model_uri=TESTLINK.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.frequency_qualifier = Slot(uri=TESTLINK.frequency_qualifier, name="frequency qualifier", curie=TESTLINK.curie('frequency_qualifier'),
                   model_uri=TESTLINK.frequency_qualifier, domain=Association, range=Optional[Union[dict, FrequencyValue]])

slots.severity_qualifier = Slot(uri=TESTLINK.severity_qualifier, name="severity qualifier", curie=TESTLINK.curie('severity_qualifier'),
                   model_uri=TESTLINK.severity_qualifier, domain=Association, range=Optional[Union[dict, SeverityValue]])

slots.architectural_style_qualifier = Slot(uri=TESTLINK.architectural_style_qualifier, name="architectural style qualifier", curie=TESTLINK.curie('architectural_style_qualifier'),
                   model_uri=TESTLINK.architectural_style_qualifier, domain=Association, range=Optional[Union[dict, ComputationalArchitecturalStyle]])

slots.onset_qualifier = Slot(uri=TESTLINK.onset_qualifier, name="onset qualifier", curie=TESTLINK.curie('onset_qualifier'),
                   model_uri=TESTLINK.onset_qualifier, domain=Association, range=Optional[Union[dict, Onset]])

slots.empirical_modifier_qualifier = Slot(uri=TESTLINK.empirical_modifier_qualifier, name="empirical modifier qualifier", curie=TESTLINK.curie('empirical_modifier_qualifier'),
                   model_uri=TESTLINK.empirical_modifier_qualifier, domain=Association, range=Optional[Union[dict, EmpiricalModifier]])

slots.sequence_variant_qualifier = Slot(uri=TESTLINK.sequence_variant_qualifier, name="sequence variant qualifier", curie=TESTLINK.curie('sequence_variant_qualifier'),
                   model_uri=TESTLINK.sequence_variant_qualifier, domain=Association, range=Optional[Union[str, SequenceVariantId]])

slots.publications = Slot(uri=TESTLINK.publications, name="publications", curie=TESTLINK.curie('publications'),
                   model_uri=TESTLINK.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.sequence_localization_attribute = Slot(uri=TESTLINK.sequence_localization_attribute, name="sequence localization attribute", curie=TESTLINK.curie('sequence_localization_attribute'),
                   model_uri=TESTLINK.sequence_localization_attribute, domain=ServiceSequenceLocalization, range=Optional[str])

slots.interbase_coordinate = Slot(uri=TESTLINK.interbase_coordinate, name="interbase coordinate", curie=TESTLINK.curie('interbase_coordinate'),
                   model_uri=TESTLINK.interbase_coordinate, domain=ServiceSequenceLocalization, range=Optional[int])

slots.start_interbase_coordinate = Slot(uri=TESTLINK.start_interbase_coordinate, name="start interbase coordinate", curie=TESTLINK.curie('start_interbase_coordinate'),
                   model_uri=TESTLINK.start_interbase_coordinate, domain=ServiceSequenceLocalization, range=Optional[int])

slots.end_interbase_coordinate = Slot(uri=TESTLINK.end_interbase_coordinate, name="end interbase coordinate", curie=TESTLINK.curie('end_interbase_coordinate'),
                   model_uri=TESTLINK.end_interbase_coordinate, domain=ServiceSequenceLocalization, range=Optional[int])

slots.workload_build = Slot(uri=TESTLINK.workload_build, name="workload build", curie=TESTLINK.curie('workload_build'),
                   model_uri=TESTLINK.workload_build, domain=ServiceSequenceLocalization, range=Optional[str])

slots.strand = Slot(uri=TESTLINK.strand, name="strand", curie=TESTLINK.curie('strand'),
                   model_uri=TESTLINK.strand, domain=ServiceSequenceLocalization, range=Optional[str])

slots.phase = Slot(uri=TESTLINK.phase, name="phase", curie=TESTLINK.curie('phase'),
                   model_uri=TESTLINK.phase, domain=CodingSequence, range=Optional[str])

slots.has_taxonomic_rank = Slot(uri=TESTLINK.has_taxonomic_rank, name="has taxonomic rank", curie=TESTLINK.curie('has_taxonomic_rank'),
                   model_uri=TESTLINK.has_taxonomic_rank, domain=None, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.attribute_name = Slot(uri=TESTLINK.name, name="attribute_name", curie=TESTLINK.curie('name'),
                   model_uri=TESTLINK.attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.named_thing_category = Slot(uri=TESTLINK.category, name="named thing_category", curie=TESTLINK.curie('category'),
                   model_uri=TESTLINK.named_thing_category, domain=NamedThing, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.system_taxon_has_taxonomic_rank = Slot(uri=TESTLINK.has_taxonomic_rank, name="system taxon_has taxonomic rank", curie=TESTLINK.curie('has_taxonomic_rank'),
                   model_uri=TESTLINK.system_taxon_has_taxonomic_rank, domain=SystemTaxon, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.system_taxon_subclass_of = Slot(uri=TESTLINK.subclass_of, name="system taxon_subclass of", curie=TESTLINK.curie('subclass_of'),
                   model_uri=TESTLINK.system_taxon_subclass_of, domain=SystemTaxon, range=Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]])

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

slots.book_id = Slot(uri=TESTLINK.id, name="book_id", curie=TESTLINK.curie('id'),
                   model_uri=TESTLINK.book_id, domain=Book, range=Union[str, BookId])

slots.book_type = Slot(uri=TESTLINK.type, name="book_type", curie=TESTLINK.curie('type'),
                   model_uri=TESTLINK.book_type, domain=Book, range=str)

slots.book_chapter_published_in = Slot(uri=TESTLINK.published_in, name="book chapter_published in", curie=TESTLINK.curie('published_in'),
                   model_uri=TESTLINK.book_chapter_published_in, domain=BookChapter, range=Union[str, URIorCURIE])

slots.serial_id = Slot(uri=TESTLINK.id, name="serial_id", curie=TESTLINK.curie('id'),
                   model_uri=TESTLINK.serial_id, domain=Serial, range=Union[str, SerialId])

slots.serial_type = Slot(uri=TESTLINK.type, name="serial_type", curie=TESTLINK.curie('type'),
                   model_uri=TESTLINK.serial_type, domain=Serial, range=str)

slots.article_published_in = Slot(uri=TESTLINK.published_in, name="article_published in", curie=TESTLINK.curie('published_in'),
                   model_uri=TESTLINK.article_published_in, domain=Article, range=Union[str, URIorCURIE])

slots.article_iso_abbreviation = Slot(uri=TESTLINK.iso_abbreviation, name="article_iso abbreviation", curie=TESTLINK.curie('iso_abbreviation'),
                   model_uri=TESTLINK.article_iso_abbreviation, domain=Article, range=Optional[str])

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

slots.sequence_variant_has_componentservice = Slot(uri=TESTLINK.has_componentservice, name="sequence variant_has componentservice", curie=TESTLINK.curie('has_componentservice'),
                   model_uri=TESTLINK.sequence_variant_has_componentservice, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.sequence_variant_has_computational_sequence = Slot(uri=TESTLINK.has_computational_sequence, name="sequence variant_has computational sequence", curie=TESTLINK.curie('has_computational_sequence'),
                   model_uri=TESTLINK.sequence_variant_has_computational_sequence, domain=SequenceVariant, range=Optional[Union[str, ComputationalSequence]])

slots.sequence_variant_id = Slot(uri=TESTLINK.id, name="sequence variant_id", curie=TESTLINK.curie('id'),
                   model_uri=TESTLINK.sequence_variant_id, domain=SequenceVariant, range=Union[str, SequenceVariantId])

slots.empirical_measurement_has_attribute_type = Slot(uri=TESTLINK.has_attribute_type, name="empirical measurement_has attribute type", curie=TESTLINK.curie('has_attribute_type'),
                   model_uri=TESTLINK.empirical_measurement_has_attribute_type, domain=EmpiricalMeasurement, range=Union[str, OntologyClassId])

slots.empirical_finding_has_attribute = Slot(uri=TESTLINK.has_attribute, name="empirical finding_has attribute", curie=TESTLINK.curie('has_attribute'),
                   model_uri=TESTLINK.empirical_finding_has_attribute, domain=EmpiricalFinding, range=Optional[Union[Union[dict, EmpiricalAttribute], List[Union[dict, EmpiricalAttribute]]]])

slots.socioeconomic_exposure_has_attribute = Slot(uri=TESTLINK.has_attribute, name="socioeconomic exposure_has attribute", curie=TESTLINK.curie('has_attribute'),
                   model_uri=TESTLINK.socioeconomic_exposure_has_attribute, domain=SocioeconomicExposure, range=Union[Union[dict, SocioeconomicAttribute], List[Union[dict, SocioeconomicAttribute]]])

slots.association_type = Slot(uri=TESTLINK.type, name="association_type", curie=TESTLINK.curie('type'),
                   model_uri=TESTLINK.association_type, domain=Association, range=Optional[str])

slots.association_category = Slot(uri=TESTLINK.category, name="association_category", curie=TESTLINK.curie('category'),
                   model_uri=TESTLINK.association_category, domain=Association, range=Union[Union[str, AssociationId], List[Union[str, AssociationId]]])

slots.contributor_association_subject = Slot(uri=TESTLINK.subject, name="contributor association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.contributor_association_subject, domain=ContributorAssociation, range=Union[str, InformationContentEntityId])

slots.contributor_association_predicate = Slot(uri=TESTLINK.predicate, name="contributor association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.contributor_association_predicate, domain=ContributorAssociation, range=Union[str, PredicateType])

slots.contributor_association_object = Slot(uri=TESTLINK.object, name="contributor association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.contributor_association_object, domain=ContributorAssociation, range=Union[str, AgentId])

slots.contributor_association_qualifiers = Slot(uri=TESTLINK.qualifiers, name="contributor association_qualifiers", curie=TESTLINK.curie('qualifiers'),
                   model_uri=TESTLINK.contributor_association_qualifiers, domain=ContributorAssociation, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.serviceunittype_to_serviceunittype_part_association_predicate = Slot(uri=TESTLINK.predicate, name="serviceunittype to serviceunittype part association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.serviceunittype_to_serviceunittype_part_association_predicate, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_serviceunittype_part_association_subject = Slot(uri=TESTLINK.subject, name="serviceunittype to serviceunittype part association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.serviceunittype_to_serviceunittype_part_association_subject, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_serviceunittype_part_association_object = Slot(uri=TESTLINK.object, name="serviceunittype to serviceunittype part association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.serviceunittype_to_serviceunittype_part_association_object, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_componentservice_association_predicate = Slot(uri=TESTLINK.predicate, name="serviceunittype to componentservice association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.serviceunittype_to_componentservice_association_predicate, domain=ServiceunittypeToComponentserviceAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_componentservice_association_subject = Slot(uri=TESTLINK.subject, name="serviceunittype to componentservice association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.serviceunittype_to_componentservice_association_subject, domain=ServiceunittypeToComponentserviceAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_componentservice_association_object = Slot(uri=TESTLINK.object, name="serviceunittype to componentservice association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.serviceunittype_to_componentservice_association_object, domain=ServiceunittypeToComponentserviceAssociation, range=Union[dict, Componentservice])

slots.serviceunittype_to_variant_association_predicate = Slot(uri=TESTLINK.predicate, name="serviceunittype to variant association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.serviceunittype_to_variant_association_predicate, domain=ServiceunittypeToVariantAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_variant_association_subject = Slot(uri=TESTLINK.subject, name="serviceunittype to variant association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.serviceunittype_to_variant_association_subject, domain=ServiceunittypeToVariantAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_variant_association_object = Slot(uri=TESTLINK.object, name="serviceunittype to variant association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.serviceunittype_to_variant_association_object, domain=ServiceunittypeToVariantAssociation, range=Union[str, SequenceVariantId])

slots.componentservice_to_componentservice_association_subject = Slot(uri=TESTLINK.subject, name="componentservice to componentservice association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_to_componentservice_association_subject, domain=ComponentserviceToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_componentservice_association_object = Slot(uri=TESTLINK.object, name="componentservice to componentservice association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.componentservice_to_componentservice_association_object, domain=ComponentserviceToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_componentservice_homology_association_predicate = Slot(uri=TESTLINK.predicate, name="componentservice to componentservice homology association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.componentservice_to_componentservice_homology_association_predicate, domain=ComponentserviceToComponentserviceHomologyAssociation, range=Union[str, PredicateType])

slots.componentservice_availability_mixin_quantifier_qualifier = Slot(uri=TESTLINK.quantifier_qualifier, name="componentservice availability mixin_quantifier qualifier", curie=TESTLINK.curie('quantifier_qualifier'),
                   model_uri=TESTLINK.componentservice_availability_mixin_quantifier_qualifier, domain=ComponentserviceAvailabilityMixin, range=Optional[Union[str, OntologyClassId]])

slots.componentservice_to_componentservice_coavailability_association_predicate = Slot(uri=TESTLINK.predicate, name="componentservice to componentservice coavailability association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.componentservice_to_componentservice_coavailability_association_predicate, domain=ComponentserviceToComponentserviceCoavailabilityAssociation, range=Union[str, PredicateType])

slots.pairwise_componentservice_to_componentservice_interaction_predicate = Slot(uri=TESTLINK.predicate, name="pairwise componentservice to componentservice interaction_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.pairwise_componentservice_to_componentservice_interaction_predicate, domain=PairwiseComponentserviceToComponentserviceInteraction, range=Union[str, PredicateType])

slots.pairwise_componentservice_to_componentservice_interaction_relation = Slot(uri=TESTLINK.relation, name="pairwise componentservice to componentservice interaction_relation", curie=TESTLINK.curie('relation'),
                   model_uri=TESTLINK.pairwise_componentservice_to_componentservice_interaction_relation, domain=PairwiseComponentserviceToComponentserviceInteraction, range=Union[str, URIorCURIE])

slots.pairwise_operationally_interaction_subject = Slot(uri=TESTLINK.subject, name="pairwise operationally interaction_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.pairwise_operationally_interaction_subject, domain=PairwiseOperationallyInteraction, range=Union[str, OperationalEntityId])

slots.pairwise_operationally_interaction_id = Slot(uri=TESTLINK.id, name="pairwise operationally interaction_id", curie=TESTLINK.curie('id'),
                   model_uri=TESTLINK.pairwise_operationally_interaction_id, domain=PairwiseOperationallyInteraction, range=Union[str, PairwiseOperationallyInteractionId])

slots.pairwise_operationally_interaction_predicate = Slot(uri=TESTLINK.predicate, name="pairwise operationally interaction_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.pairwise_operationally_interaction_predicate, domain=PairwiseOperationallyInteraction, range=Union[str, PredicateType])

slots.pairwise_operationally_interaction_relation = Slot(uri=TESTLINK.relation, name="pairwise operationally interaction_relation", curie=TESTLINK.curie('relation'),
                   model_uri=TESTLINK.pairwise_operationally_interaction_relation, domain=PairwiseOperationallyInteraction, range=Union[str, URIorCURIE])

slots.pairwise_operationally_interaction_object = Slot(uri=TESTLINK.object, name="pairwise operationally interaction_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.pairwise_operationally_interaction_object, domain=PairwiseOperationallyInteraction, range=Union[str, OperationalEntityId])

slots.component_type_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="component type to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.component_type_to_entity_association_mixin_subject, domain=None, range=Union[str, ComponentTypeId])

slots.component_type_to_error_or_observable_feature_association_subject = Slot(uri=TESTLINK.subject, name="component type to error or observable feature association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.component_type_to_error_or_observable_feature_association_subject, domain=ComponentTypeToErrorOrObservableFeatureAssociation, range=Union[str, ErrorOrObservableFeatureId])

slots.operational_entity_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="operational entity to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.operational_entity_to_entity_association_mixin_subject, domain=None, range=Union[str, OperationalEntityId])

slots.administrative_operational_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="administrative operational to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.administrative_operational_to_entity_association_mixin_subject, domain=None, range=Union[str, AdministrativeOperationId])

slots.orchestration_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="orchestration to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.orchestration_to_entity_association_mixin_subject, domain=None, range=Union[str, ControlActorId])

slots.case_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="case to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.case_to_entity_association_mixin_subject, domain=None, range=Union[str, CaseId])

slots.orchestration_to_orchestration_association_object = Slot(uri=TESTLINK.object, name="orchestration to orchestration association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.orchestration_to_orchestration_association_object, domain=OrchestrationToOrchestrationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_subject = Slot(uri=TESTLINK.subject, name="orchestration to orchestration derivation association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.orchestration_to_orchestration_derivation_association_subject, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_object = Slot(uri=TESTLINK.object, name="orchestration to orchestration derivation association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.orchestration_to_orchestration_derivation_association_object, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_predicate = Slot(uri=TESTLINK.predicate, name="orchestration to orchestration derivation association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.orchestration_to_orchestration_derivation_association_predicate, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, PredicateType])

slots.orchestration_to_orchestration_derivation_association_catalyst_qualifier = Slot(uri=TESTLINK.catalyst_qualifier, name="orchestration to orchestration derivation association_catalyst qualifier", curie=TESTLINK.curie('catalyst_qualifier'),
                   model_uri=TESTLINK.orchestration_to_orchestration_derivation_association_catalyst_qualifier, domain=OrchestrationToOrchestrationDerivationAssociation, range=Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]])

slots.orchestration_to_error_or_observable_feature_association_object = Slot(uri=TESTLINK.object, name="orchestration to error or observable feature association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.orchestration_to_error_or_observable_feature_association_object, domain=OrchestrationToErrorOrObservableFeatureAssociation, range=Union[str, ErrorOrObservableFeatureId])

slots.orchestration_to_pathway_association_object = Slot(uri=TESTLINK.object, name="orchestration to pathway association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.orchestration_to_pathway_association_object, domain=OrchestrationToPathwayAssociation, range=Union[str, PathwayId])

slots.orchestration_to_componentservice_association_object = Slot(uri=TESTLINK.object, name="orchestration to componentservice association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.orchestration_to_componentservice_association_object, domain=OrchestrationToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.administrative_operational_to_componentservice_association_object = Slot(uri=TESTLINK.object, name="administrative operational to componentservice association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.administrative_operational_to_componentservice_association_object, domain=AdministrativeOperationalToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.resource_sample_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="resource sample to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.resource_sample_to_entity_association_mixin_subject, domain=None, range=Union[str, ResourceSampleId])

slots.resource_sample_derivation_association_subject = Slot(uri=TESTLINK.subject, name="resource sample derivation association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.resource_sample_derivation_association_subject, domain=ResourceSampleDerivationAssociation, range=Union[str, ResourceSampleId])

slots.resource_sample_derivation_association_object = Slot(uri=TESTLINK.object, name="resource sample derivation association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.resource_sample_derivation_association_object, domain=ResourceSampleDerivationAssociation, range=Union[str, NamedThingId])

slots.resource_sample_derivation_association_predicate = Slot(uri=TESTLINK.predicate, name="resource sample derivation association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.resource_sample_derivation_association_predicate, domain=ResourceSampleDerivationAssociation, range=Union[str, PredicateType])

slots.error_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="error to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.error_to_entity_association_mixin_subject, domain=None, range=Union[str, ErrorId])

slots.entity_to_exposure_event_association_mixin_object = Slot(uri=TESTLINK.object, name="entity to exposure event association mixin_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.entity_to_exposure_event_association_mixin_object, domain=None, range=Union[dict, ExposureEvent])

slots.exposure_event_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="exposure event to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.exposure_event_to_entity_association_mixin_subject, domain=None, range=Union[dict, ExposureEvent])

slots.entity_to_outcome_association_mixin_object = Slot(uri=TESTLINK.object, name="entity to outcome association mixin_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.entity_to_outcome_association_mixin_object, domain=None, range=Union[dict, Outcome])

slots.entity_to_observable_feature_association_mixin_description = Slot(uri=TESTLINK.description, name="entity to observable feature association mixin_description", curie=TESTLINK.curie('description'),
                   model_uri=TESTLINK.entity_to_observable_feature_association_mixin_description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.entity_to_observable_feature_association_mixin_object = Slot(uri=TESTLINK.object, name="entity to observable feature association mixin_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.entity_to_observable_feature_association_mixin_object, domain=None, range=Union[str, ObservableFeatureId])

slots.entity_to_error_association_mixin_object = Slot(uri=TESTLINK.object, name="entity to error association mixin_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.entity_to_error_association_mixin_object, domain=None, range=Union[str, ErrorId])

slots.error_or_observable_feature_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="error or observable feature to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.error_or_observable_feature_to_entity_association_mixin_subject, domain=None, range=Union[str, ErrorOrObservableFeatureId])

slots.error_or_observable_feature_association_to_location_association_object = Slot(uri=TESTLINK.object, name="error or observable feature association to location association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.error_or_observable_feature_association_to_location_association_object, domain=ErrorOrObservableFeatureAssociationToLocationAssociation, range=Union[str, DeploymentEntityId])

slots.error_or_observable_feature_to_location_association_object = Slot(uri=TESTLINK.object, name="error or observable feature to location association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.error_or_observable_feature_to_location_association_object, domain=ErrorOrObservableFeatureToLocationAssociation, range=Union[str, DeploymentEntityId])

slots.entity_to_error_or_observable_feature_association_mixin_object = Slot(uri=TESTLINK.object, name="entity to error or observable feature association mixin_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.entity_to_error_or_observable_feature_association_mixin_object, domain=None, range=Union[str, ErrorOrObservableFeatureId])

slots.serviceunittype_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="serviceunittype to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.serviceunittype_to_entity_association_mixin_subject, domain=None, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_observable_feature_association_predicate = Slot(uri=TESTLINK.predicate, name="serviceunittype to observable feature association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.serviceunittype_to_observable_feature_association_predicate, domain=ServiceunittypeToObservableFeatureAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_observable_feature_association_subject = Slot(uri=TESTLINK.subject, name="serviceunittype to observable feature association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.serviceunittype_to_observable_feature_association_subject, domain=ServiceunittypeToObservableFeatureAssociation, range=Union[str, ServiceunittypeId])

slots.exposure_event_to_observable_feature_association_subject = Slot(uri=TESTLINK.subject, name="exposure event to observable feature association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.exposure_event_to_observable_feature_association_subject, domain=ExposureEventToObservableFeatureAssociation, range=Union[dict, ExposureEvent])

slots.behavior_to_behavioral_feature_association_subject = Slot(uri=TESTLINK.subject, name="behavior to behavioral feature association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.behavior_to_behavioral_feature_association_subject, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehaviorId])

slots.behavior_to_behavioral_feature_association_object = Slot(uri=TESTLINK.object, name="behavior to behavioral feature association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.behavior_to_behavioral_feature_association_object, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehavioralFeatureId])

slots.componentservice_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="componentservice to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_to_entity_association_mixin_subject, domain=None, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="variant to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.variant_to_entity_association_mixin_subject, domain=None, range=Union[str, SequenceVariantId])

slots.componentservice_to_observable_feature_association_subject = Slot(uri=TESTLINK.subject, name="componentservice to observable feature association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_to_observable_feature_association_subject, domain=ComponentserviceToObservableFeatureAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_error_association_subject = Slot(uri=TESTLINK.subject, name="componentservice to error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_to_error_association_subject, domain=ComponentserviceToErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_to_componentservice_association_object = Slot(uri=TESTLINK.object, name="variant to componentservice association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.variant_to_componentservice_association_object, domain=VariantToComponentserviceAssociation, range=Union[dict, Componentservice])

slots.variant_to_componentservice_association_predicate = Slot(uri=TESTLINK.predicate, name="variant to componentservice association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.variant_to_componentservice_association_predicate, domain=VariantToComponentserviceAssociation, range=Union[str, PredicateType])

slots.variant_to_componentservice_availability_association_predicate = Slot(uri=TESTLINK.predicate, name="variant to componentservice availability association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.variant_to_componentservice_availability_association_predicate, domain=VariantToComponentserviceAvailabilityAssociation, range=Union[str, PredicateType])

slots.variant_to_population_association_subject = Slot(uri=TESTLINK.subject, name="variant to population association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.variant_to_population_association_subject, domain=VariantToPopulationAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_population_association_object = Slot(uri=TESTLINK.object, name="variant to population association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.variant_to_population_association_object, domain=VariantToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.variant_to_population_association_has_quotient = Slot(uri=TESTLINK.has_quotient, name="variant to population association_has quotient", curie=TESTLINK.curie('has_quotient'),
                   model_uri=TESTLINK.variant_to_population_association_has_quotient, domain=VariantToPopulationAssociation, range=Optional[float])

slots.variant_to_population_association_has_count = Slot(uri=TESTLINK.has_count, name="variant to population association_has count", curie=TESTLINK.curie('has_count'),
                   model_uri=TESTLINK.variant_to_population_association_has_count, domain=VariantToPopulationAssociation, range=Optional[int])

slots.variant_to_population_association_has_total = Slot(uri=TESTLINK.has_total, name="variant to population association_has total", curie=TESTLINK.curie('has_total'),
                   model_uri=TESTLINK.variant_to_population_association_has_total, domain=VariantToPopulationAssociation, range=Optional[int])

slots.population_to_population_association_subject = Slot(uri=TESTLINK.subject, name="population to population association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.population_to_population_association_subject, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.population_to_population_association_object = Slot(uri=TESTLINK.object, name="population to population association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.population_to_population_association_object, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.population_to_population_association_predicate = Slot(uri=TESTLINK.predicate, name="population to population association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.population_to_population_association_predicate, domain=PopulationToPopulationAssociation, range=Union[str, PredicateType])

slots.variant_to_observable_feature_association_subject = Slot(uri=TESTLINK.subject, name="variant to observable feature association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.variant_to_observable_feature_association_subject, domain=VariantToObservableFeatureAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_error_association_subject = Slot(uri=TESTLINK.subject, name="variant to error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.variant_to_error_association_subject, domain=VariantToErrorAssociation, range=Union[str, NamedThingId])

slots.variant_to_error_association_predicate = Slot(uri=TESTLINK.predicate, name="variant to error association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.variant_to_error_association_predicate, domain=VariantToErrorAssociation, range=Union[str, PredicateType])

slots.variant_to_error_association_object = Slot(uri=TESTLINK.object, name="variant to error association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.variant_to_error_association_object, domain=VariantToErrorAssociation, range=Union[str, NamedThingId])

slots.serviceunittype_to_error_association_subject = Slot(uri=TESTLINK.subject, name="serviceunittype to error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.serviceunittype_to_error_association_subject, domain=ServiceunittypeToErrorAssociation, range=Union[str, NamedThingId])

slots.serviceunittype_to_error_association_predicate = Slot(uri=TESTLINK.predicate, name="serviceunittype to error association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.serviceunittype_to_error_association_predicate, domain=ServiceunittypeToErrorAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_error_association_object = Slot(uri=TESTLINK.object, name="serviceunittype to error association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.serviceunittype_to_error_association_object, domain=ServiceunittypeToErrorAssociation, range=Union[str, NamedThingId])

slots.model_to_error_association_mixin_subject = Slot(uri=TESTLINK.subject, name="model to error association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.model_to_error_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.model_to_error_association_mixin_predicate = Slot(uri=TESTLINK.predicate, name="model to error association mixin_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.model_to_error_association_mixin_predicate, domain=None, range=Union[str, PredicateType])

slots.componentservice_as_a_model_of_error_association_subject = Slot(uri=TESTLINK.subject, name="componentservice as a model of error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_as_a_model_of_error_association_subject, domain=ComponentserviceAsAModelOfErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_as_a_model_of_error_association_subject = Slot(uri=TESTLINK.subject, name="variant as a model of error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.variant_as_a_model_of_error_association_subject, domain=VariantAsAModelOfErrorAssociation, range=Union[str, SequenceVariantId])

slots.serviceunittype_as_a_model_of_error_association_subject = Slot(uri=TESTLINK.subject, name="serviceunittype as a model of error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.serviceunittype_as_a_model_of_error_association_subject, domain=ServiceunittypeAsAModelOfErrorAssociation, range=Union[str, ServiceunittypeId])

slots.component_type_as_a_model_of_error_association_subject = Slot(uri=TESTLINK.subject, name="component type as a model of error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.component_type_as_a_model_of_error_association_subject, domain=ComponentTypeAsAModelOfErrorAssociation, range=Union[str, ComponentTypeId])

slots.systemic_entity_as_a_model_of_error_association_subject = Slot(uri=TESTLINK.subject, name="systemic entity as a model of error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.systemic_entity_as_a_model_of_error_association_subject, domain=SystemicEntityAsAModelOfErrorAssociation, range=Union[str, SystemicEntityId])

slots.componentservice_has_variant_that_contributes_to_error_association_subject = Slot(uri=TESTLINK.subject, name="componentservice has variant that contributes to error association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_has_variant_that_contributes_to_error_association_subject, domain=ComponentserviceHasVariantThatContributesToErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_availability_site_association_subject = Slot(uri=TESTLINK.subject, name="componentservice to availability site association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_to_availability_site_association_subject, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_availability_site_association_object = Slot(uri=TESTLINK.object, name="componentservice to availability site association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.componentservice_to_availability_site_association_object, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[str, DeploymentEntityId])

slots.componentservice_to_availability_site_association_predicate = Slot(uri=TESTLINK.predicate, name="componentservice to availability site association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.componentservice_to_availability_site_association_predicate, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[str, PredicateType])

slots.componentservice_to_availability_site_association_stage_qualifier = Slot(uri=TESTLINK.stage_qualifier, name="componentservice to availability site association_stage qualifier", curie=TESTLINK.curie('stage_qualifier'),
                   model_uri=TESTLINK.componentservice_to_availability_site_association_stage_qualifier, domain=ComponentserviceToAvailabilitySiteAssociation, range=Optional[Union[str, LifecycleStageId]])

slots.componentservice_to_availability_site_association_quantifier_qualifier = Slot(uri=TESTLINK.quantifier_qualifier, name="componentservice to availability site association_quantifier qualifier", curie=TESTLINK.curie('quantifier_qualifier'),
                   model_uri=TESTLINK.componentservice_to_availability_site_association_quantifier_qualifier, domain=ComponentserviceToAvailabilitySiteAssociation, range=Optional[Union[str, OntologyClassId]])

slots.sequence_variant_modulates_repairing_association_subject = Slot(uri=TESTLINK.subject, name="sequence variant modulates repairing association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.sequence_variant_modulates_repairing_association_subject, domain=SequenceVariantModulatesRepairingAssociation, range=Union[str, SequenceVariantId])

slots.sequence_variant_modulates_repairing_association_object = Slot(uri=TESTLINK.object, name="sequence variant modulates repairing association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.sequence_variant_modulates_repairing_association_object, domain=SequenceVariantModulatesRepairingAssociation, range=Union[str, RepairingId])

slots.functional_association_subject = Slot(uri=TESTLINK.subject, name="functional association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.functional_association_subject, domain=FunctionalAssociation, range=Union[dict, MacrooperationalMachineMixin])

slots.functional_association_object = Slot(uri=TESTLINK.object, name="functional association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.functional_association_object, domain=FunctionalAssociation, range=Union[str, ComponentserviceOntologyClassId])

slots.macrooperational_machine_mixin_to_entity_association_mixin_subject = Slot(uri=TESTLINK.subject, name="macrooperational machine mixin to entity association mixin_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.macrooperational_machine_mixin_to_entity_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.macrooperational_machine_mixin_to_operational_activity_association_object = Slot(uri=TESTLINK.object, name="macrooperational machine mixin to operational activity association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.macrooperational_machine_mixin_to_operational_activity_association_object, domain=MacrooperationalMachineMixinToOperationalActivityAssociation, range=Union[str, OperationalActivityId])

slots.macrooperational_machine_mixin_to_computational_process_association_object = Slot(uri=TESTLINK.object, name="macrooperational machine mixin to computational process association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.macrooperational_machine_mixin_to_computational_process_association_object, domain=MacrooperationalMachineMixinToComputationalProcessAssociation, range=Union[str, ComputationalProcessId])

slots.macrooperational_machine_mixin_to_component_association_object = Slot(uri=TESTLINK.object, name="macrooperational machine mixin to component association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.macrooperational_machine_mixin_to_component_association_object, domain=MacrooperationalMachineMixinToComponentAssociation, range=Union[str, ComponentId])

slots.componentservice_to_go_term_association_subject = Slot(uri=TESTLINK.subject, name="componentservice to go term association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_to_go_term_association_subject, domain=ComponentserviceToGoTermAssociation, range=Union[str, OperationalEntityId])

slots.componentservice_to_go_term_association_object = Slot(uri=TESTLINK.object, name="componentservice to go term association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.componentservice_to_go_term_association_object, domain=ComponentserviceToGoTermAssociation, range=Union[str, ComponentserviceOntologyClassId])

slots.service_sequence_localization_subject = Slot(uri=TESTLINK.subject, name="service sequence localization_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.service_sequence_localization_subject, domain=ServiceSequenceLocalization, range=Union[str, WorkloadEntityId])

slots.service_sequence_localization_object = Slot(uri=TESTLINK.object, name="service sequence localization_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.service_sequence_localization_object, domain=ServiceSequenceLocalization, range=Union[str, WorkloadEntityId])

slots.service_sequence_localization_predicate = Slot(uri=TESTLINK.predicate, name="service sequence localization_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.service_sequence_localization_predicate, domain=ServiceSequenceLocalization, range=Union[str, PredicateType])

slots.sequence_feature_relationship_subject = Slot(uri=TESTLINK.subject, name="sequence feature relationship_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.sequence_feature_relationship_subject, domain=SequenceFeatureRelationship, range=Union[str, WorkloadEntityId])

slots.sequence_feature_relationship_object = Slot(uri=TESTLINK.object, name="sequence feature relationship_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.sequence_feature_relationship_object, domain=SequenceFeatureRelationship, range=Union[str, WorkloadEntityId])

slots.componentserviceinstance_to_componentservice_relationship_subject = Slot(uri=TESTLINK.subject, name="componentserviceinstance to componentservice relationship_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentserviceinstance_to_componentservice_relationship_subject, domain=ComponentserviceinstanceToComponentserviceRelationship, range=Union[str, ComponentserviceinstanceId])

slots.componentserviceinstance_to_componentservice_relationship_object = Slot(uri=TESTLINK.object, name="componentserviceinstance to componentservice relationship_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.componentserviceinstance_to_componentservice_relationship_object, domain=ComponentserviceinstanceToComponentserviceRelationship, range=Union[dict, Componentservice])

slots.componentservice_to_servicetype_relationship_subject = Slot(uri=TESTLINK.subject, name="componentservice to servicetype relationship_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_to_servicetype_relationship_subject, domain=ComponentserviceToServicetypeRelationship, range=Union[dict, Componentservice])

slots.componentservice_to_servicetype_relationship_object = Slot(uri=TESTLINK.object, name="componentservice to servicetype relationship_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.componentservice_to_servicetype_relationship_object, domain=ComponentserviceToServicetypeRelationship, range=Union[dict, ServicetypeMixin])

slots.componentservice_to_servicetype_relationship_predicate = Slot(uri=TESTLINK.predicate, name="componentservice to servicetype relationship_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.componentservice_to_servicetype_relationship_predicate, domain=ComponentserviceToServicetypeRelationship, range=Union[str, PredicateType])

slots.daemon_to_componentserviceinstance_relationship_subject = Slot(uri=TESTLINK.subject, name="daemon to componentserviceinstance relationship_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.daemon_to_componentserviceinstance_relationship_subject, domain=DaemonToComponentserviceinstanceRelationship, range=Union[str, DaemonId])

slots.daemon_to_componentserviceinstance_relationship_object = Slot(uri=TESTLINK.object, name="daemon to componentserviceinstance relationship_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.daemon_to_componentserviceinstance_relationship_object, domain=DaemonToComponentserviceinstanceRelationship, range=Union[str, ComponentserviceinstanceId])

slots.componentservice_regulatory_relationship_predicate = Slot(uri=TESTLINK.predicate, name="componentservice regulatory relationship_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.componentservice_regulatory_relationship_predicate, domain=ComponentserviceRegulatoryRelationship, range=Union[str, PredicateType])

slots.componentservice_regulatory_relationship_subject = Slot(uri=TESTLINK.subject, name="componentservice regulatory relationship_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.componentservice_regulatory_relationship_subject, domain=ComponentserviceRegulatoryRelationship, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_regulatory_relationship_object = Slot(uri=TESTLINK.object, name="componentservice regulatory relationship_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.componentservice_regulatory_relationship_object, domain=ComponentserviceRegulatoryRelationship, range=Union[dict, ComponentserviceOrServicetype])

slots.deployment_entity_to_deployment_entity_association_subject = Slot(uri=TESTLINK.subject, name="deployment entity to deployment entity association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.deployment_entity_to_deployment_entity_association_subject, domain=DeploymentEntityToDeploymentEntityAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_association_object = Slot(uri=TESTLINK.object, name="deployment entity to deployment entity association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.deployment_entity_to_deployment_entity_association_object, domain=DeploymentEntityToDeploymentEntityAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_subject = Slot(uri=TESTLINK.subject, name="deployment entity to deployment entity part of association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.deployment_entity_to_deployment_entity_part_of_association_subject, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_object = Slot(uri=TESTLINK.object, name="deployment entity to deployment entity part of association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.deployment_entity_to_deployment_entity_part_of_association_object, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_predicate = Slot(uri=TESTLINK.predicate, name="deployment entity to deployment entity part of association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.deployment_entity_to_deployment_entity_part_of_association_predicate, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, PredicateType])

slots.deployment_entity_to_deployment_entity_ontogenic_association_subject = Slot(uri=TESTLINK.subject, name="deployment entity to deployment entity ontogenic association_subject", curie=TESTLINK.curie('subject'),
                   model_uri=TESTLINK.deployment_entity_to_deployment_entity_ontogenic_association_subject, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_ontogenic_association_object = Slot(uri=TESTLINK.object, name="deployment entity to deployment entity ontogenic association_object", curie=TESTLINK.curie('object'),
                   model_uri=TESTLINK.deployment_entity_to_deployment_entity_ontogenic_association_object, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_ontogenic_association_predicate = Slot(uri=TESTLINK.predicate, name="deployment entity to deployment entity ontogenic association_predicate", curie=TESTLINK.curie('predicate'),
                   model_uri=TESTLINK.deployment_entity_to_deployment_entity_ontogenic_association_predicate, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, PredicateType])

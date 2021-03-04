# testlink model file locations
import os

basedir = os.path.abspath(os.path.join(__file__, '..', '..'))
TESTLINK_MODEL_YAML = os.path.join(basedir, 'testlink-model.yaml')
TESTLINK_MODEL_JSONLD = os.path.join(basedir, 'context.jsonld')
TESTLINK_MODEL_SHEX = os.path.join(basedir, 'shex', 'testlink-model.shex')
TESTLINK_MODEL_RDF = os.path.join(basedir, 'rdf', 'testlink-model.ttl')
TESTLINK_MODEL_OWL = os.path.join(basedir, 'ontology', 'testlink-model.owl')
TESTLINK_MODEL_JSON = os.path.join(basedir, 'testlink-model.json')
TESTLINK_MODEL_JSON_SCHEMA = os.path.join(basedir, 'json-schema', 'testlink-model.json')
TESTLINK_MODEL_JAVA = os.path.join(basedir, 'java')
TESTLINK_MODEL_PYTHON = os.path.join(basedir, 'testlink', 'model.py')

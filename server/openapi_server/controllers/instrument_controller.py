import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import INSTRUMENT_TYPE_NAME, INSTRUMENT_TYPE_URI

from openapi_server.models.instrument import Instrument  # noqa: E501
from openapi_server import util

def instruments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Instrument

    Gets a list of all instances of Instrument (more information in http://dbpedia.org/ontology/Instrument) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Instrument]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=INSTRUMENT_TYPE_URI,
        rdf_type_name=INSTRUMENT_TYPE_NAME, 
        kls=Instrument)

def instruments_id_get(id):  # noqa: E501
    """Get a single Instrument by its id

    Gets the details of a given Instrument (more information in http://dbpedia.org/ontology/Instrument) # noqa: E501

    :param id: The ID of the Instrument to be retrieved
    :type id: str

    :rtype: Instrument
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=INSTRUMENT_TYPE_URI,
        rdf_type_name=INSTRUMENT_TYPE_NAME, 
        kls=Instrument)

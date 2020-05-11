import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NASCARDRIVER_TYPE_NAME, NASCARDRIVER_TYPE_URI

from openapi_server.models.nascar_driver import NascarDriver  # noqa: E501
from openapi_server import util

def nascardrivers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NascarDriver

    Gets a list of all instances of NascarDriver (more information in http://dbpedia.org/ontology/NascarDriver) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NascarDriver]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NASCARDRIVER_TYPE_URI,
        rdf_type_name=NASCARDRIVER_TYPE_NAME, 
        kls=NascarDriver)

def nascardrivers_id_get(id):  # noqa: E501
    """Get a single NascarDriver by its id

    Gets the details of a given NascarDriver (more information in http://dbpedia.org/ontology/NascarDriver) # noqa: E501

    :param id: The ID of the NascarDriver to be retrieved
    :type id: str

    :rtype: NascarDriver
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NASCARDRIVER_TYPE_URI,
        rdf_type_name=NASCARDRIVER_TYPE_NAME, 
        kls=NascarDriver)

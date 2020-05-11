import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DEANERY_TYPE_NAME, DEANERY_TYPE_URI

from openapi_server.models.deanery import Deanery  # noqa: E501
from openapi_server import util

def deanerys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Deanery

    Gets a list of all instances of Deanery (more information in http://dbpedia.org/ontology/Deanery) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Deanery]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DEANERY_TYPE_URI,
        rdf_type_name=DEANERY_TYPE_NAME, 
        kls=Deanery)

def deanerys_id_get(id):  # noqa: E501
    """Get a single Deanery by its id

    Gets the details of a given Deanery (more information in http://dbpedia.org/ontology/Deanery) # noqa: E501

    :param id: The ID of the Deanery to be retrieved
    :type id: str

    :rtype: Deanery
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DEANERY_TYPE_URI,
        rdf_type_name=DEANERY_TYPE_NAME, 
        kls=Deanery)

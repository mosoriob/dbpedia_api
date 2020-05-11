import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HOSPITAL_TYPE_NAME, HOSPITAL_TYPE_URI

from openapi_server.models.hospital import Hospital  # noqa: E501
from openapi_server import util

def hospitals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Hospital

    Gets a list of all instances of Hospital (more information in http://dbpedia.org/ontology/Hospital) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Hospital]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HOSPITAL_TYPE_URI,
        rdf_type_name=HOSPITAL_TYPE_NAME, 
        kls=Hospital)

def hospitals_id_get(id):  # noqa: E501
    """Get a single Hospital by its id

    Gets the details of a given Hospital (more information in http://dbpedia.org/ontology/Hospital) # noqa: E501

    :param id: The ID of the Hospital to be retrieved
    :type id: str

    :rtype: Hospital
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HOSPITAL_TYPE_URI,
        rdf_type_name=HOSPITAL_TYPE_NAME, 
        kls=Hospital)

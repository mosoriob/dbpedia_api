import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BARONET_TYPE_NAME, BARONET_TYPE_URI

from openapi_server.models.baronet import Baronet  # noqa: E501
from openapi_server import util

def baronets_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Baronet

    Gets a list of all instances of Baronet (more information in http://dbpedia.org/ontology/Baronet) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Baronet]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BARONET_TYPE_URI,
        rdf_type_name=BARONET_TYPE_NAME, 
        kls=Baronet)

def baronets_id_get(id):  # noqa: E501
    """Get a single Baronet by its id

    Gets the details of a given Baronet (more information in http://dbpedia.org/ontology/Baronet) # noqa: E501

    :param id: The ID of the Baronet to be retrieved
    :type id: str

    :rtype: Baronet
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BARONET_TYPE_URI,
        rdf_type_name=BARONET_TYPE_NAME, 
        kls=Baronet)

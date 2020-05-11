import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARISTOCRAT_TYPE_NAME, ARISTOCRAT_TYPE_URI

from openapi_server.models.aristocrat import Aristocrat  # noqa: E501
from openapi_server import util

def aristocrats_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Aristocrat

    Gets a list of all instances of Aristocrat (more information in http://dbpedia.org/ontology/Aristocrat) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Aristocrat]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARISTOCRAT_TYPE_URI,
        rdf_type_name=ARISTOCRAT_TYPE_NAME, 
        kls=Aristocrat)

def aristocrats_id_get(id):  # noqa: E501
    """Get a single Aristocrat by its id

    Gets the details of a given Aristocrat (more information in http://dbpedia.org/ontology/Aristocrat) # noqa: E501

    :param id: The ID of the Aristocrat to be retrieved
    :type id: str

    :rtype: Aristocrat
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARISTOCRAT_TYPE_URI,
        rdf_type_name=ARISTOCRAT_TYPE_NAME, 
        kls=Aristocrat)

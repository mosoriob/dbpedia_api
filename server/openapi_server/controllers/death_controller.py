import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DEATH_TYPE_NAME, DEATH_TYPE_URI

from openapi_server.models.death import Death  # noqa: E501
from openapi_server import util

def deaths_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Death

    Gets a list of all instances of Death (more information in http://dbpedia.org/ontology/Death) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Death]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DEATH_TYPE_URI,
        rdf_type_name=DEATH_TYPE_NAME, 
        kls=Death)

def deaths_id_get(id):  # noqa: E501
    """Get a single Death by its id

    Gets the details of a given Death (more information in http://dbpedia.org/ontology/Death) # noqa: E501

    :param id: The ID of the Death to be retrieved
    :type id: str

    :rtype: Death
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DEATH_TYPE_URI,
        rdf_type_name=DEATH_TYPE_NAME, 
        kls=Death)

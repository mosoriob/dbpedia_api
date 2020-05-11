import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WORLDHERITAGESITE_TYPE_NAME, WORLDHERITAGESITE_TYPE_URI

from openapi_server.models.world_heritage_site import WorldHeritageSite  # noqa: E501
from openapi_server import util

def worldheritagesites_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WorldHeritageSite

    Gets a list of all instances of WorldHeritageSite (more information in http://dbpedia.org/ontology/WorldHeritageSite) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WorldHeritageSite]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WORLDHERITAGESITE_TYPE_URI,
        rdf_type_name=WORLDHERITAGESITE_TYPE_NAME, 
        kls=WorldHeritageSite)

def worldheritagesites_id_get(id):  # noqa: E501
    """Get a single WorldHeritageSite by its id

    Gets the details of a given WorldHeritageSite (more information in http://dbpedia.org/ontology/WorldHeritageSite) # noqa: E501

    :param id: The ID of the WorldHeritageSite to be retrieved
    :type id: str

    :rtype: WorldHeritageSite
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WORLDHERITAGESITE_TYPE_URI,
        rdf_type_name=WORLDHERITAGESITE_TYPE_NAME, 
        kls=WorldHeritageSite)

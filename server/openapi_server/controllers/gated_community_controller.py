import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GATEDCOMMUNITY_TYPE_NAME, GATEDCOMMUNITY_TYPE_URI

from openapi_server.models.gated_community import GatedCommunity  # noqa: E501
from openapi_server import util

def gatedcommunitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GatedCommunity

    Gets a list of all instances of GatedCommunity (more information in http://dbpedia.org/ontology/GatedCommunity) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GatedCommunity]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GATEDCOMMUNITY_TYPE_URI,
        rdf_type_name=GATEDCOMMUNITY_TYPE_NAME, 
        kls=GatedCommunity)

def gatedcommunitys_id_get(id):  # noqa: E501
    """Get a single GatedCommunity by its id

    Gets the details of a given GatedCommunity (more information in http://dbpedia.org/ontology/GatedCommunity) # noqa: E501

    :param id: The ID of the GatedCommunity to be retrieved
    :type id: str

    :rtype: GatedCommunity
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GATEDCOMMUNITY_TYPE_URI,
        rdf_type_name=GATEDCOMMUNITY_TYPE_NAME, 
        kls=GatedCommunity)

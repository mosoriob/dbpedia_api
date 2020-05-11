import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PENALTYSHOOTOUT_TYPE_NAME, PENALTYSHOOTOUT_TYPE_URI

from openapi_server.models.penalty_shoot_out import PenaltyShootOut  # noqa: E501
from openapi_server import util

def penaltyshootouts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PenaltyShootOut

    Gets a list of all instances of PenaltyShootOut (more information in http://dbpedia.org/ontology/PenaltyShootOut) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PenaltyShootOut]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PENALTYSHOOTOUT_TYPE_URI,
        rdf_type_name=PENALTYSHOOTOUT_TYPE_NAME, 
        kls=PenaltyShootOut)

def penaltyshootouts_id_get(id):  # noqa: E501
    """Get a single PenaltyShootOut by its id

    Gets the details of a given PenaltyShootOut (more information in http://dbpedia.org/ontology/PenaltyShootOut) # noqa: E501

    :param id: The ID of the PenaltyShootOut to be retrieved
    :type id: str

    :rtype: PenaltyShootOut
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PENALTYSHOOTOUT_TYPE_URI,
        rdf_type_name=PENALTYSHOOTOUT_TYPE_NAME, 
        kls=PenaltyShootOut)

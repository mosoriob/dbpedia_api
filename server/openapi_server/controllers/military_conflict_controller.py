import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MILITARYCONFLICT_TYPE_NAME, MILITARYCONFLICT_TYPE_URI

from openapi_server.models.military_conflict import MilitaryConflict  # noqa: E501
from openapi_server import util

def militaryconflicts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MilitaryConflict

    Gets a list of all instances of MilitaryConflict (more information in http://dbpedia.org/ontology/MilitaryConflict) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MilitaryConflict]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MILITARYCONFLICT_TYPE_URI,
        rdf_type_name=MILITARYCONFLICT_TYPE_NAME, 
        kls=MilitaryConflict)

def militaryconflicts_id_get(id):  # noqa: E501
    """Get a single MilitaryConflict by its id

    Gets the details of a given MilitaryConflict (more information in http://dbpedia.org/ontology/MilitaryConflict) # noqa: E501

    :param id: The ID of the MilitaryConflict to be retrieved
    :type id: str

    :rtype: MilitaryConflict
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MILITARYCONFLICT_TYPE_URI,
        rdf_type_name=MILITARYCONFLICT_TYPE_NAME, 
        kls=MilitaryConflict)

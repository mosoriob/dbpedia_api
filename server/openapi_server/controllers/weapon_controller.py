import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WEAPON_TYPE_NAME, WEAPON_TYPE_URI

from openapi_server.models.weapon import Weapon  # noqa: E501
from openapi_server import util

def weapons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Weapon

    Gets a list of all instances of Weapon (more information in http://dbpedia.org/ontology/Weapon) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Weapon]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WEAPON_TYPE_URI,
        rdf_type_name=WEAPON_TYPE_NAME, 
        kls=Weapon)

def weapons_id_get(id):  # noqa: E501
    """Get a single Weapon by its id

    Gets the details of a given Weapon (more information in http://dbpedia.org/ontology/Weapon) # noqa: E501

    :param id: The ID of the Weapon to be retrieved
    :type id: str

    :rtype: Weapon
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WEAPON_TYPE_URI,
        rdf_type_name=WEAPON_TYPE_NAME, 
        kls=Weapon)

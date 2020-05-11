import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MILITARYUNIT_TYPE_NAME, MILITARYUNIT_TYPE_URI

from openapi_server.models.military_unit import MilitaryUnit  # noqa: E501
from openapi_server import util

def militaryunits_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MilitaryUnit

    Gets a list of all instances of MilitaryUnit (more information in http://dbpedia.org/ontology/MilitaryUnit) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MilitaryUnit]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MILITARYUNIT_TYPE_URI,
        rdf_type_name=MILITARYUNIT_TYPE_NAME, 
        kls=MilitaryUnit)

def militaryunits_id_get(id):  # noqa: E501
    """Get a single MilitaryUnit by its id

    Gets the details of a given MilitaryUnit (more information in http://dbpedia.org/ontology/MilitaryUnit) # noqa: E501

    :param id: The ID of the MilitaryUnit to be retrieved
    :type id: str

    :rtype: MilitaryUnit
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MILITARYUNIT_TYPE_URI,
        rdf_type_name=MILITARYUNIT_TYPE_NAME, 
        kls=MilitaryUnit)

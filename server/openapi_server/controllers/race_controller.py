import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RACE_TYPE_NAME, RACE_TYPE_URI

from openapi_server.models.race import Race  # noqa: E501
from openapi_server import util

def races_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Race

    Gets a list of all instances of Race (more information in http://dbpedia.org/ontology/Race) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Race]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RACE_TYPE_URI,
        rdf_type_name=RACE_TYPE_NAME, 
        kls=Race)

def races_id_get(id):  # noqa: E501
    """Get a single Race by its id

    Gets the details of a given Race (more information in http://dbpedia.org/ontology/Race) # noqa: E501

    :param id: The ID of the Race to be retrieved
    :type id: str

    :rtype: Race
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RACE_TYPE_URI,
        rdf_type_name=RACE_TYPE_NAME, 
        kls=Race)

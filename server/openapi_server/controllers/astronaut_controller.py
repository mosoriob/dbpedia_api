import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ASTRONAUT_TYPE_NAME, ASTRONAUT_TYPE_URI

from openapi_server.models.astronaut import Astronaut  # noqa: E501
from openapi_server import util

def astronauts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Astronaut

    Gets a list of all instances of Astronaut (more information in http://dbpedia.org/ontology/Astronaut) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Astronaut]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ASTRONAUT_TYPE_URI,
        rdf_type_name=ASTRONAUT_TYPE_NAME, 
        kls=Astronaut)

def astronauts_id_get(id):  # noqa: E501
    """Get a single Astronaut by its id

    Gets the details of a given Astronaut (more information in http://dbpedia.org/ontology/Astronaut) # noqa: E501

    :param id: The ID of the Astronaut to be retrieved
    :type id: str

    :rtype: Astronaut
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ASTRONAUT_TYPE_URI,
        rdf_type_name=ASTRONAUT_TYPE_NAME, 
        kls=Astronaut)

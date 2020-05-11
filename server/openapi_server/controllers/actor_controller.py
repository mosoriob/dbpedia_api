import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ACTOR_TYPE_NAME, ACTOR_TYPE_URI

from openapi_server.models.actor import Actor  # noqa: E501
from openapi_server import util

def actors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Actor

    Gets a list of all instances of Actor (more information in http://dbpedia.org/ontology/Actor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Actor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ACTOR_TYPE_URI,
        rdf_type_name=ACTOR_TYPE_NAME, 
        kls=Actor)

def actors_id_get(id):  # noqa: E501
    """Get a single Actor by its id

    Gets the details of a given Actor (more information in http://dbpedia.org/ontology/Actor) # noqa: E501

    :param id: The ID of the Actor to be retrieved
    :type id: str

    :rtype: Actor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ACTOR_TYPE_URI,
        rdf_type_name=ACTOR_TYPE_NAME, 
        kls=Actor)

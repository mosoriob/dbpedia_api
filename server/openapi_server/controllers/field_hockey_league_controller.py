import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FIELDHOCKEYLEAGUE_TYPE_NAME, FIELDHOCKEYLEAGUE_TYPE_URI

from openapi_server.models.field_hockey_league import FieldHockeyLeague  # noqa: E501
from openapi_server import util

def fieldhockeyleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FieldHockeyLeague

    Gets a list of all instances of FieldHockeyLeague (more information in http://dbpedia.org/ontology/FieldHockeyLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FieldHockeyLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FIELDHOCKEYLEAGUE_TYPE_URI,
        rdf_type_name=FIELDHOCKEYLEAGUE_TYPE_NAME, 
        kls=FieldHockeyLeague)

def fieldhockeyleagues_id_get(id):  # noqa: E501
    """Get a single FieldHockeyLeague by its id

    Gets the details of a given FieldHockeyLeague (more information in http://dbpedia.org/ontology/FieldHockeyLeague) # noqa: E501

    :param id: The ID of the FieldHockeyLeague to be retrieved
    :type id: str

    :rtype: FieldHockeyLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FIELDHOCKEYLEAGUE_TYPE_URI,
        rdf_type_name=FIELDHOCKEYLEAGUE_TYPE_NAME, 
        kls=FieldHockeyLeague)

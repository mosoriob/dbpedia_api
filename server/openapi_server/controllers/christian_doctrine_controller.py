import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHRISTIANDOCTRINE_TYPE_NAME, CHRISTIANDOCTRINE_TYPE_URI

from openapi_server.models.christian_doctrine import ChristianDoctrine  # noqa: E501
from openapi_server import util

def christiandoctrines_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ChristianDoctrine

    Gets a list of all instances of ChristianDoctrine (more information in http://dbpedia.org/ontology/ChristianDoctrine) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ChristianDoctrine]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHRISTIANDOCTRINE_TYPE_URI,
        rdf_type_name=CHRISTIANDOCTRINE_TYPE_NAME, 
        kls=ChristianDoctrine)

def christiandoctrines_id_get(id):  # noqa: E501
    """Get a single ChristianDoctrine by its id

    Gets the details of a given ChristianDoctrine (more information in http://dbpedia.org/ontology/ChristianDoctrine) # noqa: E501

    :param id: The ID of the ChristianDoctrine to be retrieved
    :type id: str

    :rtype: ChristianDoctrine
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHRISTIANDOCTRINE_TYPE_URI,
        rdf_type_name=CHRISTIANDOCTRINE_TYPE_NAME, 
        kls=ChristianDoctrine)

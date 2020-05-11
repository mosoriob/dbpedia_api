import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import UNIVERSITY_TYPE_NAME, UNIVERSITY_TYPE_URI

from openapi_server.models.university import University  # noqa: E501
from openapi_server import util

def universitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of University

    Gets a list of all instances of University (more information in http://dbpedia.org/ontology/University) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[University]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=UNIVERSITY_TYPE_URI,
        rdf_type_name=UNIVERSITY_TYPE_NAME, 
        kls=University)

def universitys_id_get(id):  # noqa: E501
    """Get a single University by its id

    Gets the details of a given University (more information in http://dbpedia.org/ontology/University) # noqa: E501

    :param id: The ID of the University to be retrieved
    :type id: str

    :rtype: University
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=UNIVERSITY_TYPE_URI,
        rdf_type_name=UNIVERSITY_TYPE_NAME, 
        kls=University)

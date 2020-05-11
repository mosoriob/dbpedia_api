import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ACTIVITY_TYPE_NAME, ACTIVITY_TYPE_URI

from openapi_server.models.activity import Activity  # noqa: E501
from openapi_server import util

def activitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Activity

    Gets a list of all instances of Activity (more information in http://dbpedia.org/ontology/Activity) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Activity]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ACTIVITY_TYPE_URI,
        rdf_type_name=ACTIVITY_TYPE_NAME, 
        kls=Activity)

def activitys_id_get(id):  # noqa: E501
    """Get a single Activity by its id

    Gets the details of a given Activity (more information in http://dbpedia.org/ontology/Activity) # noqa: E501

    :param id: The ID of the Activity to be retrieved
    :type id: str

    :rtype: Activity
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ACTIVITY_TYPE_URI,
        rdf_type_name=ACTIVITY_TYPE_NAME, 
        kls=Activity)

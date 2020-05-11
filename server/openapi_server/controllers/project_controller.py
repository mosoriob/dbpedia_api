import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROJECT_TYPE_NAME, PROJECT_TYPE_URI

from openapi_server.models.project import Project  # noqa: E501
from openapi_server import util

def projects_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Project

    Gets a list of all instances of Project (more information in http://dbpedia.org/ontology/Project) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Project]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROJECT_TYPE_URI,
        rdf_type_name=PROJECT_TYPE_NAME, 
        kls=Project)

def projects_id_get(id):  # noqa: E501
    """Get a single Project by its id

    Gets the details of a given Project (more information in http://dbpedia.org/ontology/Project) # noqa: E501

    :param id: The ID of the Project to be retrieved
    :type id: str

    :rtype: Project
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PROJECT_TYPE_URI,
        rdf_type_name=PROJECT_TYPE_NAME, 
        kls=Project)

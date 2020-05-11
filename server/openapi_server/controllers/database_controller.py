import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DATABASE_TYPE_NAME, DATABASE_TYPE_URI

from openapi_server.models.database import Database  # noqa: E501
from openapi_server import util

def databases_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Database

    Gets a list of all instances of Database (more information in http://dbpedia.org/ontology/Database) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Database]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DATABASE_TYPE_URI,
        rdf_type_name=DATABASE_TYPE_NAME, 
        kls=Database)

def databases_id_get(id):  # noqa: E501
    """Get a single Database by its id

    Gets the details of a given Database (more information in http://dbpedia.org/ontology/Database) # noqa: E501

    :param id: The ID of the Database to be retrieved
    :type id: str

    :rtype: Database
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DATABASE_TYPE_URI,
        rdf_type_name=DATABASE_TYPE_NAME, 
        kls=Database)

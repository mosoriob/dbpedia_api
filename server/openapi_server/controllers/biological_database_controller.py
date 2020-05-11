import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BIOLOGICALDATABASE_TYPE_NAME, BIOLOGICALDATABASE_TYPE_URI

from openapi_server.models.biological_database import BiologicalDatabase  # noqa: E501
from openapi_server import util

def biologicaldatabases_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BiologicalDatabase

    Gets a list of all instances of BiologicalDatabase (more information in http://dbpedia.org/ontology/BiologicalDatabase) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BiologicalDatabase]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BIOLOGICALDATABASE_TYPE_URI,
        rdf_type_name=BIOLOGICALDATABASE_TYPE_NAME, 
        kls=BiologicalDatabase)

def biologicaldatabases_id_get(id):  # noqa: E501
    """Get a single BiologicalDatabase by its id

    Gets the details of a given BiologicalDatabase (more information in http://dbpedia.org/ontology/BiologicalDatabase) # noqa: E501

    :param id: The ID of the BiologicalDatabase to be retrieved
    :type id: str

    :rtype: BiologicalDatabase
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BIOLOGICALDATABASE_TYPE_URI,
        rdf_type_name=BIOLOGICALDATABASE_TYPE_NAME, 
        kls=BiologicalDatabase)

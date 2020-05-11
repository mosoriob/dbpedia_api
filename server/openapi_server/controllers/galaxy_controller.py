import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GALAXY_TYPE_NAME, GALAXY_TYPE_URI

from openapi_server.models.galaxy import Galaxy  # noqa: E501
from openapi_server import util

def galaxys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Galaxy

    Gets a list of all instances of Galaxy (more information in http://dbpedia.org/ontology/Galaxy) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Galaxy]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GALAXY_TYPE_URI,
        rdf_type_name=GALAXY_TYPE_NAME, 
        kls=Galaxy)

def galaxys_id_get(id):  # noqa: E501
    """Get a single Galaxy by its id

    Gets the details of a given Galaxy (more information in http://dbpedia.org/ontology/Galaxy) # noqa: E501

    :param id: The ID of the Galaxy to be retrieved
    :type id: str

    :rtype: Galaxy
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GALAXY_TYPE_URI,
        rdf_type_name=GALAXY_TYPE_NAME, 
        kls=Galaxy)

import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPECIES_TYPE_NAME, SPECIES_TYPE_URI

from openapi_server.models.species import Species  # noqa: E501
from openapi_server import util

def speciess_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Species

    Gets a list of all instances of Species (more information in http://dbpedia.org/ontology/Species) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Species]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPECIES_TYPE_URI,
        rdf_type_name=SPECIES_TYPE_NAME, 
        kls=Species)

def speciess_id_get(id):  # noqa: E501
    """Get a single Species by its id

    Gets the details of a given Species (more information in http://dbpedia.org/ontology/Species) # noqa: E501

    :param id: The ID of the Species to be retrieved
    :type id: str

    :rtype: Species
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPECIES_TYPE_URI,
        rdf_type_name=SPECIES_TYPE_NAME, 
        kls=Species)

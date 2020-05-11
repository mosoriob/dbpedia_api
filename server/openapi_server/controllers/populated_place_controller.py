import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POPULATEDPLACE_TYPE_NAME, POPULATEDPLACE_TYPE_URI

from openapi_server.models.populated_place import PopulatedPlace  # noqa: E501
from openapi_server import util

def populatedplaces_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PopulatedPlace

    Gets a list of all instances of PopulatedPlace (more information in http://dbpedia.org/ontology/PopulatedPlace) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PopulatedPlace]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POPULATEDPLACE_TYPE_URI,
        rdf_type_name=POPULATEDPLACE_TYPE_NAME, 
        kls=PopulatedPlace)

def populatedplaces_id_get(id):  # noqa: E501
    """Get a single PopulatedPlace by its id

    Gets the details of a given PopulatedPlace (more information in http://dbpedia.org/ontology/PopulatedPlace) # noqa: E501

    :param id: The ID of the PopulatedPlace to be retrieved
    :type id: str

    :rtype: PopulatedPlace
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POPULATEDPLACE_TYPE_URI,
        rdf_type_name=POPULATEDPLACE_TYPE_NAME, 
        kls=PopulatedPlace)

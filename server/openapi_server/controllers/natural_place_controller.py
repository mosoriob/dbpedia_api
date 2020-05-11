import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NATURALPLACE_TYPE_NAME, NATURALPLACE_TYPE_URI

from openapi_server.models.natural_place import NaturalPlace  # noqa: E501
from openapi_server import util

def naturalplaces_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NaturalPlace

    Gets a list of all instances of NaturalPlace (more information in http://dbpedia.org/ontology/NaturalPlace) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NaturalPlace]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NATURALPLACE_TYPE_URI,
        rdf_type_name=NATURALPLACE_TYPE_NAME, 
        kls=NaturalPlace)

def naturalplaces_id_get(id):  # noqa: E501
    """Get a single NaturalPlace by its id

    Gets the details of a given NaturalPlace (more information in http://dbpedia.org/ontology/NaturalPlace) # noqa: E501

    :param id: The ID of the NaturalPlace to be retrieved
    :type id: str

    :rtype: NaturalPlace
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NATURALPLACE_TYPE_URI,
        rdf_type_name=NATURALPLACE_TYPE_NAME, 
        kls=NaturalPlace)

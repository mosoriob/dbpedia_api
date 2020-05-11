import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GEOPOLITICALORGANISATION_TYPE_NAME, GEOPOLITICALORGANISATION_TYPE_URI

from openapi_server.models.geopolitical_organisation import GeopoliticalOrganisation  # noqa: E501
from openapi_server import util

def geopoliticalorganisations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GeopoliticalOrganisation

    Gets a list of all instances of GeopoliticalOrganisation (more information in http://dbpedia.org/ontology/GeopoliticalOrganisation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GeopoliticalOrganisation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GEOPOLITICALORGANISATION_TYPE_URI,
        rdf_type_name=GEOPOLITICALORGANISATION_TYPE_NAME, 
        kls=GeopoliticalOrganisation)

def geopoliticalorganisations_id_get(id):  # noqa: E501
    """Get a single GeopoliticalOrganisation by its id

    Gets the details of a given GeopoliticalOrganisation (more information in http://dbpedia.org/ontology/GeopoliticalOrganisation) # noqa: E501

    :param id: The ID of the GeopoliticalOrganisation to be retrieved
    :type id: str

    :rtype: GeopoliticalOrganisation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GEOPOLITICALORGANISATION_TYPE_URI,
        rdf_type_name=GEOPOLITICALORGANISATION_TYPE_NAME, 
        kls=GeopoliticalOrganisation)

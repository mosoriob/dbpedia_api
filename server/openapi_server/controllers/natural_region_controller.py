import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NATURALREGION_TYPE_NAME, NATURALREGION_TYPE_URI

from openapi_server.models.natural_region import NaturalRegion  # noqa: E501
from openapi_server import util

def naturalregions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NaturalRegion

    Gets a list of all instances of NaturalRegion (more information in http://dbpedia.org/ontology/NaturalRegion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NaturalRegion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NATURALREGION_TYPE_URI,
        rdf_type_name=NATURALREGION_TYPE_NAME, 
        kls=NaturalRegion)

def naturalregions_id_get(id):  # noqa: E501
    """Get a single NaturalRegion by its id

    Gets the details of a given NaturalRegion (more information in http://dbpedia.org/ontology/NaturalRegion) # noqa: E501

    :param id: The ID of the NaturalRegion to be retrieved
    :type id: str

    :rtype: NaturalRegion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NATURALREGION_TYPE_URI,
        rdf_type_name=NATURALREGION_TYPE_NAME, 
        kls=NaturalRegion)

import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TAXON_TYPE_NAME, TAXON_TYPE_URI

from openapi_server.models.taxon import Taxon  # noqa: E501
from openapi_server import util

def taxons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Taxon

    Gets a list of all instances of Taxon (more information in http://dbpedia.org/ontology/Taxon) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Taxon]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TAXON_TYPE_URI,
        rdf_type_name=TAXON_TYPE_NAME, 
        kls=Taxon)

def taxons_id_get(id):  # noqa: E501
    """Get a single Taxon by its id

    Gets the details of a given Taxon (more information in http://dbpedia.org/ontology/Taxon) # noqa: E501

    :param id: The ID of the Taxon to be retrieved
    :type id: str

    :rtype: Taxon
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TAXON_TYPE_URI,
        rdf_type_name=TAXON_TYPE_NAME, 
        kls=Taxon)

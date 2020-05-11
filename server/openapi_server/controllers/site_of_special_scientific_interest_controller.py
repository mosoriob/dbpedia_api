import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SITEOFSPECIALSCIENTIFICINTEREST_TYPE_NAME, SITEOFSPECIALSCIENTIFICINTEREST_TYPE_URI

from openapi_server.models.site_of_special_scientific_interest import SiteOfSpecialScientificInterest  # noqa: E501
from openapi_server import util

def siteofspecialscientificinterests_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SiteOfSpecialScientificInterest

    Gets a list of all instances of SiteOfSpecialScientificInterest (more information in http://dbpedia.org/ontology/SiteOfSpecialScientificInterest) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SiteOfSpecialScientificInterest]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SITEOFSPECIALSCIENTIFICINTEREST_TYPE_URI,
        rdf_type_name=SITEOFSPECIALSCIENTIFICINTEREST_TYPE_NAME, 
        kls=SiteOfSpecialScientificInterest)

def siteofspecialscientificinterests_id_get(id):  # noqa: E501
    """Get a single SiteOfSpecialScientificInterest by its id

    Gets the details of a given SiteOfSpecialScientificInterest (more information in http://dbpedia.org/ontology/SiteOfSpecialScientificInterest) # noqa: E501

    :param id: The ID of the SiteOfSpecialScientificInterest to be retrieved
    :type id: str

    :rtype: SiteOfSpecialScientificInterest
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SITEOFSPECIALSCIENTIFICINTEREST_TYPE_URI,
        rdf_type_name=SITEOFSPECIALSCIENTIFICINTEREST_TYPE_NAME, 
        kls=SiteOfSpecialScientificInterest)

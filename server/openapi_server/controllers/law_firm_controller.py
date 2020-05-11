import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LAWFIRM_TYPE_NAME, LAWFIRM_TYPE_URI

from openapi_server.models.law_firm import LawFirm  # noqa: E501
from openapi_server import util

def lawfirms_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of LawFirm

    Gets a list of all instances of LawFirm (more information in http://dbpedia.org/ontology/LawFirm) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[LawFirm]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LAWFIRM_TYPE_URI,
        rdf_type_name=LAWFIRM_TYPE_NAME, 
        kls=LawFirm)

def lawfirms_id_get(id):  # noqa: E501
    """Get a single LawFirm by its id

    Gets the details of a given LawFirm (more information in http://dbpedia.org/ontology/LawFirm) # noqa: E501

    :param id: The ID of the LawFirm to be retrieved
    :type id: str

    :rtype: LawFirm
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LAWFIRM_TYPE_URI,
        rdf_type_name=LAWFIRM_TYPE_NAME, 
        kls=LawFirm)

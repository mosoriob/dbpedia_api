import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LIECHTENSTEINSETTLEMENT_TYPE_NAME, LIECHTENSTEINSETTLEMENT_TYPE_URI

from openapi_server.models.liechtenstein_settlement import LiechtensteinSettlement  # noqa: E501
from openapi_server import util

def liechtensteinsettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of LiechtensteinSettlement

    Gets a list of all instances of LiechtensteinSettlement (more information in http://dbpedia.org/ontology/LiechtensteinSettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[LiechtensteinSettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LIECHTENSTEINSETTLEMENT_TYPE_URI,
        rdf_type_name=LIECHTENSTEINSETTLEMENT_TYPE_NAME, 
        kls=LiechtensteinSettlement)

def liechtensteinsettlements_id_get(id):  # noqa: E501
    """Get a single LiechtensteinSettlement by its id

    Gets the details of a given LiechtensteinSettlement (more information in http://dbpedia.org/ontology/LiechtensteinSettlement) # noqa: E501

    :param id: The ID of the LiechtensteinSettlement to be retrieved
    :type id: str

    :rtype: LiechtensteinSettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LIECHTENSTEINSETTLEMENT_TYPE_URI,
        rdf_type_name=LIECHTENSTEINSETTLEMENT_TYPE_NAME, 
        kls=LiechtensteinSettlement)

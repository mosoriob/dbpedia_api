import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SUBMUNICIPALITY_TYPE_NAME, SUBMUNICIPALITY_TYPE_URI

from openapi_server.models.sub_municipality import SubMunicipality  # noqa: E501
from openapi_server import util

def submunicipalitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SubMunicipality

    Gets a list of all instances of SubMunicipality (more information in http://dbpedia.org/ontology/SubMunicipality) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SubMunicipality]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SUBMUNICIPALITY_TYPE_URI,
        rdf_type_name=SUBMUNICIPALITY_TYPE_NAME, 
        kls=SubMunicipality)

def submunicipalitys_id_get(id):  # noqa: E501
    """Get a single SubMunicipality by its id

    Gets the details of a given SubMunicipality (more information in http://dbpedia.org/ontology/SubMunicipality) # noqa: E501

    :param id: The ID of the SubMunicipality to be retrieved
    :type id: str

    :rtype: SubMunicipality
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SUBMUNICIPALITY_TYPE_URI,
        rdf_type_name=SUBMUNICIPALITY_TYPE_NAME, 
        kls=SubMunicipality)

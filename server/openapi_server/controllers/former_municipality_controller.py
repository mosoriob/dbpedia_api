import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FORMERMUNICIPALITY_TYPE_NAME, FORMERMUNICIPALITY_TYPE_URI

from openapi_server.models.former_municipality import FormerMunicipality  # noqa: E501
from openapi_server import util

def formermunicipalitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FormerMunicipality

    Gets a list of all instances of FormerMunicipality (more information in http://dbpedia.org/ontology/FormerMunicipality) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FormerMunicipality]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FORMERMUNICIPALITY_TYPE_URI,
        rdf_type_name=FORMERMUNICIPALITY_TYPE_NAME, 
        kls=FormerMunicipality)

def formermunicipalitys_id_get(id):  # noqa: E501
    """Get a single FormerMunicipality by its id

    Gets the details of a given FormerMunicipality (more information in http://dbpedia.org/ontology/FormerMunicipality) # noqa: E501

    :param id: The ID of the FormerMunicipality to be retrieved
    :type id: str

    :rtype: FormerMunicipality
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FORMERMUNICIPALITY_TYPE_URI,
        rdf_type_name=FORMERMUNICIPALITY_TYPE_NAME, 
        kls=FormerMunicipality)

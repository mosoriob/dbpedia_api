import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NATIONALANTHEM_TYPE_NAME, NATIONALANTHEM_TYPE_URI

from openapi_server.models.national_anthem import NationalAnthem  # noqa: E501
from openapi_server import util

def nationalanthems_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NationalAnthem

    Gets a list of all instances of NationalAnthem (more information in http://dbpedia.org/ontology/NationalAnthem) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NationalAnthem]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NATIONALANTHEM_TYPE_URI,
        rdf_type_name=NATIONALANTHEM_TYPE_NAME, 
        kls=NationalAnthem)

def nationalanthems_id_get(id):  # noqa: E501
    """Get a single NationalAnthem by its id

    Gets the details of a given NationalAnthem (more information in http://dbpedia.org/ontology/NationalAnthem) # noqa: E501

    :param id: The ID of the NationalAnthem to be retrieved
    :type id: str

    :rtype: NationalAnthem
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NATIONALANTHEM_TYPE_URI,
        rdf_type_name=NATIONALANTHEM_TYPE_NAME, 
        kls=NationalAnthem)

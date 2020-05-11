import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BROWNDWARF_TYPE_NAME, BROWNDWARF_TYPE_URI

from openapi_server.models.brown_dwarf import BrownDwarf  # noqa: E501
from openapi_server import util

def browndwarfs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BrownDwarf

    Gets a list of all instances of BrownDwarf (more information in http://dbpedia.org/ontology/BrownDwarf) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BrownDwarf]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BROWNDWARF_TYPE_URI,
        rdf_type_name=BROWNDWARF_TYPE_NAME, 
        kls=BrownDwarf)

def browndwarfs_id_get(id):  # noqa: E501
    """Get a single BrownDwarf by its id

    Gets the details of a given BrownDwarf (more information in http://dbpedia.org/ontology/BrownDwarf) # noqa: E501

    :param id: The ID of the BrownDwarf to be retrieved
    :type id: str

    :rtype: BrownDwarf
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BROWNDWARF_TYPE_URI,
        rdf_type_name=BROWNDWARF_TYPE_NAME, 
        kls=BrownDwarf)

import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FASHIONDESIGNER_TYPE_NAME, FASHIONDESIGNER_TYPE_URI

from openapi_server.models.fashion_designer import FashionDesigner  # noqa: E501
from openapi_server import util

def fashiondesigners_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FashionDesigner

    Gets a list of all instances of FashionDesigner (more information in http://dbpedia.org/ontology/FashionDesigner) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FashionDesigner]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FASHIONDESIGNER_TYPE_URI,
        rdf_type_name=FASHIONDESIGNER_TYPE_NAME, 
        kls=FashionDesigner)

def fashiondesigners_id_get(id):  # noqa: E501
    """Get a single FashionDesigner by its id

    Gets the details of a given FashionDesigner (more information in http://dbpedia.org/ontology/FashionDesigner) # noqa: E501

    :param id: The ID of the FashionDesigner to be retrieved
    :type id: str

    :rtype: FashionDesigner
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FASHIONDESIGNER_TYPE_URI,
        rdf_type_name=FASHIONDESIGNER_TYPE_NAME, 
        kls=FashionDesigner)

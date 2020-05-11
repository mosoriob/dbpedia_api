import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BOXINGCATEGORY_TYPE_NAME, BOXINGCATEGORY_TYPE_URI

from openapi_server.models.boxing_category import BoxingCategory  # noqa: E501
from openapi_server import util

def boxingcategorys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BoxingCategory

    Gets a list of all instances of BoxingCategory (more information in http://dbpedia.org/ontology/BoxingCategory) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BoxingCategory]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BOXINGCATEGORY_TYPE_URI,
        rdf_type_name=BOXINGCATEGORY_TYPE_NAME, 
        kls=BoxingCategory)

def boxingcategorys_id_get(id):  # noqa: E501
    """Get a single BoxingCategory by its id

    Gets the details of a given BoxingCategory (more information in http://dbpedia.org/ontology/BoxingCategory) # noqa: E501

    :param id: The ID of the BoxingCategory to be retrieved
    :type id: str

    :rtype: BoxingCategory
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BOXINGCATEGORY_TYPE_URI,
        rdf_type_name=BOXINGCATEGORY_TYPE_NAME, 
        kls=BoxingCategory)

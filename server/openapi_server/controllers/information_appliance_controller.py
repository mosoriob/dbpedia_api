import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import INFORMATIONAPPLIANCE_TYPE_NAME, INFORMATIONAPPLIANCE_TYPE_URI

from openapi_server.models.information_appliance import InformationAppliance  # noqa: E501
from openapi_server import util

def informationappliances_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of InformationAppliance

    Gets a list of all instances of InformationAppliance (more information in http://dbpedia.org/ontology/InformationAppliance) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[InformationAppliance]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=INFORMATIONAPPLIANCE_TYPE_URI,
        rdf_type_name=INFORMATIONAPPLIANCE_TYPE_NAME, 
        kls=InformationAppliance)

def informationappliances_id_get(id):  # noqa: E501
    """Get a single InformationAppliance by its id

    Gets the details of a given InformationAppliance (more information in http://dbpedia.org/ontology/InformationAppliance) # noqa: E501

    :param id: The ID of the InformationAppliance to be retrieved
    :type id: str

    :rtype: InformationAppliance
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=INFORMATIONAPPLIANCE_TYPE_URI,
        rdf_type_name=INFORMATIONAPPLIANCE_TYPE_NAME, 
        kls=InformationAppliance)

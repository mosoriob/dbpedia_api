import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EDUCATIONALINSTITUTION_TYPE_NAME, EDUCATIONALINSTITUTION_TYPE_URI

from openapi_server.models.educational_institution import EducationalInstitution  # noqa: E501
from openapi_server import util

def educationalinstitutions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of EducationalInstitution

    Gets a list of all instances of EducationalInstitution (more information in http://dbpedia.org/ontology/EducationalInstitution) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[EducationalInstitution]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EDUCATIONALINSTITUTION_TYPE_URI,
        rdf_type_name=EDUCATIONALINSTITUTION_TYPE_NAME, 
        kls=EducationalInstitution)

def educationalinstitutions_id_get(id):  # noqa: E501
    """Get a single EducationalInstitution by its id

    Gets the details of a given EducationalInstitution (more information in http://dbpedia.org/ontology/EducationalInstitution) # noqa: E501

    :param id: The ID of the EducationalInstitution to be retrieved
    :type id: str

    :rtype: EducationalInstitution
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=EDUCATIONALINSTITUTION_TYPE_URI,
        rdf_type_name=EDUCATIONALINSTITUTION_TYPE_NAME, 
        kls=EducationalInstitution)

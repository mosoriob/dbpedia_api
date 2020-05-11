import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ORGANISATIONMEMBER_TYPE_NAME, ORGANISATIONMEMBER_TYPE_URI

from openapi_server.models.organisation_member import OrganisationMember  # noqa: E501
from openapi_server import util

def organisationmembers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of OrganisationMember

    Gets a list of all instances of OrganisationMember (more information in http://dbpedia.org/ontology/OrganisationMember) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[OrganisationMember]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ORGANISATIONMEMBER_TYPE_URI,
        rdf_type_name=ORGANISATIONMEMBER_TYPE_NAME, 
        kls=OrganisationMember)

def organisationmembers_id_get(id):  # noqa: E501
    """Get a single OrganisationMember by its id

    Gets the details of a given OrganisationMember (more information in http://dbpedia.org/ontology/OrganisationMember) # noqa: E501

    :param id: The ID of the OrganisationMember to be retrieved
    :type id: str

    :rtype: OrganisationMember
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ORGANISATIONMEMBER_TYPE_URI,
        rdf_type_name=ORGANISATIONMEMBER_TYPE_NAME, 
        kls=OrganisationMember)

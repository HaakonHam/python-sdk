"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from .....exabel.api.data.v1 import relationship_messages_pb2 as exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2
from .....exabel.api.data.v1 import relationship_service_pb2 as exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

class RelationshipServiceStub(object):
    """Service for managing relationship types and relationships. See the User Guide for more
    information about relationship types and relationships.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListRelationshipTypes = channel.unary_unary('/exabel.api.data.v1.RelationshipService/ListRelationshipTypes', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipTypesRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipTypesResponse.FromString)
        self.GetRelationshipType = channel.unary_unary('/exabel.api.data.v1.RelationshipService/GetRelationshipType', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.GetRelationshipTypeRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.FromString)
        self.CreateRelationshipType = channel.unary_unary('/exabel.api.data.v1.RelationshipService/CreateRelationshipType', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.CreateRelationshipTypeRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.FromString)
        self.UpdateRelationshipType = channel.unary_unary('/exabel.api.data.v1.RelationshipService/UpdateRelationshipType', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.UpdateRelationshipTypeRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.FromString)
        self.DeleteRelationshipType = channel.unary_unary('/exabel.api.data.v1.RelationshipService/DeleteRelationshipType', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.DeleteRelationshipTypeRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)
        self.ListRelationships = channel.unary_unary('/exabel.api.data.v1.RelationshipService/ListRelationships', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipsRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipsResponse.FromString)
        self.GetRelationship = channel.unary_unary('/exabel.api.data.v1.RelationshipService/GetRelationship', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.GetRelationshipRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.FromString)
        self.CreateRelationship = channel.unary_unary('/exabel.api.data.v1.RelationshipService/CreateRelationship', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.CreateRelationshipRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.FromString)
        self.UpdateRelationship = channel.unary_unary('/exabel.api.data.v1.RelationshipService/UpdateRelationship', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.UpdateRelationshipRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.FromString)
        self.DeleteRelationship = channel.unary_unary('/exabel.api.data.v1.RelationshipService/DeleteRelationship', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.DeleteRelationshipRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)

class RelationshipServiceServicer(object):
    """Service for managing relationship types and relationships. See the User Guide for more
    information about relationship types and relationships.
    """

    def ListRelationshipTypes(self, request, context):
        """List all relationship types from a common catalog.

        Lists all relationship types available to your customer, including those created by you, in
        the global catalog, and from data sets you are subscribed to.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRelationshipType(self, request, context):
        """Gets one relationship type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRelationshipType(self, request, context):
        """Creates one relationship type and returns it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRelationshipType(self, request, context):
        """Updates one relationship type and returns it.

        This can also be used to create a relationship type by setting `allow_missing` to `true`.

        Note that this method update all fields unless `update_mask` is set.

        Note that modifying the `is_ownership` property may be a slow operation, as all individual
        relationships of this type will have to be updated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRelationshipType(self, request, context):
        """Deletes one relationship type.

        This can only be performed on relationship types with no relationships. You should delete
        relationships before deleting their entity type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRelationships(self, request, context):
        """Lists relationship of a specific type.

        If neither `from_entity` or `to_entity` is given, it is expected that this call will
        take some time to complete.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRelationship(self, request, context):
        """Gets one relationship.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRelationship(self, request, context):
        """Creates one relationship and returns it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRelationship(self, request, context):
        """Updates one relationship and returns it.

        This can also be used to create a relationship by setting `allow_missing` to `true`.

        Note that that this method will update all fields unless `update_mask` is set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRelationship(self, request, context):
        """Deletes one relationship.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_RelationshipServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListRelationshipTypes': grpc.unary_unary_rpc_method_handler(servicer.ListRelationshipTypes, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipTypesRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipTypesResponse.SerializeToString), 'GetRelationshipType': grpc.unary_unary_rpc_method_handler(servicer.GetRelationshipType, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.GetRelationshipTypeRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.SerializeToString), 'CreateRelationshipType': grpc.unary_unary_rpc_method_handler(servicer.CreateRelationshipType, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.CreateRelationshipTypeRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.SerializeToString), 'UpdateRelationshipType': grpc.unary_unary_rpc_method_handler(servicer.UpdateRelationshipType, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.UpdateRelationshipTypeRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.SerializeToString), 'DeleteRelationshipType': grpc.unary_unary_rpc_method_handler(servicer.DeleteRelationshipType, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.DeleteRelationshipTypeRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ListRelationships': grpc.unary_unary_rpc_method_handler(servicer.ListRelationships, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipsRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipsResponse.SerializeToString), 'GetRelationship': grpc.unary_unary_rpc_method_handler(servicer.GetRelationship, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.GetRelationshipRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.SerializeToString), 'CreateRelationship': grpc.unary_unary_rpc_method_handler(servicer.CreateRelationship, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.CreateRelationshipRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.SerializeToString), 'UpdateRelationship': grpc.unary_unary_rpc_method_handler(servicer.UpdateRelationship, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.UpdateRelationshipRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.SerializeToString), 'DeleteRelationship': grpc.unary_unary_rpc_method_handler(servicer.DeleteRelationship, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.DeleteRelationshipRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('exabel.api.data.v1.RelationshipService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class RelationshipService(object):
    """Service for managing relationship types and relationships. See the User Guide for more
    information about relationship types and relationships.
    """

    @staticmethod
    def ListRelationshipTypes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/ListRelationshipTypes', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipTypesRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipTypesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRelationshipType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/GetRelationshipType', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.GetRelationshipTypeRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRelationshipType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/CreateRelationshipType', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.CreateRelationshipTypeRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRelationshipType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/UpdateRelationshipType', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.UpdateRelationshipTypeRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.RelationshipType.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRelationshipType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/DeleteRelationshipType', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.DeleteRelationshipTypeRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRelationships(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/ListRelationships', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipsRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.ListRelationshipsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRelationship(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/GetRelationship', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.GetRelationshipRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRelationship(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/CreateRelationship', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.CreateRelationshipRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRelationship(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/UpdateRelationship', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.UpdateRelationshipRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.Relationship.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRelationship(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.RelationshipService/DeleteRelationship', exabel_dot_api_dot_data_dot_v1_dot_relationship__service__pb2.DeleteRelationshipRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
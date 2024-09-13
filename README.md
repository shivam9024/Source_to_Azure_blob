AZURE_CONNECTION_STRING = " Enter from your Azure blob storage container"

blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)

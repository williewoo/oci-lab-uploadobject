import oci
from flask import Flask, render_template, request 

signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)

namespace = "hutchhk"  # The OCI namespace
bucket_name = "bucket-videomakers" # The OCI bucket name

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["myfile"]
        object_name = file.filename
        put_object_body = file.content_type

        # Upload object in the bucket
        object_storage_client.put_object(
            namespace,
            bucket_name,
            object_name,
            put_object_body,
        )

    # List objects in the bucket
    list_objects_response = object_storage_client.list_objects(namespace, bucket_name)
    objectslist = list_objects_response.data.objects
    
    return render_template("upload.html", objectslist_page=objectslist)

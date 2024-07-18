import ballerina/http;
import ballerina/io;

public function main() returns error? {
    http:Client clientEp = check new ("https://api.example.com");
    
    json payload = {
        "title": "Sample Form",
        "description": "This is a sample form created with Ballerina"
    };

    http:Response response = check clientEp->post("/forms", payload);

    if (response.statusCode == 201) {
        json responsePayload = check response.getJsonPayload();
        io:println("Form created successfully!");
        io:println(responsePayload.toJsonString());
    } else {
        io:println("Failed to create form. Status code: ", response.statusCode);
    }
}
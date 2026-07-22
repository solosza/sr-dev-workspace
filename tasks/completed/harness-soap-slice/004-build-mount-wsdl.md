# Task 004: Mount SOAP App + Serve WSDL
**Type:** BUILD | **Gates:** SO-04
## Action
ONE change: make the SOAP app reachable with a served WSDL. Prefer mounting the spyne WsgiApplication onto the existing FastAPI app (main.py) via WSGIMiddleware at /soap (so GET /soap?wsdl returns the WSDL), OR provide a small standalone runner (run_soap.py using wsgiref.simple_server) on a documented port. Document the WSDL URL in a comment.
## Acceptance
Booting the harness, GET <wsdl-url> returns 200 with valid WSDL XML (parses as XML, contains both operations).

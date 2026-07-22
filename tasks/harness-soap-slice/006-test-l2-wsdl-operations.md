# Task 006: L2 - WSDL + Operations
**Type:** TEST (L2) | **Gates:** SO-06
## Action
ONE script: boot the SOAP service (or generate the WSDL statically if spyne supports it); construct zeep.Client(wsdl_url); assert both GetCustomer and GetOrderStatus appear in the client's service operations with correct signatures. No live data call yet.
## Acceptance
zeep builds from the WSDL, both ops listed, exit 0. Red: fix then /kernel/learn.

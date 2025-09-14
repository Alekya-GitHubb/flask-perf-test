In the last five years, serverless computing has become a core cloud service, with AWS, Google, and Azure each building on their own strengths. AWS Lambda led the way with strong ecosystem integration and features like per-millisecond pricing, support for container images, higher memory/CPU, and stronger SnapStart for quicker cold starts. Google Cloud caused a ripple with Cloud Run, which runs any container serverlessly, and Functions 2nd Gen with Eventarc, providing developers with flexibility without needing to rebuild apps. Azure Functions aimed at enterprises, with Durable Functions for long-running workflows, multiple hosting plans to meet price and performance, and tight integration with services such as Cosmos DB and Service Bus. These advancements shifted serverless from a simple function runner to an API, data pipeline, and microservices platform.



A closer look at AWS Lambda illustrates how it evolved from small ZIP-based functions to a powerful platform. In the past five years, Lambda has reduced billing granularity to 1 ms, added container image support to enable sharing of Docker workflows, scaled up to 10 GB of memory and 6 vCPU for big workloads, and introduced SnapStart for Java to cut cold starts up to 10×. By and large, these improvements made Lambda cheaper, faster, and more versatile, expanding its use cases from glue code to high-performance workloads.



If I were Product Manager for AWS Lambda, I would introduce Predictive Warm Pools. Cold starts remain a significant user problem, with 200–800 ms latency affecting APIs and real-time applications. While SnapStart and Provisioned Concurrency help, they are either runtime-bound or require manual maintenance. Predictive Warm Pools would pre-warm environments automatically in advance of traffic spikes based on predictions and user-provided hints, with consistent latency and low overhead. For users, it would be more streamlined performance for customer-facing applications; for AWS, it would make Lambda more competitive against Google Cloud's more streamlined container start-up in Cloud Run and Azure's Premium Functions.



As a whole, AWS has been ahead on price and size, Google on flexibility, and Azure on corporate integration. Deprecative warming would complete one of the few remaining gaps in serverless adoption, leaving AWS still ahead of innovation.


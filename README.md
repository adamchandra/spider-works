# SpiderWorks Crawler

`docker-compose up` command will start a `crawler` service 

### Downloader Middleware
    process_request()
        - Modify request to check: google/bing cache, wayback machine, etc
        - Rewrite some URLs to get static html versions

    process_response()

### 1. Spider Middleware
    
    process_spider_input()
    process_spider_output()

### Item Pipeline
    process_item()
        - Write html/pdf to disk, db
    
    


Item Pipeline

```
    |                        [Spiders]
    |                            |
    |                    (Spider Middleware)(1*)
    |                            |
    |     [Item Pipeline](3*) <-- [Engine]  <--> (2*)(Downloader Middleware) <-->  [Downloader]
    |                            |
    |                       [Scheduler]

```



- Figure out I/O story
- Local fs storage? database only? i/o queue, ala zeromq? 





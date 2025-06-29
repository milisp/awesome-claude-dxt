# awesome-claude-dxt
# Awesome Claude Desktop Extensions (.dxt) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome Claude Desktop Extensions (.dxt files), tools, and resources

## Contents
- [Official Resources](#official-resources)
- [Extensions by Category](#extensions-by-category)
  - [Development Tools](#development-tools)
  - [File Management](#file-management)
  - [System Tools](#system-tools)
  - [Web Services](#web-services)
  - [Messaging](#messaging)
  - [Databases](#databases)
  - [Analytics](#analytics)
  - [AI Systems](#ai-systems)
  - [MCP Tools](#mcp-tools)
  - [API Integrations](#api-integrations)
  - [Data Analysis](#data-analysis)
  - [Knowledge Base](#knowledge-base)
  - [Media Creation](#media-creation)
  - [Productivity](#productivity)
  - [Professional Apps](#professional-apps)
  - [Finance](#finance)
  - [examples](#examples)
- [Development Tools](#development-tools-1)
- [Packaging & Management](#packaging--management)
- [Documentation & Tutorials](#documentation--tutorials)
- [Community Resources](#community-resources)

## Official Resources
- [Desktop Extensions Announcement](https://www.anthropic.com/engineering/desktop-extensions) - Official blog post
- [DXT Specification](https://github.com/anthropics/dxt) - Open-source toolchain and specs
- [Submission Form](https://forms.gle/tyiAZvch1kDADKoP9) - Submit to official directory
- [Official examples](https://github.com/anthropics/dxt/tree/main/examples) - Official examples

## Contributing
This list is community-maintained. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Extensions by Category

> All extensions are located in the [servers](./servers) folder, organized by `owner/repo`.

### Development Tools

- [chrome-applescript](https://github.com/anthropics/dxt/tree/main/examples/chrome-applescript) - Browser automation via AppleScript
- [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) - Connect to Kubernetes cluster and manage pods, deployments, and services.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - GitLab API, enabling project management
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Tools to read, search, and manipulate Git repositories
- [bazinga012/mcp_code_executor](https://github.com/bazinga012/mcp_code_executor) - An MCP server that allows LLMs to execute Python code within a specified Conda environment.
- [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) - A Model Context Protocol server for Mem0, which helps with managing coding preferences.
- [MCP Team/servers](https://github.com/modelcontextprotocol/servers) - MCP Server for the GitHub API, enabling file operations, repository management, search functionality, and more.
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) - Interact with [OpenAPI](https://www.openapis.org/) APIs.
- [semgrep/mcp](https://github.com/semgrep/mcp) - An MCP server for using Semgrep to scan code for security vulnerabilies. Secure your vibe coding! 
- [manusa/kubernetes-mcp-server](https://github.com/manusa/kubernetes-mcp-server) - A powerful Kubernetes MCP server with additional support for OpenShift. Besides providing CRUD operations for any Kubernetes resource, this server provides specialized tools to interact with your cluster.
- [pathintegral-institute/mcp.science](https://github.com/pathintegral-institute/mcp.science) - A secure sandboxed Python code execution environment for MCP (Model-Client-Program) architecture.
- [MindscapeHQ/mcp-server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) - MCP Server for Raygun's API V3 endpoints for interacting with your Crash Reporting and Real User Monitoring applications. This server provides comprehensive access to Raygun's API features through the Model Context Protocol.
- [baryhuang/mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi) - Interact with large [OpenAPI](https://www.openapis.org/) docs using built-in semantic search for endpoints. Allows for customizing the MCP server prefix.
- [yanmxa/multicluster-mcp-server](https://github.com/yanmxa/multicluster-mcp-server) - The gateway for GenAI systems to interact with multiple Kubernetes clusters.
- [leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server) - This MCP server provides tools and resources for AI assistants to manage n8n workflows and executions, including listing, creating, updating, and deleting workflows, as well as monitoring their execution status.
- [hannesj/mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema) - Allow LLMs to explore large [OpenAPI](https://www.openapis.org/) schemas without bloating the context.
- [ShenghaiWang/xcodebuild](https://github.com/ShenghaiWang/xcodebuild) - 🍎 Build iOS Xcode workspace/project and feed back errors to llm.
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) - Provides a repo-packing MCP tool with configurable profiles that specify file inclusion/exclusion patterns and optional prompts.
- [lingodotdev/lingo.dev](https://github.com/lingodotdev/lingo.dev) - The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is a standard for connecting Large Language Models (LLMs) to external services. This guide will walk you through how to connect AI tools to Lingo.dev using MCP.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Retrieving and analyzing issues from Sentry.io
- [apimatic/apimatic-validator-mcp](https://github.com/apimatic/apimatic-validator-mcp) - This repository provides a Model Context Protocol (MCP) Server for validating OpenAPI specifications using [APIMatic](https://www.apimatic.io/). The server processes OpenAPI files and returns validation summaries by leveraging APIMatic’s API.
- [riza-io/riza-mcp](https://github.com/riza-io/riza-mcp) - [Riza](https://riza.io) offers an isolated code interpreter for your LLM-generated code.
- [Boston343/starwind-ui-mcp](https://github.com/Boston343/starwind-ui-mcp) - This MCP provides relevant commands, documentation, and other information to allow LLMs to take full advantage of Starwind UI's open source Astro components.
- [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) - Model Context Protocol (MCP) is a [new, standardized protocol](https://modelcontextprotocol.io/introduction) for managing context between large language models (LLMs) and external systems. In this repository, we provide an installer as well as an MCP Server for [Cloudflare's API](https://api.cloudflare.com).
- [its-dart/dart-mcp-server](https://github.com/its-dart/dart-mcp-server) - <h1>Dart MCP Server</h1>
- [agentrpc/agentrpc](https://github.com/agentrpc/agentrpc) - > Universal RPC layer for AI agents across network boundaries and languages
- [yangkyeongmo/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) - A MCP Server that connects to [Apache Airflow](https://airflow.apache.org/) using official python client.
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) - This repository contains a Model Context Protocol (MCP) server with tools that can access the OpenTelemetry traces and
- [GongRzhe/JSON-MCP-Server](https://github.com/GongRzhe/JSON-MCP-Server) - JSON handling and processing server with advanced query capabilities using JSONPath syntax and support for array, string, numeric, and date operations.
- [hannesj/mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema) - Allow LLMs to explore large GraphQL schemas without bloating the context.
- [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) - Magic Component Platform (MCP) is a powerful AI-driven tool that helps developers create beautiful, modern UI components instantly through natural language descriptions. It integrates seamlessly with popular IDEs and provides a streamlined workflow for UI development.
- [shannonlal/mcp-postman](https://github.com/shannonlal/mcp-postman) - MCP server for running Postman Collections locally via Newman. Allows for simple execution of Postman Server and returns the results of whether the collection passed all the tests.
- [bigcodegen/mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server) - An MCP Server for your Neovim session.
- [rishikavikondala/mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws) - Perform operations on your AWS resources using an LLM.
- [ko1ynnky/github-actions-mcp-server](https://github.com/ko1ynnky/github-actions-mcp-server) - A Model Context Protocol (MCP) server for interacting with Github Actions.
- [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) - Integrate with Docker to manage containers, images, volumes, and networks.
- [shanejonas/openrpc-mpc-server](https://github.com/shanejonas/openrpc-mpc-server) - Interact with and discover JSON-RPC APIs via [OpenRPC](https://open-rpc.org/).
- [chargebee/agentkit](https://github.com/chargebee/agentkit) - MCP Server that connects AI agents to Chargebee platform.
- [ognis1205/mcp-server-unitycatalog](https://github.com/ognis1205/mcp-server-unitycatalog) - An MCP server that enables LLMs to interact with Unity Catalog AI, supporting CRUD operations on Unity Catalog Functions and executing them as MCP tools.
- [JetBrains/mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains) - The server proxies requests from client to JetBrains IDE.


### File Management

- [file-manager-python](https://github.com/anthropics/dxt/tree/main/examples/file-manager-python)

### System Tools

- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) - Integration with iTerm2 terminal emulator for macOS, enabling LLMs to execute and monitor terminal commands.
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) - Fast file searching capabilities across Windows (using [Everything SDK](https://www.voidtools.com/support/everything/sdk/)), macOS (using mdfind command), and Linux (using locate/plocate command).
- [kapilduraphe/okta-mcp-server](https://github.com/kapilduraphe/okta-mcp-server) - Interact with Okta API.
- [dvcrn/mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts) - MCP to interact with Siri Shortcuts on macOS. Exposes all Shortcuts as MCP tools.
- [SimonB97/win-cli-mcp-server](https://github.com/SimonB97/win-cli-mcp-server) - MCP server for secure command-line interactions on Windows systems, enabling controlled access to PowerShell, CMD, and Git Bash shells.
- [pathintegral-institute/mcp.science](https://github.com/pathintegral-institute/mcp.science) - A Model Context Protocol (MCP) server for executing command-line operations on remote servers via SSH.
- [GongRzhe/terminal-controller-mcp](https://github.com/GongRzhe/terminal-controller-mcp) - A MCP server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface.
- [MCP Team/servers](https://github.com/modelcontextprotocol/servers) - A Model Context Protocol server that provides time and timezone conversion capabilities. It automatically detects the system's timezone and offers tools for getting current time and converting between timezones.
- [dinghuazhou/sample-mcp-server-tos](https://github.com/dinghuazhou/sample-mcp-server-tos) - A sample MCP server for VolcEngine TOS that flexibly get objects from TOS.
- [ChristophEnglisch/keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol) - This MCP server enables natural language interaction with Keycloak for user and realm management including creating, deleting, and listing users and realms.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Secure file operations with configurable access controls
- [Descope/descope-mcp-server](https://github.com/descope-sample-apps/descope-mcp-server) - An MCP server to integrate with [Descope](https://descope.com/) to search audit logs, manage users, and more.

### Web Services

- [mendableai/firecrawl-mcp-server](https://github.com/mendableai/firecrawl-mcp-server) - Advanced web scraping with JavaScript rendering, PDF support, and smart rate limiting
- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) - Implementation of an MCP server for all [Apify Actors](https://apify.com/store).
- [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) - This MCP Server will help you run browser automation and webscraping using Playwright
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) - A server that flexibly fetches HTML, JSON, Markdown, or plaintext.
- [bharathvaj-ganesan/whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp) - MCP server that performs whois lookup against domain, IP, ASN and TLD.
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp) - This is a Python-based MCP server that provides OpenAI `web_search` build-in tool.
- [Omedia/mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal) - Server for interacting with [Drupal](https://www.drupal.org/project/mcp) using STDIO transport layer.
- [pathintegral-institute/mcp.science](https://github.com/pathintegral-institute/mcp.science) - A Model Context Protocol (MCP) server for fetching webpages including html/pdf/plain text type content.
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) - A Model Context Protocol (MCP) server lets AI assistants like Claude use the Exa AI Search API for web searches. This setup allows AI models to get real-time web information in a safe and controlled way.
- [cyberchitta/scrapling-fetch-mcp](https://github.com/cyberchitta/scrapling-fetch-mcp) - Access text content from bot-protected websites. Fetches HTML/markdown from sites with anti-automation measures using Scrapling.
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) - An MCP server for Apify's open-source RAG Web Browser [Actor](https://apify.com/apify/rag-web-browser) to perform web searches, scrape URLs, and return content in Markdown.
- [RamXX/mcp-tavily](https://github.com/RamXX/mcp-tavily) - An MCP server for Tavily's search & news API, with explicit site inclusions/exclusions
- [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) - Provides tools to search Airbnb and get listing details.
- [ihor-sokoliuk/mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng) - A Model Context Protocol Server for [SearXNG](https://docs.searxng.org/)
- [amap/amap-maps-mcp-server](https://www.npmjs.com/package/@amap/amap-maps-mcp-server) - MCP Server for the AMap Map API.
- [adenot/mcp-google-search](https://github.com/adenot/mcp-google-search) - Provides Google Search results via the Google Custom Search API
- [mfukushim/map-traveler-mcp](https://github.com/mfukushim/map-traveler-mcp) - Integrates Google Map, Google Street View, PixAI, Stability.ai, ComfyUI API and Bluesky to provide a virtual location simulation in LLM (written in Effect.ts)
- [pathintegral-institute/mcp.science](https://github.com/pathintegral-institute/mcp.science) - A Model Context Protocol (MCP) server for TXYZ Search API. Provides tools for academic and scholarly search, general web search, and smart search.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Location services, directions, and place details
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) - A Model Context Protocol (MCP) server that provides search and crawl functionality using Search1API.
- [leehanchung/bing-search-mcp](https://github.com/leehanchung/bing-search-mcp) - Server implementation for Microsoft Bing Web Search API.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Web and local search using Brave's Search API
- [pfldy2850/py-mcp-naver](https://github.com/pfldy2850/py-mcp-naver) - This MCP server provides tools to interact with various Naver services, such as searching blogs, news, books, and more.
- [sunsetcoder/flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server) - A Claude Desktop MCP server that helps you track flights in real-time using Flightradar24 data.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Browser automation and web scraping
- [fingertip-com/fingertip-mcp](https://github.com/fingertip-com/fingertip-mcp) - MCP server for Fingertip.com to search and create new sites.
- [delorenj/mcp-server-ticketmaster](https://github.com/delorenj/mcp-server-ticketmaster) - Search for events, venues, and attractions through the Ticketmaster Discovery API
- [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp) - Search engine for AI agents (search + extract) powered by Tavily
- [xxxbrian/mcp-rquest](https://github.com/xxxbrian/mcp-rquest) - An MCP server providing realistic browser-like HTTP request capabilities with accurate TLS/JA3/JA4 fingerprints for bypassing anti-bot measures.
- [hyperbrowserai/mcp](https://github.com/hyperbrowserai/mcp) - This is Hyperbrowser's Model Context Protocol (MCP) Server. It provides various tools to scrape, extract structured data, and crawl webpages. It also provides easy access to general purpose browser agents like OpenAI's CUA, Anthropic's Claude Computer Use, and Browser Use.
- [VectorInstitute/mcp-goodnews](https://github.com/VectorInstitute/mcp-goodnews) - A simple MCP server that delivers curated positive and uplifting news stories.
- [oxylabs/oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp) - A Model Context Protocol (MCP) server that enables AI assistants like Claude to seamlessly access web data through Oxylabs' powerful web scraping technology.
- [ppl-ai/modelcontextprotocol](https://github.com/ppl-ai/modelcontextprotocol) - An MCP server implementation that integrates the Sonar API to provide Claude with unparalleled real-time, web-wide research.
- [AshDevFr/discourse-mcp-server](https://github.com/AshDevFr/discourse-mcp-server) - A MCP server to search Discourse posts on a Discourse forum.
- [tinyfish-io/agentql-mcp](https://github.com/tinyfish-io/agentql-mcp) - This is a Model Context Protocol (MCP) server that integrates [AgentQL](https://agentql.com)'s data extraction capabilities.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) - A Model Context Protocol (MCP) server that provides browser automation capabilities using [Playwright](https://playwright.dev). This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - A Model Context Protocol server that provides web content fetching capabilities.

### Messaging

- [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) - The MCP server that interacts with RabbitMQ to publish and consume messages.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Channel management and messaging capabilities
- [vidhupv/x-mcp](https://github.com/vidhupv/x-mcp) - Create, manage and publish X/Twitter posts directly through Claude chat.
- [GongRzhe/Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server) - A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support.
- [teddyzxcv/ntfy-mcp](https://github.com/teddyzxcv/ntfy-mcp) - The MCP server that keeps you informed by sending the notification on phone using ntfy
- [ashiknesin/pushover-mcp](https://github.com/ashiknesin/pushover-mcp) - Send instant notifications to your devices using [Pushover.net](https://pushover.net/)
- [carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) - An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.
- [Zilong Xue/claude-post](https://github.com/ZilongXue/claude-post) - ClaudePost enables seamless email management for Gmail, offering secure features like email search, reading, and sending.
- [raoulbia-ai/mcp-server-for-intercom](https://github.com/raoulbia-ai/mcp-server-for-intercom) - An MCP-compliant server for retrieving customer support tickets from Intercom. This tool enables AI assistants like Claude Desktop and Cline to access and analyze your Intercom support tickets.
- [v-3/discordmcp](https://github.com/v-3/discordmcp) - A MCP server to connect to Discord guilds through a bot and read and write messages in channels
- [idoubi/mcp-server-chatsum](https://github.com/mcpso/mcp-server-chatsum) - Query and Summarize chat messages with LLM. by [mcpso](https://mcp.so/)

### Databases

- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) - An MCP server for ClickHouse.
- [meilisearch/meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp) - A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces like Claude.
- [prajwalnayak7/mcp-server-redis](https://github.com/prajwalnayak7/mcp-server-redis) - MCP server to interact with Redis Server, AWS Memory DB, etc for caching or other use-cases where in-memory and key-value based storage is appropriate
- [privetin/chroma](https://github.com/privetin/chroma) - Vector database server for semantic document search and metadata filtering, built on Chroma
- [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) - Server to interact with Firebase services including Firebase Authentication, Firestore, and Firebase Storage.
- [abel9851/mcp-server-mariadb](https://github.com/abel9851/mcp-server-mariadb) - MariaDB database integration with configurable access controls in Python.
- [singlestore-labs/mcp-server-singlestore](https://github.com/singlestore-labs/mcp-server-singlestore) - Interact with the SingleStore database platform
- [XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server) - An MCP server that supports fetching data from a database using natural language queries, powered by XiyanSQL as the text-to-SQL LLM.
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) - This server enables running Cypher graph queries, analyzing complex domain data, and automatically generating business insights that can be enhanced with Claude's analysis when an Anthropic API key is provided.
- [vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server) - A Model Context Protocol (MCP) server implementation that integrates with [Vectorize](https://vectorize.io/) for advanced Vector retrieval and text extraction.
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) - MySQL database integration in Python with configurable access controls and schema inspection
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Read-only database access with schema inspection
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) - A Model Context Protocol (MCP) server implementation for [GreptimeDB](https://github.com/GreptimeTeam/greptimedb).
- [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone) - MCP server for searching and uploading records to Pinecone. Allows for simple RAG features, leveraging Pinecone's Inference API.
- [furey/mongodb-lens](https://github.com/furey/mongodb-lens) - Full Featured MCP Server for MongoDB Databases.
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) - Server implementation for Google BigQuery integration that enables direct BigQuery database access and querying capabilities
- [lloydzhou/bitable-mcp](https://github.com/lloydzhou/bitable-mcp) - MCP server provides access to Lark Bitable through the Model Context Protocol. It allows users to interact with Bitable tables using predefined tools.
- [StarRocks/mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks) - The StarRocks MCP Server acts as a bridge between AI assistants and StarRocks databases, allowing for direct SQL execution and database exploration without requiring complex setup or configuration.
- [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) - Embeddings, vector search, document storage, and full-text search with the open-source AI application database
- [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) - Run queries against InfluxDB OSS API v2.
- [JexinSam/mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server) - MCP Server for MSSQL database in Python
- [pab1it0/adx-mcp-server](https://github.com/pab1it0/adx-mcp-server) - Query and analyze Azure Data Explorer databases.
- [motherduckdb/mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck) - Query and analyze data with MotherDuck and local DuckDB
- [bytebase/dbhub](https://github.com/bytebase/dbhub) - Universal database MCP server connecting to MySQL, PostgreSQL, SQLite, DuckDB and etc.
- [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) - This repository is an example of how to create a MCP server for Qdrant, a vector search engine.
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) - A Model Context Protocol Server for MongoDB.
- [lishenxydlgzs/aws-athena-mcp](https://github.com/lishenxydlgzs/aws-athena-mcp) - A MCP server for AWS Athena to run SQL queries on Glue Catalog.
- [yuanoOo/oceanbase_mcp_server](https://github.com/yuanoOo/oceanbase_mcp_server) - (by yuanoOo) A Model Context Protocol (MCP) server that enables secure interaction with OceanBase databases.
- [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) - This MCP server enables LLMs to interact with Snowflake databases, allowing for secure and controlled data operations.
- [da-okazaki/mcp-neo4j-server](https://github.com/da-okazaki/mcp-neo4j-server) - A community built server that interacts with Neo4j Graph Database.
- [zilliztech/mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus) - This repository contains a MCP server that provides access to Milvus vector database functionality.
- [ravenwits/mcp-server-arangodb](https://github.com/ravenwits/mcp-server-arangodb) - MCP Server that provides database interaction capabilities through [ArangoDB](https://arangodb.com/).
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) - MCP server implementation that provides Elasticsearch interaction.
- [Aiven-Open/mcp-aiven](https://github.com/Aiven-Open/mcp-aiven) - A [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server for Aiven.
- [felores/airtable-mcp](https://github.com/felores/airtable-mcp) - Airtable Model Context Protocol Server.
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) - Neo4j graph database server (schema + read/write-cypher) and separate graph database backed memory
- [oceanbase/mcp-oceanbase](https://github.com/oceanbase/mcp-oceanbase) - MCP Server for OceanBase database and its tools
- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) - Interact with an Apache Unomi CDP customer data platform to retrieve and update customer profiles
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) - Neo4j graph database server (schema + read/write-cypher) and separate graph database backed memory
- [suhail-ak-s/mcp-typesense-server](https://github.com/suhail-ak-s/mcp-typesense-server) - A Model Context Protocol (MCP) server implementation that provides AI models with access to Typesense search capabilities. This server enables LLMs to discover, search, and analyze data stored in Typesense collections.

### Analytics

- [aarora79/aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server) - Optimize your AWS spend (including Amazon Bedrock spend) with this MCP server by examining spend across regions, services, instance types and foundation models ([demo video](https://www.youtube.com/watch?v=WuVOmYLRFmI&feature=youtu.be)).
- [lenwood/cfbd-mcp-server](https://github.com/lenwood/cfbd-mcp-server) - An MCP server for the [College Football Data API](https://collegefootballdata.com/).
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) - Interface with the Rijksmuseum API to search artworks, retrieve artwork details, access image tiles, and explore user collections.
- [OctagonAI/octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server) - A Model Context Protocol (MCP) server implementation that integrates with Octagon Market Intelligence API.
- [jjsantos01/qgis_mcp](https://github.com/jjsantos01/qgis_mcp) - connects QGIS to Claude AI through the MCP. This integration enables prompt-assisted project creation, layer loading, code execution, and more.
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) - An MCP server to interact with a Tinybird Workspace from any MCP client.
- [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) - Query and analyze Prometheus - open-source monitoring system.
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp) - Give your coding agent direct access to up-to date Fantasy Premier League data
- [keboola/keboola-mcp-server](https://github.com/keboola/keboola-mcp-server) - <a href="https://glama.ai/mcp/servers/72mwt1x862"><img width="380" height="200" src="https://glama.ai/mcp/servers/72mwt1x862/badge" alt="Keboola Explorer Server MCP server" /></a>
- [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) - MCP server for autonomous data exploration on .csv-based datasets, providing intelligent insights with minimal effort. NOTE: Will execute arbitrary Python code on your machine, please use with caution!
- [privetin/dataset-viewer](https://github.com/privetin/dataset-viewer) - Browse and analyze Hugging Face datasets with features like search, filtering, statistics, and data export
- [asusevski/opendota-mcp-server](https://github.com/asusevski/opendota-mcp-server) - Interact with OpenDota API to retrieve Dota 2 match data, player statistics, and more.
- [syucream/lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server) - Interact with [Lightdash](https://www.lightdash.com/), a BI tool.
- [kagisearch/kagimcp](https://github.com/kagisearch/kagimcp) - <a href="https://glama.ai/mcp/servers/xabrrs4bka">

### AI Systems

- [DMontgomery40/deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server) - Model Context Protocol server integrating DeepSeek's advanced language models, in addition to [other useful API endpoints](https://github.com/DMontgomery40/deepseek-mcp-server?tab=readme-ov-file#features)
- [ruixingshi/deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp) - A MCP (Model Context Protocol) provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's thought processes from the Deepseek API service or from a local Ollama server.
- [YanxingLiu/dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server) - A simple implementation of an MCP server for dify workflows.
- [thirdweb-dev/ai](https://github.com/thirdweb-dev/ai) - Read/write to over 2k blockchains, enabling data querying, contract analysis/deployment, and transaction execution, powered by Thirdweb
- [whataboutyou-ai/eunomia-MCP-server](https://github.com/whataboutyou-ai/eunomia-MCP-server) - Extension of the Eunomia framework that connects Eunomia instruments with MCP servers
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - Interact with any OpenAI SDK Compatible Chat Completions API like OpenAI, Perplexity, Groq, xAI and many more.
- [deepfates/mcp-replicate](https://github.com/deepfates/mcp-replicate) - Search, run and manage machine learning models on Replicate through a simple tool-based interface. Browse models, create predictions, track their status, and handle generated images.
- [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) - Server for using HuggingFace Spaces, supporting Open Source Image, Audio, Text Models and more. Claude Desktop mode for easy integration.
- [66julienmartin/MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1) - A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Dynamic and reflective problem-solving through thought sequences
- [66julienmartin/MCP-server-Qwen_Max](https://github.com/66julienmartin/MCP-server-Qwen_Max) - A Model Context Protocol (MCP) server implementation for the Qwen models.

### MCP Tools

- [unifai-network/unifai-mcp-server](https://github.com/unifai-network/unifai-mcp-server) - Dynamically search and call tools using UnifAI Network
- [tesla0225/mcp-create](https://github.com/tesla0225/mcp-create) - A dynamic MCP server management service that creates, runs, and manages Model Context Protocol servers on-the-fly.
- [liuyoshio/mcp-compass](https://github.com/liuyoshio/mcp-compass) - Suggest the right MCP server for your needs
- [AIQL/chat-mcp](https://github.com/AI-QL/chat-mcp) - – An Open Source Cross-platform GUI Desktop application compatible with Linux, macOS, and Windows, enabling seamless interaction with MCP servers across dynamically selectable LLMs, by **[AIQL](https://github.com/AI-QL/chat-mcp)**
- [pathintegral-institute/mcp.science](https://github.com/pathintegral-institute/mcp.science) - A MCP (Model Context Protocol) server that interacts with the Materials Project database, allowing for material search, structure visualization, and manipulation.
- [e2b-dev/mcp-server](https://github.com/e2b-dev/mcp-server) - This repository contains the source code for the [E2B](https://e2b.dev) MCP server.
- [ChronulusAI/chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp) - <img width="150px" src="https://www.chronulus.com/brand-assets/chronulus-logo-blue-on-alpha-square.png" alt="Chronulus AI">
- [fastnai/mcp-fastn](https://github.com/fastnai/mcp-fastn) - A remote, dynamic MCP server with a unified API that connects to 1,000+ tools, actions, and workflows, featuring built-in authentication and monitoring.
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) - Connect to MCP servers that run on SSE transport, or expose stdio servers as an SSE server.
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) - This server is a server that installs other MCP servers for you.
- [MCP Team/servers](https://github.com/modelcontextprotocol/servers) - This MCP server exercises all the features of the MCP protocol. It is a test server for builders of MCP clients.
- [integration-app/mcp-server](https://github.com/integration-app/mcp-server) - This is an implementation of the [Model Context Protocol (MCP) server](https://modelcontextprotocol.org/) that exposes tools powered by [Integration App](https://integration.app).

### Knowledge Base

- [anshumax/world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server) - A server that fetches data indicators available with the World Bank as part of their data API
- [nkapila6/mcp-local-rag](https://github.com/nkapila6/mcp-local-rag) - "primitive" RAG-like web search model context protocol (MCP) server that runs locally using Google's MediaPipe Text Embedder and DuckDuckGo Search. ✨ no APIs required ✨.
- [skydeckai/mcp-server-rememberizer](https://github.com/skydeckai/mcp-server-rememberizer) - An MCP server designed for interacting with the Rememberizer data source, facilitating enhanced knowledge retrieval.
- [GongRzhe/Langflow-DOC-QA-SERVER](https://github.com/GongRzhe/Langflow-DOC-QA-SERVER) - A Model Context Protocol server for document Q&A powered by Langflow. It demonstrates core MCP concepts by providing a simple interface to query documents through a Langflow backend.
- [rember/rember-mcp](https://github.com/rember/rember-mcp) - Create spaced repetition flashcards in Rember to remember anything you learn in your chats
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Retrieval from AWS Knowledge Base using Bedrock Agent Runtime
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Knowledge graph-based persistent memory system
- [kpsunil97/devrev-mcp-server](https://github.com/kpsunil97/devrev-mcp-server) - An MCP server to integrate with DevRev APIs to search through your DevRev Knowledge Graph where objects can be imported from diff. sources listed [here](https://devrev.ai/docs/import#available-sources).
- [apeyroux/mcp-xmind](https://github.com/apeyroux/mcp-xmind) - Read and search through your XMind directory containing XMind files.
- [aws-samples/sample-mcp-server-s3](https://github.com/aws-samples/sample-mcp-server-s3) - A sample MCP server for AWS S3 that flexibly fetches objects from S3 such as PDF documents.
- [graphlit/graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) - The Model Context Protocol (MCP) Server enables integration between MCP clients and the Graphlit service. This document outlines the setup process and provides a basic example of using the client.
- [run-llama/mcp-server-llamacloud](https://github.com/run-llama/mcp-server-llamacloud) - Integrate the data stored in a managed index on [LlamaCloud](https://cloud.llamaindex.ai/)
- [kiwamizamurai/mcp-kibela-server](https://github.com/kiwamizamurai/mcp-kibela-server) - Interact with Kibela API.
- [StevenStavrakis/obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) - (by Steven Stavrakis) An MCP server for Obsidian.md with tools for searching, reading, writing, and organizing notes.
- [adityak74/mcp-scholarly](https://github.com/adityak74/mcp-scholarly) - A MCP server to search for scholarly and academic articles.
- [scorzeth/anki-mcp-server](https://github.com/scorzeth/anki-mcp-server) - An MCP server for interacting with your [Anki](https://apps.ankiweb.net/) decks and cards.
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) - Read and search through your Obsidian vault or any directory containing Markdown notes
- [dmayboroda/minima](https://github.com/dmayboroda/minima) - MCP server for RAG on local files
- [longyi1207/glean-mcp-server](https://github.com/longyi1207/glean-mcp-server) - A server that uses Glean API to search and chat.
- [needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp) - MCP (Model Context Protocol) server to manage documents and perform searches using [Needle](https://needle-ai.com) through Claude’s Desktop Application.
- [Unstructured-IO/UNS-MCP](https://github.com/Unstructured-IO/UNS-MCP) - An MCP server implementation for interacting with the Unstructured API. This server provides tools to list sources and workflows.
- [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) - Local-first knowledge management system that builds a semantic graph from Markdown files, enabling persistent memory across conversations with LLMs.
- [box-community/mcp-server-box](https://github.com/box-community/mcp-server-box) - MCP Server Box is a Python project that integrates with the Box API to perform various operations such as file search, text extraction, AI-based querying, and data extraction. It leverages the `box-sdk-gen` library and provides a set of tools to interact with Box files and folders.
- [Spathodea-Network/opencti-mcp](https://github.com/Spathodea-Network/opencti-mcp) - Interact with OpenCTI platform to retrieve threat intelligence data including reports, indicators, malware and threat actors.
- [hungryrobot1/MCP-PIF](https://github.com/hungryrobot1/MCP-PIF) - A Personal Intelligence Framework (PIF), providing tools for file operations, structured reasoning, and journal-based documentation to support continuity and evolving human-AI collaboration across sessions.
- [ProgramComputer/NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server) - Access to a unified gateway of NASA's data sources including but not limited to APOD, NEO, EPIC, GIBS.

### Media Creation

- [felores/placid-mcp-server](https://github.com/felores/placid-mcp-server) - Generate image and video creatives using Placid.app templates
- [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) - Comprehensive YouTube API integration for video management, Shorts creation, and analytics.
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) - A server that generates mindmaps from input containing markdown code.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - AI image generation using various models
- [mamertofabian/elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server) - A server that integrates with ElevenLabs text-to-speech API capable of generating full voiceovers with multiple voices.
- [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) - Blender integration allowing prompt enabled 3D scene creation, modeling and manipulation.
- [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) - This MCP allows an LLM to play and use Spotify.
- [GongRzhe/Image-Generation-MCP-Server](https://github.com/GongRzhe/Image-Generation-MCP-Server) - This MCP server provides image generation capabilities using the Replicate Flux model.
- [zcaceres/mcp-markdownify-server](https://github.com/zcaceres/mcp-markdownify-server) - MCP to convert almost anything to Markdown (PPTX, HTML, PDF, Youtube Transcripts and more)
- [GongRzhe/Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server) - A Model Context Protocol server for generating charts using QuickChart.io
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) - A Model Context Protocol Server to add, edit, and search videos with [Video Jungle](https://www.video-jungle.com/).
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) - Generate visualizations from fetched data using the VegaLite format and renderer.
- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) - An MCP server that enables LLMs to interact with Unity3d Game Engine, supporting access to a variety of the Unit's Editor engine tools (e.g. Console Logs, Test Runner logs, Editor functions, hierarchy state, etc) and executing them as MCP tools or gather them as resources.
- [felores/cloudinary-mcp-server](https://github.com/felores/cloudinary-mcp-server) - Cloudinary Model Context Protocol Server to upload media to Cloudinary and get back the media link and details.
- [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) - MCP server for seamless document format conversion using Pandoc, supporting Markdown, HTML, PDF, DOCX (.docx), csv and more.
- [dschuler36/reaper-mcp-server](https://github.com/dschuler36/reaper-mcp-server) - Interact with your [Reaper](https://www.reaper.fm/) (Digital Audio Workstation) projects.
- [quazaai/UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration) - Advanced Unity3d Game Engine MCP which supports ,Execution of Any Editor Related Code Directly Inside of Unity, Fetch Logs, Get Editor State and Allow File Access of the Project making it much more useful in Script Editing or asset creation.
- [Coding Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) - A MCP server providing comprehensive Godot engine integration for project editing, debugging, and scene management.

### Productivity

- [Fibery-inc/fibery-mcp-server](https://github.com/Fibery-inc/fibery-mcp-server) - This MCP (Model Context Protocol) server provides integration between Fibery and any LLM provider supporting the MCP protocol (e.g., Claude for Desktop), allowing you to interact with your Fibery workspace using natural language.
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) - Read, update, delete, publish content in your [Contentful](https://contentful.com/) space(s) from this MCP Server.
- [jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) - Allows LLM to interact with Linear's API for project management, including searching, creating, and updating issues.
- [osomai/servicenow-mcp](https://github.com/osomai/servicenow-mcp) - A MCP server to interact with a ServiceNow instance
- [integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) - A Model Context Protocol server that enables Make scenarios to be utilized as tools by AI assistants. This integration allows AI systems to trigger and interact with your Make automation workflows.
- [sakce/mcp-server-monday](https://github.com/sakce/mcp-server-monday) - MCP Server to interact with Monday.com boards and items.
- [smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) - Interact with Salesforce Data and Metadata
- [syucream/holaspirit-mcp-server](https://github.com/syucream/holaspirit-mcp-server) - Interact with [Holaspirit](https://www.holaspirit.com/).
- [devhub/devhub-cms-mcp](https://github.com/devhub/devhub-cms-mcp) - Manage and utilize website content within the DevHub CMS platform
- [abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server) - Interact with Todoist to manage your tasks.
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) - Interact with Atlassian Cloud products (Confluence and Jira) including searching/reading Confluence spaces/pages, accessing Jira issues, and project metadata.
- [open-strategy-partners/osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools) - Content editing codes, value map, and positioning tools for product marketing.
- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) - Google Tasks API Model Context Protocol Server.
- [esignaturescom/mcp-server-esignatures](https://github.com/esignaturescom/mcp-server-esignatures) - MCP server for eSignatures (https://esignatures.com)
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - File access and search capabilities for Google Drive
- [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) - Excel manipulation including data reading/writing, worksheet management, formatting, charts, and pivot table.
- [v-3/notion-server](https://github.com/v-3/notion-server) - Notion MCP integration. Search, Read, Update, and Create pages through Claude chat.
- [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) - Google Calendar MCP Server for managing Google calendar events. Also supports searching for events by attributes like title and location.
- [hichana/goalstory-mcp](https://github.com/hichana/goalstory-mcp) - a Goal Tracker and Visualization Tool for personal and professional development.
- [horizondatawave/hdw-mcp-server](https://github.com/horizondatawave/hdw-mcp-server) - Access to profile data and management of user account with [HorizonDataWave.ai](https://horizondatawave.ai/).
- [kenjihikmatullah/productboard-mcp](https://github.com/kenjihikmatullah/productboard-mcp) - Integrate the Productboard API into agentic workflows via MCP.

### Professional Apps

- [GongRzhe/TRAVEL-PLANNER-MCP-Server](https://github.com/GongRzhe/TRAVEL-PLANNER-MCP-Server) - Travel planning and itinerary management server integrating with Google Maps API for location search, place details, and route calculations.
- [Laksh-star/mcp-server-tmdb](https://github.com/Laksh-star/mcp-server-tmdb) - This MCP server integrates with The Movie Database (TMDB) API to provide movie information, search capabilities, and recommendations.
- [ChristianHinge/dicom-mcp](https://github.com/ChristianHinge/dicom-mcp) - An MCP server to query and retrieve medical images and for parsing and reading dicom-encapsulated documents (pdf etc.).
- [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) - Give your coding agent direct access to Figma file data, helping it one-shot design implementation.
- [MFYDev/ghost-mcp](https://github.com/MFYDev/ghost-mcp) - A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude.
- [kapilduraphe/webflow-mcp-server](https://github.com/kapilduraphe/webflow-mcp-server) - Interfact with the Webflow APIs
- [r-huijts/ns-mcp-server](https://github.com/r-huijts/ns-mcp-server) - Access Dutch Railways (NS) real-time train travel information and disruptions through the official NS API.

### Finance

- [Kukapay/dune-analytics-mcp](https://github.com/kukapay/dune-analytics-mcp) - A mcp server that bridges Dune Analytics data to AI agents.
- [magnetai/mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer) - Send USDC on [Base](https://base.org/) for free using Claude AI! Built with [Coinbase CDP](https://docs.cdp.coinbase.com/mpc-wallet/docs/welcome).
- [calvernaz/alphavantage](https://github.com/calvernaz/alphavantage) - MCP server for stock market data API [AlphaVantage](https://www.alphavantage.co/)
- [KukaPay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) - Providing real-time and historical Crypto Fear & Greed Index data.
- [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) - A powerful and efficient Blockchain address risk scoring API MCP Server, leveraging the BICScan API to provide comprehensive risk assessments and asset information for blockchain addresses, domains, and decentralized applications (dApps).
- [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) - A mcp server for tracking cryptocurrency whale transactions.
- [john-zhang-dev/xero-mcp](https://github.com/john-zhang-dev/xero-mcp) - Enabling clients to interact with Xero system for streamlined accounting, invoicing, and business operations.
- [ramp-public/ramp-mcp](https://github.com/ramp-public/ramp-mcp) - A Model Context Protocol server for retrieving and analyzing data or running tasks for [Ramp](https://ramp.com) using [Developer API](https://docs.ramp.com/developer-api/v1/overview/introduction). In order to get around token and input size limitations, this server implements a simple ETL pipeline + ephemeral sqlite database in memory for analysis by an LLM. All requests are made to demo by default, but can be changed by setting `RAMP_ENV=prd`. Large datasets may not be processable due to API and/or your MCP client limitations.
- [stripe/agent-toolkit](https://github.com/stripe/agent-toolkit) - The Stripe Model Context Protocol server allows you to integrate with Stripe APIs through function calling. This protocol supports various tools to interact with different Stripe services.
- [Adfin-Engineering/mcp-server-adfin](https://github.com/Adfin-Engineering/mcp-server-adfin) - 1. Python 3.10 or higher
- [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) - Providing latest cryptocurrency news to AI agents, powered by CryptoPanic.
- [Fewsats/fewsats-mcp](https://github.com/Fewsats/fewsats-mcp) - This MCP server integrates with [Fewsats](https://fewsats.com) and allows AI Agents to purchase anything in a secure way.
- [Heurist Network/heurist-mesh-mcp-server](https://github.com/heurist-network/heurist-mesh-mcp-server) - Access specialized web3 AI agents for blockchain analysis, smart contract security, token metrics, and blockchain interactions through the [Heurist Mesh network](https://github.com/heurist-network/heurist-agent-framework/tree/main/mesh).
- [GoPlausible/algorand-mcp](https://github.com/GoPlausible/algorand-mcp) - A comprehensive MCP server for tooling interactions (40+) and resource accessibility (60+) plus many useful prompts for interacting with the Algorand blockchain.
- [longmans/coin_api_mcp](https://github.com/longmans/coin_api_mcp) - Provides access to [coinmarketcap](https://coinmarketcap.com/) cryptocurrency data.
- [bankless/onchain-mcp](https://github.com/bankless/onchain-mcp) - MCP (Model Context Protocol) server for blockchain data interaction through the Bankless API.
- [mektigboy/server-hyperliquid](https://github.com/mektigboy/server-hyperliquid) - An MCP server implementation that integrates the Hyperliquid SDK for exchange data.
- [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) - Comprehensive blockchain services for 30+ EVM networks, supporting native tokens, ERC20, NFTs, smart contracts, transactions, and ENS resolution.
- [marctheshark3/ergo-mcp](https://github.com/marctheshark3/ergo-mcp) - -An MCP server to integrate Ergo Blockchain Node and Explorer APIs for checking address balances, analyzing transactions, viewing transaction history, performing forensic analysis of addresses, searching for tokens, and monitoring network status.
- [XeroAPI/xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server) - This is a Model Context Protocol (MCP) server implementation for Xero. It provides a bridge between the MCP protocol and Xero's API, allowing for standardized access to Xero's accounting and business features.

### examples

- [hello-world-node](https://github.com/anthropics/dxt/tree/main/examples/hello-world-node) - Basic MCP server with simple time tool
- [Blender](./servers/blender-mcp) - Blender Model Context Protocol Integration

```json
{
  "dxt_version": "0.1",
  "name": "blender-mcp",
  "display_name": "Blender",
  "version": "1.2",
  "description": "Blender Model Context Protocol Integration",
  "author": {
    "name": "ahujasid"
  },
  "server": {
    "type": "python",
    "entry_point": "main.py",
    "mcp_config": {
      "command": "uvx",
      "args": [
        "blender-mcp@1.2"
      ]
    }
  },
  "license": "MIT"
}
```

## Packaging & Management Tools
- [mcp-linker](https://github.com/milisp/mcp-linker) - Cross-platform MCP management tool with planned .dxt support 🚀
- [@anthropic-ai/dxt](https://www.npmjs.com/package/@anthropic-ai/dxt) - Official packaging toolkit

## About
Curated by [@milisp](https://github.com/milisp) | Author of [mcp-linker](https://github.com/milisp/mcp-linker)

## Community Resources
- [r/dxt on Reddit](https://www.reddit.com/r/dxt) – Community discussions, help, and showcase

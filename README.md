# E-Commerce Data Analytics & Architectural Insights

## Project Overview
This repository contains a comprehensive data analysis of a Brazilian e-commerce dataset. The project goes beyond standard reporting by extracting actionable business insights and translating them into technical system design recommendations. It evaluates over 98K orders, analyzing unit economics, fulfillment pipelines, and customer behavior to inform scalable architecture, data engineering practices, and business logic.

## Tech Stack
* **Data Processing:** Python (Pandas, NumPy)
* **Visualization:** Power BI (`dashboard.pbix`)
* **Domain:** E-commerce, Supply Chain Logistics, Payment Gateways

## Repository Structure
| Directory/File | Description |
| :--- | :--- |
| `pyscripts/` | Python scripts for data extraction, cleaning, and transformation. |
| `img/` | Exported dashboard visualizations (Executive Overview, Key Insights, Orders & Payments). |
| `dashboard.pbix` | Interactive Power BI dashboard containing the semantic model and DAX measures. |
| `README.md` | Project documentation. |

## Core Business Metrics
* **Gross Merchandise Value (GMV):** 14.12M (Order Value) vs 32.02M (Payment Value)
* **Transaction Volume:** 98.67K Orders | 116.87K Items Sold (~1.18 items/order)
* **Profitability:** 36.20% Average Profit Margin
* **Payments:** Credit Card (78.34%) and Boleto (17.92%) dominate the transaction flow.

## Architectural & System Design Implications
The data reveals several patterns that directly dictate how the underlying e-commerce platform should be architected for scale and reliability:

### 1. The Pareto Distribution (Traffic & Inventory)
* **Observation:** The top 20% of products generate 60–70% of total revenue.
* **Engineering Action:** Implement aggressive distributed caching (e.g., Redis or Memcached) for high-velocity SKUs to reduce database read replica load during peak traffic. Configure automated, low-latency inventory restock alerts for these specific items.

### 2. Retention & Customer Data
* **Observation:** Returning customers yield significantly higher Lifetime Value (LTV).
* **Engineering Action:** Architecture must support a robust Customer Data Platform (CDP). Optimize the "Order History" and "One-Click Reorder" microservices for sub-100ms latency to reduce friction in the loyalty loop.

### 3. Fulfillment State Machine
* **Observation:** High concentration of demand in SP, RJ, and MG, with isolated anomalies in delivery rates.
* **Engineering Action:** Decentralize warehousing to "edge fulfillment" centers in high-density states. Audit the webhook integrations with shipping carriers; lagging or missing delivery statuses indicate a silent failure in the event-driven architecture handling order state transitions.

### 4. Data Pipeline Integrity
* **Observation:** The dashboard reports `0.00` total discount across ~100k orders, and a massive discrepancy between Order Value (14.12M) and Payment Value (32.02M).
* **Engineering Action:** These are red flags for data pipeline health. The ETL/ELT process requires refactoring to ensure taxes, freight, and installments are correctly normalized and not double-counted. Implement strict null-handling (e.g., COALESCE) for metric calculations.

## Future Roadmap
* **Data Quality Monitoring:** Implement anomaly detection in the ingestion layer to catch missing discount applications or payment value mismatches before they reach the reporting layer.
* **Dynamic Pricing Engine:** Develop a pricing algorithm that calculates the optimal discount threshold to maximize sales volume without breaching the 36% margin baseline.
* **Predictive Auto-Scaling:** Utilize the identified seasonal trends to configure predictive auto-scaling policies for the clusters hosting the checkout and payment microservices ahead of peak load events.

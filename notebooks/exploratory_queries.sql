-- ============================================
-- N100 Financial Intelligence Platform
-- Sprint 1 - Exploratory SQL Queries
-- ============================================

-- 1. Total Companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. Companies by Sector
SELECT broad_sector, COUNT(*) AS total_companies
FROM sectors
GROUP BY broad_sector
ORDER BY total_companies DESC;

-- 3. Top 10 Companies by Market Capitalization
SELECT company_id, market_cap_crore
FROM market_cap
ORDER BY market_cap_crore DESC
LIMIT 10;

-- 4. Average PE Ratio
SELECT ROUND(AVG(pe_ratio),2) AS average_pe_ratio
FROM market_cap;

-- 5. Top ROE Companies
SELECT company_id,
       return_on_equity_pct
FROM financial_ratios
ORDER BY return_on_equity_pct DESC
LIMIT 10;

-- 6. Highest Debt Companies
SELECT company_id,
       total_debt_cr
FROM financial_ratios
ORDER BY total_debt_cr DESC
LIMIT 10;

-- 7. Highest Dividend Yield
SELECT company_id,
       dividend_yield_pct
FROM market_cap
ORDER BY dividend_yield_pct DESC
LIMIT 10;

-- 8. Average Free Cash Flow
SELECT ROUND(AVG(free_cash_flow_cr),2)
FROM financial_ratios;

-- 9. Highest Closing Price
SELECT company_id,
       MAX(close_price)
FROM stock_prices
GROUP BY company_id;

-- 10. Total Trading Volume
SELECT SUM(volume)
FROM stock_prices;
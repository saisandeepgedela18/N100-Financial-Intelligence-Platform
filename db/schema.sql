PRAGMA foreign_keys = ON;

-- Companies
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    ticker TEXT UNIQUE,
    sector TEXT,
    industry TEXT,
    isin TEXT
);

-- Profit & Loss
CREATE TABLE IF NOT EXISTS profitandloss (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    year INTEGER,
    sales REAL,
    operating_profit REAL,
    net_profit REAL,
    eps REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Balance Sheet
CREATE TABLE IF NOT EXISTS balancesheet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    year INTEGER,
    assets REAL,
    liabilities REAL,
    equity REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Cash Flow
CREATE TABLE IF NOT EXISTS cashflow (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    year INTEGER,
    operating_cashflow REAL,
    investing_cashflow REAL,
    financing_cashflow REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Analysis
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    remarks TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Documents
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    document_name TEXT,
    url TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Pros & Cons
CREATE TABLE IF NOT EXISTS prosandcons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    type TEXT,
    description TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Sectors
CREATE TABLE IF NOT EXISTS sectors (
    sector_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sector_name TEXT UNIQUE
);

-- Stock Prices
CREATE TABLE IF NOT EXISTS stock_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    trade_date TEXT,
    open_price REAL,
    high_price REAL,
    low_price REAL,
    close_price REAL,
    volume INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Financial Ratios
CREATE TABLE IF NOT EXISTS financial_ratios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    year INTEGER,
    roe REAL,
    roce REAL,
    debt_equity REAL,
    current_ratio REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Peer Groups
CREATE TABLE IF NOT EXISTS peer_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    peer_company TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);
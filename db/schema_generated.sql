
-- ANALYSIS
CREATE TABLE IF NOT EXISTS analysis (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    compounded_sales_growth TEXT,
    compounded_profit_growth TEXT,
    stock_price_cagr TEXT,
    roe TEXT
);


-- BALANCESHEET
CREATE TABLE IF NOT EXISTS balancesheet (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    equity_capital TEXT,
    reserves TEXT,
    borrowings TEXT,
    other_liabilities TEXT,
    total_liabilities TEXT,
    fixed_assets TEXT,
    cwip TEXT,
    investments TEXT,
    other_asset TEXT,
    total_assets TEXT
);


-- CASHFLOW
CREATE TABLE IF NOT EXISTS cashflow (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    operating_activity TEXT,
    investing_activity TEXT,
    financing_activity TEXT,
    net_cash_flow TEXT
);


-- COMPANIES
CREATE TABLE IF NOT EXISTS companies (
    id TEXT PRIMARY KEY,
    company_logo TEXT,
    company_name TEXT,
    chart_link TEXT,
    about_company TEXT,
    website TEXT,
    nse_profile TEXT,
    bse_profile TEXT,
    face_value TEXT,
    book_value TEXT,
    roce_percentage TEXT,
    roe_percentage TEXT
);


-- DOCUMENTS
CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    annual_report TEXT
);


-- FINANCIAL_RATIOS
CREATE TABLE IF NOT EXISTS financial_ratios (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    net_profit_margin_pct TEXT,
    operating_profit_margin_pct TEXT,
    return_on_equity_pct TEXT,
    debt_to_equity TEXT,
    interest_coverage TEXT,
    asset_turnover TEXT,
    free_cash_flow_cr TEXT,
    capex_cr TEXT,
    earnings_per_share TEXT,
    book_value_per_share TEXT,
    dividend_payout_ratio_pct TEXT,
    total_debt_cr TEXT,
    cash_from_operations_cr TEXT
);


-- MARKET_CAP
CREATE TABLE IF NOT EXISTS market_cap (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    market_cap_crore TEXT,
    enterprise_value_crore TEXT,
    pe_ratio TEXT,
    pb_ratio TEXT,
    ev_ebitda TEXT,
    dividend_yield_pct TEXT
);


-- PEER_GROUPS
CREATE TABLE IF NOT EXISTS peer_groups (
    id TEXT PRIMARY KEY,
    peer_group_name TEXT,
    company_id TEXT,
    is_benchmark TEXT
);


-- PROFITANDLOSS
CREATE TABLE IF NOT EXISTS profitandloss (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    sales TEXT,
    expenses TEXT,
    operating_profit TEXT,
    opm_percentage TEXT,
    other_income TEXT,
    interest TEXT,
    depreciation TEXT,
    profit_before_tax TEXT,
    tax_percentage TEXT,
    net_profit TEXT,
    eps TEXT,
    dividend_payout TEXT
);


-- PROSANDCONS
CREATE TABLE IF NOT EXISTS prosandcons (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    pros TEXT,
    cons TEXT
);


-- SECTORS
CREATE TABLE IF NOT EXISTS sectors (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    broad_sector TEXT,
    sub_sector TEXT,
    index_weight_pct TEXT,
    market_cap_category TEXT
);


-- STOCK_PRICES
CREATE TABLE IF NOT EXISTS stock_prices (
    id TEXT PRIMARY KEY,
    company_id TEXT,
    date TEXT,
    open_price TEXT,
    high_price TEXT,
    low_price TEXT,
    close_price TEXT,
    volume TEXT,
    adjusted_close TEXT
);
PRAGMA foreign_keys = ON;

-- ===========================================
-- N100 Financial Intelligence Platform
-- Production Database Schema
-- Sprint 1 - Version 2
-- ===========================================
-- ===========================================
-- COMPANIES
-- ===========================================

CREATE TABLE IF NOT EXISTS companies (

    id TEXT PRIMARY KEY,

    company_logo TEXT,

    company_name TEXT NOT NULL,

    current_price REAL,

    market_cap REAL,

    stock_pe REAL,

    dividend_yield REAL,

    roce_percentage REAL,

    roe_percentage REAL,

    face_value REAL,

    book_value REAL,

    sector TEXT

);
CREATE TABLE aggregated_transaction (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    Payment_Type VARCHAR(50),
    Transaction_Count BIGINT,
    Amount DOUBLE
);

CREATE TABLE aggregated_user (
    State VARCHAR(100),
    Year INT,
    Quarter INT,
    Brand VARCHAR(50),
    Users BIGINT
);

CREATE TABLE top_states (
    State VARCHAR(100),
    Total_Amount DOUBLE
);

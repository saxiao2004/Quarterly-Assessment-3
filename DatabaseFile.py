# Susana Xiao
# Quarterly Assessment 3
# DS 3850 Section 001
# A populated database file with questions for a Quiz Bowl. (Does not have to be in GUI format.)

# Importing sqlite3 module that establishes a connection to the database.
import sqlite3

# Establishing a connection to the database.
connection = sqlite3. connect ('Quiz_Questions.db')
cursor = connection.cursor()

# Tables are created using these attributes.
cursor.execute ("""CREATE TABLE IF NOT EXISTS QuizBowl_Questions
    (id INTEGER PRIMARY KEY,
    category TEXT,
    question TEXT,
    choice_a TEXT,
    choice_b TEXT,
    choice_c TEXT,
    choice_d TEXT,
    correct_answer TEXT)
                """)

# Executing SQL Query in inserting data into the table of "Accounting Quiz."
def QuizBowl_Questions (id, category, questions, choice_a, choice_b, choice_c, choice_d, correct_answer):
    cursor.execute (f"""
    INSERT INTO QuizBowl_Questions (id, category, question, choice_a, choice_b, choice_c, choice_d, correct_answer)
    VALUES (?,?,?,?,?,?,?,?)""", (id, category, questions, choice_a, choice_b, choice_c, choice_d, correct_answer))

# Importing (id, category, questions, choice_a, choice_b, choice_c, choice_d, correct_answer) into the database system for each category of the quiz.
QuizBowl_Questions (1, "Accounting", "What is the basic accounting equation?", "A. Assets = Liabilities + Equity", "B. Assets + Liabilities = Equity", "C. Assets = Liabilities = Equity", "D. Assets/ Liabilities = Equity", "Correct Answer: A")
QuizBowl_Questions (2, "Accounting", "What type of account represents amounts owed to creditors?", "A. Revenue", "B. Expenses", "C. Liability", "D. Asset", "Correct Answer: C")
QuizBowl_Questions (3, "Accounting", "Which financial statement reports a company's financial performance over a specific period?", "A. Balance Sheet", "B. Income statement", "C. Statement of Cash Flows", "D. Materiality Principle", "Correct Answer: B")
QuizBowl_Questions (4, "Accounting", "Which accounting principle states that revenue should be recognized when it is earned, regardless of when cash is received?", "A. Matching Principles", "B. Revenue Recognition Principles", "C. Conservatism Principles", "D. Materiality Principles", "Correct Answer: B")
QuizBowl_Questions (5, "Accounting", "What type of account represents ownership interests in a corporation?", "A. Revenue", "B. Expenses", "C. Equity", "D. Liability", "Correct Answer: C")
QuizBowl_Questions (6, "Accounting", "What is the formula for calculating net income?", "A. Revenue - Expenses", "B. Assers - Liabilities", "C. Assets + Liabilities", "D. Revenue/ Expenses", "Correct Answer: A")
QuizBowl_Questions (7, "Accounting", "Which financial statement shows the changes in equity over a period of time?", "A. Balance Sheet", "B. Income statement", "C. Statement of Cash Flows", "D. Statement of Retained Earnings", "Correct Answer: D")
QuizBowl_Questions (8, "Accounting", "What is the purpose of the statement of cash flows?", "A. To report a company's financial position at a specific point in time", "B. To report a company's financial performance over a specific period", "C. To show how cash is generated and used by a company during a specific period", "D. To report changes in a compan's equity over a period of time", "Correct Answer: C")
QuizBowl_Questions (9, "Accounting", "Which accounting concept requires accountant to use the same accounting method and procedures from period to period?", "A. Consistency", "B. Conservatism", "C. Materiality", "D. Matching", "Correct Answer: A")
QuizBowl_Questions (10, "Accounting", "Which type of account represnts goods and services provided to customers in exchange for payment?", "A. Revenue", "B. Epenses", "C. Liability", "D. Asset", "Correct Answer: A")
QuizBowl_Questions (11, "Money and Banking", "What is the primary role of a central bank in a country's monetary system?", "A. Issuing currency", "B. Managing fiscal policy", "C. Regulating commercial banks", "D. Conducting trade negotiations", "Correct Answer: A")
QuizBowl_Questions (12, "Money and Banking", "What is the term for the interest rate as which a central bank lends money to commercial banks?", "A. Prime rate", "B. Discount rate", "C. Federal funds rate", "D. LIBOR rate", "Correct Answer: B")
QuizBowl_Questions (13, "Money and Banking", "Which is the following is NOT considered a function of commercial banks?", "A. Issuing currency", "B. Accepting deposits", "C. Providing loans", "D. Facilitaing payments", "Correct Answer: A")
QuizBowl_Questions (14, "Money and Banking", "What does the term 'liquidity' refer to in banking?", "A. The ability to convert assets into cash quickly", "B. The amount of cash a bank holds in revenue", "C. The interest rate charged on loans", "D. The profibility of a bank's investment", "Correct Answer: A")
QuizBowl_Questions (15, "Money and Banking", "Which regulatory body is responsible for overseeing the banking system in the United States?", "A. Securities and Exchange Commission (SEC)", "B. Federal Reserve System (FED)", "C. Federal Deposit Insurance Corporation (FDIC)", "D. Office of the Comptroller of the Currency (OCC)", "Correct Answer: B")
QuizBowl_Questions (16, "Money and Banking", "What is the term for the ratio of a bank's reserve to its local deposits?", "A. Reserve requirement", "B. Capital adequancy ratio", "C. Leverage ratio", "D. Loan-to-deposit ratio", "Correct Answer: A")
QuizBowl_Questions (17, "Money and Banking", "What is the function of the Federal Deposit Insurance Corporation (FDIC) in the United States?", "A. Regualting interest rates", "B. Providing deposit insurance", "C. Conducting monetary policy", "D. Issuing currency", "Correct Answer: B")
QuizBowl_Questions (18, "Money and Banking", "When the Federal Reserve buys government securities in the open market, what effect does it have on the money supply?", "A. Increase the money supply", "B. Decreases the money supply", "C. No efect on the money supply", "D. None of above", "Correct Answer: A")
QuizBowl_Questions (19, "Money and Banking", "What is the term for the interest rate that banks carge each other for overnight loans of reserves?", "A. Prime rate", "B. Discount rate", "C. Federal funds rate", "D. LIBOR rate", "Correct Answer: C")
QuizBowl_Questions (20, "Money and Banking", "What is the primary tool used by central banks to influence monetary policy?", "A.Open Market Operations", "B. Fiscal Policy", "C. Exchange rate interventions", "D. Price controls", "Correct Answer: A")
QuizBowl_Questions (21, "Database Management", "What is the primary purpose of a database management system (DBMS)?", "A. Creating backups of files", "B. Storing and managing data", "C. Designing user interfaces", "D. Generating Reports", "Correct Answer: B")
QuizBowl_Questions (22, "Database Management", "Which of the following is NOT a types of database model?", "A. Relational", "B. Hierarchial", "C. Network", "D. Network", "Correct Answer: D")
QuizBowl_Questions (23, "Database Management", "In a relational database, what is a primary key used for?", "A. Storing large data objects", "B. Enforcing referntial integrity", "C. Uniquely identifying each record in a table", "D. Defining data types for columns", "Correct Answer: C")
QuizBowl_Questions (24, "Database Management", "What is SQL an acronym for?", "A. Simple Query Language", "B. Structured Query Language", "C. Standard Query Logic", "D. Sequential Query Link", "Correct Answer: B")
QuizBowl_Questions (25, "Database Management", "Which SQL command is used to retrieve data from database?", "A. SELECT", "B. INSERT", "C. UPDATE", "D. DELETE", "Correct Answer: A")
QuizBowl_Questions (26, "Database Management", "What does the term 'normalization refer to in database design", "A. Removing redundant data", "B. Adding new data", "C. Creating indexes", "D. Sorting data alphabetically", "Correct Answer: A")
QuizBowl_Questions (27, "Database Management", "Which type of join returns all rows from both tables, joining records where available and inserting NULLs where there is no match?", "A. Inner Join", "B. Left Outer Join", "C. Right Outer Join", "D. Ful Outer Join", "Correct Answer: D")
QuizBowl_Questions (28, "Database Management", "What is the purpose of an index ina  databse?", "A. Encrypting data", "B. Sorting data alphabetically", "C. Iporving query performance", "D. Managing user permissions", "Correct Answer: C")
QuizBowl_Questions (29, "Database Management", "Which if the following is NOT a valid data type in SQL?", "A. Integer", "B. Float", "C. String", "D. Boolean", "Correct Answer: D")
QuizBowl_Questions (30, "Database Management", "What is the ACID property in database transactions?", "A. Atomicity, Consistency, Isolation, Durability", "B. Association, Concurrency, Integrity, Durality", "C. Access, Commitment, Isolation, Durability", "D. Authorization, Consistency, Isolation, Durability", "Correct Answer: A")
QuizBowl_Questions (31, "Operation Supply Chain Management", "What is the primary objectibe of supply chain management (SCM)?", "A. Maximizing revenue", "B. Minimizing Costs", "C. Maximizing Customer Satisfaction", "D. Minimizing Competition", "Correct Answer: C") 
QuizBowl_Questions (32, "Operation Supply Chain Management", "Whic of the following is NOT a component of logistics in the supply chain?", "A. Inventory management", "B. Transportation", "C. Manufacturing", "D. Warehousing", "Correct Answer: C")
QuizBowl_Questions (33, "Operation Supply Chain Management", "What does the term 'lead time' refer to in operations management?", "A. The time it takes to manufacturing a product", "B. The time it takes to deliver a prodcut to the customer", "C. The timer it taes to process an order", "D. The time it takes to pay suppliers", "Correct Answer: C")
QuizBowl_Questions (34, "Operation Supply Chain Management", "Which inventory management technique aims to minimizing inventory levels by ordering only when needed?", "A. Just-in-time (JIT)", "B. Economic Order Quantity (EOQ)", "C. Safety stock", "D. Batch Ordering", "Correct Answer: A")
QuizBowl_Questions (35, "Operation Supply Chain Management", "What is the purpose of a supply chain network design?", "A. Maximizing transportation Costs", "B. Minimizing customer satisfaction", "C. Optimizing the flow of goods and information", "D. Increase lead times", "Correct Answer: C")
QuizBowl_Questions (36, "Operation Supply Chain Management", "Which performance metric measures the total cost incurred by the supply chain, including transportation, inventory, and wareehousing costs?", "A. Inventory Turnover Ratio", "B. Days sales of inventory (DSI)", "C. Total landed cost", "D. Order fulfillment cycle time", "Correct Answer: C")
QuizBowl_Questions (37, "Operation Supply Chain Management", "What is the term for the process of managing relationships and interactions with suppliers?", "A. Customer relationship management (CRM)", "B. Supplier relationships management (SRM)", "C. Inventory forcasting", "D. Demand forecasting", "Correct Answer: B")
QuizBowl_Questions (38, "Operation Supply Chain Management", "Which type of distribution strategy involved storing products in centralized warehouses and shipping directly to customer?", "A. Direct distribution", "B. Indirect Distribution", "C. Push Distribution", "D. Pull Distribution", "Correct Answer: A")
QuizBowl_Questions (39, "Operation Supply Chain Management", "What is the goal of demand forecasting in supply chain management?", "A. Maximizing production capacity", "B. Minimizing inventory levels", "C. Predicting future customer demand", "D. Optimizing transportation routes", "Correct Answer: C")
QuizBowl_Questions (40, "Operation Supply Chain Management", "What does the term 'reserve logistics' refer to in supply chain management?", "A. The process of returning defective products to suppliers", "B. The process of delivering products to customers", "C. The process of managing inbound logistics", "D. The process of optimizing warehouse operations", "Correct Answer: A")
QuizBowl_Questions (41, "Data Driven Analytics", "What is the primary goals of data-driven analytics?", "A. Increasing data storage capacity", "B. Identifying trends and patterns in data", "C. Reducing data collection efforts", "D. Maximizing hardware utilization", "Correct Answer: B")
QuizBowl_Questions (42, "Data Driven Analytics", "Which of the following is NOT a common data visualization technique?", "A. Scatterplot", "B. Histograms", "C. Barcodes", "D. Pie charts", "Correct Answer: C")
QuizBowl_Questions (43, "Data Driven Analytics", "What does the term 'predictive analytics' refer to in data-driven decision-making?", "A. Analyzing past data to predict future outcomes", "B. Analyzing current data to understanding present trends", "C. Identifying patterns in data without any specific outcome in mind", "D. Visualization data using charts and graphs", "Correct Answer: A")
QuizBowl_Questions (44, "Data Driven Analytics", "Which statistical measure is used to describe the spread of data around the mean?", "A. Mean", "B. Median", "C. Standard deviation", "D. Mode", "Correct Answer: C")
QuizBowl_Questions (45, "Data Driven Analytics", "What is the purpose of clustering algorithms in data analytics?", "A. Identifying outliers in data", "B. Grouping similar data points together", "C. Predicting time-series data", "D. Analyzing time-series data", "Correct Answer: B") 
QuizBowl_Questions (46, "Data Driven Analytics", "Which of the following is NOT a step in the data analytics process?", "A. Data preprocessing", "B. Data Visualization", "C. Data Sanitization", "D. Data Interpretation", "Correct Answer: C")
QuizBowl_Questions (47, "Data Driven Analytics", "Which machine learning technique is commonly used for classification tasks?", "A. Linear Regression", "B. K-means clustering", "C. Decision trees", "D. Principle component analysis (PCA)", "Correct Answer: C")
QuizBowl_Questions (48, "Data Driven Analytics", "What is the purpose of A/B testing in data-driven decision-making?", "A. Analyzing customer demographics", "B. Comparing two or more versions of a product or service", "C. Identifying outliers in data", "D. Predicting future sales trends", "Correct Answer: B")
QuizBowl_Questions (49, "Data Driven Analytics", "Which type of data analysis technique is used to identify relationships between variables?", "A. Descriptive analytics", "B. Diagnostic Analytics", "C. Predictive Analytics", "D. Prescriptive Analytics", "Correct Answer: B")
QuizBowl_Questions (50, "Data Driven Analytics", "What does the term 'big data' refer to in the context of data-driven analytics?", "A. Data sets that are too small to analyze", "B. Data sets that are too large or complex to analyze using traditional methods", "C. Data sets that are outdated and irrelevant", "D. Data sets that are highly structures and easy to analyze", "Correct Answer: B")
QuizBowl_Questions (51, "Business App Develop", "What is the primary goals of bsuiness application development?", "A. Increasing hardware sales", "B. Maxmizing software complexity", "C. Enhancing bsuiness efficiency and productivity", "D. Minimizing employee training efforts", "Correct Answer: C")
QuizBowl_Questions (52, "Business App Develop", " Which programming language is commonly used for web application development?", "A. Java", "B. C++", "C. Python", "D. HMTL/CSS", "Correct Answer: D")
QuizBowl_Questions (53, "Business App Develop", "What is th epurpose of version control system in software development?", "A. Managing customer relationships", "B. Tracking changes in code and facilitaing collaboration among developers", "C. Optimizing database performance", "D. Automating software testing", "Correct Answer: B")
QuizBowl_Questions (54, "Business App Develop", "Which software development methodology emphasizes iterative development and frequent collaboration with stakeholders?", "A. Waterfall", "B. Agile", " C. Spiral", "D. RAD (Rapid Application Development)", "Correct Answer: B")
QuizBowl_Questions (55, "Business App Develop", "What is the term for software components that can be used in multiple applications?", "A. Modularization", "B. Customization", "C. Reusability", "D. Scalability", "Correct Answer: C")
QuizBowl_Questions (56, "Business App Develop", "Which of the following is NOT a type of testing commonly performed iin software development?", "A. Unit testing", "B. Integration testing", "C. Regression testing", "D. Normalization testing", "Correct Answer: D")
QuizBowl_Questions (57, "Business App Develop", "What does the term 'deployment' refer to in the context of software development?", "A. Updating software documentation", "B. Distributing software to end-users and making it operational", "C. Testing software performance under load", "D. Optimizing software algorithms", "Correct Answer: B") 
QuizBowl_Questions (58, "Business App Develop", "Which database management system (DBMS) is commonly used for business application development?", "A. MySQL", "B. MongDB", "C. SQLite", "D. Redis", "Correct Answer: A")
QuizBowl_Questions (59, "Business App Develop", "What is the purpose of user acceptance testing (UAT) in business application development?", "A. Evaluating software performance under stress conditions", "B. Testing software compatibility with different operating systems", "C. Validating whether the software meets user requirements and expectations", "D. Assessing software security vulnerabilities", "Correct Answer: C")
QuizBowl_Questions (60, "Business App Develop", "What does the term 'scalability' refer to in business application development?", "A. Ability to handle increased workload and users without sacrificing performance", "B. Ability to customize software for specific business needs", "C. Ability to integrate with other software systems", "D. Ability to reduce software development costs", "Correct Answer: A")

# Closes the connection with the database.
connection.commit ()
connection.close ()
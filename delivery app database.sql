use delivery_app;
-- Creating the Customer table
CREATE TABLE Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerName VARCHAR(100),
    CustomerAddress TEXT,
    CustomerEmail VARCHAR(100),
    CustomerPhone VARCHAR(15)
);

-- Creating the Order table
CREATE TABLE OrderTable (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    DeliveryDate DATE,
    TotalAmount DECIMAL(10, 2),
    OrderStatus ENUM('Pending', 'In Progress', 'Delivered', 'Cancelled'),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Creating the DeliveryPersonnel table
CREATE TABLE DeliveryPersonnel (
    PersonnelID INT AUTO_INCREMENT PRIMARY KEY,
    PersonnelName VARCHAR(100),
    PersonnelPhone VARCHAR(15),
    VehicleType VARCHAR(50),
    AvailabilityStatus ENUM('Available', 'Busy', 'Unavailable')
);

-- Creating the DeliveryAssignment table
CREATE TABLE DeliveryAssignment (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    PersonnelID INT,
    AssignedDate DATE,
    DeliveryStatus ENUM('Not Started', 'In Transit', 'Delivered'),
    FOREIGN KEY (OrderID) REFERENCES OrderTable(OrderID),
    FOREIGN KEY (PersonnelID) REFERENCES DeliveryPersonnel(PersonnelID)
);

-- Creating the DeliveryLocation table
CREATE TABLE DeliveryLocation (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    LocationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Latitude DECIMAL(9,6),
    Longitude DECIMAL(9,6),
    FOREIGN KEY (OrderID) REFERENCES OrderTable(OrderID)
);
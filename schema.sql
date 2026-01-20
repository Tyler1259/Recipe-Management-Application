-- User Table
CREATE TABLE User (
    UserID INT PRIMARY KEY,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Name VARCHAR(255),
    Type VARCHAR(50)
);

-- Ingredients Table
CREATE TABLE Ingredients (
    IngredientID INT PRIMARY KEY,
    Type VARCHAR(100),
    Quantity VARCHAR(100)
);

-- Recipe Table
CREATE TABLE Recipe (
    RecipeID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Instructions TEXT NOT NULL,
    Description TEXT,
    Prep_Time INT,
    Cook_Time INT,
    Servings INT,
    Created_By VARCHAR(255),
    Label VARCHAR(100),
    DietaryID INT,
    IngredientID INT,
    UserID INT,

    FOREIGN KEY (DietaryID) REFERENCES DietaryCategories(DietCategoryID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- CuisineCategories Table
CREATE TABLE CuisineCategories (
    CategoriesID INT PRIMARY KEY,
    Name VARCHAR(100),
    RecipeID INT,
    FOREIGN KEY (RecipeID) REFERENCES Recipe(RecipeID)
);

-- DietaryCategories Table
CREATE TABLE DietaryCategories (
    DietCategoryID INT PRIMARY KEY,
    Name VARCHAR(100),
    Requirement TEXT,
    RecipeID INT,
    IngredientID INT,

    FOREIGN KEY (RecipeID) REFERENCES Recipe(RecipeID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID)
);

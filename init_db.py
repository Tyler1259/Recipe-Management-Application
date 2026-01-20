import sqlite3

conn = sqlite3.connect("db/recipes.db") 
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Create User table
cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Email TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    Name TEXT,
    Type TEXT
)
""")

# Create Ingredients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Ingredients (
    IngredientID INTEGER PRIMARY KEY AUTOINCREMENT,
    Type TEXT,
    Quantity TEXT
)
""")

# Create Recipe table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Recipe (
    RecipeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Instructions TEXT NOT NULL,
    Description TEXT,
    Prep_Time INTEGER,
    Cook_Time INTEGER,
    Servings INTEGER,
    Created_By TEXT,
    Label TEXT,
    DietaryID INTEGER,
    IngredientID INTEGER,
    UserID INTEGER,
    FOREIGN KEY (DietaryID) REFERENCES DietaryCategories(DietCategoryID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
)
""")

# Create CuisineCategories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS CuisineCategories (
    CategoriesID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    RecipeID INTEGER,
    FOREIGN KEY (RecipeID) REFERENCES Recipe(RecipeID)
)
""")

# Create DietaryCategories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS DietaryCategories (
    DietCategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Requirement TEXT,
    RecipeID INTEGER,
    IngredientID INTEGER,
    FOREIGN KEY (RecipeID) REFERENCES Recipe(RecipeID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID)
)
""")

# ---------------------------------------------------------
# Insert 3 admin users (basic test accounts)
# ---------------------------------------------------------

admins = [
    ("admin1@example.com", "admin123", "Admin One", "admin"),
    ("admin2@example.com", "password", "Admin Two", "admin"),
    ("admin3@example.com", "test123", "Admin Three", "admin")
]

for email, password, name, user_type in admins:
    try:
        cursor.execute("""
            INSERT INTO User (Email, Password, Name, Type)
            VALUES (?, ?, ?, ?)
        """, (email, password, name, user_type))
    except sqlite3.IntegrityError:
        pass  # Skip if already exists

conn.commit()
conn.close()

print("Database initialized and admin users added.")

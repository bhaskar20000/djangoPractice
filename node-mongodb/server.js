// Import required packages
const express = require("express");
const mongoose = require("mongoose");
require("dotenv").config();

// Create Express app
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Variable to store database connection
let db = null;

// ----------------------
// MongoDB Initialization
// ----------------------

const initializeDBAndServer = async () => {
  try {

    // Connect to MongoDB using Mongoose
    db = await mongoose.connect(process.env.MONGO_URI);

    console.log("MongoDB Connected");

    // Start Express Server
    app.listen(process.env.PORT || 3000, () => {
      console.log(`Server Running at http://localhost:${process.env.PORT || 3000}/`);
    });

  } catch (e) {

    console.log(`DB Error: ${e.message}`);
    process.exit(1);

  }
};

// Initialize database and server
initializeDBAndServer();

// ----------------------
// Schema and Model
// ----------------------

// Define structure of Book document
const bookSchema = new mongoose.Schema({
  title: String,
  author: String,
  rating: Number,
});

// Create Book model
const Book = mongoose.model("Book", bookSchema);

// ----------------------
// APIs
// ----------------------

// Test API
app.get("/", (request, response) => {
  response.send("MongoDB Server Running");
});

// ----------------------
// CREATE BOOK
// ----------------------

app.post("/books/", async (request, response) => {

  const { title, author, rating } = request.body;

  const newBook = new Book({
    title,
    author,
    rating,
  });

  const savedBook = await newBook.save();

  response.send(savedBook);

});

// ----------------------
// GET ALL BOOKS
// ----------------------

app.get("/books/", async (request, response) => {

  const booksArray = await Book.find();

  response.send(booksArray);

});

// ----------------------
// GET SINGLE BOOK
// ----------------------

app.get("/books/:id", async (request, response) => {

  const { id } = request.params;

  const book = await Book.findById(id);

  response.send(book);

});

// ----------------------
// UPDATE BOOK
// ----------------------

app.put("/books/:id", async (request, response) => {

  const { id } = request.params;

  const updatedBook = await Book.findByIdAndUpdate(
    id,
    request.body,
    { new: true }
  );

  response.send(updatedBook);

});

// ----------------------
// DELETE BOOK
// ----------------------

app.delete("/books/:id", async (request, response) => {

  const { id } = request.params;

  await Book.findByIdAndDelete(id);

  response.send("Book Deleted Successfully");

});